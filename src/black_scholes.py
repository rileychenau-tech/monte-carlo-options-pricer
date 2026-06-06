import numpy as np
from scipy.stats import norm


def black_scholes(S, K, r, sigma, T, option_type="call"):
    """
    Calculate the Black-Scholes price for a European option.

    Parameters:
        S     : float - current stock price
        K     : float - strike price
        r     : float - risk-free rate (e.g. 0.05 = 5%)
        sigma : float - volatility (e.g. 0.20 = 20%)
        T     : float - time to expiry in years (e.g. 0.5 = 6 months)
        option_type : str - "call" or "put"

    Returns:
        float - theoretical option price
    """
    if T <= 0:
        if option_type == "call":
            return max(S - K, 0)
        else:
            return max(K - S, 0)

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price


if __name__ == "__main__":
    S, K, r, sigma, T = 100, 100, 0.05, 0.20, 0.5

    call = black_scholes(S, K, r, sigma, T, "call")
    put  = black_scholes(S, K, r, sigma, T, "put")

    print(f"Black-Scholes Call: ${call:.4f}")
    print(f"Black-Scholes Put:  ${put:.4f}")

    # Put-Call parity check
    parity = S - K * np.exp(-r * T)
    print(f"\nPut-Call parity check:")
    print(f"  C - P        = ${call - put:.4f}")
    print(f"  S - Ke^(-rT) = ${parity:.4f}")
    print(f"  Match: {abs((call - put) - parity) < 0.0001}")