"""PROTECTED. The decision step and the backtest share one code path."""
import pandas as pd
import pytest

from bot import backtest, config, data, paper, strategy
from bot.run import step

RCFG = {
    "fee_bps": 10, "slippage_bps": 5, "initial_cash": 10_000, "pairs": ["BTC", "ETH"],
    "history_hours": 720, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0,
    "min_trade_notional": 50, "rebalance_threshold": 0.05, "daily_loss_halt": 0.05,
    "backtest_gate": {"min_days": 7, "max_days": 120, "max_drawdown": 0.3,
                      "min_cost_coverage": 1.0, "max_trades_per_pair_per_day": 4},
}


def candles(n=400, seed=1):
    return {p: data.SyntheticSource(["BTC", "ETH"], n=n, seed=seed, start=1_700_000_000).ohlc(p)
            for p in ["BTC", "ETH"]}


def test_step_fills_toward_target_and_logs_reason():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    fn = lambda c, p, w: {"BTC": strategy.Target(0.2, "because"), "ETH": 0.0}  # noqa: E731
    decisions, fills, equity = step(acct, {"params": {}}, fn, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_000_000, RCFG)
    assert len(fills) == 1 and fills[0].side == "buy"
    assert fills[0].notional == pytest.approx(2000.0, rel=1e-3)
    btc = next(d for d in decisions if d["pair"] == "BTC")
    assert btc["action"] == "buy" and "because" in btc["reason"]
    assert equity < 10_000  # costs were paid


def test_strategy_error_goes_flat_not_crash():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 1000.0, 100.0, 1, "seed")
    def boom(c, p, w):
        raise RuntimeError("bad")
    decisions, fills, _ = step(acct, {"params": {}}, boom, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_000_000, RCFG)
    assert fills and fills[0].side == "sell" and "BTC" not in acct.positions
    assert "strategy error" in decisions[0]["reason"]
    from bot import promote, run
    assert promote._forced(fills[0].reason)                  # not an exit the strategy chose
    # the same sell in the account's first hour under a new strategy, for a position held over from the last
    # one, and in an hour that is replayed: the engine puts words before the reason, and it is still not a choice
    acct.trade("BTC", 1000.0, 100.0, 2, "seed")
    _, fills, _ = step(acct, {"params": {}}, boom, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_003_600, RCFG, fresh=True)
    assert fills[0].reason.startswith(promote.AS_IF_FLAT[0] + "strategy error") and promote._forced(fills[0].reason)
    acct.trade("BTC", 1000.0, 100.0, 3, "seed")
    acct.state["inherited"] = ["BTC"]
    _, fills, _ = step(acct, {"params": {}}, boom, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_007_200, RCFG)
    assert fills[0].reason.startswith(promote.AS_IF_FLAT[1] + "strategy error") and promote._forced(fills[0].reason)
    assert promote.REPLAYED == run.REPLAYED and promote._forced(run.REPLAYED + fills[0].reason)
    # an exit the strategy chose stays one, whatever comes before its reason or sits inside it
    for own in ("exit: z back inside 0.5", promote.AS_IF_FLAT[1] + "flat", run.REPLAYED + "trend down | strategy error",
                None, float("nan")):
        assert not promote._forced(own)


