"""PROTECTED. Rule 1 (PROMOTION.md): two looks before a promotion, the fast pass,
the unproven outcome, the confidence figure, what a finished trade is and what
it made, a test kept on the value of its trades, and old tests keeping their
one look."""
import csv
import json
import math

import pandas as pd
import pytest

from bot import config, promote, report, shadow, slot

DAY = 86400
RULES = {"slots": 2, "window_days": 60, "confirm_days": 60, "min_skill_t": 1.0, "fast_pass_skill_t": 2.0,
         "two_looks_from_ruleset": 7,
         "min_trades": 30, "max_dd_ratio": 1.5, "max_dd_floor": 0.10, "min_return_edge": 0.0,
         "compare_on": "skill", "min_skill": 0.0, "min_trade_profit": 0.0, "early_kill_drawdown": 0.15,
         "treadmill_kill_multiple": 3.0, "treadmill_min_days": 14,
         "confidence": {"prior": 0.10, "edge_sharpe": 1.5}}
GATE = {"max_cost_drag": 0.15}           # the one line of the gate's block the verdict code reads

STRONG = [0.0040, -0.0020] * 60          # +0.10% a day on 0.30% of noise: t of about 2.6 at day 60, 3.6 at day 120
STEADY = [0.0035, -0.0025] * 60          # +0.05% a day on 0.30% of noise: t of about 1.3 at day 60, 1.8 at day 120
THIN = [0.0062, -0.0058] * 60            # +0.02% a day on 0.60% of noise: above zero, t of about 0.4
LOSING = [-0.0030, 0.0010] * 60          # skill below zero
CHAMP = [-0.0004, 0.0000] * 60           # a champion that bleeds a little


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    root = tmp_path
    (root / "configs").mkdir()
    for attr, sub in (("ROOT", ""), ("CONFIGS", "configs"), ("STATE", "state"), ("CANDLES", "state/candles"),
                      ("HISTORY", "state/history"), ("ARCHIVE", "state/archive"), ("LEDGER", "LEDGER.md")):
        monkeypatch.setattr(config, attr, root / sub if sub else root)
    config.dump_yaml(root / "configs" / "risk.yaml", {"ruleset": 7, "challenger": RULES, "pairs": ["BTC"],
                                                      "initial_cash": 10000, "fee_bps": 10, "slippage_bps": 5,
                                                      "backtest_gate": GATE})
    config.dump_yaml(root / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    config.dump_yaml(root / "configs" / "challenger1.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    config.write_challenger_from_champion("challenger2")
    (root / "LEDGER.md").write_text("# Ledger\n\n## H0: base\n- Status: champion\n\n## H5: pick coins\n"
                                    "- Expected gross bps per round trip: 150\n- Status: testing\n")
    # a flat market: the basket makes nothing, so skill is simply the account's own return
    (root / "state" / "candles").mkdir(parents=True)
    hours = 125 * 24
    pd.DataFrame({"time": [i * 3600 for i in range(hours)], "open": 100.0, "high": 100.0, "low": 100.0,
                  "close": 100.0, "vwap": 100.0, "volume": 1, "count": 1}
                 ).to_csv(root / "state" / "candles" / "BTC.csv", index=False)
    monkeypatch.setattr(promote, "design_exposure", lambda cfg, before_ts, days=365: 0.5)
    return root


def equity(root, name, daily_returns):
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    eq = 10_000.0
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "equity", "cash", "gross_exposure", "n_positions",
                                          "fees_paid", "slippage_paid"])
        w.writeheader()
        for k, r in enumerate(daily_returns):
            eq *= 1 + r
            w.writerow({"ts": k * DAY + 3600, "equity": eq, "cash": eq / 2, "gross_exposure": eq / 2,
                        "n_positions": 1, "fees_paid": 0.01 * k, "slippage_paid": 0})


def trades(root, name, n=40, sides=("buy", "sell"), sell_price=101.0):
    """One fill a day: ten units bought at 100, then the sell that closes them,
    and so on, so n fills are n // 2 finished trades. At the default sell price
    each makes 10, a thousandth of the account. sides=("buy",) is a bot that
    only buys; sell_price=99.0 is one whose trades lose."""
    p = root / "state" / name / "trades.csv"
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "account", "pair", "side", "qty", "price", "ref_price",
                                          "notional", "fee", "slippage_cost", "reason", "equity_after"])
        w.writeheader()
        for i in range(n):
            side = sides[i % len(sides)]
            price = 100.0 if side == "buy" else sell_price
            w.writerow({"ts": (i + 1) * DAY, "account": name, "pair": "BTC", "side": side, "qty": 10,
                        "price": price, "ref_price": price, "notional": 10 * price, "fee": 0, "slippage_cost": 0,
                        "reason": "", "equity_after": 0})


def set_rules(root, **changes):
    """Rewrite the sandbox's rules file with some challenger keys changed (None removes one; False is
    how `off` reads)."""
    rules = {k: v for k, v in {**RULES, **changes}.items() if v is not None}
    config.dump_yaml(root / "configs" / "risk.yaml", {"ruleset": 7, "challenger": rules, "pairs": ["BTC"],
                                                      "initial_cash": 10000, "fee_bps": 10, "slippage_bps": 5,
                                                      "backtest_gate": GATE})
    return rules


def start_test(root, challenger_returns, ruleset=7, champion_returns=None):
    meta = {"status": "testing", "hypothesis": "H5", "started_at": 0,
            "start_equity": {"champion": 10000.0, "challenger1": 10000.0}}
    if ruleset is not None:
        meta["ruleset"] = ruleset
    slot.save("challenger1", meta)
    equity(root, "champion", CHAMP if champion_returns is None else champion_returns)
    equity(root, "challenger1", challenger_returns)
    trades(root, "challenger1")
    (root / "state" / "challenger1" / "account.json").write_text(json.dumps({"cash": 1}))


def at(day):
    return int(day * DAY + 2 * 3600)


def ledger(root):
    return (root / "LEDGER.md").read_text()


