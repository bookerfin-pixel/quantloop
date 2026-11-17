"""Tests for the daily_trend strategy."""
import numpy as np
import pandas as pd

from bot import strategy


def _candles(drift):
    n = 24 * 40
    t = 1_700_000_000 // 86400 * 86400 + np.arange(n) * 3600
    p = 100 * np.exp(drift * np.arange(n))
    mk = lambda p: pd.DataFrame({"time": t, "open": p, "high": p, "low": p, "close": p,
                                 "vwap": p, "volume": 1.0, "count": 1})
    return {"BTC": mk(p), "SOL": mk(p)}


def test_long_when_up_flat_when_down_and_only_named_coins():
    up = strategy.daily_trend(_candles(0.001), {"pairs": ["BTC"]}, {})
    assert up["BTC"].weight == 0.25 and up["SOL"].weight == 0.0
    down = strategy.daily_trend(_candles(-0.001), {"pairs": ["BTC"]}, {})
    assert down["BTC"].weight == 0.0


def test_same_target_every_hour_of_a_day():
    c = _candles(0.001)
    outs = {strategy.daily_trend({p: d.iloc[:k] for p, d in c.items()}, {"pairs": ["BTC"]}, {})["BTC"].weight
            for k in range(24 * 36, 24 * 36 + 24)}
    assert outs == {0.25}
