"""The shadow champion: a guard against lucky promotions. PROTECTED.

When a challenger is promoted, the config it deposed keeps running in the
`shadow` account for one more window (challenger.window_days), starting from
fresh cash at the moment of promotion. At the end of that window
bot/promote.py compares the new champion against the shadow over the same
prospective span with the same rule used for promotion. If the deposed config
wins, the promotion is reverted: configs/champion.yaml goes back to it and the
ledger records that the promotion did not hold.

A second promotion during a shadow window supersedes the shadow: the newly
deposed champion becomes the shadow and the older one is dropped, with a line
in the ledger saying so. The shadow never trades against the champion for
promotion; it can only put back what was there before.

state/shadow/meta.json
  status       "active" or "idle"
  hypothesis   ledger id of the deposed champion config
  replaced_by  ledger id of the promotion being guarded
  started_at   unix ts of the promotion
  start_equity {"champion": x, "shadow": initial cash}
"""
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone

from . import config

SHADOW_HEADER = ("# PROTECTED. Written only by bot/promote.py: the config a promotion deposed,\n"
                 "# kept running for one window so a lucky promotion can be reverted.\n")
IDLE = {"status": "idle", "hypothesis": None, "replaced_by": None, "started_at": None, "start_equity": {}}


def meta_path():
    return config.account_dir(config.SHADOW) / "meta.json"


def load() -> dict:
    p = meta_path()
    if p.exists():
        return json.loads(p.read_text())
    return dict(IDLE)


def save(meta: dict) -> None:
    p = meta_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(meta, indent=2, sort_keys=True))


def archive(reason_tag: str) -> None:
    adir = config.account_dir(config.SHADOW)
    meta = load()
    hyp = meta.get("hypothesis") or "none"
    dest = config.ARCHIVE / f"shadow_{hyp}_{reason_tag}_{datetime.now(timezone.utc):%Y%m%d%H%M}"
    dest.mkdir(parents=True, exist_ok=True)
    for fname in ("account.json", "decisions.csv", "trades.csv", "equity.csv"):
        src = adir / fname
        if src.exists():
            shutil.move(str(src), str(dest / fname))


def start(deposed_cfg: dict, replaced_by: str, now: int, champion_equity: float, initial_cash: float) -> None:
    """Called by promote.py right after a promotion, with the deposed champion config."""
    if load().get("status") == "active":
        archive("superseded")
    config.dump_yaml(config.CONFIGS / "shadow.yaml",
                     {"hypothesis": deposed_cfg["hypothesis"], "strategy": deposed_cfg["strategy"],
                      "params": deposed_cfg["params"]}, SHADOW_HEADER)
    save({"status": "active", "hypothesis": deposed_cfg["hypothesis"], "replaced_by": replaced_by,
          "started_at": int(now),
          "start_equity": {config.CHAMPION: float(champion_equity), config.SHADOW: float(initial_cash)}})


def stop(reason_tag: str) -> None:
    archive(reason_tag)
    cfg = config.CONFIGS / "shadow.yaml"
    if cfg.exists():
        cfg.unlink()
    save(dict(IDLE))


def describe(now: int) -> str:
    meta = load()
    if meta.get("status") != "active":
        return "shadow: none (no promotion within the last window)"
    window_days = float(config.risk_cfg()["challenger"]["window_days"])
    elapsed = (now - meta["started_at"]) / 86400
    return (f"shadow: {meta['hypothesis']} (deposed by {meta['replaced_by']}) running since "
            f"{datetime.fromtimestamp(meta['started_at'], timezone.utc):%Y-%m-%d %H:%M}Z, "
            f"day {elapsed:.1f} of {window_days:.0f}; the promotion is reverted if it wins")