def test_a_strategy_that_asks_the_interpreter_to_stop_is_a_strategy_error_and_not_the_end_of_the_run():
    """sys.exit() and exit() are not Exceptions. From a strategy they used to end the hourly run there and
    then, with exit code 0 and a green tick, and every account after that one went undecided (found in
    review, 2026-10-07). They are handled like any other failure: flat, with the reason on the record."""
    from bot import promote, run
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 1000.0, 100.0, 1, "seed")

    def quits(c, p, w):
        raise SystemExit(0)

    def closes(c, p, w):
        raise GeneratorExit("gone")
    decisions, fills, equity = step(acct, {"params": {}}, quits, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_000_000, RCFG)
    assert fills and fills[0].side == "sell" and "BTC" not in acct.positions and equity > 0
    assert all(d["reason"].endswith("strategy error SystemExit: 0") for d in decisions) and len(decisions) == 2
    assert run.ERRED == "strategy error " and promote._forced(fills[0].reason)
    acct.trade("BTC", 1000.0, 100.0, 2, "seed")
    decisions, fills, _ = step(acct, {"params": {}}, closes, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_003_600, RCFG)
    assert fills and "strategy error GeneratorExit: gone" in decisions[0]["reason"]

    def interrupted(c, p, w):
        raise KeyboardInterrupt
    with pytest.raises(KeyboardInterrupt):                      # somebody stopping the run by hand still stops it
        step(acct, {"params": {}}, interrupted, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_007_200, RCFG)
    # and the backtest goes on through such an hour, as the hourly loop does, and counts it on the record
    calls = {"n": 0}

    def quits_now_and_then(c, p, w):
        calls["n"] += 1
        if calls["n"] % 50 == 0:
            raise SystemExit(3)
        return {pair: 0.2 for pair in c}
    strategy.STRATEGIES["quits_now_and_then"] = quits_now_and_then
    try:
        m = backtest.run_backtest(candles(300), {"strategy": "quits_now_and_then", "params": {}}, RCFG, record=True)
    finally:
        del strategy.STRATEGIES["quits_now_and_then"]
    path = m["path"]
    assert path["errors"] == calls["n"] // 50 >= 4 and path["first_error"] == "SystemExit: 3" and len(path["ts"]) == calls["n"]
    assert path["memory_hours"] == RCFG["history_hours"] == 720
    clean = backtest.run_backtest(candles(300), {"strategy": "ts_momentum", "params": {"lookback_hours": 24, "ema_hours": 6}}, RCFG, record=True)["path"]
    assert clean["errors"] == 0 and clean["first_error"] is None


def test_daily_halt_flattens_and_blocks_new_entries():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 2000.0, 100.0, 1, "seed")
    fn = lambda c, p, w: {"BTC": 0.25, "ETH": 0.25}  # noqa: E731
    ts = 1_700_000_000
    step(acct, {"params": {}}, fn, candles(), {"BTC": 100.0, "ETH": 50.0}, ts, RCFG)      # sets the day open
    _, fills, _ = step(acct, {"params": {}}, fn, candles(), {"BTC": 60.0, "ETH": 50.0}, ts + 3600, RCFG)
    assert all(f.side == "sell" for f in fills) and not acct.positions
    assert acct.state["halted_day"] is not None
    # the verdict code tells these sells from exits the strategy chose by how their reason begins
    from bot import promote
    assert fills and all(promote._forced(f.reason) for f in fills)


def test_backtest_costs_match_paper_model_and_metrics_are_consistent():
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum",
           "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
    m = backtest.run_backtest(candles(n=600), cfg, RCFG, max_days=None)
    assert m["bars"] > 100 and m["n_trades"] > 0
    assert m["net_pnl"] == pytest.approx(m["gross_pnl"] - m["fees"] - m["slippage"], abs=0.05)
    assert m["final_equity"] == pytest.approx(RCFG["initial_cash"] * (1 + m["total_return"]), rel=1e-4)
    assert -1 < m["max_drawdown"] <= 0
    assert m["fees"] > 0 and m["slippage"] > 0
    # fee per unit notional is exactly fee_bps: slippage is exactly slippage_bps of notional at the ref price
    assert m["fees"] == pytest.approx(m["slippage"] * 2, rel=0.02)


def test_backtest_refuses_thin_data():
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}}
    with pytest.raises(ValueError):
        backtest.run_backtest(candles(n=60), cfg, RCFG)


