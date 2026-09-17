"""PROTECTED. The cost model is the one thing the agent must never be able to soften."""
import pytest

from bot.paper import PaperAccount


def make(cash=10_000.0, fee_bps=10, slip_bps=5):
    return PaperAccount("t", cash, fee_bps, slip_bps)


def test_buy_pays_fee_and_slippage():
    a = make()
    f = a.trade("BTC", 1000.0, ref_price=100.0, ts=1, reason="x")
    assert f.side == "buy"
    assert f.price == pytest.approx(100.05)              # 5 bps slippage
    assert f.notional == pytest.approx(1000.0)
    assert f.fee == pytest.approx(1.0)                   # 10 bps of notional
    assert f.slippage_cost == pytest.approx(f.qty * 0.05)
    assert a.cash == pytest.approx(10_000 - 1000 - 1.0)
    assert a.equity({"BTC": 100.0}) == pytest.approx(10_000 - 1.0 - f.slippage_cost)


def test_sell_pays_fee_and_slippage_and_cannot_short():
    a = make()
    a.trade("BTC", 1000.0, 100.0, ts=1, reason="x")
    qty = a.positions["BTC"]
    f = a.trade("BTC", -5000.0, 100.0, ts=2, reason="y")   # asks for more than held
    assert f.side == "sell"
    assert f.qty == pytest.approx(qty)
    assert "BTC" not in a.positions
    assert f.price == pytest.approx(99.95)
    assert a.trade("BTC", -100.0, 100.0, ts=3, reason="z") is None   # nothing left to sell


def test_cash_cannot_go_negative():
    a = make(cash=100.0)
    f = a.trade("ETH", 1_000_000.0, 10.0, ts=1, reason="x")
    assert f.notional <= 100.0
    assert a.cash >= -1e-9


def test_gross_equals_net_plus_costs_identity():
    a = make()
    a.trade("BTC", 2000.0, 100.0, ts=1, reason="x")
    a.trade("BTC", -1000.0, 110.0, ts=2, reason="y")
    prices = {"BTC": 120.0}
    net = a.equity(prices) - a.state["initial_cash"]
    assert a.gross_pnl(prices) == pytest.approx(net + a.total_costs())
    assert a.total_costs() > 0


def test_min_notional_skips_small_trades_but_allows_closing_dust():
    a = make()
    assert a.trade("BTC", 10.0, 100.0, ts=1, reason="x", min_notional=50) is None
    a.trade("BTC", 60.0, 100.0, ts=1, reason="x", min_notional=50)
    f = a.trade("BTC", -60.0, 100.0, ts=2, reason="close", min_notional=50)
    assert f is not None and "BTC" not in a.positions


def test_save_and_load_roundtrip(tmp_path):
    a = make()
    a.trade("SOL", 500.0, 20.0, ts=5, reason="x")
    a.save(tmp_path / "acct.json")
    b = PaperAccount.load(tmp_path / "acct.json", "t", 10_000, 10, 5)
    assert b.positions == a.positions
    assert b.cash == pytest.approx(a.cash)
    assert b.state["n_trades"] == 1


def test_paper_slippage_is_never_below_the_floor_but_follows_a_wide_market():
    a = make(fee_bps=10, slip_bps=5)
    assert a.effective_slip_rate(None) == pytest.approx(5e-4)
    assert a.effective_slip_rate(1.0, impact_bps=2) == pytest.approx(5e-4)      # 3 bps observed: floor wins
    assert a.effective_slip_rate(12.0, impact_bps=2) == pytest.approx(14e-4)    # 14 bps observed: market wins
    f = a.trade("DOGE", 1000.0, 100.0, ts=1, reason="x", half_spread_bps=12.0, impact_bps=2)
    assert f.price == pytest.approx(100.14)
    assert f.slip_bps == pytest.approx(14.0) and f.half_spread_bps == pytest.approx(12.0)


def test_append_rows_migrates_an_older_header(tmp_path):
    from bot.paper import append_rows
    p = tmp_path / "t.csv"
    p.write_text("a,b\n1,2\n")
    append_rows(p, ["a", "b", "c"], [{"a": 3, "b": 4, "c": 5}])
    import pandas as pd
    df = pd.read_csv(p)
    assert list(df.columns) == ["a", "b", "c"] and len(df) == 2
    assert df.iloc[1]["c"] == 5