# --- the confidence figure ----------------------------------------------------------

def test_confidence_starts_at_the_prior_and_moves_slowly():
    c = lambda t, days: promote.confidence(t, days, RULES)       # noqa: E731
    assert c(None, 60) is None and c(1.0, 0) is None
    assert c(1.0, 60) == pytest.approx(0.145, abs=0.005)         # 60 days say little
    assert c(2.0, 365) == pytest.approx(0.42, abs=0.01)
    assert c(3.0, 365) == pytest.approx(0.76, abs=0.01)
    assert c(0.0, 120) < 0.10 < c(1.0, 120)                      # no skill shown pulls it under the start
    assert c(1.0, 120) < c(1.5, 120) < c(2.0, 120)
    # the same t over more days is worth less, not more, once it falls short of what a real edge would show
    assert c(1.0, 365) < c(1.0, 60)


def test_confidence_is_never_certain():
    """The sum has no room for "the measuring is wrong", so it may not say 0% or 100%."""
    c = lambda t, days: promote.confidence(t, days, RULES)       # noqa: E731
    assert promote.CONFIDENCE_FLOOR == 0.01 and promote.CONFIDENCE_CAP == 0.95
    assert c(-2.0, 365) == 0.01 and c(-30.0, 3650) == 0.01 and c(-1e9, 60) == 0.01
    assert c(6.0, 365) == 0.95 and c(30.0, 3650) == 0.95 and c(1e9, 60) == 0.95
    assert all(0.01 <= c(t, d) <= 0.95 for t in (-30, -3, 0, 3, 30) for d in (1, 60, 3650))
    assert 0.01 < c(3.0, 365) < 0.95                             # and inside the limits it is the plain sum
    low = promote.confidence_text({"skill_t": -4.0, "skill_days": 200}, RULES)
    high = promote.confidence_text({"skill_t": 9.0, "skill_days": 200}, RULES)
    assert low.startswith("1% or less that this is a real edge")
    assert high.startswith("95%, the most this figure will say, that this is a real edge")
    assert promote.confidence_text({"skill_t": None, "skill_days": 0}, RULES).startswith("10%, the starting figure")


def test_confidence_follows_the_formula_in_the_docstring():
    t, days = 1.7, 150
    m = 1.5 * math.sqrt(days / 365)
    odds = (0.10 / 0.90) * math.exp(m * (2 * t - m) / 2)
    assert promote.confidence(t, days, RULES) == pytest.approx(odds / (1 + odds))
    assert promote.confidence(t, days, {}) == pytest.approx(odds / (1 + odds))       # the defaults are these numbers


def test_skill_t_reads_the_accounts_own_daily_skill(sandbox):
    start_test(sandbox, STRONG)
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)
    import numpy as np
    d = np.array(STRONG)
    want = d.mean() / (d.std(ddof=1) / math.sqrt(len(d)))
    assert chal["skill_days"] == 120 and chal["skill_t"] == pytest.approx(want, rel=0.02)
    assert chal["skill_t"] > 3 and champ["skill_t"] < 0
    thin = np.array(THIN)
    equity(sandbox, "challenger1", THIN)
    _, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)
    assert 0 < chal["skill_t"] < 1 and chal["skill"] > 0 and thin.sum() > 0


# --- which tests get two looks ----------------------------------------------------------

def test_only_tests_that_began_under_the_new_ruleset_get_two_looks():
    assert promote.two_looks({"ruleset": 7}, RULES) and promote.two_looks({"ruleset": 9}, RULES)
    assert not promote.two_looks({"ruleset": 6}, RULES) and not promote.two_looks({"ruleset": "6"}, RULES)
    assert not promote.two_looks({}, RULES) and not promote.two_looks({"ruleset": None}, RULES)
    # the switch is two_looks_from_ruleset alone; a missing confirm_days means the documented 60
    without_confirm = {k: v for k, v in RULES.items() if k != "confirm_days"}
    assert promote.two_looks({"ruleset": 7}, without_confirm) and promote.total_days({"ruleset": 7}, without_confirm) == 120
    assert not promote.two_looks({"ruleset": 7}, {**RULES, "two_looks_from_ruleset": False})    # `off` in the file
    # a line that is simply not there is not "off": the documented ruleset 7 stands in
    assert promote.two_looks({"ruleset": 7}, {k: v for k, v in RULES.items() if k != "two_looks_from_ruleset"})
    assert promote.two_looks({"ruleset": "7"}, RULES) and promote.two_looks({"ruleset": 7.0}, RULES)
    assert promote.two_looks({"ruleset": "7.0"}, RULES)
    # A stamp that is there and cannot be read is not an old test's stamp (those have none, or a number under
    # seven). Read as an old one it put a new test on the one look rule, and a thin pass was promoted at day 60.
    for odd in ("seven", "7b", [7], True, {"n": 7}):
        assert promote.two_looks({"ruleset": odd}, RULES), odd
    assert promote.total_days({"ruleset": 7}, RULES) == 120 and promote.total_days({}, RULES) == 60


# --- the two looks, end to end through main ------------------------------------------------

def test_a_first_look_pass_earns_sixty_more_days_and_is_not_a_promotion(sandbox):
    start_test(sandbox, STEADY)
    assert promote.main(["--now", str(at(30))]) == 0
    assert "First look" not in ledger(sandbox)
    assert promote.main(["--now", str(at(60))]) == 0
    text = ledger(sandbox)
    assert "### First look H5: passed" in text and "### Result H5" not in text
    assert "- Status: testing" in text                               # the entry is still under test
    assert "Not a promotion: 60 more days" in text and "- Confidence: " in text
    meta = slot.load("challenger1")
    assert meta["status"] == "testing" and meta["first_look"]["at"] == at(60)
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    assert (sandbox / "state" / "challenger1" / "equity.csv").exists()   # nothing archived
    # the next hours change nothing: one block, not one an hour
    promote.main(["--now", str(at(60) + 3600)])
    promote.main(["--now", str(at(90))])
    assert ledger(sandbox).count("### First look H5") == 1 and "### Result H5" not in ledger(sandbox)
    assert "day 90.1 of 120" in slot.describe_one("challenger1", at(90))
    assert "first look passed (two look rule)" in slot.describe_one("challenger1", at(90))


