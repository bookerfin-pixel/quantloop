"""PROTECTED. The bench on daily bars across many coins (bot/widebench.py): that a book is run on what it
could have known, pays for what it trades, cannot trade a coin that is not trading, is sold out of a coin
that dies, and that both yardsticks read a book with no skill as luck and one with skill as skill."""
import numpy as np
import pandas as pd
import pytest

from bot import binance, widebench as wb

DAY = pd.Timedelta(days=1)


def frame(closes: dict, start="2021-01-01", volume=1e7):
    """closes: coin -> list of closes, one a day from `start`, None for a day with no candle."""
    rows = []
    for coin, cs in closes.items():
        for i, c in enumerate(cs):
            if c is None:
                continue
            v = volume(coin, i) if callable(volume) else volume
            rows.append({"symbol": coin + "USDT", "day": pd.Timestamp(start, tz="UTC") + i * DAY, "open": c, "high": c,
                         "low": c, "close": c, "volume": v / c, "quote_volume": v, "trades": 1.0,
                         "taker_buy_quote_volume": v / 2})
    df = pd.DataFrame(rows).sort_values(["symbol", "day"]).reset_index(drop=True)
    df["coin"] = binance.coins(df)
    return df


def synthetic(days=900, coins=40, momentum=0.0, seed=1, deaths=0.0, young=0.0, young_days=60, young_from=0):
    """Coins with a common market move, noise, and, with `momentum`, a drift of each coin's own that persists.
    Volumes differ between coins and wander, starts are spread over the first half, `deaths` of the coins
    end early, and `young` is a drift each coin has from day `young_from` to `young_days` of its life."""
    rng = np.random.default_rng(seed)
    mkt = rng.normal(0, 0.03, days)
    drift = np.zeros((days, coins))
    x = np.zeros(coins)
    for t in range(days):
        x = 0.98 * x + rng.normal(0, 0.002, coins)
        drift[t] = x * momentum
    r = mkt[:, None] + drift + rng.normal(0, 0.04, (days, coins))
    start = rng.integers(0, days // 2, coins)
    end = np.full(coins, days)
    dying = rng.random(coins) < deaths
    end[dying] = rng.integers(days // 2, days - 30, int(dying.sum()))
    for j in range(coins):
        r[start[j] + young_from: start[j] + young_days, j] += young
    closes = np.exp(np.cumsum(np.log1p(np.clip(r, -0.9, 3.0)), axis=0))
    level = np.exp(rng.normal(15, 1.5, coins))
    wander = np.exp(np.cumsum(rng.normal(0, 0.05, (days, coins)), axis=0))
    out = {}
    for j in range(coins):
        cs = [None if (t < start[j] or t >= end[j]) else float(closes[t, j]) for t in range(days)]
        out[f"C{j:02d}"] = cs
    return frame(out, start="2019-01-01", volume=lambda coin, i: float(level[int(coin[1:])] * wander[i, int(coin[1:])]))


SPEC = {"strategy": "strongest", "n": 3, "lookback": 20, "every": 7, "phase": 0, "list": 20}


# --- the market ----------------------------------------------------------------------

def test_the_market_knows_when_a_coin_can_be_traded_and_when_it_has_gone():
    up = [10.0 * 1.01 ** i for i in range(100)]
    halt = [5.0] * 40 + [None, None] + [4.0] * 58                   # two days with no candle in the middle of its life
    dies = [8.0] * 70 + [None] * 30
    late = [None] * 50 + [2.0] * 50
    m = wb.market(frame({"UP": up, "HALT": halt, "DIES": dies, "LATE": late}), n_list=10)
    j = {c: m["coins"].index(c) for c in m["coins"]}
    assert not m["tradable"][0].any()                                   # nothing has a candle the day before day one
    # no candle on days 40 and 41: it cannot be traded as days 41 and 42 begin, and can again on day 43
    assert m["tradable"][40, j["HALT"]] and not m["tradable"][41, j["HALT"]] and not m["tradable"][42, j["HALT"]]
    assert m["tradable"][43, j["HALT"]] and m["life"][41, j["HALT"]]
    assert m["r"][42, j["HALT"]] == pytest.approx(-0.2)                   # the fall over the halt is booked when it trades
    assert m["gone"][70, j["DIES"]] and not m["gone"][69, j["DIES"]] and m["r"][75, j["DIES"]] == 0.0
    assert not m["life"][49, j["LATE"]] and m["life"][50, j["LATE"]] and not m["tradable"][50, j["LATE"]]


def test_costs_follow_the_engines_model_and_the_dollars_a_coin_trades():
    assert wb.half_spread_bps(np.array([1e6]))[0] == pytest.approx(3.17, abs=0.05)
    assert wb.cost_per_side(np.array([1e9]))[0] == pytest.approx(0.0015)                  # the floor: 10 + 5 bps
    assert wb.cost_per_side(np.array([1e5]))[0] == pytest.approx((10 + 8.85 + 2) / 1e4, abs=1e-5)
    assert wb.cost_per_side(np.array([0.0]))[0] == pytest.approx((10 + 100 + 2) / 1e4)   # no dollars: the most it can be


# --- the book ------------------------------------------------------------------------

def test_strongest_chooses_on_the_days_before_only():
    df = synthetic(days=300, coins=15, seed=3)
    m = wb.market(df, n_list=10)
    targets, rebalance, eligible = wb.strongest(m, n=3, lookback=20, every=7, phase=2)
    assert rebalance[2] and rebalance[9] and not rebalance[3] and np.allclose(targets[~rebalance], 0)
    held = targets[rebalance]
    count = (held > 0).sum(axis=1)
    assert np.allclose(held.sum(axis=1), count / 3) and np.array_equal(count, np.minimum(3, eligible[rebalance].sum(axis=1)))
    # one coin the book did not hold, its closes multiplied by ten from rebalance day 149 on: that day's choice
    # cannot move, and moved from the day before it must
    day = 149
    assert rebalance[day]
    out = int(np.flatnonzero(eligible[day] & (targets[day] == 0))[0])
    name = m["coins"][out] + "USDT"
    for shift, moves in ((0, False), (1, True)):
        later = df.copy()
        sel = (later["symbol"] == name) & (later["day"] >= later["day"].min() + (day - shift) * DAY)
        later.loc[sel, ["open", "high", "low", "close"]] *= 10.0
        t2, _, _ = wb.strongest(wb.market(later, n_list=10), n=3, lookback=20, every=7, phase=2)
        assert np.array_equal(targets[:day], t2[:day])
        assert (not np.array_equal(targets[day], t2[day])) == moves and (t2[day, out] > 0) == moves
    # and it chose the three with the best 20 days to the day before, among those on the list
    d = 100 if rebalance[100] else int(np.flatnonzero(rebalance[100:])[0]) + 100
    score = m["close"][d - 1] / m["close"][d - 21] - 1
    score = np.where(m["listed"][d] & np.isfinite(score), score, -np.inf)
    assert set(np.flatnonzero(targets[d] > 0)) == set(np.argsort(-score)[:3])


def test_a_book_drifts_with_its_prices_and_pays_for_what_it_trades():
    df = frame({"A": [10.0 * 1.1 ** i for i in range(10)], "B": [10.0] * 10})
    m = wb.market(df, n_list=10)
    targets = np.zeros((10, 2))
    rebalance = np.zeros(10, dtype=bool)
    rebalance[[2, 6]] = True
    targets[2] = [0.5, 0.5]
    targets[6] = [0.0, 1.0]
    book = wb.run(m, targets, rebalance)
    a, b = m["coins"].index("A"), m["coins"].index("B")
    assert book["held"][2, a] == pytest.approx(0.5) and book["gross"][2] == pytest.approx(0.05)
    assert book["held"][3, a] == pytest.approx(0.55 / 1.05)                        # moved with A's price
    cost = m["cost"][2]
    assert book["costs"][2] == pytest.approx(0.5 * cost[a] + 0.5 * cost[b])
    sold = book["held"][5, a] * 1.1 / (1 + book["gross"][5])                        # what A had grown to by day 6
    assert book["costs"][6] == pytest.approx(sold * cost[a] + sold * cost[b])
    assert book["w"][5, a] == pytest.approx(0.5) and book["w"][6, a] == 0.0           # as last traded, not as drifted
    assert book["daily"][2] == pytest.approx(book["gross"][2] - book["costs"][2] * (1 + book["gross"][2]))


def test_a_coin_that_cannot_trade_keeps_its_place_and_one_that_dies_is_sold_at_its_last_close():
    df = frame({"HALT": [10.0] * 5 + [None] * 3 + [5.0] * 7, "DIES": [10.0] * 9 + [None] * 6, "C": [10.0] * 15})
    m = wb.market(df, n_list=10)
    h, d, c = (m["coins"].index(x) for x in ("HALT", "DIES", "C"))
    targets = np.zeros((15, 3))
    rebalance = np.zeros(15, dtype=bool)
    rebalance[[2, 6]] = True
    targets[2, [h, d]] = 0.5
    targets[6, c] = 1.0                       # on day 6 the book wants out of both, but HALT has no candle on day 5
    book = wb.run(m, targets, rebalance)
    assert book["held"][6, h] == pytest.approx(0.5) and book["held"][6, d] == 0 and book["held"][6, c] == pytest.approx(0.5)
    assert book["gross"][8] == pytest.approx(0.5 * -0.5)                            # it bears the fall over the halt
    targets2 = np.zeros((15, 3))
    rebalance2 = np.zeros(15, dtype=bool)
    rebalance2[2] = True
    targets2[2, d] = 1.0
    book2 = wb.run(m, targets2, rebalance2)
    assert book2["held"][8, d] == pytest.approx(1.0) and book2["held"][9, d] == 0.0      # gone the day after its last candle
    assert book2["costs"][9] == pytest.approx(m["cost"][8, d])                          # at what a fill cost on its last day


# --- the yardsticks ------------------------------------------------------------------

def no_skill(seeds, spec=SPEC, **kw):
    """The share of its twins and of its picks a book with no skill beats, on markets made by `synthetic`. On 200
    such markets (seeds 200 to 399, deaths 0.3) the book made +0.3% a year over the coins it could have chosen,
    give or take 1.8%: nothing. One market's share is as likely to be anything from 0 to 1, so the average of 24
    has a spread of about 0.06, and 0.35 to 0.65 is two and a half of those either way."""
    twins, picks = [], []
    for seed in seeds:
        m = wb.market(synthetic(days=700, coins=30, seed=seed, **kw), n_list=spec["list"])
        book, rebalance = wb.book_of(m, spec)
        twins.append(wb.twins(m, book, wb.memory_of(spec), n=60, seed=seed)["beaten"]["all"])
        picks.append(wb.picks(m, book, rebalance, n=60, seed=seed)["beaten"]["all"])
    return np.array(twins), np.array(picks)


def test_a_book_with_no_skill_reads_as_luck_on_both_yardsticks():
    twins, picks = no_skill(range(40, 64), deaths=0.3)
    assert 0.35 < twins.mean() < 0.65 and 0.35 < picks.mean() < 0.65
    assert twins.min() < 0.3 and twins.max() > 0.7 and picks.min() < 0.3 and picks.max() > 0.7  # spread as luck is


def test_coins_that_fall_before_the_book_could_hold_them_tilt_neither_yardstick():
    # every coin falls a percent a day in its first 60 days, before it can be on the list (found in review,
    # 2026-11-11: twins slid over a coin's whole life held those days, and books with no skill beat 76% of them)
    twins, picks = no_skill(range(60, 84), young=-0.01)
    assert 0.35 < twins.mean() < 0.65 and 0.35 < picks.mean() < 0.65


def test_coins_the_rule_cannot_rank_yet_are_not_among_its_picks():
    # with a 90 day lookback a coin is on the list 30 days before it can be ranked; there each falls a percent
    # a day (found in review, 2026-11-11: picks drew them and books with no skill beat 80% of their picks)
    spec = dict(SPEC, lookback=90)
    twins, picks = no_skill(range(80, 104), spec=spec, young=-0.01, young_from=60, young_days=90)
    assert 0.35 < picks.mean() < 0.65 and 0.35 < twins.mean() < 0.65


def test_a_book_with_skill_reads_as_skill_and_not_on_the_markets_made_with_its_direction_tossed():
    m = wb.market(synthetic(momentum=1.0, seed=7), n_list=20)
    r = wb.one(m, SPEC, 200, 200)
    assert r["twins"]["beaten"] > 0.95 and r["picks"]["beaten"] > 0.95 and r["picks"]["chance"] < 0.05
    null = [wb.one(wb.tossed(m, wb.NULL_SEED + k), SPEC, 100, 100) for k in range(8)]
    assert np.mean([x["picks"]["beaten"] for x in null]) < 0.7 and np.mean([x["twins"]["beaten"] for x in null]) < 0.7


def test_a_book_that_knows_tomorrow_beats_every_pick_and_twin():
    m = wb.market(synthetic(seed=11), n_list=20)
    days, coins = m["r"].shape
    targets = np.zeros((days, coins))
    rebalance = np.ones(days, dtype=bool)
    ok = m["listed"] & m["tradable"]
    best = np.argmax(np.where(ok, m["r"], -np.inf), axis=1)                    # the coin that goes up most that very day
    targets[np.arange(days), best] = np.where(ok.any(axis=1), 1.0, 0.0)
    book = wb.run(m, targets, rebalance)
    book["eligible"] = ok
    assert wb.picks(m, book, rebalance, n=100)["beaten"]["all"] == 1.0
    assert wb.twins(m, book, 2, n=100)["beaten"]["all"] == 1.0


def test_tossed_markets_keep_each_days_size_and_lose_its_direction():
    m = wb.market(synthetic(seed=2), n_list=20)
    t = wb.tossed(m, 5)
    live = m["life"] & (np.abs(m["r"]) > 1e-9)
    keep = np.abs(np.log1p(t["r"][live]) + np.log(np.cosh(np.log1p(m["r"][live]))))
    assert np.allclose(keep, np.abs(np.log1p(m["r"][live])))
    move = np.log1p(m["r"][live])
    up, down = np.expm1(move - np.log(np.cosh(move))), np.expm1(-move - np.log(np.cosh(move)))
    assert np.allclose((up + down) / 2, 0.0)                     # either way the toss goes, nothing on average
    assert abs(float(t["r"][m["life"]].mean())) < 0.005
    assert np.array_equal(t["listed"], m["listed"]) and np.array_equal(t["cost"], m["cost"])


def test_the_survivors_market_keeps_only_the_coins_most_traded_as_it_ends(monkeypatch):
    df = synthetic(seed=4, deaths=0.4)
    monkeypatch.setattr(wb, "SURVIVORS_TOP", 10)
    full, alive = wb.market(df, n_list=20), wb.market(df, survivors=True, n_list=20)
    end = wb.binance.listing(10, df).iloc[-1]
    assert set(alive["coins"]) == set(end[end].index) and len(alive["coins"]) == 10
    assert all(full["last"][full["coins"].index(c)] >= len(full["days"]) - 2 for c in alive["coins"])


# --- the whole reading ---------------------------------------------------------------

def test_a_whole_reading_has_every_check_and_says_them_in_words():
    m = wb.market(synthetic(momentum=0.5, seed=9), n_list=20)
    rd = wb.whole(m, SPEC, 100, 100, 50)
    assert len(rd["phases"]) == 6 and len(rd["null"]) == wb.NULL_MARKETS and len(rd["halves"]) == 2 and rd["nearby"]
    assert rd["double_costs"]["left_per_year"] < rd["own"]["picks"]["left_per_year"]
    text = wb.words(rd)
    assert text[0].startswith("strongest 3 of the top 20 by 20 day return, every 7 days, phase 0: made ")
    assert any(ln.startswith("  null: picks beaten ") for ln in text) and any("by year: 2019" in ln for ln in text)


def test_the_filter_reads_the_list_on_the_days_before_only():
    # four coins fall a percent a day; from day 90 on every close is doubled, so day 90 makes +100% for all
    falls = {c: [100.0 * 0.99 ** i for i in range(140)] for c in ("A", "B", "C", "D")}
    jumped = {c: [x * (2.0 if i >= 90 else 1.0) for i, x in enumerate(cs)] for c, cs in falls.items()}
    m = wb.market(frame(falls), n_list=10)
    targets, rebalance, _ = wb.strongest(m, n=2, lookback=5, every=1, filter_days=10)
    assert m["listed"][89:].all() and rebalance.all() and np.allclose(targets, 0)
    m = wb.market(frame(jumped), n_list=10)
    targets, _, _ = wb.strongest(m, n=2, lookback=5, every=1, filter_days=10)
    held = targets.sum(axis=1) > 0
    assert not held[90] and held[91:101].all() and not held[101:].any()      # the jump is seen from the day after it,
    assert np.allclose(targets[91:101].sum(axis=1), 1.0)                      # for the ten days it is among the days before
    t = wb.trailing(wb.listed_basket(m), 10)
    assert t[91] == pytest.approx(np.log(2.0) + 10 * np.log(0.99)) and np.isnan(t[10]) and np.isfinite(t[11])


def test_btc_timed_holds_btc_only_once_it_has_risen_over_the_days_before():
    m = wb.market(frame({"BTC": [100.0] * 50 + [150.0] * 40, "X": [10.0] * 90}), n_list=10)
    j = m["coins"].index("BTC")
    book = wb.timed(m, "BTC", 10, every=1)
    held = book["held"][:, j]
    assert held[50] == 0.0 and held[51] == pytest.approx(1.0) and held[60] == pytest.approx(1.0) and held[61] == 0.0
    assert book["costs"][51] == pytest.approx(m["cost"][51, j]) and book["costs"][52] == pytest.approx(0.0)
    weekly = wb.timed(m, "BTC", 10, every=7, phase=4)          # decided on days 46, 53, 60, 67: in from 53 to 66
    assert weekly["held"][52, j] == 0.0 and weekly["held"][53, j] == pytest.approx(1.0)
    assert weekly["held"][66, j] == pytest.approx(1.0) and weekly["held"][67, j] == 0.0
    assert wb.timed(m, "ETH") is None


def test_a_whole_reading_sets_the_book_beside_btc_held_and_btc_timed():
    df = synthetic(momentum=0.5, seed=9, days=1300)
    df.loc[df["coin"] == "C00", ["symbol", "coin"]] = ["BTCUSDT", "BTC"]
    m = wb.market(df, n_list=20)
    rd = wb.whole(m, dict(SPEC, filter=20), 50, 50, 20)
    a = rd["own"]["against_btc"]
    j = m["coins"].index("BTC")
    assert a["timed_days"] == 20 and a["held"]["net"] == pytest.approx(rd["own"]["btc"])
    assert a["timed"]["net"] == pytest.approx(wb.bench.compounded(wb.timed(m, "BTC", 20, every=7)["daily"]))
    assert a["book"]["net"] == pytest.approx(rd["own"]["net"]) and -1 < a["book"]["worst"] <= 0
    assert a["last_days"] == 1096 and a["held_last"]["net"] == pytest.approx(wb.bench.compounded(m["r"][-1096:, j]))
    text = wb.words(rd)
    assert any(ln.startswith("  against BTC alone, at the same costs: this book ") for ln in text)
    assert any(ln.startswith("  the last three years alone (1096 days): ") for ln in text)
    assert rd["name"].endswith("held only while the list rose over the 20 days before")
    dear = wb.one(m, SPEC, 0, 0, costs=2.0, yardsticks=True)["against_btc"]
    assert dear["timed"]["net"] < wb.one(m, SPEC, 0, 0, yardsticks=True)["against_btc"]["timed"]["net"]
    assert wb.one(wb.market(synthetic(seed=9), n_list=20), SPEC, 0, 0, yardsticks=True)["against_btc"] is None


def test_the_command_reads_a_spec_with_or_without_its_filter():
    assert wb.parse_spec("strongest,5,14,1,0,30,30") == {"strategy": "strongest", "n": 5, "lookback": 14, "every": 1,
                                                          "phase": 0, "list": 30, "filter": 30}
    assert "filter" not in wb.parse_spec("strongest,5,14,7,3,30") and "filter" not in wb.parse_spec("strongest,5,14,7,3,30,0")
    for bad in ("strongest,5,14", "weakest,5,14,7,0,30", "strongest,5,14,7,0,30,30,1"):
        with pytest.raises(SystemExit):
            wb.parse_spec(bad)


def test_the_study_reads_every_setting_on_both_markets():
    tab = wb.study(synthetic(seed=12, deaths=0.3), lists=(20,), ns=(3,), lookbacks=(10, 20), rhythms=((1, 0), (7, 0)), sub=30)
    assert len(tab) == 8 and set(tab["market"]) == {"with the dead", "survivors"}
    assert tab["picks_beaten"].between(0, 1).all() and tab["twins_beaten"].notna().all()
    table = wb.summary_table(tab)
    assert len(table) == 2 and {"dead_edge_weekly", "surv_edge_weekly", "dead_picks_daily", "surv_picks_weekly_lowest"} <= set(table)
    count = wb.luck_count(tab)
    assert count["with the dead"]["replays"] == 4 and count["survivors"]["luck_gives_about"] == 0.4


def test_it_is_protected_and_apart_from_the_hourly_loop():
    import re
    from pathlib import Path
    from gate import check_protected
    repo = Path(__file__).resolve().parents[2]
    patterns = check_protected.load_patterns(repo / "PROTECTED.txt")
    for path in ("bot/widebench.py", "tests/gate/test_widebench.py"):
        assert any(check_protected.matches(path, p) for p in patterns), path
    src = (repo / "bot" / "widebench.py").read_text(encoding="utf-8")
    for pat in check_protected.FORBIDDEN:
        assert not re.search(pat, src), pat
    for module in ("__init__", "run", "promote", "report", "slot", "config", "data", "paper", "risk", "shadow",
                   "backtest", "strategy"):
        assert "widebench" not in (repo / "bot" / f"{module}.py").read_text(encoding="utf-8"), module
