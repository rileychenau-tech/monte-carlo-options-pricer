import numpy as np


def simulate_gbm_paths(
    S0: float,
    r: float,
    sigma: float,
    T: float,
    steps: int = 252,  # 252 as default trading days
    n_sims: int = 10_000,
    seed: int | None = None
) -> np.ndarray:
    """
    Simulate stock price paths using Geometric Brownian Motion (GBM).

    GBM model:
        dS = rS dt + sigma S dW

    Exact simulation formula:
        S_t = S_0 * exp((r - 0.5*sigma^2)t + sigma*W_t)

    Parameters
    ----------
    S0 : float
        Initial stock price.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the stock.
    T : float
        Time to maturity in years.
    steps : int
        Number of time steps.
    n_sims : int
        Number of simulated paths.
    seed : int | None
        Random seed for reproducibility.

    Returns
    -------
    np.ndarray
        Simulated price paths with shape (n_sims, steps + 1).
    """

    if S0 <= 0:
        raise ValueError("Initial stock price S0 must be positive.")
    if sigma < 0:
        raise ValueError("Volatility sigma cannot be negative.")
    if T <= 0:
        raise ValueError("Time to maturity T must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")
    if n_sims <= 0:
        raise ValueError("n_sims must be positive.")

    rng = np.random.default_rng(seed)

    dt = T / steps

    Z = rng.standard_normal((n_sims, steps))

    drift = (r - 0.5 * sigma ** 2) * dt
    diffusion = sigma * np.sqrt(dt) * Z

    log_returns = drift + diffusion

    paths = np.empty((n_sims, steps + 1))
    paths[:, 0] = S0
    paths[:, 1:] = S0 * np.exp(np.cumsum(log_returns, axis=1))

    return paths


def simulate_terminal_prices(
    S0: float,
    r: float,
    sigma: float,
    T: float,
    n_sims: int = 100_000,
    seed: int | None = None
) -> np.ndarray:
    """
    Simulate only the terminal stock prices S_T.

    This is faster than simulating full paths and is useful for pricing
    European options, since only the final price is needed.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the stock.
    T : float
        Time to maturity in years.
    n_sims : int
        Number of simulations.
    seed : int | None
        Random seed for reproducibility.

    Returns
    -------
    np.ndarray
        Terminal stock prices with shape (n_sims,).
    """

    if S0 <= 0:
        raise ValueError("Initial stock price S0 must be positive.")
    if sigma < 0:
        raise ValueError("Volatility sigma cannot be negative.")
    if T <= 0:
        raise ValueError("Time to maturity T must be positive.")
    if n_sims <= 0:
        raise ValueError("n_sims must be positive.")

    rng = np.random.default_rng(seed)

    Z = rng.standard_normal(n_sims)

    terminal_prices = S0 * np.exp(
        (r - 0.5 * sigma ** 2) * T
        + sigma * np.sqrt(T) * Z
    )

    return terminal_prices


if __name__ == "__main__":
    paths = simulate_gbm_paths(
        S0=100,
        r=0.05,
        sigma=0.20,
        T=0.5,
        steps=126,
        n_sims=5,
        seed=42
    )

    terminal_prices = simulate_terminal_prices(
        S0=100,
        r=0.05,
        sigma=0.20,
        T=0.5,
        n_sims=5,
        seed=42
    )

    print("Path shape:", paths.shape)
    print("Path terminal prices:", paths[:, -1].round(2))
    print("Direct terminal prices:", terminal_prices.round(2))