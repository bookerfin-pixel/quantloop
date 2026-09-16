"""PROTECTED."""
import math

from bot import risk

CFG = {"max_weight_per_pair": 0.25, "max_gross_weight": 1.0, "rebalance_threshold": 0.05,
       "min_trade_notional": 50, "daily_loss_halt": 0.05}


def test_clips_per_pair_and_gross():
    out = risk.apply_limits({"A": 0.9, "B": 0.5, "C": 0.5, "D": 0.5, "E": 0.5, "F": 0.5}, CFG)
    assert max(out.values()) <= 0.25 + 1e-12
    assert sum(out.values()) <= 1.0 + 1e-12


def test_no_negatives_or_nans():
    out = risk.apply_limits({"A": -0.3, "B": math.nan, "C": float("inf"), "D": "junk"}, CFG)
    assert out == {"A": 0.0, "B": 0.0, "C": 0.0, "D": 0.0}


def test_worth_trading_threshold_and_full_exit():
    ok, why = risk.worth_trading(0.22, 0.20, 10_000, CFG)
    assert not ok and "threshold" in why
    ok, _ = risk.worth_trading(0.0, 0.03, 10_000, CFG)       # closing a position is always allowed
    assert ok
    ok, why = risk.worth_trading(0.004, 0.0, 1_000, CFG)
    assert not ok


def test_daily_halt():
    assert risk.daily_halt_triggered(9_400, 10_000, CFG)
    assert not risk.daily_halt_triggered(9_600, 10_000, CFG)
    assert not risk.daily_halt_triggered(9_000, 0, CFG)