def test_a_steady_edge_is_promoted_at_day_120(sandbox):
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    assert promote.main(["--now", str(at(120))]) == 0
    text = ledger(sandbox)
    assert "### Result H5: promoted" in text and "- Status: promoted" in text
    assert "second look" in text and "at or above the 1.0 bar" in text
    assert config.account_cfg("champion")["hypothesis"] == "H5"
    assert shadow.load()["status"] == "active"                       # the shadow guard still stands behind it
    assert slot.load("challenger1")["status"] == "idle"
    result = text[text.index("### Result H5"):]
    assert "- Confidence: " in result and "Two look rule (measured" not in result


# --- the fast pass ---------------------------------------------------------------------------

def test_the_fast_pass_bar():
    assert promote.fast_pass({"skill_t": 1.99, "skill_days": 61}, RULES) is None
    said = promote.fast_pass({"skill_t": 2.0, "skill_days": 61}, RULES)
    assert said and "+2.00 over 61 days" in said and "2.0 fast pass bar" in said
    assert promote.fast_pass({"skill_t": float("nan"), "skill_days": 61}, RULES) is None   # NaN < bar is False
    assert promote.fast_pass({"skill_t": 9.0, "skill_days": 61}, {**RULES, "fast_pass_skill_t": None}) is None
    assert promote.fast_pass({"skill_t": None, "skill_days": 0}, RULES) is None       # no reading, no fast pass
    assert promote.fast_pass({"skill_t": 9.0, "skill_days": 61},
                             {k: v for k, v in RULES.items() if k != "fast_pass_skill_t"}) is None


def test_a_first_look_strong_enough_on_its_own_is_promoted_at_day_60(sandbox):
    start_test(sandbox, STRONG)
    _, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert chal["skill_t"] >= 2.0
    assert promote.main(["--now", str(at(60))]) == 0
    text = ledger(sandbox)
    assert "### Result H5: promoted" in text and "- Status: promoted" in text
    assert "first look:" in text and "at or above the 2.0 fast pass bar" in text
    assert "### First look H5" not in text                         # a verdict, not a stage
    assert config.account_cfg("champion")["hypothesis"] == "H5"
    assert shadow.load()["status"] == "active" and slot.load("challenger1")["status"] == "idle"
    assert "- Confidence: " in text[text.index("### Result H5"):]


def test_without_a_fast_pass_bar_a_strong_first_look_still_waits(sandbox):
    rules = set_rules(sandbox, fast_pass_skill_t=None)
    assert "fast_pass_skill_t" not in rules
    start_test(sandbox, STRONG)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox) and "### Result H5" not in ledger(sandbox)
    promote.main(["--now", str(at(120))])
    assert "### Result H5: promoted" in ledger(sandbox) and "fast pass" not in ledger(sandbox)


def test_the_fast_pass_is_asked_once_at_the_first_look_and_never_after(sandbox):
    """Every extra look is another chance for luck. A test that only gets strong
    after its first look waits for day 120 like any other."""
    late = STEADY[:60] + [0.0060, 0.0010] * 30
    start_test(sandbox, late)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    _, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(100), RULES)
    assert chal["skill_t"] >= 2.0                                   # it would clear the bar now
    for day in (70, 85, 100, 119):
        promote.main(["--now", str(at(day))])
    assert "### Result H5" not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    promote.main(["--now", str(at(120))])
    assert "### Result H5: promoted" in ledger(sandbox) and "second look" in ledger(sandbox)


def test_a_fast_pass_still_needs_the_rule_itself(sandbox):
    """A high t does not promote a test that does not pass the rule: here the
    champion did better still. It is of value, so it is kept, not promoted."""
    start_test(sandbox, STRONG, champion_returns=[0.0060, -0.0020] * 60)
    _, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert chal["skill_t"] >= 2.0
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### First look H5: kept on value" in text and "### Result H5" not in text
    assert "it does not pass the rule (challenger skill" in text and "did not beat champion skill" in text
    assert "but its trades are of value: its 20 finished trades made +2.00% of its starting equity after costs " \
           "(20 won, 0 lost)" in text
    assert "fast pass" not in text and config.account_cfg("champion")["hypothesis"] == "H0"
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: unproven" in text and "Its trades are of value all the same" in text   # kept, not crowned
    assert config.account_cfg("champion")["hypothesis"] == "H0"


# --- too few fills, and trades of value ----------------------------------------------------------------

def test_a_slow_test_whose_trades_were_of_value_is_not_killed_for_trading_little(sandbox):
    """Fin, 2026-10-05: if it trades less but its trades are of value, that is a
    usable skill. So it is kept. It is not promoted either, however good the
    numbers: a handful of good trades cannot be told from luck."""
    start_test(sandbox, STRONG)                                      # a t of 2.6 at day 60, which would fast pass
    trades(sandbox, "challenger1", n=12)                             # six finished trades, each a winner
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### First look H5: kept on value" in text and "### Result H5" not in text
    assert "it does not pass the rule (challenger made 12 fills, fewer than the 30 the rule asks for before it rules " \
           "in a strategy's favour: too few separate bets to tell from luck), but its trades are of value: its 6 " \
           "finished trades made +0.60% of its starting equity after costs (6 won, 0 lost)" in text
    assert "cannot be judged" not in text                             # it was judged: its trades are of value
    assert "A test whose trades are of value is kept, not killed" in text and "fast pass" not in text
    meta = slot.load("challenger1")
    assert meta["status"] == "testing" and meta["first_look"]["on"] == "value"
    assert config.account_cfg("champion")["hypothesis"] == "H0" and shadow.load()["status"] != "active"
    promote.main(["--now", str(at(90))])
    assert "### Result H5" not in ledger(sandbox) and ledger(sandbox).count("### First look H5") == 1
    # day 120 and still short of 30 fills: it passes the rule's numbers, and that is not proof
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: unproven" in text and "- Status: unproven" in text
    assert "but it made 12 fills, fewer than the 30 a promotion needs: too few separate bets" in text
    assert "does not count against the idea's family" in text
    assert slot.load("challenger1")["status"] == "idle" and config.account_cfg("champion")["hypothesis"] == "H0"


