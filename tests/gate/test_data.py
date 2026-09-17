"""PROTECTED. Candle caches, backfill and quotes."""
import pandas as pd
import pytest

from bot import config, data


@pytest.fixture
def caches(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STATE", tmp_path)
    monkeypatch.setattr(config, "CANDLES", tmp_path / "candles")
    monkeypatch.setattr(config, "HISTORY", tmp_path / "history")
    return tmp_path


def test_quote_half_spread():
    q = data.Quote(bid=99.95, ask=100.05, last=100.0)
    assert q.mid == pytest.approx(100.0)
    assert q.half_spread_bps == pytest.approx(5.0)


def test_backfill_fills_only_before_the_earliest_live_candle(caches):
    pairs = ["BTC"]
    live = data.SyntheticSource(pairs, n=100, seed=1, start=1_700_000_000)
    data.update_candles(pairs, live)
    hist = data.SyntheticSource(pairs, n=1000, seed=2, start=1_700_000_000 - 1000 * 3600)
    added = data.backfill_if_short(pairs, target_hours=500, history_source=hist, now=1_700_000_000 + 100 * 3600)
    assert added["BTC"] > 0
    h = data.load_history("BTC")
    assert int(h["time"].max()) < 1_700_000_000                       # nothing overlapping the live cache
    assert int(h["time"].min()) >= 1_700_000_000 + 100 * 3600 - 500 * 3600
    merged = data.load_all_candles("BTC")
    assert merged["time"].is_monotonic_increasing and merged["time"].is_unique
    assert len(merged) == len(h) + 100
    # second call: within a day of target, so nothing more is fetched
    again = data.backfill_if_short(pairs, target_hours=500, history_source=hist, now=1_700_000_000 + 100 * 3600)
    assert again == {}


def test_live_rows_win_over_history_on_overlap(caches):
    data.config.HISTORY.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"time": [0, 3600], "open": [1, 1], "high": [1, 1], "low": [1, 1], "close": [1.0, 1.0],
                  "vwap": [1, 1], "volume": [1, 1], "count": [0, 0]}).to_csv(data.history_path("X"), index=False)
    data.save_candles("X", pd.DataFrame({"time": [3600, 7200], "open": [2, 2], "high": [2, 2], "low": [2, 2],
                                         "close": [2.0, 2.0], "vwap": [2, 2], "volume": [1, 1], "count": [1, 1]}))
    merged = data.load_all_candles("X")
    assert list(merged["time"]) == [0, 3600, 7200]
    assert float(merged.loc[merged["time"] == 3600, "close"].iloc[0]) == 2.0


def test_kraken_pair_names():
    assert data.kraken_pair("BTC") == "XBTUSD"
    assert data.kraken_pair("DOGE") == "XDGUSD"
    assert data.kraken_pair("XRP") == "XRPUSD"
