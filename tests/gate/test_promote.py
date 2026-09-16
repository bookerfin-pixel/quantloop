"""PROTECTED. The promotion rule, early kill, slot bookkeeping and legacy migration."""
import csv
import json

import pytest

from bot import config, promote, slot

RULES = {"slots": 3, "window_days": 21, "min_trades": 20, "max_dd_ratio": 1.5, "max_dd_floor": 0.10,
         "min_return_edge": 0.0, "early_kill_drawdown": 0.15}


def m(ret, dd, trades, gross=None, notional=0.0):
    bps = gross / (notional / 2) * 1e4 if gross is not None and notional else None
    return {"return": ret, "max_drawdown": dd, "trades": trades, "bars": 500, "fees": 10.0,
            "gross_pnl": gross, "traded_notional": notional, "realised_bps": bps}


def test_decide_rules():
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.06, 30), RULES)[0] == "promoted"
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.06, 5), RULES)[0] == "killed"     # too few fills
    assert promote.decide(m(0.02, -0.05, 30), m(0.01, -0.02, 30), RULES)[0] == "killed"    # worse return
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.12, 30), RULES)[0] == "killed"    # 12% > max(7.5%, 10%)
    assert promote.decide(m(None, None, 0), m(0.02, -0.01, 30), RULES)[0] == "killed"      # no data


def test_drawdown_floor_protects_against_a_flat_champion():
    # champion sat in cash: 0% drawdown. Without the floor any risk at all would be a kill.
    verdict, _ = promote.decide(m(0.0, 0.0, 0), m(0.04, -0.06, 30), RULES)
    assert verdict == "promoted"
    verdict, _ = promote.decide(m(0.0, 0.0, 0), m(0.04, -0.11, 30), RULES)
    assert verdict == "killed"


def test_early_kill():
    assert promote.early_kill(m(-0.16, -0.16, 3), RULES) is not None
    assert promote.early_kill(m(-0.05, -0.08, 3), RULES) is None
    assert promote.early_kill(m(None, None, 0), RULES) is None


def _write_equity(root, name, rows):
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "equity", "cash", "gross_exposure", "n_positions",
                                          "fees_paid", "slippage_paid"])
        w.writeheader()
        for ts, eq, fees in rows:
            w.writerow({"ts": ts, "equity": eq, "cash": eq, "gross_exposure": 0, "n_positions": 0,
                        "fees_paid": fees, "slippage_paid": 0})