def test_a_slow_test_that_reaches_thirty_fills_by_day_120_gets_the_ordinary_verdict(sandbox):
    start_test(sandbox, STRONG)
    trades(sandbox, "challenger1", n=20)                             # one a day: 20 by day 60
    promote.main(["--now", str(at(60))])
    assert "### First look H5: kept on value" in ledger(sandbox)
    trades(sandbox, "challenger1", n=45)                             # 45 by day 120
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: promoted" in text and "second look:" in text and "at or above the 1.0 bar" in text


def test_a_slow_test_whose_trades_lost_money_is_killed(sandbox):
    """"If not, kill." Twenty nine fills, fourteen finished trades, every one a loss."""
    start_test(sandbox, LOSING)
    trades(sandbox, "challenger1", n=29, sell_price=99.0)
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "- Status: killed" in text and "First look H5" not in text
    assert "first look: challenger made 29 fills, fewer than the 30 the rule asks for" in text
    assert "It is not kept on value either: its 14 finished trades made -1.40% of its starting equity after costs " \
           "(0 won, 14 lost), and a test that does not pass the rule is kept only when they have made money" in text
    assert slot.load("challenger1")["status"] == "idle"


def test_a_test_whose_trades_made_money_is_kept_even_when_the_account_is_behind(sandbox):
    """The other half of the same steer. The account is behind the champion and
    behind the market; the positions it chose to leave made money. Kept for 60
    more days, and at day 120 unproven, not killed."""
    start_test(sandbox, [-0.0012, 0.0006] * 60)                      # loses 0.03% a day; the champion 0.02%
    trades(sandbox, "challenger1", n=40)                             # twenty winners
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### First look H5: kept on value" in text and "### Result H5" not in text
    assert "it does not pass the rule (challenger skill -1.90%" in text and "did not beat champion skill -1.23%" in text
    assert "its 20 finished trades made +2.00% of its starting equity after costs (20 won, 0 lost)" in text
    promote.main(["--now", str(at(120))])
    assert "### Result H5: unproven" in ledger(sandbox) and "Its trades are of value all the same" in ledger(sandbox)
    # the same account once it slides past the drawdown guard is killed, trades of value or not
    start_test(sandbox, LOSING)
    (sandbox / "LEDGER.md").write_text(ledger(sandbox).split("## Results")[0].replace("- Status: unproven", "- Status: testing"))
    promote.main(["--now", str(at(60))])
    assert "### First look H5: kept on value" in ledger(sandbox)
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "second look:" in text and "exceeded the limit" in text


def test_a_test_that_only_bought_and_held_is_killed_however_much_it_shows(sandbox):
    """Fin, 2026-10-05: selling at the right time is the skill; kill bots that
    are just buying and holding. Buys and no sell is no finished trade, with
    twelve fills or with forty, and whatever the numbers say."""
    for n in (12, 40):
        start_test(sandbox, STRONG)
        (sandbox / "LEDGER.md").write_text(ledger(sandbox).split("## Results")[0].replace("- Status: killed", "- Status: testing"))
        trades(sandbox, "challenger1", n=n, sides=("buy",))
        promote.main(["--now", str(at(60))])
        text = ledger(sandbox)
        assert "### Result H5: killed" in text and "First look H5" not in text
        assert f"it has finished no trade of its own: none of its {n} fills closed a position it had bought or had " \
               f"chosen to keep, so the +" in text and "it shows is not from an exit it chose" in text
        if n == 40:                                                  # its numbers pass, and that does not save it
            assert "It clears the rule's numbers all the same (challenger skill" in text
            assert "a test that has not left a position by its own choice is not promoted on them" in text
        else:
            assert "Nor does it pass the rule: challenger made 12 fills" in text
        assert config.account_cfg("champion")["hypothesis"] == "H0"


def test_what_counts_as_a_finished_trade(sandbox):
    start_test(sandbox, STRONG)
    count = lambda: promote.window_metrics("challenger1", 0, at(60), 10000.0)["round_trips"]     # noqa: E731

    def fills(rows):
        """(day, pair, side, qty)"""
        pd.DataFrame([{"ts": int(d * DAY), "account": "challenger1", "pair": p, "side": sd, "qty": q, "price": 1,
                       "ref_price": 1, "notional": 1000, "fee": 0, "slippage_cost": 0, "reason": "", "equity_after": 0}
                      for d, p, sd, q in rows]).to_csv(sandbox / "state" / "challenger1" / "trades.csv", index=False)

    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 1.0)])
    assert count() == 1
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 0.05)])                    # a trim is not an exit
    assert count() == 0
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 0.9)])                     # a tenth is still held: not out
    assert count() == 0
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 0.96)])                    # a twentieth or less left: out
    assert count() == 1
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 0.5), (3, "BTC", "sell", 0.5)])     # sold in pieces: once
    assert count() == 1
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 0.96), (3, "BTC", "sell", 0.04)])   # the crumb sold later
    assert count() == 1                                                          # is not a second trade
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "buy", 1.0), (3, "BTC", "sell", 1.0), (4, "BTC", "sell", 1.0)])
    assert count() == 1                                                          # bought twice, left once
    fills([(1, "BTC", "buy", 1.0), (2, "ETH", "buy", 1.0), (3, "ETH", "sell", 1.0)])      # two pairs held, one left:
    assert count() == 1                                                          # each pair is its own position
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", 1.0), (3, "BTC", "buy", 1.0), (4, "BTC", "sell", 1.0)])
    assert count() == 2
    fills([(70, "BTC", "buy", 1.0), (71, "BTC", "sell", 1.0)])                   # after the window: not in it
    assert count() == 0
    fills([(1, "BTC", "buy", 1.0), (2, "BTC", "sell", float("nan"))])            # a quantity that is not a number
    assert count() == 0                                                          # is not a sell
    assert promote.finished_trades(pd.DataFrame({"ts": [1], "side": ["buy"]})) == []     # columns missing: nothing counted


