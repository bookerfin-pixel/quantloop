"""Every coin Binance has quoted in USDT, the dead with the living. PROTECTED.

Why it exists. The wide data (bot/wide.py) is the hundred or so coins most
traded on Kraken today, and their past is a survivor's past: the coins that a
rule buying what went up would have bought on the way up and held into nothing
are not in it, so any such rule reads better on it than it would have done.
Binance keeps a public archive of the daily candles of every pair it has
listed, also after it delists one, and GitHub's runners can read it (the wide
collector has probed it every day since 2026-10-07). This job copies the daily
candles of every pair quoted in USDT from January 2018 on, so that a study can
take the coins as they were on each day, the ones that later died among them.

What it writes, under state/wide/binance/:

  months/<YYYY-MM>.csv.gz  every pair's daily candles for that month, one row a
                           pair a UTC day it has a candle for: symbol, day, open,
                           high, low, close, volume (in coins), quote_volume (in
                           USDT, dollars give or take the peg), trades,
                           taker_buy_quote_volume. Prices are the archive's as
                           they are, their trailing zeros dropped; volumes are
                           rounded, in coins to eight significant figures and in
                           USDT to the whole dollar.
  pairs.json               every USDT pair the archive or Binance's list of
                           symbols knows of: its status on Binance today, where
                           it was found, its first and last month in the archive,
                           and why it was left out, if it was.
  status.json              the last run that did something, and which months
                           are settled.

When. The archive puts a month's files up in the first days of the month after.
A month is sought from the 3rd of the month after, and again on each day until
a run on or after the 8th finds it whole: no file that failed, a file from
every pair Binance still trades that had one the month before, and at least
nine in ten as many pairs as then. Then it is settled and never asked for
again. On the other days a run asks nothing and writes nothing. The days of
the month under way are not in it.

Left out: dollar, euro, money and gold tokens and wrapped or staked copies of
other coins (PEGGED: configs/wide.yaml's list and Binance's own), and Binance's
leveraged tokens (BTCUP, ETHDOWN, BULL, EOSBEAR and the like: a name that ends
in UP, DOWN, BULL or BEAR and whose stem is another pair's coin, or nothing).
A coin that trades within 3% of a dollar is kept out of the list on the days it
does so, whatever it is called (listing()).

Where the pairs come from. The archive is a bucket on Amazon S3, and the list
of its folders is the list of every pair it has ever held (LISTING). Binance's
list of symbols (exchangeInfo, on its market data only host) gives each pair's
status today, and stands in when the archive's list cannot be read, though it
leaves out pairs delisted long ago. The run stops, red, with nothing written
but status.json, when neither can be read; when fewer than MIN_ENDED of the
pairs it keeps end before the newest month (a history of survivors, which is
what this exists to avoid); and when many pairs Binance trades today are not
in the archive's list (a list that was cut off). A file that cannot be fetched
is named in status.json and asked for again by the next run, and its month is
not settled until it comes; nor is any month whose pairs came from Binance's
list alone. A run has BUDGET_S seconds, looked at before each file: what it
had no time for waits for the next run. A run that fails in a way none of
this foresaw writes status.json saying so.

Reading it back. load() gives the candles. A pair's candles are one coin
unless they stop for more than LONG_GAP_DAYS days (delisted and listed again,
which no holder sat through), or stop and come back at more than JUMP times
the price they left at (a token swapped at a ratio, not a move): what comes
after is taken for another coin, named with #2 after it. A shorter stop is a
suspension, and a holder bears what the price did meanwhile, a fall as much
as a rise: one that comes back at under a fifth is kept as one coin and
listed in status.json to be looked at, since a crash in a halt and a swap at
a ratio look the same from here. (LUNAUSDT, which Binance gave to a new LUNA
weeks after the old one collapsed in May 2022, should read as LUNA and
LUNA#2.) panel() puts every coin side by side; returns() gives each coin's
return from one close to the next, a suspension booked on the day it trades
again; listing(n) says which coins were the n most traded on each day,
judged only on the days before it.

`python -m bot.binance` prints the last run and only reads (`python -m
bot.wide` prints the same lines under its own). `--collect` is the workflow's
business (.github/workflows/binance.yml): it writes state/, and the gate
refuses a pull request that changes state/. Nothing here places an order,
needs a key, or touches an account, and no account and no strategy reads it.
"""

from __future__ import annotations

import gzip
import io
import json
import re
import sys
import threading
import time
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from decimal import ROUND_HALF_EVEN, Decimal, InvalidOperation
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from . import config

ARCHIVE = "https://data.binance.vision"
LISTING = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"   # the bucket behind ARCHIVE; it lists, ARCHIVE serves
API = "https://data-api.binance.vision/api/v3"                            # Binance's market data only host
MONTHLY = "data/spot/monthly/klines/"
QUOTE = "USDT"
FIRST_MONTH = "2018-01"
COLUMNS = ["symbol", "day", "open", "high", "low", "close", "volume", "quote_volume", "trades", "taker_buy_quote_volume"]
HEADER = ",".join(COLUMNS)
SYMBOL = re.compile(r"[A-Z0-9]{1,30}USDT")
MONTH_KEY = re.compile(r"-1d-(\d{4}-\d{2})\.zip$")
DAY = 86400

