"""Challenger slots: which prospective tests are running, and since when. PROTECTED.

state/challenger<k>/meta.json
  status      "idle" (slot config equals champion) or "testing"
  hypothesis  ledger id under test
  started_at  unix ts of the first hourly run with the new config
  start_equity {"champion": x, "<slot>": y}
  ruleset     configs/risk.yaml's ruleset when the test began (decides which
              promotion rule judges it; absent on tests from before 2026-10-04)
  first_look  written by bot/promote.py when a test is kept at its first look:
              {"at": ts, "start": the started_at it belongs to, "reason": ...,
              "on": "rule" (it passed the rule) or "value" (it did not, and
              its trades are of value; PROMOTION.md)}
  usual_exposure  each side's average exposure over the year before the test,
              worked out once by bot/promote.py

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
        try:
            meta = load(name)
            if not isinstance(meta, dict) or "status" not in meta:
                raise ValueError("it is not a slot record")
        except Exception as e:  # noqa: BLE001
            # Its account has traded this hour like the others, and the hour is not lost for all of them over
            # one file. A slot whose config is the champion's holds no test, so its record is written afresh.
            # One with a config of its own holds a test whose start cannot be read: nothing is started or
            # ended in it, and bot/promote.py and the summary say so every hour until the file is mended or
            # the test is voided (configs/void.yaml).
            try:
                idle = not configs_differ(name)
            except Exception:  # noqa: BLE001
                idle = False
            if idle:
                save(name, dict(IDLE))
                out[name] = dict(IDLE)
                print(f"[slot] {name}: its slot record (meta.json) could not be read ({type(e).__name__}: {e}); its "
                      f"config is the champion's, so it holds no test and the record was written afresh")
            else:
                print(f"[slot] WARNING: {name}: its slot record (meta.json) could not be read ({type(e).__name__}: "
                      f"{e}); no test is started or ended in it until it can be")
            continue
        differ = configs_differ(name)
        if differ and meta["status"] != "testing":
            cfg = config.account_cfg(name)
            meta = {
                "status": "testing",
                "hypothesis": cfg["hypothesis"],
                "started_at": int(now),
                "start_equity": {k: float(v) for k, v in equities.items() if k in (config.CHAMPION, name)},
                "ruleset": config.ruleset_stamp(),
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
    from . import promote            # promote imports this module; by the time this runs both are loaded
    now = now or int(time.time())
    meta = load(name)
    if meta["status"] != "testing":
        return f"{name}: idle (free for a hypothesis)"
    rules = config.risk_cfg()["challenger"]
    st = promote.rule_settings(rules)[0]
    first = st["window_days"]
    started = int(float(meta["started_at"]))
    elapsed_days = (now - started) / 86400
    two = promote.two_looks(meta, rules)
    total = promote.total_days(meta, rules)
    left = max(0.0, total - elapsed_days)
    look = promote.first_look_of(meta)
    # Due and not yet taken: it comes at the next hourly run, unless the candles for its window or a record are
    # not whole, and then the summary and the log say which.
    when = "at the next hourly run for which the market data and its record are whole"
    due = f" (due: taken {when})" if elapsed_days >= first and not look else ""
    if two:
        if not look:
            stage = f", first look at day {first:.0f}{due}"
        elif look.get("on") == "value":
            stage = ", kept on value at its first look"      # its trades are of value; it did not pass the rule
        else:
            stage = ", first look passed"
        stage += " (two look rule)"
        if look and elapsed_days >= total:
            stage += f" (its verdict is due: made {when})"
    else:
        stage = (f" (one look at day {first:.0f}{due}: promoted, killed, or kept {st['confirm_days']:.0f} more days "
                 f"if its trades are of value and it does not pass)")
    return (f"{name}: testing {meta['hypothesis']} since "
            f"{datetime.fromtimestamp(started, timezone.utc):%Y-%m-%d %H:%M}Z, "
            f"day {elapsed_days:.1f} of {total:.0f}, {left:.1f} days until the verdict{stage}")


def describe(now: int | None = None) -> str:
    """One line per slot. A slot whose record cannot be read gets a line saying
    so: this is printed in the workflow's Summary step, ahead of the commit of
    the hour's trading, and must not be what stops it."""
    lines = []
    for name in config.challengers():
        try:
            lines.append(describe_one(name, now))
        except Exception as e:  # noqa: BLE001
            lines.append(f"{name}: its slot record could not be read ({type(e).__name__}: {e})")
    return "\n".join(lines)


def free_slots() -> list[str]:
    """Slots with no test running. A slot whose record cannot be read is not free."""
    free = []
    for name in config.challengers():
        try:
            if load(name)["status"] != "testing":
                free.append(name)
        except Exception:  # noqa: BLE001
            pass
    return free


if __name__ == "__main__":
    config.prepare()
    print(describe())
    free = free_slots()
    print(f"free slots: {', '.join(free) if free else 'none'}")
    sys.exit(0)