def test_a_position_held_from_before_the_test_is_judged_from_its_size_at_the_start(sandbox):
    """A slot runs the champion's config while it is idle, so a test can begin
    holding positions it never bought (H4 began with five). The fills before
    the test say how big they were. Trimming one is not leaving it, selling it
    in the first day is the last config's unwinding, and leaving it later is
    this strategy's own exit."""
    start_test(sandbox, STRONG)
    begin = 10 * DAY                                                             # the test begins on day 10
    count = lambda: promote.window_metrics("challenger1", begin, at(60), 10000.0)["round_trips"]   # noqa: E731

    def fills(rows):
        pd.DataFrame([{"ts": int(d * DAY), "account": "challenger1", "pair": p, "side": sd, "qty": q, "price": 1,
                       "ref_price": 1, "notional": 1000, "fee": 0, "slippage_cost": 0, "reason": "", "equity_after": 0}
                      for d, p, sd, q in rows]).to_csv(sandbox / "state" / "challenger1" / "trades.csv", index=False)

    before = [(5, "SOL", "buy", 10.0)]
    fills(before + [(30, "SOL", "sell", 2.0)])                                   # a trim of what it was handed
    assert count() == 0
    fills(before + [(30, "SOL", "sell", 2.0), (31, "SOL", "sell", 3.0), (32, "SOL", "sell", 4.0)])   # nine tenths gone
    assert count() == 0
    fills(before + [(30, "SOL", "sell", 10.0)])                                  # left on day 20 of the test
    assert count() == 1
    fills(before + [(30, "SOL", "sell", 6.0), (40, "SOL", "sell", 4.0)])         # left in two pieces: once
    assert count() == 1
    fills(before + [(10.5, "SOL", "sell", 10.0)])                                # sold in the test's first day:
    assert count() == 0                                                          # the unwinding of the last config
    fills(before + [(10.1, "SOL", "sell", 4.0), (30, "SOL", "sell", 6.0)])       # part unwound, the rest kept, then left
    assert count() == 1
    fills(before + [(10.1, "SOL", "buy", 5.0), (10.6, "SOL", "sell", 15.0)])     # it bought more, so the position is
    assert count() == 1                                                          # its own, first day or not
    fills([(5, "SOL", "buy", 10.0), (7, "SOL", "sell", 5.0), (30, "SOL", "sell", 4.6)])   # 5 held at the start, 0.4 left
    assert count() == 0                                                          # more than a twentieth of the 5
    fills([(5, "SOL", "buy", 10.0), (7, "SOL", "sell", 5.0), (30, "SOL", "sell", 4.8)])   # 0.2 left
    assert count() == 1
    fills([(5, "SOL", "buy", 10.0), (8, "SOL", "sell", 10.0)])                   # bought and left before the test
    assert count() == 0
    fills([(5, "SOL", "buy", 10.0), (8, "SOL", "sell", 10.0), (20, "SOL", "buy", 3.0), (25, "SOL", "sell", 3.0)])
    assert count() == 1                                                          # only the one inside the test
    # rows lost from the file: a sell of something it does not show. Read as leaving a holding from before
    fills([(30, "ETH", "sell", 1.0)])
    assert count() == 1
    fills([(10.5, "ETH", "sell", 1.0)])                                          # ...and not in the first day
    assert count() == 0
    assert promote.window_metrics("challenger1", begin, at(60), 10000.0)["trades"] == 1    # fills inside the window


def test_a_test_that_made_no_trades_at_all_is_killed(sandbox):
    start_test(sandbox, STRONG)
    trades(sandbox, "challenger1", n=0)
    promote.main(["--now", str(at(60))])
    assert "### Result H5: killed" in ledger(sandbox) and "it made no trades to judge" in ledger(sandbox)


def fills_file(sandbox, rows):
    """(day, pair, side, qty, price[, fee[, reason]]) as a trades file for challenger1."""
    out = []
    for row in rows:
        d, pair, side, qty, price = row[:5]
        fee = row[5] if len(row) > 5 else 0.0
        out.append({"ts": int(d * DAY), "account": "challenger1", "pair": pair, "side": side, "qty": qty,
                    "price": price, "ref_price": price, "notional": qty * price, "fee": fee, "slippage_cost": 0,
                    "reason": row[6] if len(row) > 6 else "", "equity_after": 0})
    pd.DataFrame(out).to_csv(sandbox / "state" / "challenger1" / "trades.csv", index=False)


