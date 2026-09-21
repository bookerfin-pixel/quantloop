"""Tests for bot/strategy.py. The agent may add to this file when it adds a strategy."""
import pandas as pd
import pytest

from bot import data, strategy

PAIRS = ["BTC", "ETH", "SOL"]


def candles(n=500, seed=3):
    src = data.SyntheticSource(PAIRS, n=n, seed=seed, start=1_700_000_000)
    return {p: src.ohlc(p) for p in PAIRS}


@pytest.mark.parametrize("name", sorted(strategy.STRATEGIES))
def test_every_strategy_returns_valid_targets(name):
    fn = strategy.get(name)
    out = strategy.normalise(fn(candles(), {}, {}))
    assert set(out) == set(PAIRS)
    for pair, t in out.items():
        assert 0.0 <= t.weight <= 1.0, (pair, t)
        assert isinstance(t.reason, str) and t.reason, "every decision needs a reason"


@pytest.mark.parametrize("name", sorted(strategy.STRATEGIES))
def test_strategies_go_flat_on_short_history(name):
    fn = strategy.get(name)
    short = {p: df.tail(10) for p, df in candles().items()}
    out = strategy.normalise(fn(short, {}, {}))
    assert all(t.weight == 0.0 for t in out.values())


def test_momentum_enters_on_uptrend_and_stays_flat_in_downtrend():
    up = pd.DataFrame({"close": [100 * 1.002 ** i for i in range(300)]})
    down = pd.DataFrame({"close": [100 * 0.998 ** i for i in range(300)]})
    for df in (up, down):
        df["open"] = df["close"]; df["high"] = df["close"]; df["low"] = df["close"]
        df["time"] = range(300); df["vwap"] = df["close"]; df["volume"] = 1; df["count"] = 1
    out = strategy.ts_momentum({"UP": up, "DOWN": down}, {}, {})
    assert out["UP"].weight > 0 and "enter long" in out["UP"].reason
    assert out["DOWN"].weight == 0 and "flat" in out["DOWN"].reason


def test_momentum_hysteresis_holds_through_small_dip():
    closes = [100 * 1.002 ** i for i in range(300)]
    closes[-1] = closes[-2] * 0.995          # a small dip: still inside the exit band
    df = pd.DataFrame({"close": closes, "open": closes, "high": closes, "low": closes,
                       "time": range(300), "vwap": closes, "volume": 1, "count": 1})
    held = strategy.ts_momentum({"X": df}, {}, {"X": 0.2})
    assert held["X"].weight > 0 and "stay long" in held["X"].reason


def test_unknown_strategy_raises():
    with pytest.raises(KeyError):
        strategy.get("does_not_exist")


def _breakout_params(**overrides):
    params = dict(compression_hours=48, lookback_hours=400, vol_percentile=0.25,
                  breakout_hours=30, squeeze_memory_hours=20, exit_hours=20)
    params.update(overrides)
    return params


def _ohlc(closes):
    df = pd.DataFrame({"close": closes})
    df["open"] = df["close"]; df["high"] = df["close"]; df["low"] = df["close"]
    df["time"] = range(len(closes)); df["vwap"] = df["close"]; df["volume"] = 1; df["count"] = 1
    return df


def test_vol_breakout_enters_after_squeeze_then_new_high():
    import numpy as np
    rng = np.random.default_rng(0)
    noisy = 100 * np.exp(np.cumsum(rng.normal(0, 0.01, 420)))       # normal chop, vol ~1%/h
    quiet = noisy[-1] * np.exp(np.cumsum(rng.normal(0, 0.0005, 40)))  # squeeze: vol ~0.05%/h
    breakout = [quiet[-1] * 1.05]                                     # a clean new high
    closes = list(noisy) + list(quiet) + breakout
    df = _ohlc(closes)
    out = strategy.vol_breakout({"X": df}, _breakout_params(), {})
    assert out["X"].weight > 0 and "enter long" in out["X"].reason


def test_vol_breakout_flat_without_squeeze():
    import numpy as np
    rng = np.random.default_rng(1)
    noisy = 100 * np.exp(np.cumsum(rng.normal(0, 0.01, 450)))
    breakout = [noisy[-1] * 1.1]                                      # new high, but no prior squeeze
    df = _ohlc(list(noisy) + breakout)
    out = strategy.vol_breakout({"X": df}, _breakout_params(), {})
    assert out["X"].weight == 0.0 and "flat" in out["X"].reason


def test_vol_breakout_exits_on_breakdown():
    closes = [100 + i * 0.1 for i in range(450)] + [90]                # sharp breakdown
    df = _ohlc(closes)
    out = strategy.vol_breakout({"X": df}, _breakout_params(), {"X": 0.2})
    assert out["X"].weight == 0.0 and "exit" in out["X"].reason


def _swing_params(**overrides):
    params = dict(recent_hours=20, min_higher_low=0.03, exit_hours=10, vol_lookback_hours=20)
    params.update(overrides)
    return params


def test_swing_reversal_enters_on_higher_low_breakout():
    # older low at 80 (first half), recent low at 85 (a higher low), reaction
    # high of 95 between them, then a close above it.
    first_half = [100, 90, 90, 80, 90, 95] + [92] * 15
    second_half = [90, 88, 85, 87, 90] + [90] * 15
    closes = first_half + second_half + [96]
    df = _ohlc(closes)
    out = strategy.swing_reversal({"X": df}, _swing_params(), {})
    assert out["X"].weight > 0 and "enter long" in out["X"].reason


def test_swing_reversal_flat_without_higher_low():
    # recent low (80) is no higher than the older low (80): no reversal.
    first_half = [100, 90, 90, 80, 90, 95] + [92] * 15
    second_half = [90, 88, 80, 87, 90] + [90] * 15
    closes = first_half + second_half + [96]
    df = _ohlc(closes)
    out = strategy.swing_reversal({"X": df}, _swing_params(), {})
    assert out["X"].weight == 0.0 and "not a higher low" in out["X"].reason


def test_swing_reversal_exits_below_recent_low():
    closes = [100 + i * 0.1 for i in range(41)] + [80]  # sharp breakdown below the trailing exit low
    df = _ohlc(closes)
    out = strategy.swing_reversal({"X": df}, _swing_params(), {"X": 0.2})
    assert out["X"].weight == 0.0 and "exit" in out["X"].reason
