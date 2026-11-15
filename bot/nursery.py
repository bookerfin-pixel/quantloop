"""The nursery: every idea on paper from the day it was first seen. PROTECTED.

A slot tests one idea for 60 to 120 days, and there are four. The nursery runs
every idea at once: each config under configs/nursery/ is replayed through the
engine over the year before the day this job first saw it and over every day
since, and the days since are read the way a test's are read: what it made
after costs, against the equal weight basket of the pairs held from that day
and never set back, its skill against that basket at its usual exposure (its
average over the year before), the t of its daily skill and the confidence
figure the verdicts print, its fills, its costs, its worst fall, and the day
the early kill on losses would have ended it. Those days are ones the idea had
not seen when it was written down, so they are out of sample, which no
backtest of it is. They are still a replay and not a slot: fills at the next
candle's open, no live quotes, no daily loss halt.

It never promotes. With many ideas at once some will read well by luck, so it
ranks: the idea with the highest confidence among those with LEADER_DAYS days
or more on paper, that no slot holds and that the early kill would not have
ended, is the one a free slot goes to first (CLAUDE.md). And an idea that
cannot be proven in a slot can still build a record here.

Why the day first seen and not a date written in the config: a date in a file
can be anything; the day this job first saw a config is kept in
state/nursery/seen.json and cannot be moved back. An idea whose strategy,
params or strategy code changes is a new idea from the day the change is seen.
The ledger's ideas from before the nursery began (H0, H1, H2, H4, H5 and H6;
H3 was voided for broken code and is left out) were seeded with the dates of
their ledger entries, which is when they were written down.

Like the bench, no account trades on it, no rule leans on it, and no strategy
may read state/nursery (a test in the gate sees to that).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone

import numpy as np

from . import backtest, bench, config, promote

YEAR_DAYS = 365         # the year before an idea was seen, replayed for its usual exposure
LEADER_DAYS = 60        # days on paper before an idea can lead the table
VERSION = 1


def ideas_dir():
    return config.CONFIGS / "nursery"


def state_dir():
    return config.STATE / "nursery"


def idea_signature(cfg: dict) -> str:
    """Changes when the idea changes: its strategy, its params, or the code of its strategy. A change to the
    engine or to another strategy leaves it the same idea, seen from the same day."""
    text = config.strategy_signature(cfg).encode() + bench.strategy_code(str(cfg["strategy"]))
    return hashlib.sha256(text).hexdigest()[:16]


def ideas() -> tuple[list[tuple[str, dict]], list[str]]:
    """Every config under configs/nursery/, by name, and a line for each that cannot be taken. A config's
    `hypothesis` names it and must be its file's name, so two files can never be one idea."""
    out, problems = [], []
    folder = ideas_dir()
    for path in sorted(folder.glob("*.yaml")) if folder.exists() else []:
        try:
            cfg = config.load_yaml(path)
            for key in ("hypothesis", "strategy", "params"):
                if key not in cfg:
                    raise ValueError(f"it has no {key!r}")
            if str(cfg["hypothesis"]) != path.stem:
                raise ValueError(f"its hypothesis {cfg['hypothesis']!r} is not its file's name")
            backtest.strategy_fn(str(cfg["strategy"]))
        except Exception as e:  # noqa: BLE001 - any config that cannot be taken is said, not raised
            problems.append(f"FAILED: configs/nursery/{path.name} cannot be taken ({e})")
            continue
        out.append((path.stem, cfg))
    return out, problems


def stamp(seen: dict, found: list[tuple[str, dict]], today: str) -> dict:
    """The day each idea was first seen as it now is: one not on record, or whose signature has changed, is seen
    from today. An idea no longer on file keeps its line, so that it is the same idea if it comes back unchanged."""
    out = dict(seen)
    for name, cfg in found:
        sig = idea_signature(cfg)
        old = seen.get(name)
        if not (isinstance(old, dict) and old.get("signature") == sig and old.get("seen")):
            out[name] = {"signature": sig, "seen": today}
    return out


