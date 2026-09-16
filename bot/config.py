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
ARCHIVE = STATE / "archive"
LEDGER = ROOT / "LEDGER.md"

CHAMPION = "champion"
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


def n_slots() -> int:
    return int(risk_cfg().get("challenger", {}).get("slots", 1))


def challengers() -> list[str]:
    return [f"challenger{i}" for i in range(1, n_slots() + 1)]


def accounts() -> list[str]:
    return [CHAMPION] + challengers()


def is_challenger(name: str) -> bool:
    return name in challengers()


def account_cfg(name: str) -> dict:
    if name not in accounts():
        raise ValueError(f"unknown account {name!r}; expected one of {accounts()}")
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


def write_challenger_from_champion(name: str) -> None:
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
    """Every slot needs a config file. A missing one is created idle (equal to
    the champion)."""
    created = []
    for name in challengers():
        if not (CONFIGS / f"{name}.yaml").exists():
            write_challenger_from_champion(name)
            created.append(name)
    return created


def prepare() -> None:
    """Run at the start of every entry point."""
    for line in migrate_legacy():
        print(f"[config] migrated {line}")
    for name in ensure_slot_configs():
        print(f"[config] created idle configs/{name}.yaml")