def test_config_loader_rejects_incomplete_config(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "CONFIGS", tmp_path)
    (tmp_path / "risk.yaml").write_text("challenger:\n  slots: 3\n")
    (tmp_path / "challenger1.yaml").write_text("strategy: ts_momentum\n")
    with pytest.raises(ValueError):
        config.account_cfg("challenger1")
    with pytest.raises(ValueError):
        config.account_cfg("challenger9")


def test_backtest_tolerates_a_pair_with_shorter_history():
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum",
           "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
    c = candles(n=600)
    c["ETH"] = c["ETH"].iloc[300:].reset_index(drop=True)      # ETH only exists for the second half
    m = backtest.run_backtest(c, cfg, RCFG, max_days=None)
    assert m["bars"] > 500                                     # the clock is BTC's full length
    assert m["pairs"] == 2
    assert m["final_equity"] == pytest.approx(RCFG["initial_cash"] * (1 + m["total_return"]), rel=1e-4)


GATE_RULES = {"min_days": 7, "max_days": 365, "min_trades": 30, "max_cost_drag": 0.15,
              "max_avg_fills_per_pair_per_day": 1.0, "max_drawdown": 0.30, "drawdown_vs_basket": 0.75}


def _metrics(**kw):
    base = {"days": 365.0, "pairs": 10, "n_trades": 400, "fees": 500.0, "slippage": 250.0,
            "max_drawdown": -0.20, "total_return": 0.05, "avg_gross_exposure": 0.5, "equity_curve": []}
    base.update(kw)
    return base


def test_plausibility_is_regime_independent():
    bear = {"basket_return": -0.565, "basket_max_dd": -0.715, "basket_path": None}
    calm = {"basket_return": 0.10, "basket_max_dd": -0.15, "basket_path": None}
    # a 45% drawdown passes in a year whose basket fell 71.5% (limit 0.75 x 71.5% = 53.6%) ...
    problems, report = backtest.plausibility(_metrics(max_drawdown=-0.45), GATE_RULES, bear, 10_000)
    assert problems == [] and report["drawdown_limit"] == pytest.approx(-0.536, abs=1e-3)
    # ... and fails in a calm year (limit is the 30% floor)
    problems, _ = backtest.plausibility(_metrics(max_drawdown=-0.45), GATE_RULES, calm, 10_000)
    assert any("drawdown" in p for p in problems)
    # losing money in sample is not a gate failure; it is reported as skill vs benchmark
    problems, report = backtest.plausibility(_metrics(total_return=-0.31, avg_gross_exposure=0.38), GATE_RULES, bear, 10_000)
    assert problems == []
    assert report["exposure_matched_benchmark"] == pytest.approx(-0.565 * 0.38, abs=1e-4)
    assert report["skill_vs_benchmark"] == pytest.approx(-0.31 + 0.565 * 0.38, abs=1e-4)


def test_plausibility_catches_the_fee_treadmill_and_thin_evidence():
    problems, report = backtest.plausibility(_metrics(fees=1800.0, slippage=900.0, n_trades=2775), GATE_RULES, None, 10_000)
    assert report["cost_drag_per_year"] == pytest.approx(0.27)
    assert any("treadmill" in p for p in problems)
    problems, _ = backtest.plausibility(_metrics(n_trades=12), GATE_RULES, None, 10_000)
    assert any("fewer than the 30" in p for p in problems)
    problems, _ = backtest.plausibility(_metrics(n_trades=4000, fees=100.0, slippage=50.0), GATE_RULES, None, 10_000)
    assert any("fills per pair per day" in p for p in problems)


def test_gate_skips_when_no_slot_config_changed():
    import importlib.util, os, sys
    spec = importlib.util.spec_from_file_location("bg", os.path.join(os.getcwd(), "gate", "backtest_gate.py"))
    bg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bg)
    assert bg.slot_from_paths(["notes/2026-09-17.md", "hypotheses/backlog.md"]) is None
    assert bg.slot_from_paths(["LEDGER.md", "configs/challenger2.yaml"]) == "challenger2"
    assert bg.slot_from_paths(["configs/champion.yaml", "configs/risk.yaml"]) is None


