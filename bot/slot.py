"""Challenger slots: which prospective tests are running, and since when. PROTECTED.

state/challenger<k>/meta.json
  status      "idle" (slot config equals champion) or "testing"
  hypothesis  ledger id under test
  started_at  unix ts of the first hourly run with the new config
  start_equity {"champion": x, "<slot>": y}

A test starts by itself the first time the bot runs after a PR changed that
slot's config. It ends when bot/promote.py rules on it.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone

from . import config

IDLE = {"status": "idle", "hypothesis": None, "started_at": None, "start_equity": {}}


def meta_path(name: str):
    return config.account_dir(name) / "meta.json"


def load(name: str) -> dict:
    p = meta_path(name)
    if p.exists():
        return json.loads(p.read_text())
    return dict(IDLE)


def save(name: str, meta: dict) -> None:
    p = meta_path(name)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(meta, indent=2, sort_keys=True))


def reset(name: str) -> None:
    save(name, dict(IDLE))


def configs_differ(name: str) -> bool:
    champ = config.account_cfg(config.CHAMPION)
    return config.strategy_signature(champ) != config.strategy_signature(config.account_cfg(name))


def maybe_start(now: int, equities: dict[str, float]) -> dict[str, dict]:
    """Called after every hourly run. Opens a test in every slot whose config
    is live and not yet under test."""
    out = {}
    for name in config.challengers():
        meta = load(name)
        differ = configs_differ(name)
        if differ and meta["status"] != "testing":
            cfg = config.account_cfg(name)
            meta = {
                "status": "testing",
                "hypothesis": cfg["hypothesis"],
                "started_at": int(now),
                "start_equity": {k: float(v) for k, v in equities.items() if k in (config.CHAMPION, name)},
            }
            save(name, meta)
            print(f"[slot] {name}: test started for {meta['hypothesis']} at "
                  f"{datetime.fromtimestamp(now, timezone.utc):%Y-%m-%d %H:%M}Z")
        elif not differ and meta["status"] == "testing":
            meta = dict(IDLE)
            save(name, meta)
            print(f"[slot] {name}: config equals champion again; slot idle")
        out[name] = meta
    return out


def describe_one(name: str, now: int | None = None) -> str:
    now = now or int(time.time())
    meta = load(name)
    if meta["status"] != "testing":
        return f"{name}: idle (free for a hypothesis)"
    window_days = float(config.risk_cfg()["challenger"]["window_days"])
    elapsed_days = (now - meta["started_at"]) / 86400
    left = max(0.0, window_days - elapsed_days)
    return (f"{name}: testing {meta['hypothesis']} since "
            f"{datetime.fromtimestamp(meta['started_at'], timezone.utc):%Y-%m-%d %H:%M}Z, "
            f"day {elapsed_days:.1f} of {window_days:.0f}, {left:.1f} days until the verdict")


def describe(now: int | None = None) -> str:
    return "\n".join(describe_one(name, now) for name in config.challengers())


def free_slots() -> list[str]:
    return [name for name in config.challengers() if load(name)["status"] != "testing"]


if __name__ == "__main__":
    config.prepare()
    print(describe())
    free = free_slots()
    print(f"free slots: {', '.join(free) if free else 'none'}")
    sys.exit(0)
