import os
import numpy as np
import matplotlib.pyplot as plt

from src.simulator import simulate_gbm_paths, simulate_terminal_prices
from src.black_scholes import black_scholes


OUTPUT_DIR = "outputs"  # Folder name for saving generated plots
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Create the folder if it does not already exist


def plot_price_paths(S, r, sigma, T, n_paths=300, steps=252, seed=42):
    """
    Plot simulated GBM stock price paths.
    """

    paths = simulate_gbm_paths(
        S0=S,
        r=r,
        sigma=sigma,
        T=T,
        steps=steps,
        n_sims=n_paths,
        seed=seed
    )

    time_grid = np.linspace(0, T, steps + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(time_grid, paths.T, alpha=0.15, linewidth=0.7)
    plt.axhline(S, linestyle="--", linewidth=1.2, label=f"Start price = ${S}")

    plt.title(f"GBM Simulated Stock Price Paths ({n_paths} paths)")
    plt.xlabel("Time (years)")
    plt.ylabel("Stock Price ($)")
    plt.legend()
    plt.tight_layout()

    file_path = os.path.join(OUTPUT_DIR, "price_paths.png")
    plt.savefig(file_path, dpi=150)
    plt.show()

    print(f"Saved: {file_path}")


def plot_payoff_distribution(S, K, r, sigma, T, option_type="call", n_sims=100_000, seed=42):
    """
    Plot the distribution of discounted option payoffs.
    """

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
    elif option_type == "put":
        payoffs = np.maximum(K - S_T, 0)
    else:
        raise ValueError("option_type must be either 'call' or 'put'.")

    discounted_payoffs = np.exp(-r * T) * payoffs

    mc_price = discounted_payoffs.mean()
    bs_price = black_scholes(S, K, r, sigma, T, option_type)

    positive_payoffs = discounted_payoffs[discounted_payoffs > 0]

    plt.figure(figsize=(9, 5))
    plt.hist(positive_payoffs, bins=80, edgecolor="white", alpha=0.85)

    plt.axvline(mc_price, linestyle="--", linewidth=2, label=f"MC price = ${mc_price:.4f}")
    plt.axvline(bs_price, linestyle="--", linewidth=2, label=f"BS price = ${bs_price:.4f}")

    plt.title(f"Discounted Payoff Distribution ({option_type.capitalize()})")
    plt.xlabel("Discounted Payoff ($)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()

    file_path = os.path.join(OUTPUT_DIR, f"payoff_distribution_{option_type}.png")
    plt.savefig(file_path, dpi=150)
    plt.show()

    print(f"Saved: {file_path}")


def plot_convergence(S, K, r, sigma, T, option_type="call", seed=42):
    """
    Plot Monte Carlo option price convergence to the Black-Scholes price.
    """

    rng = np.random.default_rng(seed)

    bs_price = black_scholes(S, K, r, sigma, T, option_type)

    sim_sizes = np.unique(np.logspace(2, 5, 60).astype(int))
    mc_prices = []

    for n_sims in sim_sizes:
        Z = rng.standard_normal(n_sims)

        S_T = S * np.exp(
            (r - 0.5 * sigma ** 2) * T
            + sigma * np.sqrt(T) * Z
        )

        if option_type == "call":
            payoffs = np.maximum(S_T - K, 0)
        elif option_type == "put":
            payoffs = np.maximum(K - S_T, 0)
        else:
            raise ValueError("option_type must be either 'call' or 'put'.")

        mc_price = np.exp(-r * T) * payoffs.mean()
        mc_prices.append(mc_price)

    plt.figure(figsize=(9, 5))
    plt.semilogx(sim_sizes, mc_prices, linewidth=1.5, label="Monte Carlo price")
    plt.axhline(bs_price, linestyle="--", linewidth=2, label=f"Black-Scholes price = ${bs_price:.4f}")

    plt.title(f"Monte Carlo Convergence ({option_type.capitalize()})")
    plt.xlabel("Number of Simulations")
    plt.ylabel("Option Price ($)")
    plt.legend()
    plt.tight_layout()

    file_path = os.path.join(OUTPUT_DIR, f"convergence_{option_type}.png")
    plt.savefig(file_path, dpi=150)
    plt.show()

    print(f"Saved: {file_path}")


if __name__ == "__main__":
    S = 100
    K = 100
    r = 0.05
    sigma = 0.20
    T = 0.5

    plot_price_paths(S, r, sigma, T)
    plot_payoff_distribution(S, K, r, sigma, T, option_type="call")
    plot_convergence(S, K, r, sigma, T, option_type="call")