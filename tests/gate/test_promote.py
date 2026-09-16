"""PROTECTED. The promotion rule and the ledger bookkeeping."""
import json

import pytest

from bot import config, promote, slot

RULES = {"window_days": 21, "min_trades": 20, "max_dd_ratio": 1.5, "min_return_edge": 0.0}


def m(ret, dd, trades):
    return {"return": ret, "max_drawdown": dd, "trades": trades, "bars": 500, "fees": 10.0}


def test_decide_rules():
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.06, 30), RULES)[0] == "promoted"
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.06, 5), RULES)[0] == "killed"     # too few fills
    assert promote.decide(m(0.02, -0.05, 30), m(0.01, -0.02, 30), RULES)[0] == "killed"    # worse return
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.09, 30), RULES)[0] == "killed"    # drawdown 1.8x
    assert promote.decide(m(None, None, 0), m(0.02, -0.01, 30), RULES)[0] == "killed"      # no data


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    root = tmp_path
    (root / "configs").mkdir()
    (root / "state" / "challenger").mkdir(parents=True)
    (root / "state" / "champion").mkdir(parents=True)
    monkeypatch.setattr(config, "ROOT", root)
    monkeypatch.setattr(config, "CONFIGS", root / "configs")
    monkeypatch.setattr(config, "STATE", root / "state")
    monkeypatch.setattr(config, "ARCHIVE", root / "state" / "archive")
    monkeypatch.setattr(config, "LEDGER", root / "LEDGER.md")
    monkeypatch.setattr(slot, "META", root / "state" / "challenger" / "meta.json")
    config.dump_yaml(root / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    config.dump_yaml(root / "configs" / "challenger.yaml",
                     {"hypothesis": "H1", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (root / "LEDGER.md").write_text("# Ledger\n\n## H0: base\n- Status: champion\n\n## H1: longer\n- Status: testing\n")
    (root / "state" / "challenger" / "account.json").write_text(json.dumps({"cash": 1}))
    slot.save({"status": "testing", "hypothesis": "H1", "started_at": 0, "start_equity": {}})
    return root


def test_promotion_copies_challenger_into_champion_and_resets(sandbox):
    promote.update_ledger("H1", "promoted", "because", m(0.01, -0.05, 30), m(0.02, -0.06, 30), 0, 21 * 86400)
    promote.apply("promoted", "H1")
    champ = config.account_cfg("champion")
    chal = config.account_cfg("challenger")
    assert champ["hypothesis"] == "H1" and champ["params"]["lookback_hours"] == 168
    assert config.strategy_signature(champ) == config.strategy_signature(chal)
    assert slot.load()["status"] == "idle"
    assert not (sandbox / "state" / "challenger" / "account.json").exists()      # archived
    assert list((sandbox / "state" / "archive").iterdir())
    text = (sandbox / "LEDGER.md").read_text()
    assert "- Status: promoted" in text and "### Result H1: promoted" in text
    assert "- Status: champion" in text                                          # H0 untouched


def test_kill_keeps_champion(sandbox):
    promote.update_ledger("H1", "killed", "nope", m(0.02, -0.05, 30), m(0.01, -0.06, 30), 0, 21 * 86400)
    promote.apply("killed", "H1")
    champ = config.account_cfg("champion")
    assert champ["hypothesis"] == "H0" and champ["params"]["lookback_hours"] == 72
    assert config.account_cfg("challenger")["hypothesis"] == "H0"
    assert "- Status: killed" in (sandbox / "LEDGER.md").read_text()


def test_slot_starts_when_configs_differ(sandbox):
    slot.save({"status": "idle", "hypothesis": None, "started_at": None, "start_equity": {}})
    meta = slot.maybe_start(1000, {"champion": 10_000.0, "challenger": 10_000.0})
    assert meta["status"] == "testing" and meta["hypothesis"] == "H1" and meta["started_at"] == 1000
    # second call does not restart the clock
    meta = slot.maybe_start(2000, {"champion": 1, "challenger": 1})
    assert meta["started_at"] == 1000