def _day_ts(day: str) -> int:
    return int(datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())


def reading(s: dict, seen_ts: int, rules: dict) -> dict:
    """The whole days of a replay (bench.series) from seen_ts on, read as a test is read. `usual` is the book's
    average exposure over the hours before seen_ts. Days are UTC days, whole ones only."""
    ts, starts = np.asarray(s["ts"]), np.asarray(s["starts"])
    h0 = int(np.searchsorted(ts, seen_ts))
    d0 = int(np.searchsorted(starts, h0))
    if d0 >= len(starts) or int(starts[d0]) != h0:
        return {"days": 0, "why": "the replay has no hour at the start of the day first seen"}
    days = len(starts) - 1 - d0                       # the last day on record may not be whole yet
    if days < 1:
        return {"days": 0, "why": "no whole day on paper yet"}
    h1 = int(starts[d0 + days])
    expo = s["held"].sum(axis=1)
    usual = float(expo[:h0].mean()) if h0 > 0 else None
    net = bench._after(s["hourly"], s["c"])[h0:h1]
    E = np.cumprod(1.0 + net)
    there = s["valid"][h0]
    B = np.cumprod(1.0 + s["r"][h0:h1][:, there], axis=0).mean(axis=1) if there.any() else np.ones(h1 - h0)
    ends = starts[d0 + 1: d0 + days + 1] - h0 - 1
    e_day, b_day = np.r_[1.0, E[ends]], np.r_[1.0, B[ends]]
    daily, bdaily = e_day[1:] / e_day[:-1] - 1.0, b_day[1:] / b_day[:-1] - 1.0
    st = promote.rule_settings(rules)[0]
    out = {"days": int(days), "net": float(E[-1] - 1.0), "basket": float(B[-1] - 1.0), "usual": usual,
           "exposure": float(expo[h0:h1].mean()), "fills": int(np.asarray(s["fills"])[d0: d0 + days].sum()),
           "costs": float((s["c"][h0:h1] * np.r_[1.0, E[:-1]]).sum()),
           "max_drawdown": float((np.r_[1.0, E] / np.maximum.accumulate(np.r_[1.0, E]) - 1.0).min()),
           "skill": None, "skill_t": None, "confidence": None, "early_kill_day": None}
    limit = st["early_kill"]
    if limit:
        hit = np.flatnonzero((E - 1.0 < -limit) & (E < B))
        out["early_kill_day"] = float((hit[0] + 1) / 24.0) if len(hit) else None
    if usual is not None:
        out["skill"] = float(out["net"] - usual * out["basket"])
        skill_daily = daily - usual * bdaily
        if days >= 2:
            sd = float(skill_daily.std(ddof=1))
            out["skill_t"] = float(skill_daily.mean() / (sd / math.sqrt(days))) if sd > 1e-12 else None
        out["confidence"] = promote.confidence(out["skill_t"], days, rules)
    return out


def in_slots() -> dict[str, str]:
    """Which hypothesis each running test, and the champion, is: hypothesis -> where it runs."""
    out = {}
    for name in [config.CHAMPION] + config.challengers():
        try:
            cfg = config.account_cfg(name)
        except Exception:  # noqa: BLE001 - a slot that cannot be read holds nothing the table can name
            continue
        if not config.is_cash(cfg) and cfg.get("hypothesis"):
            out.setdefault(str(cfg["hypothesis"]), name)
    return out


def leader(rows: list[dict]) -> str | None:
    """The idea a free slot goes to first: the highest confidence among those with LEADER_DAYS days or more on
    paper, in no slot, and not ended by the early kill on losses. None when no idea is there yet."""
    fit = [r for r in rows if (r.get("days") or 0) >= LEADER_DAYS and not r.get("slot") and r.get("early_kill_day") is None
           and r.get("confidence") is not None]
    return max(fit, key=lambda r: (r["confidence"], r["days"]))["idea"] if fit else None