def _write_trades(root, name, rows):
    p = root / "state" / name / "trades.csv"
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "account", "pair", "side", "qty", "price", "ref_price",
                                          "notional", "fee", "slippage_cost", "reason", "equity_after"])
        w.writeheader()
        for ts, notional in rows:
            w.writerow({"ts": ts, "account": name, "pair": "BTC", "side": "buy", "qty": 1, "price": 1,
                        "ref_price": 1, "notional": notional, "fee": 0, "slippage_cost": 0,
                        "reason": "", "equity_after": 0})


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    root = tmp_path
    (root / "configs").mkdir()
    (root / "state").mkdir()
    monkeypatch.setattr(config, "ROOT", root)
    monkeypatch.setattr(config, "CONFIGS", root / "configs")
    monkeypatch.setattr(config, "STATE", root / "state")
    monkeypatch.setattr(config, "ARCHIVE", root / "state" / "archive")
    monkeypatch.setattr(config, "LEDGER", root / "LEDGER.md")
    config.dump_yaml(root / "configs" / "risk.yaml", {"challenger": RULES, "pairs": ["BTC"]})
    config.dump_yaml(root / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    config.dump_yaml(root / "configs" / "challenger1.yaml",
                     {"hypothesis": "H1", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    config.dump_yaml(root / "configs" / "challenger2.yaml",
                     {"hypothesis": "H2", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    config.write_challenger_from_champion("challenger3")
    (root / "LEDGER.md").write_text(
        "# Ledger\n\n## H0: base\n- Status: champion\n\n## H1: longer\n- Expected gross bps per round trip: 150\n"
        "- Status: testing\n\n## H2: mr\n- Expected gross bps per round trip: 300\n- Status: testing\n")
    for name in ("champion", "challenger1", "challenger2", "challenger3"):
        (root / "state" / name).mkdir(parents=True, exist_ok=True)
        (root / "state" / name / "account.json").write_text(json.dumps({"cash": 1}))
    return root


def test_window_metrics_realised_bps(sandbox):
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (3600, 10100, 20)])   # +100 net, 20 costs -> 120 gross
    _write_trades(sandbox, "challenger1", [(1000, 3000), (2000, 3000)])         # 6000 traded = 3000 per round trip
    w = promote.window_metrics("challenger1", 0, 3600, 10000)
    assert w["gross_pnl"] == pytest.approx(120)
    assert w["realised_bps"] == pytest.approx(120 / 3000 * 1e4)


def test_promotion_copies_slot_into_champion_and_resets_that_slot_only(sandbox):
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0, "start_equity": {}})
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": 0, "start_equity": {}})
    promote.update_ledger("H1", "promoted", "because", m(0.01, -0.05, 30, 100, 1000),
                          m(0.02, -0.06, 30, 300, 3000), 0, 21 * 86400, "challenger1")
    promote.apply("promoted", "H1", "challenger1")
    champ = config.account_cfg("champion")
    assert champ["hypothesis"] == "H1" and champ["params"]["lookback_hours"] == 168
    assert config.strategy_signature(champ) == config.strategy_signature(config.account_cfg("challenger1"))
    assert slot.load("challenger1")["status"] == "idle"
    assert slot.load("challenger2")["status"] == "testing"                       # untouched
    assert config.account_cfg("challenger2")["hypothesis"] == "H2"
    assert not (sandbox / "state" / "challenger1" / "account.json").exists()     # archived
    assert list((sandbox / "state" / "archive").iterdir())
    text = (sandbox / "LEDGER.md").read_text()
    assert "- Status: promoted" in text and "### Result H1: promoted" in text and "- Slot: challenger1" in text
    assert "realised gross bps per round trip 2000 (ledger expected 150)" in text
    assert "## H2: mr\n- Expected gross bps per round trip: 300\n- Status: testing" in text   # H2 untouched


def test_kill_keeps_champion(sandbox):
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": 0, "start_equity": {}})
    promote.update_ledger("H2", "killed", "nope", m(0.02, -0.05, 30), m(0.01, -0.06, 30), 0, 21 * 86400, "challenger2")
    promote.apply("killed", "H2", "challenger2")
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    assert config.account_cfg("challenger2")["hypothesis"] == "H0"
    assert slot.load("challenger2")["status"] == "idle"
    assert "- Status: killed" in (sandbox / "LEDGER.md").read_text()


def test_slots_start_independently(sandbox):
    metas = slot.maybe_start(1000, {"champion": 10_000.0, "challenger1": 10_000.0,
                                     "challenger2": 9_000.0, "challenger3": 10_000.0})
    assert metas["challenger1"]["status"] == "testing" and metas["challenger1"]["hypothesis"] == "H1"
    assert metas["challenger2"]["status"] == "testing" and metas["challenger2"]["start_equity"]["challenger2"] == 9_000.0
    assert metas["challenger3"]["status"] == "idle"
    assert slot.free_slots() == ["challenger3"]
    # second call does not restart the clocks
    metas = slot.maybe_start(2000, {"champion": 1, "challenger1": 1, "challenger2": 1, "challenger3": 1})
    assert metas["challenger1"]["started_at"] == 1000


def test_main_early_kills_and_rules_at_window_end(sandbox):
    now = 21 * 86400 + 100
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0,
                              "start_equity": {"champion": 10000, "challenger1": 10000}})
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": now - 3 * 86400,
                              "start_equity": {"champion": 10000, "challenger2": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (now, 10300, 8)])
    _write_trades(sandbox, "challenger1", [(i * 3600, 1000) for i in range(25)])
    _write_equity(sandbox, "challenger2", [(now - 3 * 86400, 10000, 0), (now, 8200, 3)])   # -18%: early kill
    _write_trades(sandbox, "challenger2", [(now - 3600, 1000)])
    assert promote.main(["--now", str(now)]) == 0
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: promoted" in text
    assert "### Result H2: killed" in text and "early kill" in text
    assert config.account_cfg("champion")["hypothesis"] == "H1"
    assert slot.load("challenger1")["status"] == "idle" and slot.load("challenger2")["status"] == "idle"


def test_two_winners_same_hour_promotes_one_and_restarts_the_other(sandbox):
    now = 21 * 86400 + 100
    for name, hyp, end_eq in (("challenger1", "H1", 10300), ("challenger2", "H2", 10500)):
        slot.save(name, {"status": "testing", "hypothesis": hyp, "started_at": 0,
                         "start_equity": {"champion": 10000, name: 10000}})
        _write_equity(sandbox, name, [(0, 10000, 0), (now, end_eq, 8)])
        _write_trades(sandbox, name, [(i * 3600, 1000) for i in range(25)])
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    assert promote.main(["--now", str(now)]) == 0
    assert config.account_cfg("champion")["hypothesis"] == "H2"                  # the stronger one
    assert slot.load("challenger2")["status"] == "idle"
    meta1 = slot.load("challenger1")
    assert meta1["status"] == "testing" and meta1["started_at"] == now and meta1["restarted_against"] == "H2"
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: restarted" in text
    assert "## H1: longer\n- Expected gross bps per round trip: 150\n- Status: testing" in text


def test_legacy_single_challenger_is_migrated_into_slot_one(sandbox):
    (sandbox / "configs" / "challenger1.yaml").unlink()
    config.dump_yaml(sandbox / "configs" / "challenger.yaml",
                     {"hypothesis": "H9", "strategy": "ts_momentum", "params": {"lookback_hours": 9}})
    import shutil
    shutil.rmtree(sandbox / "state" / "challenger1")
    (sandbox / "state" / "challenger").mkdir()
    (sandbox / "state" / "challenger" / "meta.json").write_text(json.dumps(
        {"status": "testing", "hypothesis": "H9", "started_at": 5, "start_equity": {"challenger": 1.0}}))
    config.prepare()
    assert config.account_cfg("challenger1")["hypothesis"] == "H9"
    assert not (sandbox / "configs" / "challenger.yaml").exists()
    assert slot.load("challenger1")["hypothesis"] == "H9"
    assert not (sandbox / "state" / "challenger").exists()