PEGGED = frozenset({
    # what configs/wide.yaml leaves out of Kraken's list
    "USDT", "USDC", "DAI", "PYUSD", "TUSD", "USDD", "USDE", "USDS", "FDUSD", "RLUSD", "USDG", "USD1", "USDQ", "USDR",
    "GUSD", "BUSD", "EURT", "EURC", "EURR", "EURQ", "EUR", "GBP", "AUD", "CAD", "CHF", "JPY", "AED", "PAXG", "XAUT",
    "WBTC", "TBTC", "CBETH", "STETH", "WSTETH", "MSOL", "JITOSOL", "BRL1",
    # and what Binance has quoted in USDT besides: dollar tokens old and new, money tokens, gold, wrapped and staked copies
    "USDP", "PAX", "USDSB", "TUSDB", "SUSD", "UST", "AEUR", "EURI", "BFUSD", "XUSD", "VAI", "IDRT", "BIDR", "BVND",
    "BKRW", "TRY", "RUB", "UAH", "NGN", "ZAR", "BRL", "ARS", "MXN", "PLN", "RON", "CZK", "IDR", "COP",
    "BETH", "WBETH", "BNSOL", "RENBTC", "BTCB",
})
LEVERAGED_ENDINGS = ("DOWN", "BULL", "BEAR", "UP")

SOUGHT_FROM_DAY = 3        # from this day of a month the month before is sought
SETTLED_FROM_DAY = 8       # a run on or after this day of the month after settles a month it finds whole
LATE_DAY = 20              # a month not settled by this day of the month after is reported
WHOLE_SHARE = 0.9          # whole: at least this share of the month before's pairs
MIN_ENDED = 100            # fewer kept pairs than this that end before the newest month: survivors only
CUT_OFF_SHARE = 0.1        # more than this share of the pairs Binance trades today missing from the archive's list: cut off
LONG_GAP_DAYS = 30         # candles that stop for more days than this are another coin when they come back: delisted
                           # and listed again, which a holder could not have sat through
JUMP = 5.0                 # ... and so are candles that stop and come back above this many times the price they left at
FIRST_RUN_BY = "2026-11-24"   # no run on record after this day is reported: the job was put in on 2026-11-10
LIST_WINDOW = 30           # listing(): days of dollars traded the ranking takes the median of
LIST_MIN_DAYS = 60         # listing(): days with a candle a coin needs behind it before it can rank
PEG_BAND = 0.03            # listing(): a median close this near a dollar ...
PEG_RANGE = 1.04           # ... with its highest close this near its lowest over LIST_WINDOW days: a dollar token
WORKERS = 8                # requests at once: the archive is a CDN made for this, and eight is polite to it
BUDGET_S = 40 * 60         # a run's time; the job's limit (60 minutes) leaves room to commit
MAX_PAGES = 200            # pages of a listing; the archive's whole list of spot pairs is a few


class BinanceError(RuntimeError):
    pass


def _now() -> int:
    return int(time.time())


def _clock() -> float:
    return time.monotonic()


def _sleep(seconds: float) -> None:
    time.sleep(seconds)


# --- paths and months ------------------------------------------------------------

def root() -> Path:
    return config.STATE / "wide" / "binance"


def month_path(month: str) -> Path:
    return root() / "months" / f"{month}.csv.gz"


def _utc(ts: int) -> datetime:
    return datetime.fromtimestamp(int(ts), timezone.utc)


def _next(month: str) -> str:
    y, m = int(month[:4]), int(month[5:7])
    return f"{y + 1:04d}-01" if m == 12 else f"{y:04d}-{m + 1:02d}"


def _prev(month: str) -> str:
    y, m = int(month[:4]), int(month[5:7])
    return f"{y - 1:04d}-12" if m == 1 else f"{y:04d}-{m - 1:02d}"


def months_from(first: str, last: str) -> list[str]:
    out, m = [], first
    while m <= last:
        out.append(m)
        m = _next(m)
    return out


def newest_month(now: int | None = None) -> str:
    """The newest month whose files the archive should have: the month before, from the 3rd."""
    today = _utc(now if now is not None else _now())
    last = _prev(today.strftime("%Y-%m"))
    return last if today.day >= SOUGHT_FROM_DAY else _prev(last)


def due_month(now: int | None = None) -> str:
    """The newest month that should be settled by now: the month before, from the 20th."""
    today = _utc(now if now is not None else _now())
    last = _prev(today.strftime("%Y-%m"))
    return last if today.day >= LATE_DAY else _prev(last)


def _month_ms(month: str) -> int:
    return int(datetime(int(month[:4]), int(month[5:7]), 1, tzinfo=timezone.utc).timestamp()) * 1000


# --- asking ----------------------------------------------------------------------

_local = threading.local()