def _pct(x, signed: bool = True) -> str:
    return "" if x is None else (f"{x:+.1%}" if signed else f"{x:.0%}")


def table(rows: list[dict], problems: list[str], made_on: str) -> str:
    rows = sorted(rows, key=lambda r: (-(r.get("confidence") or 0.0), -(r.get("days") or 0), r["idea"]))
    lead = leader(rows)
    lines = [f"# The nursery", "", f"Read on {made_on}, on candles to the end of that day's last whole UTC day. "
             f"Each idea on paper from the day it was first seen, replayed through the engine; out of sample, and "
             f"a replay, not a slot. Nothing is promoted from here (bot/nursery.py says how it is read).", "",
             f"Next in line for a free slot: {lead or 'none yet (an idea needs ' + str(LEADER_DAYS) + ' days on paper, no slot, and no early kill)'}",
             "", "| idea | strategy | first seen | days | net | basket | skill | daily skill t | confidence | fills | "
             "worst fall | early kill | slot |", "|" + "---|" * 13]
    for r in rows:
        kill = "" if r.get("early_kill_day") is None else f"day {r['early_kill_day']:.0f}"
        t = "" if r.get("skill_t") is None else f"{r['skill_t']:+.2f}"
        lines.append(f"| {r['idea']} | {r.get('strategy', '')} | {r.get('seen', '')} | {r.get('days', 0)} | "
                     f"{_pct(r.get('net'))} | {_pct(r.get('basket'))} | {_pct(r.get('skill'))} | {t} | "
                     f"{_pct(r.get('confidence'), signed=False)} | {r.get('fills', '')} | {_pct(r.get('max_drawdown'))} | "
                     f"{kill} | {r.get('slot') or ''} |")
    if problems:
        lines += ["", "## Not read", ""] + [f"- {p}" for p in problems]
    return "\n".join(lines) + "\n"


def last_day(candles: dict) -> str:
    """The UTC day of the newest candle on file: the nursery's today, so that days count on data, not on a clock."""
    newest = max(int(df["time"].max()) for df in candles.values() if len(df))
    return datetime.fromtimestamp(newest, timezone.utc).strftime("%Y-%m-%d")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Every idea on paper from the day it was first seen.")
    ap.add_argument("--save", action="store_true", help="keep the readings and the days first seen under state/nursery")
    args = ap.parse_args(argv)
    rcfg = config.risk_cfg()
    candles = backtest.load_cached_candles(list(rcfg["pairs"]))
    today = last_day(candles)
    found, problems = ideas()
    seen_path = state_dir() / "seen.json"
    seen = json.loads(seen_path.read_text(encoding="utf-8")) if seen_path.exists() else {}
    seen = stamp(seen, found, today)
    slots = in_slots()
    rows = []
    for name, cfg in found:
        day = seen[name]["seen"]
        row = {"idea": name, "strategy": cfg["strategy"], "seen": day, "slot": slots.get(name), "days": 0}
        forward = (_day_ts(today) - _day_ts(day)) // 86400
        if forward >= 1:
            try:
                s, _ = bench.replay(candles, rcfg, cfg, days=int(forward) + YEAR_DAYS)
                row.update(reading(s, _day_ts(day), rcfg.get("challenger")))
            except Exception as e:  # noqa: BLE001 - one idea that cannot be replayed stops no other
                problems.append(f"FAILED: {name} could not be replayed ({str(e)[:200]})")
        rows.append(row)
    text = table(rows, problems, today)
    if args.save:
        out = state_dir()
        out.mkdir(parents=True, exist_ok=True)
        seen_path.write_text(json.dumps(seen, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        for row in rows:
            (out / f"{row['idea']}.json").write_text(json.dumps({**row, "version": VERSION}, indent=1, sort_keys=True,
                                                                 default=float) + "\n", encoding="utf-8")
        (out / "README.md").write_text(text, encoding="utf-8")
    print(text, end="")
    return 1 if any(p.startswith("FAILED") for p in problems) else 0


if __name__ == "__main__":
    sys.exit(main())
