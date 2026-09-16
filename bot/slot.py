"""The challenger slot: is a prospective test running, and since when. PROTECTED.

state/challenger/meta.json
  status      "idle" (challenger config equals champion) or "testing"
  hypothesis  ledger id under test
  started_at  unix ts of the first hourly run with the new config
  start_equity {"champion": x, "challenger": y}

A test starts by itself the first time the bot runs after a PR changed
configs/challenger.yaml. It ends when bot/promote.py rules on it.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone

from . import config

META = config.account_dir("challenger") / "meta.json"


def load() -> dict:
    if META.exists():
        return json.loads(META.read_text())
    return {"status": "idle", "hypothesis": None, "started_at": None, "start_equity": {}}


def save(meta: dict) -> None:
    META.parent.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps(meta, indent=2, sort_keys=True))


def configs_differ() -> bool:
    champ = config.account_cfg("champion")
    chal = config.account_cfg("challenger")
    return config.strategy_signature(champ) != config.strategy_signature(chal)


def maybe_start(now: int, equities: dict[str, float]) -> dict:
    """Called after every hourly run. Opens a test when a new challenger config
    is live and none is running."""
    meta = load()
    differ = configs_differ()
    if differ and meta["status"] != "testing":
        chal = config.account_cfg("challenger")
        meta = {
            "status": "testing",
            "hypothesis": chal["hypothesis"],
            "started_at": int(now),
            "start_equity": {k: float(v) for k, v in equities.items()},
        }
        save(meta)
        print(f"[slot] test started for {meta['hypothesis']} at {datetime.fromtimestamp(now, timezone.utc):%Y-%m-%d %H:%M}Z")
    elif not differ and meta["status"] == "testing":
        # Configs were made identical outside promote.py (a manual reset). Close the slot.
        meta = {"status": "idle", "hypothesis": None, "started_at": None, "start_equity": {}}
        save(meta)
        print("[slot] challenger config equals champion again; slot idle")
    return meta


def describe(now: int | None = None) -> str:
    now = now or int(time.time())
    meta = load()
    if meta["status"] != "testing":
        return "idle (challenger config equals champion; the agent may propose a hypothesis)"
    window_days = float(config.risk_cfg()["challenger"]["window_days"])
    elapsed_days = (now - meta["started_at"]) / 86400
    left = max(0.0, window_days - elapsed_days)
    return (f"testing {meta['hypothesis']} since "
            f"{datetime.fromtimestamp(meta['started_at'], timezone.utc):%Y-%m-%d %H:%M}Z, "
            f"day {elapsed_days:.1f} of {window_days:.0f}, {left:.1f} days until the verdict")


if __name__ == "__main__":
    print(describe())
    sys.exit(0)
