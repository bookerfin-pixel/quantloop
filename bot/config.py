"""Paths and config loading. PROTECTED."""
from __future__ import annotations

import os
from pathlib import Path

import yaml

ROOT = Path(os.environ.get("QUANTLOOP_ROOT", Path(__file__).resolve().parent.parent))
CONFIGS = ROOT / "configs"
STATE = ROOT / "state"
CANDLES = STATE / "candles"
ARCHIVE = STATE / "archive"
LEDGER = ROOT / "LEDGER.md"

ACCOUNTS = ("champion", "challenger")


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


def account_cfg(name: str) -> dict:
    if name not in ACCOUNTS:
        raise ValueError(f"unknown account {name!r}; expected one of {ACCOUNTS}")
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
    decide whether the challenger differs from the champion."""
    return yaml.safe_dump({"strategy": cfg["strategy"], "params": cfg["params"]}, sort_keys=True)
