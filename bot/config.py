"""Paths and config loading. PROTECTED."""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import yaml

ROOT = Path(os.environ.get("QUANTLOOP_ROOT", Path(__file__).resolve().parent.parent))
CONFIGS = ROOT / "configs"
STATE = ROOT / "state"
CANDLES = STATE / "candles"
HISTORY = STATE / "history"
ARCHIVE = STATE / "archive"
LEDGER = ROOT / "LEDGER.md"

CHAMPION = "champion"
SHADOW = "shadow"
CHALLENGER_HEADER = ("# The agent edits this file. When it differs from champion.yaml the bot starts a\n"
                     "# prospective test in this slot automatically. `hypothesis` must match the newest\n"
                     "# entry in LEDGER.md.\n")


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f) or {}


def dump_yaml(path: Path, data: dict, header: str | None = None) -> None:
    text = yaml.safe_dump(data, sort_keys=False)
    if header:
        text = header.rstrip("\n") + "\n" + text
    path.write_text(text)


def risk_cfg() -> dict:
    return load_yaml(CONFIGS / "risk.yaml")


NO_RULESET = "unreadable"


def ruleset_number():
    """The `ruleset:` line of configs/risk.yaml as a number, or None when it
    is missing, blank or not a number (`7` and `'7'` are both 7)."""
    rs = risk_cfg().get("ruleset")
    try:
        if rs is None or isinstance(rs, bool):
            return None
        n = float(rs)
        if n != n or n in (float("inf"), float("-inf")):
            return None
        return int(n) if n == int(n) else n
    except (TypeError, ValueError, OverflowError):
        return None


def ruleset_stamp():
    """What to stamp on a test that starts now: the ruleset number, or
    NO_RULESET when that line cannot be read. Never nothing: a test with no
    stamp is read as one from before rulesets existed and keeps the one look
    rule, so a blank `ruleset:` line put new tests on it (found in review,
    2026-10-05). A stamp that is there and is not a number means two looks
    (bot/promote.py, `two_looks`)."""
    n = ruleset_number()
    return NO_RULESET if n is None else n


def n_slots() -> int:
    """How many challenger slots there are: `challenger.slots`, a whole number
    of 1 or more. Anything else stops whatever asked. With a wrong count some
    slots are simply not run, and a test in one of them stands still with
    nothing said: `slots: 2.9` ran two slots and a slip in the line's name
    ran one, the run going green each hour (found in review, 2026-10-05)."""
    block = risk_cfg().get("challenger")
    raw = block.get("slots") if isinstance(block, dict) else None
    try:
        if isinstance(raw, bool) or not isinstance(raw, (int, float)) or raw != int(raw) or raw < 1:
            raise ValueError
    except (ValueError, OverflowError):
        raise ValueError(f"configs/risk.yaml: challenger.slots must be a whole number of 1 or more, and it is "
                         f"{raw!r}; nothing is run until it is mended") from None
    return int(raw)


def challengers() -> list[str]:
    return [f"challenger{i}" for i in range(1, n_slots() + 1)]


def shadow_active() -> bool:
    """The deposed champion keeps running for one window after a promotion."""
    meta = STATE / SHADOW / "meta.json"
    if not (CONFIGS / "shadow.yaml").exists() or not meta.exists():
        return False
    try:
        return json.loads(meta.read_text()).get("status") == "active"
    except Exception:  # noqa: BLE001
        return False


def accounts() -> list[str]:
    names = [CHAMPION] + challengers()
    if shadow_active():
        names.append(SHADOW)
    return names


def is_challenger(name: str) -> bool:
    return name in challengers()


def account_cfg(name: str) -> dict:
    allowed = [CHAMPION, SHADOW] + challengers()
    if name not in allowed:
        raise ValueError(f"unknown account {name!r}; expected one of {allowed}")
    cfg = load_yaml(CONFIGS / f"{name}.yaml")
    for key in ("hypothesis", "strategy", "params"):
        if key not in cfg:
            raise ValueError(f"configs/{name}.yaml is missing required key {key!r}")
    if not isinstance(cfg["params"], dict):
        raise ValueError(f"configs/{name}.yaml: params must be a mapping")
    return cfg


def account_dir(name: str) -> Path:
    d = STATE / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def strategy_signature(cfg: dict) -> str:
    """Canonical text of the part of a config that changes behaviour. Used to
    decide whether a challenger differs from the champion."""
    return yaml.safe_dump({"strategy": cfg["strategy"], "params": cfg["params"]}, sort_keys=True)


# What an idle slot holds from ruleset 8 on (Fin, 2026-10-08): nothing. Until then it held the champion's config,
# so a new test began on the champion's book and spent its first hour unwinding it. The strategy is bot/run.py's.
CASH_CFG = {"hypothesis": "cash", "strategy": "cash", "params": {}}


def is_cash(cfg: dict) -> bool:
    return isinstance(cfg, dict) and cfg.get("strategy") == CASH_CFG["strategy"]


def write_challenger_idle(name: str) -> None:
    """A slot with no test: its config is cash."""
    dump_yaml(CONFIGS / f"{name}.yaml", dict(CASH_CFG, params={}), CHALLENGER_HEADER)


def write_challenger_from_champion(name: str) -> None:
    """A slot given the champion's config. Before ruleset 8 that was what made a slot idle; it is still read as
    idle (bot/slot.py, configs_differ), and the hourly ruling moves such a slot to cash."""
    champ = account_cfg(CHAMPION)
    dump_yaml(CONFIGS / f"{name}.yaml",
              {"hypothesis": champ["hypothesis"], "strategy": champ["strategy"], "params": champ["params"]},
              CHALLENGER_HEADER)


def migrate_legacy() -> list[str]:
    """The first version had one challenger at configs/challenger.yaml and
    state/challenger/. Move it into slot 1 the first time the new code runs, so
    a test that was already under way carries on uninterrupted."""
    moved = []
    old_cfg, new_cfg = CONFIGS / "challenger.yaml", CONFIGS / "challenger1.yaml"
    if old_cfg.exists() and not new_cfg.exists():
        shutil.move(str(old_cfg), str(new_cfg))
        moved.append("configs/challenger.yaml -> configs/challenger1.yaml")
    old_state, new_state = STATE / "challenger", STATE / "challenger1"
    if old_state.exists() and not new_state.exists():
        shutil.move(str(old_state), str(new_state))
        moved.append("state/challenger/ -> state/challenger1/")
        meta = new_state / "meta.json"
        if meta.exists():
            m = json.loads(meta.read_text())
            se = m.get("start_equity") or {}
            if "challenger" in se and "challenger1" not in se:
                se["challenger1"] = se.pop("challenger")
                m["start_equity"] = se
                meta.write_text(json.dumps(m, indent=2, sort_keys=True))
    return moved


def ensure_slot_configs() -> list[str]:
    """Every slot needs a config file. A missing one is created idle (cash)."""
    created = []
    for name in challengers():
        if not (CONFIGS / f"{name}.yaml").exists():
            write_challenger_idle(name)
            created.append(name)
    return created


def prepare() -> None:
    """Run at the start of every entry point."""
    for line in migrate_legacy():
        print(f"[config] migrated {line}")
    for name in ensure_slot_configs():
        print(f"[config] created idle configs/{name}.yaml")
