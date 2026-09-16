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