def _needs(n):
    def fn(c, params, w):
        out = {}
        for p, df in c.items():
            if len(df) < n:
                out[p] = strategy.Target(0.0, f"flat: only {len(df)} candles, need {n}")
            else:
                out[p] = strategy.Target(0.2, "enter")
        return out
    return fn


def test_a_short_backtest_still_hands_the_strategy_its_full_history(monkeypatch):
    """Until 2026-10-04 a short backtest cut the history to the replayed window
    plus the largest single *_hours parameter, so a strategy needing more sat
    flat on "only N candles" for the whole run and the result looked like calm."""
    monkeypatch.setitem(strategy.STRATEGIES, "needs_400", _needs(400))
    cfg = {"hypothesis": "HX", "strategy": "needs_400", "params": {"x_hours": 50}}
    m = backtest.run_backtest(candles(n=700), cfg, RCFG, max_days=3)
    assert m["n_trades"] >= 1 and m["starved_share"] == 0.0


def test_a_strategy_that_needs_more_history_than_it_can_get_fails_the_gate(monkeypatch):
    monkeypatch.setitem(strategy.STRATEGIES, "needs_5000", _needs(5000))     # history_hours is 720 here
    cfg = {"hypothesis": "HX", "strategy": "needs_5000", "params": {"x_hours": 50}}
    m = backtest.run_backtest(candles(n=900), cfg, RCFG, max_days=20)
    assert m["starved_share"] == 1.0
    rules = {"max_drawdown": 0.3, "max_cost_drag": 0.15, "max_avg_fills_per_pair_per_day": 1.0, "min_trades": 0}
    problems, _ = backtest.plausibility(m, rules, None, 10_000)
    assert any("too few candles" in p for p in problems)


def test_a_strategy_held_back_only_by_the_fill_cap_fails_the_gate(monkeypatch):
    def flip(c, params, w):
        return {p: strategy.Target(0.0, "exit") if w.get(p, 0) > 0 else strategy.Target(0.2, "enter") for p in c}
    monkeypatch.setitem(strategy.STRATEGIES, "flip", flip)
    cfg = {"hypothesis": "HX", "strategy": "flip", "params": {"x_hours": 24}}
    rc = {**RCFG, "max_fills_per_pair_per_day": 4}
    m = backtest.run_backtest(candles(n=900), cfg, rc, max_days=20)
    assert m["trades_per_pair_per_day_max"] <= 5 and m["pair_days_at_fill_cap"] > 20     # buys stopped most days
    rules = {"max_drawdown": 0.3, "max_cost_drag": 10.0, "max_avg_fills_per_pair_per_day": 10.0, "min_trades": 0,
             "max_pair_days_at_fill_cap": 12}
    problems, _ = backtest.plausibility(m, rules, None, 10_000)
    assert any("loop" in p for p in problems)


def test_a_strategy_that_says_capped_in_a_reason_of_its_own_has_had_no_buy_stopped(monkeypatch):
    """The count looked for the word anywhere in a reason, and a reason is a strategy's own free text: one that
    wrote "capped:" for a limit of its own would have failed the gate as a loop on every day it traded."""
    def steady(c, params, w):
        return {p: strategy.Target(0.2, "capped: at my own limit of 0.2") for p in c}
    monkeypatch.setitem(strategy.STRATEGIES, "steady", steady)
    cfg = {"hypothesis": "HX", "strategy": "steady", "params": {"x_hours": 24}}
    m = backtest.run_backtest(candles(n=900), cfg, {**RCFG, "max_fills_per_pair_per_day": 4}, max_days=20)
    assert m["n_trades"] >= 2 and m["pair_days_at_fill_cap"] == 0


