"""PROTECTED. Verdicts on skill: beta removed, timing kept, noise reported."""
import csv
import json

import pytest

from bot import config, promote

RULES = {"slots": 3, "window_days": 60, "min_trades": 30, "max_dd_ratio": 1.5, "max_dd_floor": 0.10,
         "min_return_edge": 0.0, "early_kill_drawdown": 0.15}


def m(ret, exp, basket, dd=-0.05, trades=40):
    d = {"return": ret, "max_drawdown": dd, "trades": trades, "bars": 1440, "fees": 10.0, "gross_pnl": None,
         "traded_notional": 0.0, "realised_bps": None, "avg_exposure": exp, "skill": None,
         "edge_t": None, "edge_days": 0}
    return promote.add_skill(d, basket)


def test_skill_is_return_minus_the_basket_at_the_same_average_exposure():
    assert m(0.20, 0.72, 0.2334)["skill"] == pytest.approx(0.20 - 0.72 * 0.2334)
    assert m(0.03, 0.0, 0.25)["skill"] == pytest.approx(0.03)
    assert m(0.03, 0.5, None)["skill"] is None                     # no basket data, no skill


def test_a_rally_does_not_decide_the_verdict_on_skill():
    # the basket rose 25%: a 90% invested champion made 20% (it lagged the market it held),
    # a 20% invested challenger made 5% (all of it beyond its exposure)
    champ, chal = m(0.20, 0.90, 0.25), m(0.05, 0.20, 0.25)
    assert promote.decide(champ, chal, {**RULES, "compare_on": "return"})[0] == "killed"
    verdict, reason = promote.decide(champ, chal, {**RULES, "compare_on": "skill"})
    assert verdict == "promoted" and "skill" in reason


def test_skill_rule_still_kills_a_challenger_that_is_only_less_invested():
    # falling basket: the challenger lost less only because it held less
    champ, chal = m(-0.16, 0.80, -0.20), m(-0.05, 0.20, -0.20)   # skills 0.00 and -0.01
    assert promote.decide(champ, chal, {**RULES, "compare_on": "return"})[0] == "promoted"
    assert promote.decide(champ, chal, {**RULES, "compare_on": "skill"})[0] == "killed"


def test_skill_rule_falls_back_to_return_without_market_data():
    champ, chal = m(0.01, 0.5, None), m(0.02, 0.5, None)
    assert promote.compare_on({**RULES, "compare_on": "skill"}, champ, chal) == "return"
    assert promote.decide(champ, chal, {**RULES, "compare_on": "skill"})[0] == "promoted"


def test_drawdown_and_min_trades_guards_apply_on_skill_too():
    champ = m(0.20, 0.90, 0.25, dd=-0.04)
    assert promote.decide(champ, m(0.05, 0.20, 0.25, trades=5), {**RULES, "compare_on": "skill"})[0] == "killed"
    assert promote.decide(champ, m(0.05, 0.20, 0.25, dd=-0.12), {**RULES, "compare_on": "skill"})[0] == "killed"


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    return tmp_path


def _equity(root, name, daily_returns, start=0):
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    eq = 10_000.0
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "equity", "cash", "gross_exposure", "n_positions",
                                          "fees_paid", "slippage_paid"])
        w.writeheader()
        for k, r in enumerate(daily_returns):
            eq *= 1 + r
            w.writerow({"ts": start + k * 86400 + 3600, "equity": eq, "cash": 0, "gross_exposure": eq * 0.5,
                        "n_positions": 1, "fees_paid": 0, "slippage_paid": 0})


def test_edge_t_separates_a_steady_edge_from_noise(sandbox):
    import numpy as np
    rng = np.random.default_rng(0)
    base = rng.normal(0, 0.03, 60)
    _equity(sandbox, "champion", base)
    _equity(sandbox, "steady", base + 0.004 + rng.normal(0, 0.002, 60))
    _equity(sandbox, "noisy", base + rng.normal(0, 0.03, 60))
    se = {"champion": 10_000.0, "steady": 10_000.0, "noisy": 10_000.0}
    champ = promote.window_metrics("champion", 0, 60 * 86400, 10_000.0)
    t_steady, n = promote.edge_t("champion", "steady", 0, 60 * 86400, se, champ, champ, None, "return")
    t_noisy, _ = promote.edge_t("champion", "noisy", 0, 60 * 86400, se, champ, champ, None, "return")
    assert n == 60 and t_steady > 5 and abs(t_noisy) < 3


def test_beating_a_weak_champion_is_not_enough_without_positive_skill():
    rules = {**RULES, "compare_on": "skill", "min_skill": 0.0}
    champ = m(-0.20, 0.60, -0.10)                       # skill -14%: a fees treadmill
    no_edge = m(-0.03, 0.30, -0.10)                     # skill 0.0: held the market, nothing more
    real = m(0.01, 0.30, -0.10)                         # skill +4%
    verdict, reason = promote.decide(champ, no_edge, rules)
    assert verdict == "killed" and "floor" in reason
    assert promote.decide(champ, real, rules)[0] == "promoted"
    assert promote.decide(champ, no_edge, {k: v for k, v in rules.items() if k != "min_skill"})[0] == "promoted"
    assert promote.decide(champ, no_edge, rules, absolute=False)[0] == "promoted"   # the shadow check
