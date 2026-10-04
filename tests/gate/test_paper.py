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


# --- a held pair with no price keeps its last known one --------------------------

def test_a_held_pair_with_no_price_is_valued_at_its_mark_not_at_zero():
    a = make()
    a.trade("BTC", 2500.0, 100.0, ts=1, reason="x")
    a.trade("ETH", 2500.0, 50.0, ts=1, reason="x")
    assert a.remember({"BTC": 100.0, "ETH": 50.0}, ts=1) == []
    both = a.equity({"BTC": 100.0, "ETH": 50.0})
    assert a.equity({"ETH": 50.0}) == pytest.approx(both)              # no BTC price: its mark stands in
    assert a.gross_exposure({"ETH": 50.0}) == pytest.approx(a.gross_exposure({"BTC": 100.0, "ETH": 50.0}))
    assert set(a.weights({"ETH": 50.0})) == {"BTC", "ETH"}
    assert a.equity({"BTC": 0.0, "ETH": 50.0}) == pytest.approx(both)   # a zero price is no price either
    assert a.equity({"BTC": float("nan"), "ETH": 50.0}) == pytest.approx(both)


def test_a_real_price_always_beats_the_mark():
    a = make()
    a.trade("BTC", 2500.0, 100.0, ts=1, reason="x")
    a.remember({"BTC": 100.0}, ts=1)
    qty = a.positions["BTC"]
    assert a.equity({"BTC": 80.0}) == pytest.approx(a.cash + qty * 80.0)


def test_marks_take_the_newer_of_what_is_known_and_drop_closed_positions():
    a = make()
    a.trade("BTC", 2500.0, 100.0, ts=1, reason="x")
    a.remember({"BTC": 100.0}, ts=1000)
    assert a.remember({}, ts=2000, known={"BTC": (90.0, 500)}) == ["BTC"]     # an older candle close
    assert a.state["marks"]["BTC"] == [100.0, 1000]                           # does not replace a newer mark
    a.remember({}, ts=3000, known={"BTC": (95.0, 2500)})                      # a newer one does
    assert a.state["marks"]["BTC"] == [95.0, 2500]
    a.remember({"BTC": 0.0}, ts=3500)                                         # a zero price never becomes the mark
    assert a.state["marks"]["BTC"] == [95.0, 2500]
    a.trade("BTC", -1e9, 95.0, ts=4000, reason="close")
    a.remember({}, ts=4000)
    assert a.state["marks"] == {}


def test_marks_survive_a_save_and_load(tmp_path):
    a = make()
    a.trade("BTC", 2500.0, 100.0, ts=1, reason="x")
    a.remember({"BTC": 100.0}, ts=1)
    a.save(tmp_path / "account.json")
    b = PaperAccount.load(tmp_path / "account.json", "t", 10_000.0, 10, 5)
    assert b.equity({}) == pytest.approx(a.equity({"BTC": 100.0}))
    old = PaperAccount("t", 10_000.0, 10, 5)                # an account file from before marks existed
    old.trade("BTC", 2500.0, 100.0, ts=1, reason="x")
    del old.state["marks"]
    old.save(tmp_path / "old.json")
    c = PaperAccount.load(tmp_path / "old.json", "t", 10_000.0, 10, 5)
    assert c.equity({"BTC": 100.0}) == pytest.approx(a.equity({"BTC": 100.0}))
    assert c.remember({}, ts=5, known={"BTC": (100.0, 4)}) == ["BTC"] and c.equity({}) == pytest.approx(a.equity({"BTC": 100.0}))
