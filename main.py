import numpy as np

from src.black_scholes import black_scholes
from src.simulator import simulate_terminal_prices
from src.greeks import compute_greeks
from src.plotter import plot_price_paths, plot_payoff_distribution, plot_convergence


def monte_carlo_price(S, K, r, sigma, T, n_sims=100_000, option_type="call", seed=42):
    """
    Price a European option using Monte Carlo simulation.

    Returns the estimated price, standard error, and 95% confidence interval.
    """

    if S <= 0:
        raise ValueError("Stock price S must be positive.")
    if K <= 0:
        raise ValueError("Strike price K must be positive.")
    if sigma <= 0:
        raise ValueError("Volatility sigma must be positive.")
    if T <= 0:
        raise ValueError("Time to expiry T must be positive.")
    if option_type not in ["call", "put"]:
        raise ValueError("option_type must be either 'call' or 'put'.")

    S_T = simulate_terminal_prices(
        S0=S,
        r=r,
        sigma=sigma,
        T=T,
        n_sims=n_sims,
        seed=seed
    )

    if option_type == "call":
        payoffs = np.maximum(S_T - K, 0)
    else:
        payoffs = np.maximum(K - S_T, 0)

    discounted_payoffs = np.exp(-r * T) * payoffs

    mc_price = discounted_payoffs.mean()
    std_error = discounted_payoffs.std(ddof=1) / np.sqrt(n_sims)

    ci_low = mc_price - 1.96 * std_error
    ci_high = mc_price + 1.96 * std_error

    return mc_price, std_error, (ci_low, ci_high)


if __name__ == "__main__":
    S = 100
    K = 100
    r = 0.05
    sigma = 0.20
    T = 0.5
    n_sims = 100_000

    print("=" * 60)
    print("MONTE CARLO OPTIONS PRICER".center(60))
    print("=" * 60)
    print(f"S = {S}")
    print(f"K = {K}")
    print(f"r = {r:.2%}")
    print(f"sigma = {sigma:.2%}")
    print(f"T = {T} years")
    print(f"Simulations = {n_sims:,}")
    print("=" * 60)

    for option_type in ["call", "put"]:
        mc_price, std_error, ci = monte_carlo_price(
            S=S,
            K=K,
            r=r,
            sigma=sigma,
            T=T,
            n_sims=n_sims,
            option_type=option_type,
            seed=42
        )

        bs_price = black_scholes(
            S=S,
            K=K,
            r=r,
            sigma=sigma,
            T=T,
            option_type=option_type
        )

        difference = abs(mc_price - bs_price)

        print(f"\n{option_type.upper()} OPTION")
        print(f"Monte Carlo price:   ${mc_price:.4f}")
        print(f"Standard error:      ${std_error:.4f}")
        print(f"95% confidence int:  (${ci[0]:.4f}, ${ci[1]:.4f})")
        print(f"Black-Scholes price: ${bs_price:.4f}")
        print(f"Absolute difference: ${difference:.4f}")

    print("\n" + "=" * 60)
    print("GREEKS FOR AT-THE-MONEY CALL".center(60))
    print("=" * 60)

    greeks = compute_greeks(
        S=S,
        K=K,
        r=r,
        sigma=sigma,
        T=T,
        option_type="call"
    )

    print(f"Price:  ${greeks['price']:.4f}")
    print(f"Delta:  {greeks['delta']:+.4f}")
    print(f"Gamma:  {greeks['gamma']:+.6f}")
    print(f"Theta:  {greeks['theta']:+.4f}")
    print(f"Vega:   {greeks['vega']:+.4f}")
    print(f"Rho:    {greeks['rho']:+.4f}")

    print("\nGenerating charts...")

    plot_price_paths(S, r, sigma, T)
    plot_payoff_distribution(S, K, r, sigma, T, option_type="call")
    plot_convergence(S, K, r, sigma, T, option_type="call")

    print("\nDone. Charts saved in the outputs folder.")