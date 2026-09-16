"""Market data: Kraken public OHLC and ticker, a growing local candle cache,
and a synthetic source for tests and dry runs. PROTECTED.

Why Kraken: Binance's API refuses US IP addresses and GitHub Actions runners
sit in the US. Kraken's public endpoints need no key and serve the same majors.
Costs are still modelled on Binance fees (configs/risk.yaml).
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass

import numpy as np
import pandas as pd
import requests

from . import config

KRAKEN = "https://api.kraken.com/0/public"
KRAKEN_NAMES = {"BTC": "XBT"}  # Kraken still calls bitcoin XBT
CANDLE_COLUMNS = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]
INTERVAL_MIN = 60
MAX_CACHE_ROWS = 24 * 366 * 2  # two years of hourly candles per pair


@dataclass
class Quote:
    bid: float
    ask: float
    last: float


def kraken_pair(pair: str, quote: str = "USD") -> str:
    return f"{KRAKEN_NAMES.get(pair, pair)}{quote}"


def _kraken_get(path: str, params: dict, retries: int = 3) -> dict:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            r = requests.get(f"{KRAKEN}/{path}", params=params, timeout=20)
            r.raise_for_status()
            body = r.json()
            if body.get("error"):
                raise RuntimeError(f"kraken {path} error: {body['error']}")
            return body["result"]
        except Exception as e:  # noqa: BLE001 - we retry on anything transient
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"kraken {path} failed after {retries} attempts: {last_err}")


def _first_pair_key(result: dict) -> str:
    keys = [k for k in result if k != "last"]
    if not keys:
        raise RuntimeError("kraken returned no pair data")
    return keys[0]


class KrakenSource:
    def __init__(self, quote: str = "USD"):
        self.quote = quote

    def ohlc(self, pair: str, since: int | None = None) -> pd.DataFrame:
        params = {"pair": kraken_pair(pair, self.quote), "interval": INTERVAL_MIN}
        if since:
            params["since"] = int(since)
        result = _kraken_get("OHLC", params)
        rows = result[_first_pair_key(result)]
        df = pd.DataFrame(rows, columns=CANDLE_COLUMNS)
        for c in CANDLE_COLUMNS:
            df[c] = pd.to_numeric(df[c])
        df["time"] = df["time"].astype("int64")
        # The final row is the candle still forming. Only closed candles are usable.
        now = int(time.time())
        df = df[df["time"] + INTERVAL_MIN * 60 <= now]
        time.sleep(0.35)  # stay well inside Kraken's public rate limit
        return df.reset_index(drop=True)

    def quote_for(self, pair: str) -> Quote:
        result = _kraken_get("Ticker", {"pair": kraken_pair(pair, self.quote)})
        t = result[_first_pair_key(result)]
        time.sleep(0.35)
        return Quote(bid=float(t["b"][0]), ask=float(t["a"][0]), last=float(t["c"][0]))


class SyntheticSource:
    """Geometric random walk with slow regime drift. Deterministic per seed so
    tests and dry runs are repeatable. Quotes are the last close with a spread."""

    def __init__(self, pairs: list[str], n: int = 900, seed: int = 7, start: int | None = None):
        self.pairs = pairs
        self.n = n
        self.seed = seed
        self.start = start or (int(time.time()) // 3600 * 3600 - n * 3600)
        self._frames = {p: self._make(i) for i, p in enumerate(pairs)}

    def _make(self, i: int) -> pd.DataFrame:
        rng = np.random.default_rng(self.seed + i)
        n = self.n
        drift = np.zeros(n)
        regime = 0.0
        for k in range(n):
            if k % 120 == 0:
                regime = rng.normal(0, 0.0006)
            drift[k] = regime
        rets = rng.normal(0, 0.006, n) + drift
        close = 100.0 * (1 + i) * np.exp(np.cumsum(rets))
        open_ = np.roll(close, 1)
        open_[0] = close[0]
        high = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, 0.002, n)))
        low = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, 0.002, n)))
        times = self.start + np.arange(n) * 3600
        return pd.DataFrame(
            {"time": times, "open": open_, "high": high, "low": low, "close": close,
             "vwap": (open_ + close) / 2, "volume": rng.uniform(10, 100, n), "count": 50}
        )

    def ohlc(self, pair: str, since: int | None = None) -> pd.DataFrame:
        df = self._frames[pair]
        if since:
            df = df[df["time"] > since]
        return df.reset_index(drop=True)

    def quote_for(self, pair: str) -> Quote:
        last = float(self._frames[pair]["close"].iloc[-1])
        return Quote(bid=last * 0.9995, ask=last * 1.0005, last=last)


def get_source(pairs: list[str], quote: str = "USD"):
    if os.environ.get("QUANTLOOP_FAKE_DATA"):
        return SyntheticSource(pairs, seed=int(os.environ.get("QUANTLOOP_FAKE_SEED", "7")))
    return KrakenSource(quote)


# --- local cache -----------------------------------------------------------

def cache_path(pair: str):
    config.CANDLES.mkdir(parents=True, exist_ok=True)
    return config.CANDLES / f"{pair}.csv"


def load_candles(pair: str) -> pd.DataFrame:
    p = cache_path(pair)
    if not p.exists():
        return pd.DataFrame(columns=CANDLE_COLUMNS)
    df = pd.read_csv(p)
    df["time"] = df["time"].astype("int64")
    return df


def save_candles(pair: str, df: pd.DataFrame) -> None:
    df = df.drop_duplicates("time").sort_values("time").tail(MAX_CACHE_ROWS)
    df.to_csv(cache_path(pair), index=False)


def update_candles(pairs: list[str], source) -> dict[str, pd.DataFrame]:
    """Fetch new closed candles for every pair, merge into the cache, return
    the merged frames. A pair that fails to fetch keeps its cached data so one
    bad request does not stall the whole run."""
    out: dict[str, pd.DataFrame] = {}
    for pair in pairs:
        cached = load_candles(pair)
        since = int(cached["time"].max()) if len(cached) else None
        try:
            fresh = source.ohlc(pair, since=since)
        except Exception as e:  # noqa: BLE001
            print(f"[data] {pair}: fetch failed ({e}); using cached candles only")
            fresh = pd.DataFrame(columns=CANDLE_COLUMNS)
        merged = pd.concat([cached, fresh], ignore_index=True) if len(fresh) else cached
        merged = merged.drop_duplicates("time").sort_values("time").reset_index(drop=True)
        if len(merged):
            save_candles(pair, merged)
        out[pair] = merged
    return out


def quotes(pairs: list[str], source) -> dict[str, Quote]:
    out = {}
    for pair in pairs:
        try:
            out[pair] = source.quote_for(pair)
        except Exception as e:  # noqa: BLE001
            print(f"[data] {pair}: quote failed ({e}); pair skipped this run")
    return out