def _session() -> requests.Session:
    s = getattr(_local, "session", None)
    if s is None:
        s = _local.session = requests.Session()
        s.headers["User-Agent"] = "quantloop/1.0 (research, daily candles)"
    return s


def get(url: str, params: dict | None = None, tries: int = 3, timeout: float = 30.0) -> tuple[int | None, bytes | None, str]:
    """One GET. Returns (http status or None, the body when the status is 200, a note).
    Tried again only when the request could not be made, the server failed or it
    said to slow down; any other answer is returned at once."""
    note = ""
    for attempt in range(tries):
        try:
            r = _session().get(url, params=params, timeout=timeout)
        except Exception as e:  # noqa: BLE001
            note = f"{type(e).__name__}: {e}"[:200]
            _sleep(2.0 * (attempt + 1))
            continue
        if r.status_code in (418, 429) or r.status_code >= 500:
            note = f"http {r.status_code}"
            _sleep(5.0 * (attempt + 1))
            continue
        if r.status_code != 200:
            return r.status_code, None, f"http {r.status_code}"
        return 200, r.content, ""
    return None, None, note or "no answer"


def get_json(url: str, params: dict | None = None) -> tuple[int | None, object, str]:
    status, body, note = get(url, params)
    if status != 200 or body is None:
        return status, None, note
    try:
        return status, json.loads(body), ""
    except ValueError:
        return status, None, f"not JSON, {len(body)} bytes"


def _map(fn, items: list) -> list:
    """fn over items, WORKERS at a time, the answers in the order of the items. fn must not raise."""
    if not items:
        return []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        return list(pool.map(fn, items))


def list_bucket(prefix: str, delimiter: str | None = "/") -> tuple[list[str], str]:
    """The archive's folders (with a delimiter) or files (without) under prefix, every page of
    them. Returns (names, note); a note that is not empty says the list is not whole."""
    found, marker = [], ""
    for _ in range(MAX_PAGES):
        params = {"prefix": prefix}
        if delimiter:
            params["delimiter"] = delimiter
        if marker:
            params["marker"] = marker
        status, body, note = get(LISTING, params)
        if status != 200 or body is None:
            return found, note or f"http {status}"
        try:
            page = ET.fromstring(body)
        except ET.ParseError as e:
            return found, f"not a bucket listing ({e})"[:200]
        if not page.tag.endswith("ListBucketResult"):
            return found, f"not a bucket listing (<{page.tag[-40:]}>)"
        names = [e.text for e in page.findall("{*}CommonPrefixes/{*}Prefix") + page.findall("{*}Contents/{*}Key") if e.text]
        found += names
        if (page.findtext("{*}IsTruncated") or "").strip().lower() != "true":
            return found, ""
        # a listing with a delimiter says where the next page starts; one without does not, and goes on after its last name
        nxt = (page.findtext("{*}NextMarker") or "").strip() or (max(names) if names else "")
        if not nxt or nxt <= marker:
            return found, "the listing says there is more and gives no place to go on from"
        marker = nxt
    return found, f"the listing ran past {MAX_PAGES} pages"


def archive_symbols() -> tuple[list[str], list[str], str]:
    """Every USDT pair with a folder of monthly candles in the archive, delisted ones included.
    Returns (pairs, folders ending in USDT whose name this job does not read, note)."""
    names, note = list_bucket(MONTHLY, "/")
    folders = sorted({n[len(MONTHLY):].strip("/") for n in names if n.startswith(MONTHLY)})
    syms = [f for f in folders if SYMBOL.fullmatch(f)]
    unread = [f for f in folders if f.endswith(QUOTE) and not SYMBOL.fullmatch(f)]   # a name in other letters, say
    if not note and not syms:
        note = "the archive's list holds no USDT pair"
    return syms, unread, note


def archive_months(symbol: str) -> tuple[list[str], str]:
    """The months the archive has a file of daily candles for, for one pair."""
    folder = f"{MONTHLY}{symbol}/1d/"
    names, note = list_bucket(folder, None)
    months = sorted({m.group(1) for n in names if n.startswith(f"{folder}{symbol}-1d-") and (m := MONTH_KEY.search(n))})
    return months, note