def test_what_a_finished_trade_made_is_counted_after_costs(sandbox):
    start_test(sandbox, STRONG)
    m = lambda start=0: promote.window_metrics("challenger1", start, at(60), 10000.0)         # noqa: E731
    # bought 10 at 100 and sold at 105, a fee of 1 each way: 50 less 2
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0, 1.0), (2, "BTC", "sell", 10, 105.0, 1.0)])
    got = m()
    assert got["round_trips"] == 1 and got["trade_profit"] == pytest.approx(0.0048)
    assert (got["trade_wins"], got["trade_losses"], got["trade_unknown"]) == (1, 0, 0)
    assert promote.trade_tally(got) == "its 1 finished trade made +0.48% of its starting equity after costs (1 won, 0 lost)"
    # bought in two lots, sold in two lots: one trade, and the sums are the whole position's
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0), (2, "BTC", "buy", 10, 110.0), (3, "BTC", "sell", 15, 120.0),
                         (4, "BTC", "sell", 5, 90.0)])
    got = m()
    assert got["round_trips"] == 1 and got["trade_profit"] == pytest.approx((15 * 120 + 5 * 90 - 2100) / 10000)
    # a winner and a loser: both count, and a position still open does not
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0), (2, "BTC", "sell", 10, 104.0), (3, "ETH", "buy", 10, 50.0),
                         (4, "ETH", "sell", 10, 47.0), (5, "SOL", "buy", 10, 20.0)])
    got = m()
    assert got["round_trips"] == 2 and got["trade_profit"] == pytest.approx((40 - 30) / 10000)
    assert (got["trade_wins"], got["trade_losses"]) == (1, 1)
    # a crumb left behind is valued at the price of the sell that closed the position
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0), (2, "BTC", "sell", 9.6, 110.0)])
    assert m()["trade_profit"] == pytest.approx((9.6 * 110 + 0.4 * 110 - 1000) / 10000)
    # a trim makes nothing yet: nothing is counted until the position is left
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0), (2, "BTC", "sell", 5, 150.0)])
    got = m()
    assert got["round_trips"] == 0 and got["trade_profit"] is None
    # no fills at all, or a file without the columns: nothing to count, and no error
    fills_file(sandbox, [(70, "BTC", "buy", 10, 100.0)])
    assert m()["trade_profit"] is None and m()["trades"] == 0
    assert promote.finished_trades(pd.DataFrame({"ts": [1], "side": ["buy"]})) == []


def test_a_position_held_from_before_the_test_is_costed_at_its_price_when_the_test_began(sandbox):
    """Only what happened during the test counts. The slot bought SOL at 20
    while it was idle; the test began with SOL at 100 (the sandbox's candles)
    and left it at 110. That is 10 a unit, not 90."""
    start_test(sandbox, STRONG)
    pd.read_csv(sandbox / "state" / "candles" / "BTC.csv").to_csv(sandbox / "state" / "candles" / "SOL.csv", index=False)
    begin = 10 * DAY
    m = lambda: promote.window_metrics("challenger1", begin, at(60), 10000.0)                 # noqa: E731
    fills_file(sandbox, [(5, "SOL", "buy", 10, 20.0), (30, "SOL", "sell", 10, 110.0)])
    got = m()
    assert got["round_trips"] == 1 and got["trade_profit"] == pytest.approx(100 / 10000)
    # bought more during the test: the old units at 100, the new ones at what was paid
    fills_file(sandbox, [(5, "SOL", "buy", 10, 20.0), (12, "SOL", "buy", 10, 90.0), (30, "SOL", "sell", 20, 110.0)])
    assert m()["trade_profit"] == pytest.approx((2200 - 1000 - 900) / 10000)
    # part unwound in the first day at 95, the rest left later at 110: all of it since the start
    fills_file(sandbox, [(5, "SOL", "buy", 10, 20.0), (10.1, "SOL", "sell", 4, 95.0), (30, "SOL", "sell", 6, 110.0)])
    assert m()["trade_profit"] == pytest.approx((380 + 660 - 1000) / 10000)
    # no candles for the pair: the price of its first fill in the test stands in for the price at the start
    fills_file(sandbox, [(5, "XYZ", "buy", 10, 20.0), (30, "XYZ", "sell", 5, 40.0), (40, "XYZ", "sell", 5, 50.0)])
    assert m()["trade_profit"] == pytest.approx((200 + 250 - 400) / 10000)
    # a sell the file cannot explain is a finished trade with no figure
    fills_file(sandbox, [(30, "ETH", "sell", 1, 50.0)])
    got = m()
    assert got["round_trips"] == 1 and got["trade_profit"] is None and got["trade_unknown"] == 1
    assert "cannot be put a figure on from the record" in promote.trade_tally(got)


def test_a_position_closed_by_the_daily_loss_halt_is_not_an_exit_the_strategy_chose(sandbox):
    """The daily loss halt sells the whole book, and a strategy that raises is
    sold out. A bot whose only target is "always long" would otherwise show a
    finished trade the first time the halt sold it."""
    from bot import run
    assert promote.REPLAYED == run.REPLAYED
    halt = "daily halt: equity 11482.46 is down 5.1% from the day's open"
    assert promote._forced(halt) and promote._forced("daily halt in force: flat for the rest of the UTC day")
    assert promote._forced(run.REPLAYED + halt) and promote._forced("strategy error ValueError: bad")
    assert not promote._forced("exit: price more than 2.0% below 24h EMA") and not promote._forced(None)
    assert not promote._forced(float("nan")) and not promote._forced("stay long | daily halt is mentioned later")
    start_test(sandbox, STRONG)
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0, 0.0, "enter long"), (2, "BTC", "sell", 10, 94.0, 0.0, halt),
                         (3, "BTC", "buy", 10, 95.0, 0.0, "enter long")])
    got = promote.window_metrics("challenger1", 0, at(60), 10000.0)
    assert got["round_trips"] == 0 and got["forced_exits"] == 1
    assert got["trade_profit"] == pytest.approx(-60 / 10000)          # the money is counted all the same
    said = promote.no_trade_of_its_own({**got, "return": 0.02})
    assert said == ("it has finished no trade of its own: none of its 3 fills closed a position it had bought or had "
                    "chosen to keep (1 position was closed for it by the daily loss halt or a strategy error, which "
                    "is not a choice), so the +2.00% it shows is not from an exit it chose")
    promote.main(["--now", str(at(60))])
    assert "### Result H5: killed" in ledger(sandbox) and "which is not a choice" in ledger(sandbox)
    # one exit of its own beside it, and it has finished a trade; the tally says which were forced
    fills_file(sandbox, [(1, "BTC", "buy", 10, 100.0, 0.0, "enter long"), (2, "BTC", "sell", 10, 94.0, 0.0, halt),
                         (3, "BTC", "buy", 10, 95.0, 0.0, "enter long"), (4, "BTC", "sell", 10, 106.0, 0.0, "exit")])
    got = promote.window_metrics("challenger1", 0, at(60), 10000.0)
    assert got["round_trips"] == 1 and got["forced_exits"] == 1 and promote.no_trade_of_its_own({**got, "return": 0.0}) is None
    assert promote.trade_tally(got) == ("its 2 finished trades made +0.50% of its starting equity after costs (1 won, "
                                        "1 lost, 1 of them closed by the daily loss halt or a strategy error)")


