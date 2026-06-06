# 📈 Monte Carlo Options Pricer

> Options pricing using Monte Carlo simulation and Black-Scholes, with Greeks

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Language](https://img.shields.io/badge/python-3.x-blue)
![Level](https://img.shields.io/badge/level-beginner%20→%20intermediate-green)

---

## What Is This Project?

This project builds a financial tool that calculates the fair price of a **stock option** using a technique called **Monte Carlo simulation**.

In plain English: the program runs thousands of "what if?" scenarios for how a stock price might move over time, then uses those scenarios to figure out what an option contract is worth today.

**Options** are contracts that give you the right — but not the obligation — to buy or sell a stock at a specific price in the future. They are used by investors worldwide to manage risk and speculate on price movements. Pricing them accurately is one of the most important problems in modern finance.

---

## Why Build This?

### Real-world relevance
Banks, hedge funds, and trading desks use exactly these methods every day. Building this project from scratch gives direct exposure to how quantitative finance actually works.

### What this project covers

| Area | What you learn |
|---|---|
| 💰 Finance | How options work, why they have value, what Greeks are |
| 📐 Math | Monte Carlo simulation, Geometric Brownian Motion, probability |
| 🐍 Python | NumPy for fast computation, Matplotlib for visualisation |
| ⚙️ Engineering | Validating results, structuring code, writing clean documentation |

### Why Monte Carlo specifically?
The famous Black-Scholes formula works well for simple European options but breaks down for complex ones. Monte Carlo does not have this limitation — it can price almost any option if you can describe its payoff rule, making it the industry standard for complex derivatives.

---

## What This Will Build

By the end of this project, the repository will contain a working Python program that:

- ✅ Accepts user inputs: stock price, strike price, expiry, risk-free rate, volatility
- ✅ Simulates thousands of stock price paths using Geometric Brownian Motion
- ✅ Calculates option price for both **calls** and **puts**
- ✅ Validates results against the **Black-Scholes** closed-form formula
- ✅ Computes the **Greeks** — Delta, Gamma, Vega, Theta, Rho
- ✅ Produces visualisation plots: price paths, payoff distribution, convergence chart

---

## Core Concepts (Plain English)

<details>
<summary><strong>What is an option?</strong></summary>

A **call option** gives you the right to BUY a stock at a fixed price (the strike) on a future date.  
A **put option** gives you the right to SELL a stock at a fixed price on a future date.  
You pay a premium upfront for this right. The question this project answers: *how much should that premium be?*

</details>

<details>
<summary><strong>What is Monte Carlo simulation?</strong></summary>

Imagine flipping a coin 10,000 times and recording every outcome to estimate the probability of heads. Monte Carlo does the same for stock prices — simulate thousands of possible futures, compute the option payoff in each one, and average them. That average (discounted back to today) is the fair price.

</details>

<details>
<summary><strong>What is Black-Scholes?</strong></summary>

A mathematical formula published in 1973 that gives an exact option price for European options. It won the Nobel Prize in Economics in 1997. In this project, it serves as a benchmark to verify that the Monte Carlo results are converging to the right answer.

</details>

<details>
<summary><strong>What are the Greeks?</strong></summary>

The Greeks measure how sensitive an option's price is to different factors:
- **Delta** — how much the price changes when the stock moves $1
- **Gamma** — how fast Delta itself changes
- **Vega** — sensitivity to changes in volatility
- **Theta** — how much value the option loses each day
- **Rho** — sensitivity to interest rate changes

</details>

---

## Project Roadmap

**25 days · 75 hours · 3 hours per day**

| Phase | Topic | What happens | Days |
|---|---|---|---|
| 1 | Setup & Prerequisites | Install Python, NumPy, Matplotlib. Get comfortable with basic syntax | 2 |
| 2 | Options Theory Basics | Learn calls, puts, strike price, expiry, volatility | 3 |
| 3 | Monte Carlo Intuition | Understand random walks, probability, and why simulation works | 3 |
| 4 | Simulate Stock Price Paths | Code Geometric Brownian Motion in NumPy | 4 |
| 5 | Price a European Option | Run 10,000+ paths, compute payoffs, discount to today | 4 |
| 6 | Validate with Black-Scholes | Implement the formula and compare results | 3 |
| 7 | Improve Accuracy | Add antithetic variates, plot convergence | 3 |
| 8 | Package & Present | Clean code, CLI input, output plots | 3 |

---

## Tech Stack

- **Python 3.x** — main language
- **NumPy** — fast array maths and random number generation
- **Matplotlib** — charts and visualisation
- **SciPy** — statistical functions for Black-Scholes (Phase 6+)
- **Git + GitHub** — version control throughout

No paid software. No cloud accounts. Runs entirely on your local machine.

---

## Progress

- [x] Repository created
- [ ] Phase 1 — Setup & prerequisites
- [ ] Phase 2 — Options theory basics
- [ ] Phase 3 — Monte Carlo intuition
- [ ] Phase 4 — Simulate stock price paths
- [ ] Phase 5 — Price a European option
- [ ] Phase 6 — Validate with Black-Scholes
- [ ] Phase 7 — Improve accuracy
- [ ] Phase 8 — Package & present

---

## How to Follow Along

Each phase will be committed to this repository as it is completed. The commit history reflects the exact order things were built — so anyone reading this repo can follow the learning journey from the first line of code to a finished pricer.

If you are reading this, the code does not exist yet. By the time this repo is complete, every concept above will have been implemented, tested, and explained.

---

*Built from scratch as a learning project. No prior finance knowledge required.*