def api_months(symbol: str) -> tuple[list[str], str]:
    """The fallback for archive_months: the months Binance's own monthly candles cover, for one pair."""
    status, body, note = get_json(f"{API}/klines", {"symbol": symbol, "interval": "1M",
                                                     "startTime": _month_ms(FIRST_MONTH), "limit": 1000})
    if status == 400:
        return [], ""                                  # a pair Binance no longer knows: none on this road
    if status != 200 or not isinstance(body, list):
        return [], note or f"http {status}"
    months = set()
    for row in body:
        if isinstance(row, list) and row and str(row[0]).isdigit():
            months.add(_utc(int(row[0]) // 1000).strftime("%Y-%m"))
    return sorted(months), ""


def exchange_info() -> tuple[dict[str, dict], str]:
    """Every pair quoted in USDT on Binance's list of symbols, whatever its status (TRADING, BREAK, ...)."""
    status, body, note = get_json(f"{API}/exchangeInfo", {"showPermissionSets": "false"})
    if status == 400:
        status, body, note = get_json(f"{API}/exchangeInfo")      # a host that does not know the parameter
    if status != 200 or not isinstance(body, dict) or not isinstance(body.get("symbols"), list):
        return {}, note or f"http {status}, no list of symbols"
    out = {}
    for s in body["symbols"]:
        if isinstance(s, dict) and s.get("quoteAsset") == QUOTE and isinstance(s.get("symbol"), str) \
                and SYMBOL.fullmatch(s["symbol"]):
            out[s["symbol"]] = {"status": str(s.get("status") or "?"), "base": str(s.get("baseAsset") or s["symbol"][:-len(QUOTE)])}
    return out, ("" if out else "no USDT pair in the answer")


# --- what is kept ----------------------------------------------------------------

def coin_of(symbol: str) -> str:
    return symbol[:-len(QUOTE)] if symbol.endswith(QUOTE) else symbol


def leave_out(coin: str, coins: set[str]) -> str:
    """Why a coin is left out ('' when it is kept). coins: every coin quoted in USDT, kept or not."""
    if coin in PEGGED:
        return "pegged"
    for ending in LEVERAGED_ENDINGS:
        if coin.endswith(ending):
            stem = coin[:-len(ending)]
            # BTCUP's stem is BTC. JUP's is J and SYRUP's SYR: coins of their own, kept
            if stem == "" or (len(stem) >= 3 and stem in coins):
                return "leveraged token"
    return ""


# --- the files -------------------------------------------------------------------

def _dec(text: str) -> Decimal:
    try:
        d = Decimal(text)
    except InvalidOperation:
        raise ValueError(f"not a number: {text[:20]!r}") from None
    if not d.is_finite() or d < 0:
        raise ValueError(f"not a figure a candle holds: {text[:20]!r}")
    return d


def _num(text: str) -> str:
    """A price as the archive has it, its trailing zeros dropped."""
    return format(_dec(text).normalize(), "f")


def _coins(text: str) -> str:
    """A volume in coins to eight significant figures: the archive's last digits are noise to a study,
    and they are most of what the files would weigh."""
    d = _dec(text)
    if d == 0:
        return "0"
    return format(d.quantize(Decimal(1).scaleb(d.adjusted() - 7), rounding=ROUND_HALF_EVEN).normalize(), "f")


def _dollars(text: str) -> str:
    """A volume in USDT to the whole dollar, for the same reason."""
    return str(int(_dec(text).quantize(Decimal(1), rounding=ROUND_HALF_EVEN)))


def read_zip(blob: bytes, symbol: str, month: str) -> tuple[list[list[str]], int]:
    """One monthly file of daily candles as rows of COLUMNS. Returns (rows, rows left out because a
    price in them was not above nothing). Raises ValueError on a file that is not what it should be."""
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        names = [n for n in z.namelist() if n.lower().endswith(".csv")]
        if len(names) != 1:
            raise ValueError(f"{len(names)} csv files in the zip")
        text = z.read(names[0]).decode("utf-8-sig")       # a damaged file fails its CRC check here
    rows, bad, days = [], 0, set()
    for line in text.splitlines():
        f = [x.strip() for x in line.split(",")]
        if not f[0]:
            continue
        if not f[0].isdigit():
            if rows:
                raise ValueError(f"a line that is not a candle among the candles: {line[:40]!r}")
            continue                                       # a header line
        if len(f) < 11:
            raise ValueError(f"{len(f)} fields where a candle has 12")
        ts = int(f[0])
        if ts >= 10 ** 14:
            ts //= 1000                                    # microseconds: Binance's spot files from January 2025 on
        if ts % (DAY * 1000):
            raise ValueError(f"a candle that does not open at midnight UTC ({f[0]})")
        day = _utc(ts // 1000).strftime("%Y-%m-%d")
        if day[:7] != month:
            raise ValueError(f"a candle of {day} in the file for {month}")
        if day in days:
            raise ValueError(f"two candles for {day}")
        days.add(day)
        o, h, lo, c = (_num(x) for x in f[1:5])
        if min(Decimal(o), Decimal(h), Decimal(lo), Decimal(c)) <= 0:
            bad += 1
            continue
        rows.append([symbol, day, o, h, lo, c, _coins(f[5]), _dollars(f[7]), str(int(_dec(f[8]))), _dollars(f[10])])
    return rows, bad


def fetch_month(symbol: str, month: str) -> tuple[list[list[str]], int, str]:
    """(rows, rows left out, note); a note that is not empty says the file could not be had."""
    url = f"{ARCHIVE}/{MONTHLY}{symbol}/1d/{symbol}-1d-{month}.zip"
    status, body, note = get(url)
    if status != 200 or body is None:
        return [], 0, note or f"http {status}"
    try:
        rows, bad = read_zip(body, symbol, month)
    except Exception as e:  # noqa: BLE001 - a bad file is named and asked for again, it never stops the run
        return [], 0, f"{type(e).__name__}: {e}"[:200]
    return rows, bad, ""


def write_month(month: str, rows: list[list[str]]) -> bool:
    """Writes a month's file; the same rows always give the same bytes. True when the file changed."""
    rows = sorted(rows, key=lambda r: (r[0], r[1]))
    text = HEADER + "\n" + "".join(",".join(r) + "\n" for r in rows)
    blob = gzip.compress(text.encode("utf-8"), compresslevel=9, mtime=0)
    path = month_path(month)
    if path.exists() and path.read_bytes() == blob:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(blob)
    tmp.replace(path)
    return True


def read_month(month: str) -> list[list[str]]:
    path = month_path(month)
    if not path.exists():
        return []
    lines = gzip.decompress(path.read_bytes()).decode("utf-8").splitlines()
    if not lines or lines[0] != HEADER:
        raise BinanceError(f"{path.name} does not begin with the header this job writes")
    rows = [ln.split(",") for ln in lines[1:] if ln]
    if any(len(r) != len(COLUMNS) for r in rows):
        raise BinanceError(f"{path.name} has a row that is not {len(COLUMNS)} fields")
    return rows


def load_status() -> dict:
    p = root() / "status.json"
    try:
        s = json.loads(p.read_text())
        return s if isinstance(s, dict) else {}
    except Exception:  # noqa: BLE001 - no record, or one that cannot be read: every month is sought again
        return {}


def _settled(status: dict) -> set[str]:
    months = status.get("settled")
    return {m for m in months if isinstance(m, str) and re.fullmatch(r"\d{4}-\d{2}", m)} if isinstance(months, list) else set()


def _write_json(name: str, obj) -> None:
    root().mkdir(parents=True, exist_ok=True)
    (root() / name).write_text(json.dumps(obj, indent=1, sort_keys=True) + "\n")


# --- the run ---------------------------------------------------------------------

NO_TIME = "not asked: the run's time was up"


def _months_on_disk() -> dict:
    on_file = sorted(p.name[:7] for p in (root() / "months").glob("*.csv.gz")) if (root() / "months").exists() else []
    return {"on_file": len(on_file), "first": on_file[0] if on_file else None, "last": on_file[-1] if on_file else None}


def collect(now: int | None = None) -> dict:
    """Fetch every month not yet settled. Returns the status written, or {} when there was nothing to do
    (and then nothing was asked and nothing written). Raises BinanceError, with status.json written, when
    the run has to stop."""
    now = int(now if now is not None else _now())
    deadline = _clock() + BUDGET_S
    settled = _settled(load_status())
    newest = newest_month(now)
    todo = [m for m in months_from(FIRST_MONTH, newest) if m not in settled]
    if not todo:
        return {}

    status = {"ran": now, "ran_utc": _utc(now).strftime("%Y-%m-%d %H:%MZ"), "ok": False, "stopped": "",
              "newest_month": newest, "settled": sorted(settled)}

    def stop(why: str):
        status["stopped"] = why
        status["months"] = _months_on_disk()
        _write_json("status.json", status)
        raise BinanceError(why)

    # which pairs there are, and which months each has
    info, info_note = exchange_info()
    listed, unread, listing_note = archive_symbols()
    fallback = bool(listing_note)
    status["sources"] = {"archive_list": {"ok": not fallback, "pairs": len(listed), "note": listing_note,
                                          "names_not_read": unread[:20]},
                         "exchange_info": {"ok": bool(info), "pairs": len(info), "note": info_note,
                                           "trading": sum(1 for v in info.values() if v["status"] == "TRADING")},
                         "fallback": fallback}
    if fallback and not info:
        stop(f"neither the archive's list of pairs ({listing_note}) nor Binance's list of symbols ({info_note}) could be read")
    candidates = sorted(info) if fallback else listed
    months_of, unreadable = {}, []
    for sym, (months, note) in zip(candidates, _map(api_months if fallback else archive_months, candidates)):
        if note:
            unreadable.append(f"{sym}: {note}")
        months_of[sym] = [m for m in months if FIRST_MONTH <= m <= newest]
    everyone = sorted(set(candidates) | set(info))
    coin = {s: info[s]["base"] if s in info else coin_of(s) for s in everyone}
    all_coins = set(coin.values())
    why_out = {s: w for s in everyone if (w := leave_out(coin[s], all_coins))}
    kept = [s for s in candidates if s not in why_out and months_of[s]]
    ended = [s for s in kept if months_of[s][-1] < newest]
    trading = [s for s, v in info.items() if v["status"] == "TRADING" and s not in why_out]
    in_list = set(listed)
    missing = sorted(set(trading) - in_list) if not fallback else []
    status["pairs"] = {"found": len(candidates), "kept": len(kept), "ended_before_newest": len(ended),
                       "left_out": {w: sorted(s for s in why_out if why_out[s] == w) for w in sorted(set(why_out.values()))},
                       "trading_not_in_archive": missing,
                       "months_unreadable": len(unreadable), "months_unreadable_first": unreadable[:10]}
    if not kept:
        stop("not one pair with daily candles was found")
    if len(ended) < MIN_ENDED:
        road = f"from Binance's list of symbols alone, the archive's list failing ({listing_note})" if fallback \
            else "from the archive's list"
        stop(f"only {len(ended)} of the {len(kept)} pairs found ({road}) end before {newest}: a history of the pairs "
             f"alive today is a history of survivors, which is what this job exists to avoid")
    if len(missing) > max(10, CUT_OFF_SHARE * len(trading)):
        stop(f"{len(missing)} of the {len(trading)} pairs Binance trades today are not in the archive's list "
             f"({', '.join(missing[:5])}, ...); taken for a list that was cut off")

    def fetch(sym: str, month: str):
        # the time is looked at before each file, so a slow archive costs the files after it and never the run
        return ([], 0, NO_TIME) if _clock() > deadline else fetch_month(sym, month)

    # the months, oldest first, each written before the next is begun
    asked = fetched = dropped = 0
    failed, changed, newly, left, waiting = {}, [], [], [], []
    for i, month in enumerate(todo):
        if _clock() > deadline:
            left = todo[i:]
            break
        try:
            have = [r for r in read_month(month) if r[0] not in why_out]
        except Exception:  # noqa: BLE001 - a damaged file is fetched again whole
            have = []
        held = {r[0] for r in have}
        ask = [s for s in kept if month in months_of[s] and s not in held]
        rows, fails, late = list(have), [], 0
        for sym, (got, bad, note) in zip(ask, _map(lambda x, m=month: fetch(x, m), ask)):
            if note == NO_TIME:
                late += 1
            elif note:
                fails.append(f"{month} {sym}: {note}")
            else:
                rows += got
                dropped += bad
        asked += len(ask) - late
        fetched += len(ask) - late - len(fails)
        if fails:
            failed[month] = fails
            if len(fails) == len(ask) - late and not have and len(fails):
                stop(f"not one of the {len(fails)} files of {month} could be fetched ({fails[0]}); the archive is "
                     f"not answering, and nothing more was asked")
        if rows and write_month(month, rows):
            changed.append(month)
        # a month the run's time cut short is carried on with by the next run; one whose pairs came from
        # Binance's list of symbols alone lacks the pairs it dropped long ago, so it is never settled
        whole = not fails and not unreadable and not late and not fallback
        if month == newest and whole:
            # the newest month's files go up over its first days: settled from the 8th, when every pair
            # Binance still trades that had a file the month before has one, and about as many pairs as then
            try:
                before = {r[0] for r in read_month(_prev(month))}
            except Exception:  # noqa: BLE001
                before = set()
            now_in = {r[0] for r in rows}
            waiting = sorted(s for s in trading if s in before and s not in now_in)
            whole = _utc(now).day >= SETTLED_FROM_DAY and not waiting and len(now_in) >= WHOLE_SHARE * len(before)
        if whole:
            newly.append(month)
        if late:
            left = todo[i:]
            break

    _write_json("pairs.json", {s: {"coin": coin[s],
                                   "binance_status": info[s]["status"] if s in info else "not in Binance's list",
                                   "found_in": [w for w, there in (("archive", s in in_list), ("exchangeInfo", s in info)) if there],
                                   "first_month": months_of[s][0] if months_of.get(s) else None,
                                   "last_month": months_of[s][-1] if months_of.get(s) else None,
                                   "left_out": why_out.get(s, "")} for s in everyone})
    try:
        cut = breaks(load())
    except Exception as e:  # noqa: BLE001 - what to look at by hand; never a reason to lose the run
        cut = [{"error": f"{type(e).__name__}: {e}"[:200]}]
    status.update({
        "ok": True,
        "settled": sorted(settled | set(newly)),
        "files": {"asked": asked, "fetched": fetched, "rows_left_out": dropped,
                  "failed": sum(len(v) for v in failed.values()), "failed_first": [x for v in failed.values() for x in v][:10]},
        "months": {**_months_on_disk(), "changed": changed, "settled_this_run": newly, "left_for_next_run": left,
                   "newest_waiting_for": waiting[:20], "newest_waiting_count": len(waiting)},
        "breaks": cut[:80], "breaks_count": len(cut),
    })
    _write_json("status.json", status)
    return status


def _record_crash(e: Exception, now: int | None = None) -> None:
    """A run that failed in a way collect() did not foresee still leaves a record that says so."""
    now = int(now if now is not None else _now())
    s = load_status()
    s.update({"ran": now, "ran_utc": _utc(now).strftime("%Y-%m-%d %H:%MZ"), "ok": False,
              "stopped": f"the run failed: {type(e).__name__}: {e}"[:300], "settled": sorted(_settled(s)),
              "months": {**(s.get("months") or {}), **_months_on_disk()}})
    _write_json("status.json", s)


# --- the report ------------------------------------------------------------------

def summary_lines(now: int | None = None) -> list[str]:
    """The last run in a few lines. A line about something that went wrong begins with FAILED, and one
    about a month that should be in and is not with STALE."""
    p = root() / "status.json"
    if not p.exists():
        if _utc(now if now is not None else _now()).strftime("%Y-%m-%d") > FIRST_RUN_BY:
            return [f"STALE: Binance history: no run on record, and the job has been in place since before {FIRST_RUN_BY}; "
                    f"it has not run, or no run of it has been able to commit"]
        return ["- Binance history: no run on record yet; the job's first run fills it (bot/binance.py)"]
    try:
        s = json.loads(p.read_text())
        pa, mo, fi, so = s.get("pairs") or {}, s.get("months") or {}, s.get("files") or {}, s.get("sources") or {}
        settled = sorted(_settled(s))
        left_out = sum(len(v) for v in (pa.get("left_out") or {}).values())
        lines = [f"- Binance history, run of {s.get('ran_utc', '?')}: {mo.get('on_file', 0)} months on file "
                 f"({mo.get('first')} to {mo.get('last')}), settled to {settled[-1] if settled else 'none yet'}; "
                 f"{pa.get('kept', 0)} pairs kept, {pa.get('ended_before_newest', 0)} of them ending before "
                 f"{s.get('newest_month', '?')}, {left_out} left out (pegged or leveraged)"]
        if s.get("ok") is not True:
            lines.append(f"FAILED: Binance history: the run stopped: {s.get('stopped') or 'status.json does not say why'}")
        if (so.get("archive_list") or {}).get("ok") is False:
            lines.append(f"FAILED: Binance history: the archive's list of pairs could not be read "
                         f"({so['archive_list'].get('note')}), so the pairs came from Binance's list of symbols, "
                         f"which leaves out pairs delisted long ago")
        if (so.get("exchange_info") or {}).get("ok") is False:
            lines.append(f"FAILED: Binance history: Binance's list of symbols could not be read "
                         f"({so['exchange_info'].get('note')}), so nothing checked the archive's list against it")
        if pa.get("months_unreadable"):
            lines.append(f"FAILED: Binance history: the months on file could not be listed for {pa['months_unreadable']} "
                         f"pairs ({'; '.join(pa.get('months_unreadable_first', [])[:3])}); nothing is settled until they can")
        if fi.get("failed"):
            lines.append(f"FAILED: Binance history: {fi['failed']} files could not be fetched "
                         f"({'; '.join(fi.get('failed_first', [])[:3])}); their months are asked for again by the next run")
        if mo.get("left_for_next_run"):
            lines.append(f"- Binance history: {len(mo['left_for_next_run'])} months were left for the next run, "
                         f"the run's time being up")
        if mo.get("newest_waiting_count"):
            lines.append(f"- Binance history: {s.get('newest_month')} waits for the files of {mo['newest_waiting_count']} pairs "
                         f"Binance still trades ({', '.join(mo.get('newest_waiting_for', [])[:5])}) before it is settled")
        unread = (so.get("archive_list") or {}).get("names_not_read") or []
        if unread:
            lines.append(f"- Binance history: {len(unread)} folders of the archive end in USDT under a name this job does "
                         f"not read, and are not collected ({', '.join(unread[:3])})")
        if s.get("breaks_count"):
            lines.append(f"- Binance history: {s['breaks_count']} places where a pair stopped and came back far from where it "
                         f"left, listed under `breaks` in status.json to be looked at by hand")
        due = due_month(now)
        if due >= FIRST_MONTH and due not in settled:
            lines.append(f"STALE: Binance history: {due} is not settled and it is past the {LATE_DAY}th of the month "
                         f"after; the job has not run, or has not been able to fetch the month whole")
        return lines
    except Exception as e:  # noqa: BLE001 - the report must come out whatever the file holds
        return [f"FAILED: Binance history: status.json cannot be read ({type(e).__name__})"]


# --- reading it back (for studies) -----------------------------------------------

def load(first: str | None = None, last: str | None = None) -> pd.DataFrame:
    """Every candle on file (from month `first` to month `last`), one row a pair a day, with a `coin`
    column: the pair's coin, or the coin with #2, #3 after it for candles that came back as another coin.
    Which coin is which is worked out on the whole history, whatever months are asked for."""
    frames = []
    folder = root() / "months"
    for path in sorted(folder.glob("*.csv.gz")) if folder.exists() else []:
        frames.append(pd.read_csv(path, dtype={"symbol": str, "day": str}, compression="gzip"))
    if not frames:
        return pd.DataFrame(columns=COLUMNS + ["coin"])
    df = pd.concat(frames, ignore_index=True)
    for c in COLUMNS[2:]:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype(float)
    df["day"] = pd.to_datetime(df["day"], format="%Y-%m-%d", utc=True)
    df = df.drop_duplicates(["symbol", "day"], keep="last").sort_values(["symbol", "day"], kind="stable")
    pairs = list(df["symbol"].unique())
    everyone = {coin_of(s) for s in pairs}
    df = df[df["symbol"].isin([s for s in pairs if not leave_out(coin_of(s), everyone)])].reset_index(drop=True)
    df["coin"] = coins(df)
    month = df["day"].dt.strftime("%Y-%m")
    if first or last:
        df = df[(month >= (first or "")) & (month <= (last or "9999-99"))].reset_index(drop=True)
    return df


def coins(df: pd.DataFrame) -> pd.Series:
    """Which coin each row is: a pair's candles are one coin until they stop for more than LONG_GAP_DAYS
    days, or stop for a day or more and come back above JUMP times the close they left at."""
    out = pd.Series(index=df.index, dtype=object)
    for sym, g in df.groupby("symbol", sort=False):
        gap = (g["day"].diff().dt.days.fillna(1).to_numpy() - 1)
        back = (g["open"].to_numpy() / g["close"].shift(1).to_numpy())
        new = (gap > LONG_GAP_DAYS) | ((gap > 0) & (back > JUMP))
        k = 1 + np.cumsum(new)
        base = coin_of(sym)
        out.loc[g.index] = [base if i == 1 else f"{base}#{i}" for i in k]
    return out


def breaks(df: pd.DataFrame) -> list[dict]:
    """What to look at by hand: every place a pair's candles were taken for another coin, and every place
    they stopped and came back at under 1/JUMP of where they left, which stays one coin (a crash in a halt
    and a swap at a ratio look the same from here, and the first is the one a study must not miss)."""
    out = []
    for sym, g in df.groupby("symbol", sort=False):
        g = g.reset_index(drop=True)
        gap = g["day"].diff().dt.days.fillna(1).to_numpy() - 1
        back = g["open"].to_numpy() / g["close"].shift(1).to_numpy()
        split = g["coin"].ne(g["coin"].shift(1)).to_numpy().copy()
        split[0] = False
        low = (gap > 0) & (back < 1.0 / JUMP) & ~split
        for j in np.flatnonzero(split | low):
            out.append({"pair": sym, "coin": g["coin"].iloc[j], "split": bool(split[j]),
                        "left": g["day"].iloc[j - 1].strftime("%Y-%m-%d"), "back": g["day"].iloc[j].strftime("%Y-%m-%d"),
                        "missing_days": int(gap[j]), "price_back_over_left": round(float(back[j]), 6)})
    return out


def returns(df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Each coin's return from one close to the next, one row a UTC day. A day a coin has no candle in the
    middle of its life (a suspension) earns nothing, and what the price did meanwhile is booked on the day
    it trades again; there is none before a coin's first candle or after its last."""
    close = panel("close", df)
    if close.empty:
        return close
    life = close.ffill().notna() & close.bfill().notna()
    held = close.ffill().where(life)
    return held.pct_change(fill_method=None).where(life & life.shift(1, fill_value=False))


def panel(column: str = "close", df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Every coin side by side: one row a UTC day (every day, no candle being no value), one column a coin."""
    df = load() if df is None else df
    if df.empty:
        return pd.DataFrame()
    frame = df.pivot(index="day", columns="coin", values=column).sort_index()
    days = pd.date_range(frame.index.min(), frame.index.max(), freq="D", tz="UTC")
    return frame.reindex(days).sort_index(axis=1)


def listing(n: int = 100, df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Which coins were among the n most traded on each day, as that day began: True or False, one row a
    day, one column a coin. Judged on the days before only: the median of dollars traded over the
    LIST_WINDOW days before (a day with no candle counting as none), among coins with a candle on the day
    before, with LIST_MIN_DAYS days of candles behind them, and not trading at a dollar (a median close
    within PEG_BAND of a dollar and a highest close within PEG_RANGE times its lowest over the same days)."""
    df = load() if df is None else df
    if df.empty:
        return pd.DataFrame()
    qv = panel("quote_volume", df)
    close = panel("close", df)
    traded = qv.notna()
    median = qv.fillna(0.0).rolling(LIST_WINDOW, min_periods=LIST_WINDOW).median().shift(1)
    behind = traded.cumsum().shift(1, fill_value=0)
    alive = traded.shift(1, fill_value=False)
    c = close.ffill()
    hi = c.rolling(LIST_WINDOW, min_periods=1).max().shift(1)
    lo = c.rolling(LIST_WINDOW, min_periods=1).min().shift(1)
    mid = c.rolling(LIST_WINDOW, min_periods=1).median().shift(1)
    pegged = (hi <= lo * PEG_RANGE) & ((mid - 1.0).abs() <= PEG_BAND)
    ok = (behind >= LIST_MIN_DAYS) & alive & (median > 0) & ~pegged
    rank = median.where(ok).rank(axis=1, ascending=False, method="first")
    return (rank <= n) & ok


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--collect" not in argv:
        print("\n".join(summary_lines()))
        return 0
    try:
        status = collect()
    except BinanceError as e:
        print(f"[binance] stopped: {e}")
        print("\n".join(summary_lines()))
        return 1
    except Exception as e:  # noqa: BLE001 - not foreseen: say so in the record, and fail
        _record_crash(e)
        print(f"[binance] failed: {type(e).__name__}: {e}")
        print("\n".join(summary_lines()))
        return 1
    if not status:
        print("[binance] every month there is to fetch is settled; nothing asked, nothing written")
        return 0
    print("\n".join(summary_lines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
