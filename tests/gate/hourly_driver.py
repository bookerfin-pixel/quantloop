"""PROTECTED. Three hours of the real hourly loop on made up candles.

For the tests that hold the wide data collector and the bench apart from the
hourly loop (tests/gate/test_wide.py, tests/gate/test_bench.py). It imports
nothing of bot.wide or bot.bench, so it can also be run where those modules
cannot be imported at all. Each hour it runs what the hourly workflow runs, in
the workflow's order: the accounts (with the history backfill switched on, as
in the repo's own risk.yaml), the rulings, the report written to
state/summary.md, the slots. The three hours cross a UTC midnight.

While the loop runs it watches, through Python's own audit hook, for any file
opened and any folder listed, by path or by file descriptor, with `state/wide`
or `state/bench` in its path. What the hook is not told of, it cannot see: a
file's size or date being looked up, a folder being made, a child process. The
comparison of what the loop prints and of every file and folder it leaves is
there for those. Not a test file itself.
"""
import contextlib
import io
import json
import os
import sys
import types
from pathlib import Path

from bot import config, data, promote, report, run, slot

RISK = {"fee_bps": 10, "slippage_bps": 5, "impact_bps": 2, "initial_cash": 10_000, "pairs": ["BTC", "ETH"],
        "history_hours": 720, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0, "min_trade_notional": 50,
        "rebalance_threshold": 0.05, "daily_loss_halt": 0.05, "max_fills_per_pair_per_day": 4, "ruleset": 7,
        "history_target_hours": 2000, "history_backfill_budget_s": 600,       # the backfill runs, as it does live
        "challenger": {"slots": 2}}