def test_a_day_at_the_cap_is_the_engine_s_own_words_first_on_a_buy_it_did_not_fill(monkeypatch):
    """What the count reads, decision by decision. The engine's words at the head of a reason on a decision with
    nothing filled count, once for a pair and a UTC day however many hours they come in. The same words anywhere
    else in a reason, or on a decision that filled or held, do not."""
    real = backtest.step
    days = []

    def spy(acct, cfg, fn, window, prices, ts, *args, **kwargs):
        decisions, fills, equity = real(acct, cfg, fn, window, prices, ts, *args, **kwargs)
        engine_s = "capped: 4 fills in ETH today, the limit is 4 a day, so no new buys until the next UTC day | x"
        extra = [{"pair": "BTC", "action": "none", "reason": "waits for cash: the book is fully invested | " + engine_s},
                 {"pair": "BTC", "action": "buy", "reason": engine_s},
                 {"pair": "BTC", "action": "hold", "reason": engine_s}]
        day = ts // 86400
        days.append(day)
        if day in (min(days) + 2, min(days) + 5) and ts % 86400 // 3600 in (5, 6, 7):
            extra.append({"pair": "ETH", "action": "none", "reason": engine_s})       # three hours on each of two days
        return decisions + extra, fills, equity
    monkeypatch.setattr(backtest, "step", spy)
    monkeypatch.setitem(strategy.STRATEGIES, "steady", lambda c, params, w: {p: strategy.Target(0.2, "in") for p in c})
    cfg = {"hypothesis": "HX", "strategy": "steady", "params": {"x_hours": 24}}
    m = backtest.run_backtest(candles(n=900), cfg, {**RCFG, "max_fills_per_pair_per_day": 4}, max_days=20)
    assert len(set(days)) > 6 and m["pair_days_at_fill_cap"] == 2


def test_a_long_run_is_read_out_by_calendar_year_against_that_year_s_basket():
    start = 1_640_995_200                                    # 2022-01-01 00:00 UTC
    hours = 24 * 365 * 2
    curve = [(start + i * 3600, 10_000 * (1 + 0.5 * i / hours)) for i in range(hours)]   # +50% over two years
    asked = []

    def market_fn(a, b):
        asked.append((a, b))
        year = pd.to_datetime(a, unit="s").year
        return {"basket_return": {2022: -0.60, 2023: 0.90}[year], "pairs": {2022: 9, 2023: 10}[year]}
    m = _metrics(days=730.0, equity_curve=curve)
    _, report = backtest.plausibility(m, GATE_RULES, None, 10_000, market_fn=market_fn)
    assert [y["year"] for y in report["years"]] == [2022, 2023] and len(asked) == 2
    assert report["years"][0]["basket"] == -0.60 and report["years"][0]["pairs"] == 9
    assert report["years"][0]["strategy"] == pytest.approx(0.25, abs=0.01)
    line = backtest.format_report(report).splitlines()[-1]
    assert line.startswith("by calendar year") and "2022 +25.0% / -60.0% (9 pairs)" in line and "(10 pairs)" not in line
    # the gate's own 365 day run never asks for it
    _, short = backtest.plausibility(_metrics(equity_curve=curve[:24 * 365]), GATE_RULES, None, 10_000, market_fn=market_fn)
    assert short["years"] == [] and len(asked) == 2


# --- the market a backtest is read against covers the same span as its curve ---------------------------

def _two_year_curve():
    start = 1_640_995_200                                    # 2022-01-01 00:00 UTC
    return [(start + i * 3600, 10_000.0 + i) for i in range(24 * 365 * 2)]


def _canned_run(monkeypatch, curve, days):
    monkeypatch.setattr(config, "prepare", lambda: None)
    monkeypatch.setattr(config, "risk_cfg", lambda: {**RCFG, "backtest_gate": dict(GATE_RULES)})
    monkeypatch.setattr(backtest, "load_cached_candles",
                        lambda pairs: {p: pd.DataFrame({"time": range(24 * 400)}) for p in pairs})
    monkeypatch.setattr(backtest, "run_backtest",
                        lambda *a, **k: _metrics(days=days, pairs=2, equity_curve=list(curve)))


