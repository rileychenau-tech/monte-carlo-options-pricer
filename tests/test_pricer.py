"""
Tests for the Monte Carlo Options Pricer project.

This file uses pytest. To run the tests, install pytest first:

    python3 -m pip install pytest

Then run from the project root:

    python3 -m pytest

These tests check:
- Black-Scholes call and put prices
- put-call parity
- option Greeks
- Monte Carlo price accuracy
"""

import pytest
import numpy as np

from src.black_scholes import black_scholes
from src.greeks import compute_greeks
from main import monte_carlo_price


# Black-Scholes tests

def test_bs_call_known_value():
    price = black_scholes(100, 100, 0.05, 0.20, 0.5, "call")
    assert abs(price - 6.8887) < 0.001


def test_bs_put_known_value():
    price = black_scholes(100, 100, 0.05, 0.20, 0.5, "put")
    assert abs(price - 4.4197) < 0.001


def test_put_call_parity():
    S, K, r, sigma, T = 100, 100, 0.05, 0.20, 0.5

    call = black_scholes(S, K, r, sigma, T, "call")
    put = black_scholes(S, K, r, sigma, T, "put")

    parity = S - K * np.exp(-r * T)

    assert abs((call - put) - parity) < 0.0001


def test_bs_expiry():
    call = black_scholes(110, 100, 0.05, 0.20, 0, "call")
    put = black_scholes(90, 100, 0.05, 0.20, 0, "put")

    assert abs(call - 10) < 0.001
    assert abs(put - 10) < 0.001


def test_bs_invalid_option_type():
    with pytest.raises(ValueError):
        black_scholes(100, 100, 0.05, 0.20, 0.5, "banana")


# Greeks tests

def test_delta_range():
    g_call = compute_greeks(100, 100, 0.05, 0.20, 0.5, "call")
    g_put = compute_greeks(100, 100, 0.05, 0.20, 0.5, "put")

    assert 0 < g_call["delta"] < 1
    assert -1 < g_put["delta"] < 0


def test_delta_parity():
    g_call = compute_greeks(100, 100, 0.05, 0.20, 0.5, "call")
    g_put = compute_greeks(100, 100, 0.05, 0.20, 0.5, "put")

    assert abs(g_call["delta"] - g_put["delta"] - 1.0) < 0.001


def test_gamma_equal():
    g_call = compute_greeks(100, 100, 0.05, 0.20, 0.5, "call")
    g_put = compute_greeks(100, 100, 0.05, 0.20, 0.5, "put")

    assert abs(g_call["gamma"] - g_put["gamma"]) < 0.000001


def test_theta_negative_for_atm_call():
    g = compute_greeks(100, 100, 0.05, 0.20, 0.5, "call")

    assert g["theta"] < 0


def test_vega_positive():
    g = compute_greeks(100, 100, 0.05, 0.20, 0.5, "call")

    assert g["vega"] > 0


# Monte Carlo tests

def test_mc_close_to_bs():
    mc, _, _ = monte_carlo_price(
        100, 100, 0.05, 0.20, 0.5,
        n_sims=100_000,
        option_type="call",
        seed=42
    )

    bs = black_scholes(100, 100, 0.05, 0.20, 0.5, "call")

    assert abs(mc - bs) < 0.15


def test_mc_confidence_interval():
    mc, _, ci = monte_carlo_price(
        100, 100, 0.05, 0.20, 0.5,
        n_sims=100_000,
        option_type="call",
        seed=42
    )

    bs = black_scholes(100, 100, 0.05, 0.20, 0.5, "call")

    assert ci[0] < bs < ci[1]