def test_of_value_asks_for_a_trade_of_its_own_trades_that_made_money_and_the_drawdown_guard():
    champ = {"return": 0.0, "max_drawdown": -0.02}
    base = {"return": 0.05, "trades": 4, "round_trips": 2, "trade_profit": 0.02, "trade_wins": 2, "trade_losses": 0,
            "max_drawdown": -0.03}
    v = lambda **k: promote.of_value(champ, {**base, **k}, RULES)                # noqa: E731
    ok, why = v()
    assert ok is True and why == "its 2 finished trades made +2.00% of its starting equity after costs (2 won, 0 lost)"
    assert v(round_trips=1, trade_wins=1)[1].startswith("its 1 finished trade made")
    assert v(trade_profit=0.0001)[0] is True                                     # any profit after costs is enough
    for made in (0.0, -0.0001, -0.03):
        no, why = v(trade_profit=made, trade_wins=0, trade_losses=2)
        assert no is False and why.endswith("and a test that does not pass the rule is kept only when they have made money")
    assert v(trade_profit=None)[0] is False and v(trade_profit=float("nan"))[0] is False
    assert v(round_trips=0)[0] is False and "it has finished no trade of its own" in v(round_trips=0)[1]
    assert v(trades=0) == (False, "it made no trades to judge")
    assert v(**{"return": float("nan")}) == (False, "there is no usable record of what it made")
    assert v(max_drawdown=-0.12)[0] is False and "exceeded the limit" in v(max_drawdown=-0.12)[1]
    # the floor can be raised in the rules file; under it the sentence says what was asked
    strict = {**RULES, "min_trade_profit": 0.01}
    assert promote.of_value(champ, {**base, "trade_profit": 0.0101}, strict)[0] is True
    no, why = promote.of_value(champ, {**base, "trade_profit": 0.0099}, strict)
    assert no is False and why.endswith("kept only when they have made more than 1.00% of it")
    assert promote.too_few_fills({"return": 0.1, "trades": 30}, RULES) is None
    assert "it made 29 fills, fewer than the 30 a promotion needs" == promote.too_few_fills({"return": 0.1, "trades": 29}, RULES)
    assert "it made 1 fill, fewer than the 30 a promotion needs" == promote.too_few_fills({"return": 0.1, "trades": 1}, RULES)
    assert promote.too_few_fills({"return": None, "trades": 0}, RULES) is None


def test_an_old_test_that_does_not_pass_its_rule_but_whose_trades_are_of_value_is_kept_too(sandbox):
    """H1, H2 and H4 began under the one look rule, which killed for too few
    fills. Fin's steer covers them: trades of value, they get the 60 more days
    and the two look verdict; not of value, they are killed."""
    start_test(sandbox, STRONG, ruleset=6)
    trades(sandbox, "challenger1", n=6)
    interim = promote.other_rule_reading(*promote.paired_slot("challenger1", slot.load("challenger1"), at(30), RULES)[:2],
                                         RULES, 30.0)
    assert "on today's numbers it would be kept at day 60 on the value of its trades without passing the rule, the " \
           "same as under its own rule. From there the two rules are one: 60 more days, and a promotion asks for " \
           "a daily skill t of 1.0 over all 120 (its daily skill t is +" in interim
    line = slot.describe_one("challenger1", at(30))
    assert "day 30.1 of 60" in line
    assert line.endswith("(one look at day 60: promoted, killed, or kept 60 more days if its trades are of value "
                         "and it does not pass)")
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### First look H5: kept on value" in text and "### Result H5" not in text
    meta = slot.load("challenger1")
    assert meta["ruleset"] == 6 and promote.two_looks(meta, RULES)   # from here on it is a two look test
    assert "day 61.1 of 120" in slot.describe_one("challenger1", at(61))
    line = slot.describe_one("challenger1", at(61))
    assert "kept on value at its first look (two look rule)" in line and "first look passed" not in line
    assert "two look rule (measured" not in report.test_section(at(61))
    promote.main(["--now", str(at(120))])
    assert "### Result H5: unproven" in ledger(sandbox)              # 6 fills in 120 days: kept, not proven


def test_an_old_test_whose_trades_are_not_of_value_is_killed(sandbox):
    start_test(sandbox, LOSING, ruleset=6)
    trades(sandbox, "challenger1", n=6, sell_price=99.0)
    promote.main(["--now", str(at(60))])
    result = ledger(sandbox)[ledger(sandbox).index("### Result H5"):]
    assert "### Result H5: killed" in result and "- Status: killed" in ledger(sandbox)
    assert "challenger made 6 fills, fewer than the 30 the rule asks for" in result
    assert "It is not kept on value either: its 3 finished trades made -0.30% of its starting equity after costs" in result
    assert "first look:" not in result.split("- Two look rule")[0]   # an old test has no first look to speak of
    assert "- Two look rule (measured, not applied to this test): the two look rule would also have ended it here, " \
           "for the same reason" in result