def test_the_backtest_reads_the_market_to_the_close_its_last_mark_was_taken_at(monkeypatch, capsys):
    """A curve point is stamped with a candle's open time and marked at its
    close, an hour later. The market has to be read to that same close. It was
    read to the stamp, so every backtest's basket ended an hour before its
    strategy did, and each calendar year's began and ended an hour early."""
    from bot import promote
    curve, asked = _two_year_curve(), []

    def market(a, b, pairs):
        asked.append((a, b))
        return {"basket_return": 0.10, "basket_max_dd": -0.20, "basket_path": None, "pairs": len(pairs)}
    _canned_run(monkeypatch, curve, 730.0)
    monkeypatch.setattr(config, "load_yaml", lambda path: {"hypothesis": "HX", "strategy": "ts_momentum", "params": {}})
    monkeypatch.setattr(promote, "market_context", market)
    assert backtest.main(["--gate"]) == 0
    assert asked[0] == (curve[0][0], curve[-1][0] + 3600)      # the whole run: first fill to last mark
    first_2023 = 1_672_531_200                                  # 2023-01-01 00:00 UTC
    assert asked[1] == (curve[0][0] + 3600, first_2023 - 3600 + 3600)      # 2022: its first mark to its last
    assert asked[2] == (first_2023 + 3600, curve[-1][0] + 3600)            # 2023 likewise
    assert "by calendar year" in capsys.readouterr().out


def test_the_gate_reads_the_market_to_the_close_its_last_mark_was_taken_at(monkeypatch, capsys):
    import importlib.util, os
    spec = importlib.util.spec_from_file_location("bg2", os.path.join(os.getcwd(), "gate", "backtest_gate.py"))
    bg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bg)
    curve, asked = _two_year_curve()[:24 * 365], []

    def market(a, b, pairs):
        asked.append((a, b))
        return {"basket_return": 0.10, "basket_max_dd": -0.20, "basket_path": None, "pairs": len(pairs)}
    _canned_run(monkeypatch, curve, 365.0)
    monkeypatch.setattr(config, "account_cfg", lambda name: {"hypothesis": "HX", "strategy": "ts_momentum", "params": {}})
    monkeypatch.setattr(bg, "changed_slot", lambda: "challenger1")
    monkeypatch.setattr(bg, "market_context", market)
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    assert bg.main() == 0
    assert asked == [(curve[0][0], curve[-1][0] + 3600)]
    assert "backtest gate passed" in capsys.readouterr().out


def test_the_backtest_counts_finished_trades_and_the_windows_that_had_none(monkeypatch):
    """A live test that has left no position of its own by day 60 is killed as
    bought and held. The backtest says how often that would have happened to
    this strategy: one 60 day window starting each day of the run."""
    day = 86400
    fill = lambda d, side, qty=1.0, reason="": paper.Fill(                                       # noqa: E731
        ts=int(d * day), account="b", pair="BTC", side=side, qty=qty, price=1.0, ref_price=1.0, notional=qty,
        fee=0.0, slippage_cost=0.0, reason=reason)
    # 200 days; one position bought on day 10 and left on day 30, another bought on day 150 and never sold
    fills = [fill(10, "buy"), fill(30, "sell"), fill(150, "buy")]
    n, forced, none = backtest.finished_trades(fills, 0, 200 * day, 60)
    assert (n, forced) == (1, 0)
    # windows start on days 0 to 140; only those starting on days 0 to 29 hold the exit on day 30
    assert none == pytest.approx(111 / 141, abs=0.001)
    assert backtest.finished_trades(fills, 0, 200 * day, 250) == (1, 0, None)     # shorter than one window
    assert backtest.finished_trades([], 0, 200 * day, 60) == (0, 0, 1.0)          # never traded: every window
    assert backtest.finished_trades([fill(10, "buy"), fill(30, "sell", 0.5)], 0, 200 * day, 60) == (0, 0, 1.0)   # a trim
    weekly = [fill(d + off, side) for d in range(0, 196, 7) for off, side in ((1, "buy"), (3, "sell"))]
    assert backtest.finished_trades(weekly, 0, 200 * day, 60) == (28, 0, 0.0)
    # a position the daily loss halt closed is not an exit the strategy chose: counted apart, and no window is saved by it
    halted = [fill(10, "buy"), fill(30, "sell", reason="daily halt: equity 9400.00 is down 6.0% from the day's open")]
    assert backtest.finished_trades(halted, 0, 200 * day, 60) == (0, 1, 1.0)
    # and the real engine reports all three
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum",
           "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
    m = backtest.run_backtest(candles(n=600), cfg, RCFG, max_days=None)
    assert m["finished_trades"] >= 1 and m["windows_with_no_finished_trade"] is None     # 600 hours: under 60 days
    text = backtest.format_metrics(m)
    assert all(k in text for k in ("finished_trades", "closed_by_halt_or_error", "windows_with_no_finished_trade"))