MOMO = {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
TEST = {"hypothesis": "H9", "strategy": "ts_momentum", "params": {"lookback_hours": 24, "ema_hours": 6, "vol_lookback_hours": 96}}
HOUR0 = 1_790_000_000 // 86400 * 86400 + 22 * 3600           # 22:00 UTC: the third hour is the first of the next UTC day
PATHS = ("ROOT", "CONFIGS", "STATE", "CANDLES", "HISTORY", "ARCHIVE", "LEDGER")


class Feed:
    """Made up hourly candles that grow by one each hour, the same every time they are built."""

    def __init__(self):
        self.full = data.SyntheticSource(RISK["pairs"], n=910, seed=7, start=HOUR0 - 900 * 3600)
        self.upto = 900

    def ohlc(self, pair, since=None):
        df = self.full.ohlc(pair).iloc[: self.upto]
        return df[df["time"] > since].reset_index(drop=True) if since else df.reset_index(drop=True)

    def quote_for(self, pair):
        last = float(self.full.ohlc(pair)["close"].iloc[self.upto - 1])
        return data.Quote(bid=last * 0.9995, ask=last * 1.0005, last=last)


def older_candles():
    """A made up past for the history backfill, ending where the Feed's candles begin."""
    return data.SyntheticSource(RISK["pairs"], n=1300, seed=107, start=HOUR0 - 2200 * 3600)


def plant(root: Path, feed: Feed) -> None:
    """A state/wide as full as the collector would leave it, and then some: every kind of file it
    writes, and beside them folders that look like accounts, candle caches, an archive and a summary."""
    w = root / "state" / "wide"
    for sub in ("daily", "quotes", "funding", "challenger9", "champion", "candles", "history", "archive/H1"):
        (w / sub).mkdir(parents=True)
    candles = feed.ohlc("BTC")
    candles.assign(source="kraken").to_csv(w / "daily" / "BTC.csv", index=False)
    candles.assign(source="kraken").to_csv(w / "daily" / "ETH.csv", index=False)
    candles.to_csv(w / "candles" / "BTC.csv", index=False)
    feed.ohlc("ETH").to_csv(w / "history" / "ETH.csv", index=False)
    (w / "quotes" / "2026.csv").write_text("time,pair,bid,ask,last,volume_24h,vwap_24h,trades_24h,usd_volume_24h,half_spread_bps,rank\n"
                                           f"{HOUR0},BTC,1.0,2.0,1.5,10,1.5,7,15.0,3333.33,1\n")
    (w / "funding" / "PF_XBTUSD.csv").write_text(f"time,hours,relative_sum,absolute_sum\n{HOUR0 // 86400 * 86400},24,0.5,9.0\n")
    (w / "universe.json").write_text(json.dumps({"pairs": {"BTC": {"since": "2026-10-04", "listed": True, "altname": "XBTUSD"}}}))
    (w / "status.json").write_text(json.dumps({"ran": HOUR0, "ok": True, "kraken": {"pairs_read": 1}}))
    (w / "deepen.json").write_text(json.dumps({"BTC": {"at": HOUR0, "want_from": 0, "result": "not listed"}}))
    for d in ("challenger9", "champion", "archive/H1"):
        (w / d / "account.json").write_text(json.dumps({"cash": 1.0, "positions": {"BTC": 99.0}, "n_trades": 7}))
        (w / d / "meta.json").write_text(json.dumps({"status": "testing", "hypothesis": "H9", "start_ts": 1}))
        (w / d / "trades.csv").write_text("ts,pair,side,qty,price\n1,BTC,buy,1,1\n")
        (w / d / "equity.csv").write_text("ts,equity\n1,1\n")
    (w / "summary.md").write_text("# not the summary\n")


BENCH_FILES = {"H9.json": b'{"hypothesis": "H9", "sharpe": 9.9, "twins": {"beaten": 1.0}}\n',
               "README.md": b"# The bench's league table\n\nH9 beats every twin\n"}
WATCHED = ("wide", "bench")                    # the folders under state/ that the hourly loop must leave alone


def plant_bench(root: Path, hypotheses=()) -> None:
    """A state/bench as the bench's own job would leave it, with a reading that flatters the slot's
    test. It is put beside the run that has the wide data and left out of the one that has none, so
    that the two are compared with the readings there and without them. hypotheses: more names to
    leave a reading under."""
    (root / "state" / "bench").mkdir(parents=True)
    for name, content in BENCH_FILES.items():
        (root / "state" / "bench" / name).write_bytes(content)
    for hyp in hypotheses:
        (root / "state" / "bench" / f"{hyp}.json").write_bytes(BENCH_FILES["H9.json"].replace(b"H9", str(hyp).encode()))


_WATCH = {"on": False, "seen": []}


def _audit(event, args):
    """Python tells this of every file the process opens and every folder it lists. While the watch
    is on, those with `state/wide` or `state/bench` in their path are noted, wherever that folder is:
    in a root a test made, or in the checkout itself. It must never be what breaks a run, so it raises
    nothing."""
    if not _WATCH["on"] or event not in ("open", "os.listdir", "os.scandir"):
        return
    try:
        path = args[0]
        if isinstance(path, int):                          # by file descriptor: ask the system what it stands for
            path = os.readlink(f"/proc/self/fd/{path}")
        if isinstance(path, (str, bytes, os.PathLike)):
            parts = Path(os.path.realpath(os.fsdecode(path))).parts
            for i in range(len(parts) - 1):
                if parts[i] == "state" and parts[i + 1] in WATCHED:
                    _WATCH["seen"].append(f"{event} {'/'.join(parts[i:])}")
                    break
    except Exception:  # noqa: BLE001
        pass


sys.addaudithook(_audit)                       # cannot be taken off again; it does nothing unless the watch is on


@contextlib.contextmanager
def watching():
    """While this is open, every file opened and every folder listed under a state/wide or a
    state/bench is noted."""
    _WATCH["on"], _WATCH["seen"] = True, []
    try:
        yield _WATCH["seen"]
    finally:
        _WATCH["on"] = False


def _files(root: Path, inside: bool) -> dict:
    """Every file under root with what it holds, and every folder (its name ends in a slash): those
    under the folders the loop must leave alone (state/wide, state/bench), or all the others."""
    out = {}
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if any(rel == f"state/{w}" or rel.startswith(f"state/{w}/") for w in WATCHED) == inside:
            if p.is_file():
                out[rel] = p.read_bytes()
            elif p.is_dir():
                out[rel + "/"] = b""
    return out


def drive(root: Path, bait: bool, hours: int = 3):
    """Run the hourly steps `hours` times in a fresh root. bait: with a full state/wide and a
    state/bench beside it. Returns what the loop printed and said each hour, every file and folder it
    left outside those two, what was under them before and after, and whatever under a state/wide or
    a state/bench the loop opened or listed while it ran."""
    root = Path(root)
    for name, value in (("ROOT", root), ("CONFIGS", root / "configs"), ("STATE", root / "state"), ("CANDLES", root / "state" / "candles"),
                        ("HISTORY", root / "state" / "history"), ("ARCHIVE", root / "state" / "archive"), ("LEDGER", root / "LEDGER.md")):
        setattr(config, name, value)
    (root / "configs").mkdir(parents=True)
    config.dump_yaml(root / "configs" / "risk.yaml", RISK)
    config.dump_yaml(root / "configs" / "champion.yaml", MOMO)
    config.dump_yaml(root / "configs" / "challenger1.yaml", TEST, header=config.CHALLENGER_HEADER)
    (root / "LEDGER.md").write_text("# Ledger\n\n## H9: a test\n- Status: testing\n\n## Results\n")
    feed = Feed()
    if bait:
        plant(root, feed)
        plant_bench(root)
    before = _files(root, inside=True)
    data.get_source = lambda pairs, quote="USD": feed
    data.get_history_source = lambda pairs, quote="USD": older_candles()
    said = []
    report_clock = report.time
    with watching() as seen:
        for hour in range(hours):
            ts = HOUR0 + hour * 3600 + 600
            feed.upto = 900 + hour
            printed = io.StringIO()
            with contextlib.redirect_stdout(printed):
                assert run.main(["--now", str(ts)]) == 0
                assert promote.main(["--now", str(ts)]) == 0
                report.time = types.SimpleNamespace(time=lambda: ts)       # report.main reads the clock: give it the hour's
                try:
                    assert report.main() == 0
                finally:
                    report.time = report_clock
            said += [printed.getvalue().replace(str(root), "<root>"), slot.describe(ts), ",".join(slot.free_slots())]
        touched = list(seen)
    return said, _files(root, inside=False), before, _files(root, inside=True), touched