def test_the_summary_says_when_a_test_is_not_on_pace_for_the_fills_a_promotion_needs(sandbox):
    start_test(sandbox, STEADY)
    trades(sandbox, "challenger1", n=1)
    assert "  fills: " not in report.test_section(at(5))             # one fill in five days, and too early to say
    assert "  fills: 1 in 7.1 days" in report.test_section(at(7))    # from day 7 it is said
    trades(sandbox, "challenger1", n=3)
    week3 = report.test_section(at(20))
    assert "  fills: 3 in 20.1 days; at this pace about 17 by day 120, under the 30 a promotion needs" in week3
    assert "Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills " \
           "one whose are not" in week3 and "ends unproven, not promoted" in week3
    trades(sandbox, "challenger1", n=6)                              # 6 by day 20: 35 by day 120, and 17 by day 60
    assert "  fills: 6 in 20.1 days; at this pace about 17 by day 60, under the 30 a pass at the first look needs, " \
           "and about 35 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then " \
           "ruled on at day 120" in report.test_section(at(20))
    trades(sandbox, "challenger1", n=12)                             # 12 by day 20 is on pace for both
    assert "  fills: " not in report.test_section(at(20))
    assert report.fills_pace({"trades": 0}, RULES, 30.0, 120.0).startswith("0 in 30.0 days; at this pace about 0")
    assert "it is past day 60 and still running" in report.fills_pace({"trades": 5}, RULES, 80.0, 120.0)
    assert report.fills_pace({"trades": 5}, RULES, 120.5, 120.0) is None        # the verdict speaks from here on
    # 29.9 is not 30: the line never says "about 30 ... under the 30", for either day
    assert "about 29 by day 120, under the 30" in report.fills_pace({"trades": 10}, RULES, 40.1, 120.0)
    assert "about 29 by day 60, under the 30" in report.fills_pace({"trades": 10}, RULES, 20.05, 120.0)
    # a test from before ruleset 7 is promoted at day 60 if it passes there, and the line says that
    old = report.fills_pace({"trades": 12}, RULES, 30.0, 120.0, one_look=True)
    assert old == ("12 in 30.0 days; at this pace about 24 by day 60, under the 30 a promotion there needs, and "
                   "about 48 by day 120. Short of them at day 60 it is kept only if its trades are of value, and "
                   "then ruled on at day 120")
    assert "under the 30 a pass at the first look needs" in report.fills_pace({"trades": 12}, RULES, 30.0, 120.0)
    assert report.fills_pace({"trades": 16}, RULES, 30.0, 120.0, one_look=True) is None
    assert report.fills_pace({"trades": 16}, RULES, 30.0, 120.0) is None
    assert report.fills_pace({"trades": 25}, RULES, 61.0, 120.0) is None          # past the first look, on pace for 120


def test_the_summary_shows_what_each_tests_finished_trades_made(sandbox):
    start_test(sandbox, STEADY)
    text = report.test_section(at(30))
    assert "  trades: its 15 finished trades made +1.50% of its starting equity after costs (15 won, 0 lost). Of " \
           "value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)" in text
    trades(sandbox, "challenger1", n=30, sides=("buy",))
    held = report.test_section(at(30))
    assert "  trades: it has finished no trade of its own: none of its 30 fills closed a position it had bought or " \
           "had chosen to keep" in held
    assert "A test that has finished no trade of its own by its look is killed" in held
    trades(sandbox, "challenger1", n=30, sell_price=99.0)
    lost = report.test_section(at(30))
    assert "  trades: its 15 finished trades made -1.50% of its starting equity after costs (0 won, 15 lost), and a " \
           "test that does not pass the rule is kept only when they have made money" in lost
    trades(sandbox, "challenger1", n=0)
    assert "  trades: none yet." in report.test_section(at(30))
    assert "a finished trade is a position the account left" in text         # the legend


# --- tests that were already running finish under the old rule ---------------------------------

@pytest.mark.parametrize("stamp", [None, 6])
def test_a_test_from_before_the_rule_is_judged_at_day_60_by_the_old_rule(sandbox, stamp):
    start_test(sandbox, THIN, ruleset=stamp)                           # the old rule promotes this; the new would not
    assert "day 30.1 of 60" in slot.describe_one("challenger1", at(30))
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H5: promoted" in text and "First look" not in text
    assert config.account_cfg("champion")["hypothesis"] == "H5"
    result = text[text.index("### Result H5"):]
    assert "- Confidence: " in result
    assert "- Two look rule (measured, not applied to this test): it passes the first look, and the two look rule " \
           "would not promote it yet" in result


@pytest.mark.parametrize("series,said", [
    (STRONG, "at or above the 2.0 fast pass bar: the two look rule would also have promoted it here"),
    (LOSING, "the two look rule would also have ended it here, for the same reason"),
])
def test_an_old_test_says_what_the_two_look_rule_would_have_done(sandbox, series, said):
    start_test(sandbox, series, ruleset=6)
    if series is LOSING:
        trades(sandbox, "challenger1", sell_price=99.0)              # and its trades lost money
    promote.main(["--now", str(at(60))])
    result = ledger(sandbox)[ledger(sandbox).index("### Result H5"):]
    assert "- Two look rule (measured, not applied to this test): " in result and said in result
    assert ("### Result H5: promoted" in result) == (series is STRONG)     # and the old rule decided it


def test_the_summary_shows_both_readings_for_an_old_test_and_one_for_a_new_one(sandbox):
    start_test(sandbox, THIN, ruleset=None)
    old = report.test_section(at(30))
    assert "confidence: " in old and "that this is a real edge (every idea starts at 10%" in old
    assert "two look rule (measured, not applied to this test): on today's numbers it would pass the first look " \
           "at day 60, where its own rule promotes it; its daily skill t is +" in old
    assert "and the two look rule would need 2.0 at day 60 to be promoted there, or 1.0 by day 120" in old
    # a test that only bought is not of value, and that comes before whether its numbers pass
    trades(sandbox, "challenger1", n=40, sides=("buy",))
    held = report.test_section(at(30))
    assert "two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, " \
           "the same as under its own rule" in held
    assert "it would pass the first look" not in held
    trades(sandbox, "challenger1")
    start_test(sandbox, THIN, ruleset=7)
    new = report.test_section(at(30))
    assert "confidence: " in new and "two look rule (measured" not in new
    assert "day 30.1 of 120" in new and "first look at day 60 (two look rule)" in new


def test_a_restart_against_a_new_champion_begins_with_a_fresh_first_look(sandbox):
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    assert slot.load("challenger1").get("first_look")
    promote.restart("challenger1", at(61), {"champion": 10000.0, "challenger1": 10500.0}, "H9")
    meta = slot.load("challenger1")
    assert "first_look" not in meta and meta["started_at"] == at(61) and meta["ruleset"] == 7
