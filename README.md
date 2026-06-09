# Monte Carlo Options Pricer

A personal quantitative finance project for pricing European options using Monte Carlo simulation, with Black-Scholes validation, finite-difference Greeks, and visualisation of simulation behaviour.

The project is written from scratch in Python and organised as a small research-style pricing engine, with separate modules for simulation, analytical pricing, Greeks, plotting, and tests.

---

## Overview

This project prices European call and put options by simulating stock price paths under a Geometric Brownian Motion model. The Monte Carlo estimate is then compared against the Black-Scholes analytical price to check convergence and pricing accuracy.

The project also computes option Greeks using finite difference methods, allowing the model to estimate how option value changes with respect to stock price, volatility, time to expiry, and interest rates.

---

## What It Does

* Prices European call and put options using Monte Carlo simulation
* Simulates terminal stock prices under Geometric Brownian Motion
* Validates Monte Carlo prices against the Black-Scholes analytical model
* Computes option Greeks: Delta, Gamma, Theta, Vega, and Rho
* Visualises simulated price paths, payoff distributions, and Monte Carlo convergence
* Includes unit tests for pricing logic, input validation, and model consistency

---

## Project Structure

```text
monte-carlo-options-pricer/
├── src/
│   ├── black_scholes.py   # Black-Scholes analytical pricer
│   ├── simulator.py       # Geometric Brownian Motion simulation engine
│   ├── greeks.py          # Option Greeks via finite differences
│   └── plotter.py         # Visualisations for paths, payoff, and convergence
├── tests/
│   └── test_pricer.py     # Unit tests for pricing and validation
├── outputs/               # Generated charts saved here
├── main.py                # Entry point for running the full pricing pipeline
├── requirements.txt
└── README.md
```

---

## Model Overview

The pricing engine simulates possible future stock prices under a risk-neutral Geometric Brownian Motion process. For each simulated stock price, the option payoff is calculated and discounted back to present value.

For a European call option, the payoff is:

```text
max(S_T - K, 0)
```

For a European put option, the payoff is:

```text
max(K - S_T, 0)
```

The final option price is estimated as the discounted expected payoff across all simulated paths.

---

## Monte Carlo Simulation

The terminal stock price is modelled as:

```text
S_T = S_0 * exp((r - 0.5σ²)T + σ√T * Z)
```

where:

```text
S_T = terminal stock price
S_0 = initial stock price
K   = strike price
r   = risk-free interest rate
σ   = volatility
T   = time to expiry
Z   = standard normal random variable
```

The Monte Carlo pricing process is:

1. Generate many random samples from a standard normal distribution
2. Simulate terminal stock prices using the GBM equation
3. Compute the option payoff for each simulated terminal price
4. Take the average payoff across all simulations
5. Discount the expected payoff back to present value

The option price is estimated by:

```text
price = exp(-rT) * E[payoff]
```

As the number of simulations increases, the Monte Carlo estimate should converge towards the analytical Black-Scholes price.

---

## Black-Scholes Benchmark

The Black-Scholes model provides a closed-form analytical price for European options.

In this project, the Black-Scholes price is used as a benchmark for validating the Monte Carlo simulation. The output compares:

* Monte Carlo estimated price
* 95% confidence interval
* Black-Scholes analytical price
* Absolute difference between both methods

This benchmark helps confirm that the simulation is implemented correctly and that the Monte Carlo result converges as expected.

---

## Option Greeks

The project computes option Greeks using finite difference methods applied to the Black-Scholes pricing function.

| Greek | Meaning                      | Method                                         |
| ----- | ---------------------------- | ---------------------------------------------- |
| Delta | Sensitivity to stock price   | Central difference on stock price              |
| Gamma | Rate of change of Delta      | Second-order central difference on stock price |
| Theta | Sensitivity to time decay    | Difference on time to expiry                   |
| Vega  | Sensitivity to volatility    | Central difference on volatility               |
| Rho   | Sensitivity to interest rate | Central difference on interest rate            |

These Greeks are useful for understanding how option prices respond to changes in the underlying market inputs.

---

## Sample Output

```text
==========================================================
          MONTE CARLO OPTIONS PRICER
==========================================================
  S=100  K=100  r=5%  σ=20%  T=0.5yr
==========================================================

  CALL
  Monte Carlo:   $6.8879 ± 0.0220
  95% CI:        ($6.8448, $6.9311)
  Black-Scholes: $6.8887
  Difference:    $0.0008

  PUT
  Monte Carlo:   $4.4189 ± 0.0156
  95% CI:        ($4.3883, $4.4495)
  Black-Scholes: $4.4197
  Difference:    $0.0008
```

---

## Visualisations

The project generates charts for:

* Simulated GBM stock price paths
* Option payoff distribution
* Monte Carlo convergence against the Black-Scholes price

Generated charts are saved in the `outputs/` folder.

---

## Testing

Unit tests are included to check the main pricing logic and model behaviour.

The tests cover:

* Black-Scholes pricing outputs
* Monte Carlo pricing behaviour
* Input validation
* Put-call parity
* Greeks calculation
* Basic consistency between simulation and analytical pricing

Run all tests with:

```bash
python3 -m pytest tests/ -v
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rileychenau-tech/monte-carlo-options-pricer
cd monte-carlo-options-pricer
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the full pricing pipeline:

```bash
python3 main.py
```

Run individual modules:

```bash
python3 -m src.black_scholes
python3 -m src.simulator
python3 -m src.greeks
python3 -m src.plotter
```

Run all tests:

```bash
python3 -m pytest tests/ -v
```

---

## Requirements

```text
numpy
scipy
matplotlib
pandas
pytest
```

---

## Current Status

* Monte Carlo option pricing completed
* Black-Scholes analytical pricing completed
* Option Greeks calculation completed
* Visualisations completed
* Unit tests completed
* Public GitHub version completed