def test_the_engine_hands_its_own_fills_and_window_to_the_finished_trade_count(monkeypatch):
    """Long from day 5 to day 15 of about a hundred, flat otherwise, with a ten
    day window: the share of windows with no finished trade is the share that
    start after the exit, worked out from where the run really begins."""
    start = 1_700_000_000
    def one_trade(c, params, w):
        hours = {p: int((df["time"].iloc[-1] - start) // 3600) for p, df in c.items()}
        return {p: strategy.Target(0.2 if 5 * 24 <= h < 15 * 24 and p == "BTC" else 0.0, "in" if h < 15 * 24 else "out")
                for p, h in hours.items()}
    monkeypatch.setitem(strategy.STRATEGIES, "one_trade", one_trade)
    cfg = {"hypothesis": "HX", "strategy": "one_trade", "params": {"x_hours": 24}}
    rc = {**RCFG, "challenger": {"window_days": 10}}
    m = backtest.run_backtest(candles(n=100 * 24), cfg, rc, max_days=None)
    assert m["n_trades"] == 2 and m["finished_trades"] == 1 and m["closed_by_halt_or_error"] == 0
    warm = backtest.warmup_hours(cfg["params"])
    first_day = warm / 24                                    # the run begins after the warm up
    last_start = (100 * 24 - 1) / 24 - 10                    # the last day a ten day window can start on
    starts = int(last_start - first_day) + 1
    holding = sum(1 for k in range(starts) if first_day + k < 15 + 1 / 24 <= first_day + k + 10)
    assert m["windows_with_no_finished_trade"] == pytest.approx(1 - holding / starts, abs=0.02)
    assert 0.80 < m["windows_with_no_finished_trade"] < 0.90
    # A rules file with a window that cannot be used does not stop a backtest, and the documented 60 days stand
    # in, as they do for the verdict code (the backtest used to read the line by itself: 0 gave windows of no
    # length, every one of them "with no finished trade").
    sixty = backtest.run_backtest(candles(n=100 * 24), cfg, {**RCFG, "challenger": {"window_days": 60}}, max_days=None)
    assert 0 < sixty["windows_with_no_finished_trade"] < 0.80
    for written in ("sixty", 0, -10, None):
        got = backtest.run_backtest(candles(n=100 * 24), cfg, {**RCFG, "challenger": {"window_days": written}}, max_days=None)
        assert got["windows_with_no_finished_trade"] == sixty["windows_with_no_finished_trade"], written
    assert backtest.run_backtest(candles(n=100 * 24), cfg, RCFG, max_days=None)["windows_with_no_finished_trade"] == \
        sixty["windows_with_no_finished_trade"]                          # and with no challenger block at all
