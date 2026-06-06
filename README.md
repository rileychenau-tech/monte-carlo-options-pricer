# 📈 Monte Carlo Options Pricer

> A quantitative finance project pricing European options via Monte Carlo simulation, validated against Black-Scholes, with Greeks and visualisations.

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Language](https://img.shields.io/badge/python-3.14-blue)
![Topics](https://img.shields.io/badge/topics-quant%20finance%20%7C%20simulation%20%7C%20derivatives-lightgrey)

---

## Overview

This project implements a **European options pricer** using Monte Carlo simulation in Python. It models stock price evolution via **Geometric Brownian Motion**, prices call and put options by averaging discounted payoffs across thousands of simulated paths, and validates every result against the **Black-Scholes analytical formula**.

The goal is to demonstrate a working understanding of derivatives pricing, numerical methods, and professional Python project structure — relevant to quantitative finance, risk, and data-driven roles.

---

## Features

| Feature | Status |
|---|---|
| Monte Carlo simulation (European call & put) | ✅ Complete |
| Geometric Brownian Motion path simulation | ✅ Complete |
| Black-Scholes analytical validation | ✅ Complete |
| Visualisations (paths, payoff distribution, convergence) | ✅ Complete |
| Option Greeks (Δ, Γ, ν, Θ, ρ) | 🔄 In progress |
| Variance reduction — antithetic variates | 🔄 In progress |
| Unit tests | 🔄 In progress |

---

## Example

```python
from src.simulator import MonteCarloSimulator

pricer = MonteCarloSimulator(
    S=100,      # Current stock price
    K=100,      # Strike price
    T=1.0,      # Time to expiry (years)
    r=0.05,     # Risk-free rate
    sigma=0.2,  # Volatility
    n_paths=100_000
)

print(pricer.price(option_type="call"))
# Monte Carlo:   10.45
# Black-Scholes: 10.45
```

---

## Visualisations

### Simulated Stock Price Paths
Thousands of possible stock price trajectories under Geometric Brownian Motion.

### Payoff Distribution
Histogram of option payoffs across all simulated paths, showing the distribution of outcomes.

### Convergence Chart
How the Monte Carlo price converges toward the Black-Scholes value as the number of paths increases — demonstrating the law of large numbers in practice.

---

## Project Structure

```
monte-carlo-options-pricer/
│
├── src/
│   ├── simulator.py       # Monte Carlo engine & GBM path simulation
│   ├── black_scholes.py   # Analytical Black-Scholes formula
│   ├── greeks.py          # Option Greeks via finite differences
│   └── plotter.py         # Visualisation functions
│
├── tests/                 # Unit tests
├── notebooks/             # Exploratory Jupyter notebooks
├── main.py                # Entry point — run from command line
├── requirements.txt       # Dependencies
└── README.md
```

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/rileychenau-tech/monte-carlo-options-pricer.git
cd monte-carlo-options-pricer
```

**2. Install dependencies**
```bash
pip3 install -r requirements.txt
```

**3. Run the pricer**
```bash
python3 main.py
```

---

## Tech Stack

- **Python 3.14** — core language
- **NumPy** — vectorised simulation and random number generation
- **SciPy** — statistical functions for Black-Scholes
- **Matplotlib** — visualisation

---

## Key Concepts

<details>
<summary><strong>Geometric Brownian Motion</strong></summary>

GBM is the standard model for stock price evolution. It assumes prices follow a random walk with a drift (expected return) and diffusion (volatility) term. The discrete-time form used in simulation is:

```
S(t+Δt) = S(t) × exp((r - σ²/2)Δt + σ√Δt × Z)
```

where Z ~ N(0,1) is a standard normal random variable.

</details>

<details>
<summary><strong>Monte Carlo Pricing</strong></summary>

1. Simulate N stock price paths from today to expiry
2. Compute the option payoff for each path — max(S_T - K, 0) for a call
3. Average the payoffs
4. Discount back to today using the risk-free rate
5. As N → ∞, the price converges to the true theoretical value

</details>

<details>
<summary><strong>Black-Scholes Validation</strong></summary>

Black-Scholes gives a closed-form analytical price for European options. Since Monte Carlo is a numerical approximation, comparing the two confirms the simulation is working correctly and converging at the expected rate.

</details>

<details>
<summary><strong>Option Greeks</strong></summary>

The Greeks measure how sensitive the option price is to each input:

| Greek | Measures sensitivity to... |
|---|---|
| Delta (Δ) | Stock price movement |
| Gamma (Γ) | Rate of change of Delta |
| Vega (ν) | Volatility |
| Theta (Θ) | Time decay |
| Rho (ρ) | Interest rate changes |

</details>

---

## Roadmap

- [x] Repository structure set up
- [x] GBM path simulation
- [x] Monte Carlo pricer (call & put)
- [x] Black-Scholes validation
- [x] Visualisations
- [ ] Option Greeks
- [ ] Variance reduction (antithetic variates)
- [ ] Unit tests
- [ ] CLI with user input

---

*Built as a quantitative finance portfolio project. Demonstrates Monte Carlo methods, derivatives pricing, and professional Python project structure.*