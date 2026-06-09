from src.black_scholes import black_scholes


def compute_greeks(S, K, r, sigma, T, option_type="call"):
    """
    Calculate option price and Greeks using finite differences.

    Returns price, delta, gamma, theta, vega and rho in a dictionary.
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

    dS = S * 0.01          # 1% stock price move
    dT = 1 / 365           # one calendar day
    d_sigma = 0.01         # 1% volatility move
    dr = 0.01              # 1% interest rate move

    price = black_scholes(S, K, r, sigma, T, option_type)

    # Delta and Gamma
    price_up = black_scholes(S + dS, K, r, sigma, T, option_type)
    price_down = black_scholes(S - dS, K, r, sigma, T, option_type)

    delta = (price_up - price_down) / (2 * dS)
    gamma = (price_up - 2 * price + price_down) / (dS ** 2)

    # Theta: one-day time decay
    T_next_day = max(T - dT, 1e-6)
    price_next_day = black_scholes(S, K, r, sigma, T_next_day, option_type)
    theta = price_next_day - price

    # Vega: price change for 1% volatility move
    vol_up = black_scholes(S, K, r, sigma + d_sigma, T, option_type)
    vol_down = black_scholes(S, K, r, sigma - d_sigma, T, option_type)
    vega = (vol_up - vol_down) / 2

    # Rho: price change for 1% interest rate move
    rate_up = black_scholes(S, K, r + dr, sigma, T, option_type)
    rate_down = black_scholes(S, K, r - dr, sigma, T, option_type)
    rho = (rate_up - rate_down) / 2

    return {
        "price": price,
        "delta": delta,
        "gamma": gamma,
        "theta": theta,
        "vega": vega,
        "rho": rho,
    }


if __name__ == "__main__":
    S = 100
    K = 100
    r = 0.05
    sigma = 0.20
    T = 0.5

    print("=" * 52)
    print("OPTION GREEKS".center(52))
    print("=" * 52)

    for option_type in ["call", "put"]:
        greeks = compute_greeks(S, K, r, sigma, T, option_type)

        print(f"\n{option_type.upper()}")
        print(f"Price:  ${greeks['price']:.4f}")
        print(f"Delta:  {greeks['delta']:+.4f}   ($ change per $1 stock move)")
        print(f"Gamma:  {greeks['gamma']:+.6f}  (delta change per $1 move)")
        print(f"Theta:  {greeks['theta']:+.4f}   ($ change after 1 day)")
        print(f"Vega:   {greeks['vega']:+.4f}   ($ change per 1% vol move)")
        print(f"Rho:    {greeks['rho']:+.4f}   ($ change per 1% rate move)")

    print("\n" + "=" * 52)