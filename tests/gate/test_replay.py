"""PROTECTED. The hourly run is driven by closed candles: it is safe to trigger
twice, it replays hours it missed exactly as the backtest would have traded
them, it never counts a held pair as worth nothing, it never replays a
strategy over hours from before it existed, a dead candle feed fails loudly
instead of passing for a duplicate trigger, and no pair can be traded in a loop."""
import json

import pandas as pd
import pytest

from bot import backtest, config, data, paper, promote, run, strategy
from bot.run import REPLAYED, SITS_OUT, pending_bars, run_account, step

RCFG = {"fee_bps": 10, "slippage_bps": 5, "impact_bps": 2, "initial_cash": 10_000, "pairs": ["BTC", "ETH"],
        "history_hours": 720, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0,
        "min_trade_notional": 50, "rebalance_threshold": 0.05, "daily_loss_halt": 0.05,
        "max_fills_per_pair_per_day": 4}
START = 1_700_006_400            # on the hour
MOMO = {"hypothesis": "HX", "strategy": "ts_momentum",
        "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
# a quick version of the same strategy, so a short stretch holds dozens of fills
BUSY = {"hypothesis": "HB", "strategy": "ts_momentum",
        "params": {"lookback_hours": 12, "ema_hours": 6, "vol_lookback_hours": 48, "entry_return": 0.003,
                   "exit_return": -0.003, "ema_exit_buffer": 0.004, "target_vol_annual": 0.2}}


def series(n=400, pairs=("BTC", "ETH")):
    src = data.SyntheticSource(list(pairs), n=n, seed=5, start=START)
    return {p: src.ohlc(p) for p in pairs}


def upto(full, n):
    return {p: df.iloc[:n].reset_index(drop=True) for p, df in full.items()}


def last_close(frames):
    return {p: float(df["close"].iloc[-1]) for p, df in frames.items()}


def without(df, times):
    return df[~df["time"].isin(list(times))].reset_index(drop=True)


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "ROOT", tmp_path)
    monkeypatch.setattr(config, "CONFIGS", tmp_path / "configs")
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    monkeypatch.setattr(config, "CANDLES", tmp_path / "state" / "candles")
    monkeypatch.setattr(config, "HISTORY", tmp_path / "state" / "history")
    monkeypatch.setattr(config, "ARCHIVE", tmp_path / "state" / "archive")
    monkeypatch.setattr(config, "LEDGER", tmp_path / "LEDGER.md")
    (tmp_path / "configs").mkdir()
    config.dump_yaml(tmp_path / "configs" / "risk.yaml", {**RCFG, "challenger": {"slots": 1}})
    config.dump_yaml(tmp_path / "configs" / "champion.yaml", MOMO)
    monkeypatch.setitem(strategy.STRATEGIES, "hold_all",
                        lambda c, p, w: {pair: strategy.Target(0.25, "hold") for pair in c})
    return tmp_path


def rows(root, name, fname):
    p = root / "state" / name / fname
    return pd.read_csv(p) if p.exists() else pd.DataFrame()


def account(root, name="champion"):
    return json.loads((root / "state" / name / "account.json").read_text())


def in_order(root, name="champion"):
    """Every log of the account is in time order: a replay never writes behind a row already there."""
    return all(rows(root, name, f)["ts"].is_monotonic_increasing
               for f in ("equity.csv", "decisions.csv", "trades.csv") if len(rows(root, name, f)))


# --- a second trigger, and hours that were missed ------------------------------

def test_a_second_trigger_in_the_same_hour_does_nothing(sandbox):
    frames = upto(series(), 200)
    run_account("champion", frames, last_close(frames), START + 200 * 3600 + 600, RCFG)
    before = (len(rows(sandbox, "champion", "equity.csv")), len(rows(sandbox, "champion", "decisions.csv")))
    state = account(sandbox)
    run_account("champion", frames, last_close(frames), START + 200 * 3600 + 1500, RCFG)
    assert (len(rows(sandbox, "champion", "equity.csv")), len(rows(sandbox, "champion", "decisions.csv"))) == before
    assert before[0] == 1 and account(sandbox) == state


def test_missed_hours_are_replayed_in_order_at_the_next_open(sandbox):
    full = series()
    first = upto(full, 200)
    run_account("champion", first, last_close(first), START + 200 * 3600 + 600, RCFG)
    late = upto(full, 204)                                   # three runs were dropped
    run_account("champion", late, last_close(late), START + 204 * 3600 + 600, RCFG)
    eq = rows(sandbox, "champion", "equity.csv")
    assert len(eq) == 1 + 4                                   # three replayed hours and the live one
    replay_ts = list(eq["ts"].iloc[1:4])
    assert replay_ts == [START + k * 3600 for k in (201, 202, 203)]      # each fills at the next candle's open
    dec = rows(sandbox, "champion", "decisions.csv")
    replayed = dec[dec["ts"].isin(replay_ts)]
    assert len(replayed) and replayed["reason"].str.startswith(REPLAYED).all()
    btc_open = float(full["BTC"].loc[full["BTC"]["time"] == replay_ts[0], "open"].iloc[0])
    assert float(replayed[(replayed["ts"] == replay_ts[0]) & (replayed["pair"] == "BTC")]["price"].iloc[0]) \
        == pytest.approx(btc_open, rel=1e-6)
    live = dec[dec["ts"] == START + 204 * 3600 + 600]
    assert len(live) and not live["reason"].str.startswith(REPLAYED).any()
    assert account(sandbox)["last_bar"] == int(late["BTC"]["time"].iloc[-1])
    assert in_order(sandbox)


def test_replayed_hours_trade_exactly_as_the_backtest_does(sandbox, monkeypatch):
    """The parity that matters: an account that missed a stretch and replays it
    makes the backtest engine's fills, one for one, and carries the same equity
    after every hour. Four pairs on three different clocks: ADA loses four
    candles while it is held and ETH loses one, so the comparison also covers
    a held pair sitting hours out at its last known price."""
    pairs = ["BTC", "ETH", "SOL", "ADA"]
    rc = {**RCFG, "pairs": pairs}
    full = series(120, pairs)
    warm = backtest.warmup_hours(BUSY["params"])
    times = list(full["BTC"]["time"].astype(int))
    full["ADA"] = without(full["ADA"], times[warm + 14: warm + 18])
    full["ETH"] = without(full["ETH"], [times[warm + 41]])

    seen = []                                                 # what the backtest engine did, hour by hour
    real = backtest.step

    def spy(*a, **k):
        decisions, fills, equity = real(*a, **k)
        seen.append((a[5], fills, equity, [d["pair"] for d in decisions if d["reason"] == SITS_OUT]))
        return decisions, fills, equity
    monkeypatch.setattr(backtest, "step", spy)
    m = backtest.run_backtest(full, BUSY, rc, max_days=None)
    assert m["n_trades"] >= 20                                # otherwise the comparison says little
    sat_out = {p for _, _, _, out in seen for p in out}
    assert {"ADA", "ETH"} <= sat_out                          # the holes did land on held pairs

    config.dump_yaml(sandbox / "configs" / "champion.yaml", BUSY)
    acct = paper.PaperAccount("champion", 10_000, 10, 5)
    acct.state["last_bar"] = times[warm - 1]                  # everything from the backtest's first bar is "missed"
    acct.state["strategy_sig"] = config.strategy_signature(BUSY)
    acct.save(sandbox / "state" / "champion" / "account.json")
    run_account("champion", full, last_close(full), times[-1] + 3600 + 600, rc)

    tr = rows(sandbox, "champion", "trades.csv")
    replayed = tr[tr["reason"].str.startswith(REPLAYED)]
    want = [f for _, fills, _, _ in seen for f in fills]
    assert len(replayed) == len(want) == m["n_trades"]
    assert [(int(r.ts), r.pair, r.side) for r in replayed.itertuples()] == [(f.ts, f.pair, f.side) for f in want]
    for col in ("qty", "price", "notional", "fee"):
        assert list(replayed[col]) == pytest.approx([getattr(f, col) for f in want], rel=1e-7), col
    eq = rows(sandbox, "champion", "equity.csv")
    assert list(eq["ts"].iloc[:-1]) == [ts for ts, _, _, _ in seen]             # the last row is the live step
    assert list(eq["equity"].iloc[:-1]) == pytest.approx([e for _, _, e, _ in seen], abs=1e-3)
    assert in_order(sandbox)


def test_an_account_from_before_this_change_carries_on_from_its_last_run(sandbox):
    """The live accounts hold no last_bar yet, only the time they last ran. The
    first run of the new loop replays the hours missed since then and does not
    decide a second time on a candle the old loop already decided on."""
    full = series()
    old_run = START + 300 * 3600 + 1620                       # the old loop ran at 27 past, on the candle that closed at :00
    acct = paper.PaperAccount("champion", 10_000, 10, 5)
    acct.state["last_run_ts"] = old_run
    acct.state["strategy_sig"] = config.strategy_signature(MOMO)
    acct.save(sandbox / "state" / "champion" / "account.json")
    same_hour = upto(full, 300)
    run_account("champion", same_hour, last_close(same_hour), old_run + 900, RCFG)
    assert len(rows(sandbox, "champion", "equity.csv")) == 0  # that candle is done: no second decision
    late = upto(full, 303)                                    # two runs dropped, then this one
    run_account("champion", late, last_close(late), START + 303 * 3600 + 600, RCFG)
    eq = rows(sandbox, "champion", "equity.csv")
    assert list(eq["ts"]) == [START + 301 * 3600, START + 302 * 3600, START + 303 * 3600 + 600]
    assert eq["ts"].iloc[0] > old_run and account(sandbox)["last_bar"] == START + 302 * 3600


def test_a_new_account_starts_on_the_newest_candle(sandbox):
    frames = upto(series(), 300)
    run_account("champion", frames, last_close(frames), START + 300 * 3600 + 600, RCFG)
    assert len(rows(sandbox, "champion", "equity.csv")) == 1


def test_a_gap_longer_than_the_limit_is_not_replayed_hour_by_hour():
    full = series(400)
    times = list(full["BTC"]["time"].astype(int))
    bars = pending_bars(full, times[10], times[-1])
    assert len(bars) == 72 + 1 and bars[-1] == times[-1]
    assert pending_bars(full, times[-1], times[-1]) == []
    assert pending_bars(full, None, times[-1]) == [times[-1]]


# --- a held pair with no price is never worth nothing --------------------------

def test_a_held_pair_whose_candles_went_missing_is_not_counted_as_zero(sandbox):
    """One pair's candle requests fail through a catch up while the account
    holds a quarter of its equity in it. Counted as zero, that reads as a 25%
    loss: the daily halt fires, the rest of the book is sold, and promote kills
    a challenger for a drawdown that never happened."""
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "HA", "strategy": "hold_all", "params": {}})
    full = series()
    first = upto(full, 200)
    run_account("champion", first, last_close(first), START + 200 * 3600 + 600, RCFG)
    before = account(sandbox)
    assert set(before["positions"]) == {"BTC", "ETH"}
    eq0 = float(rows(sandbox, "champion", "equity.csv")["equity"].iloc[-1])

    late = upto(full, 204)
    late["BTC"] = late["BTC"].iloc[:200].reset_index(drop=True)          # BTC's candles for the gap never arrived
    quotes = {"ETH": float(late["ETH"]["close"].iloc[-1])}                # and neither did its quote
    run_account("champion", late, quotes, START + 204 * 3600 + 600, RCFG)

    after = account(sandbox)
    assert after["halted_day"] is None
    assert after["positions"] == before["positions"]                     # nothing was sold in a panic
    eq = rows(sandbox, "champion", "equity.csv")
    assert len(eq) == 5 and (eq["equity"] / eq0 - 1).abs().max() < 0.03   # a quiet few hours, not minus 25%
    assert (eq["gross_exposure"] / eq["equity"]).min() > 0.45            # BTC is still in the exposure figure
    dec = rows(sandbox, "champion", "decisions.csv")
    gap = dec[dec["ts"] > START + 200 * 3600 + 600]
    assert not gap["reason"].str.contains("daily halt").any()
    btc = gap[gap["pair"] == "BTC"]
    assert len(btc) == 4 and btc["reason"].str.endswith(SITS_OUT).all() and (btc["action"] == "none").all()
    assert float(btc["price"].iloc[0]) == pytest.approx(float(first["BTC"]["close"].iloc[-1]), rel=1e-6)
    assert (gap[gap["pair"] == "ETH"]["action"] == "hold").all()         # the pair that has data carries on
    assert in_order(sandbox)


def test_a_failed_quote_values_the_pair_at_its_newest_candle_close(sandbox):
    """The live step: candles arrived for both pairs, the quote for one did not."""
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "HA", "strategy": "hold_all", "params": {}})
    full = series()
    first = upto(full, 200)
    run_account("champion", first, last_close(first), START + 200 * 3600 + 600, RCFG)
    qty = account(sandbox)["positions"]["BTC"]
    nxt = upto(full, 201)
    eth = float(nxt["ETH"]["close"].iloc[-1])
    run_account("champion", nxt, {"ETH": eth}, START + 201 * 3600 + 600, RCFG)
    st = account(sandbox)
    btc_close = float(nxt["BTC"]["close"].iloc[-1])
    assert st["halted_day"] is None and st["positions"]["BTC"] == qty
    assert st["marks"]["BTC"] == [pytest.approx(btc_close), START + 201 * 3600]   # the candle that just closed
    want = st["cash"] + qty * btc_close + st["positions"]["ETH"] * eth
    assert float(rows(sandbox, "champion", "equity.csv")["equity"].iloc[-1]) == pytest.approx(want, abs=0.01)


def test_a_position_sitting_out_still_counts_towards_the_gross_limit():
    pairs = ["BTC", "ETH", "SOL", "ADA", "AVAX"]
    frames = series(100, pairs)
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 2500.0, 100.0, 1, "seed")
    prices = {"ETH": 50.0, "SOL": 20.0, "ADA": 1.0, "AVAX": 30.0}       # no price for BTC this hour
    want_all = lambda c, p, w: {pair: strategy.Target(0.25, "enter") for pair in c}   # noqa: E731
    d, fills, equity = step(acct, {"params": {}}, want_all, frames, prices, START + 100 * 3600,
                            {**RCFG, "pairs": pairs}, marks={"BTC": (100.0, START + 100 * 3600)})
    assert equity == pytest.approx(10_000, rel=0.01)                     # BTC valued at 100, not at nothing
    targets = {x["pair"]: x["target_weight"] for x in d}
    assert targets["BTC"] == pytest.approx(0.25, abs=0.005)              # held as it is
    assert sum(v for k, v in targets.items() if k != "BTC") == pytest.approx(0.75, abs=0.005)
    assert {f.pair for f in fills} == {"ETH", "SOL", "ADA", "AVAX"} and acct.cash > -1e-6
    # without the mark the same book reads as 7,500 of equity and the four buys are sized off that
    blind = paper.PaperAccount("t", 10_000, 10, 5)
    blind.trade("BTC", 2500.0, 100.0, 1, "seed")
    assert blind.equity(prices) == pytest.approx(7_500, rel=0.01)


# --- a strategy is never replayed over hours from before it existed -------------

def test_a_strategy_that_changed_during_missed_hours_is_not_replayed(sandbox):
    """GitHub drops five runs and the agent's pull request lands somewhere in
    them. Nobody knows at which hour, and fills dated before the test window
    opens would not count in it. The new strategy starts on the current candle."""
    full = series()
    first = upto(full, 200)
    run_account("champion", first, last_close(first), START + 200 * 3600 + 600, RCFG)
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "HA", "strategy": "hold_all", "params": {}})
    late = upto(full, 206)
    now = START + 206 * 3600 + 600
    run_account("champion", late, last_close(late), now, RCFG)
    eq = rows(sandbox, "champion", "equity.csv")
    assert list(eq["ts"]) == [START + 200 * 3600 + 600, now]              # no rows for the hours in between
    dec = rows(sandbox, "champion", "decisions.csv")
    new = dec[dec["ts"] == now]
    assert len(new) == 2 and new["reason"].str.contains("decided as if flat").all()
    assert not dec["reason"].str.startswith(REPLAYED).any()
    tr = rows(sandbox, "champion", "trades.csv")
    assert len(tr[tr["ts"] == now]) and (tr["ts"] <= now).all()
    st = account(sandbox)
    assert st["last_bar"] == int(late["BTC"]["time"].iloc[-1])
    assert st["strategy_sig"] == config.strategy_signature(config.account_cfg("champion"))
    # the hour after, with the strategy unchanged, a missed hour is replayed as usual
    later = upto(full, 208)
    run_account("champion", later, last_close(later), START + 208 * 3600 + 600, RCFG)
    assert len(rows(sandbox, "champion", "equity.csv")) == 4 and in_order(sandbox)


# --- the whole entry point: duplicate triggers and a dead feed -----------------

class Feed:
    """A stand in for Kraken. Serves the candles that have closed by `now`; can
    go dead altogether, or lose the candles or the quote of single pairs."""

    def __init__(self, pairs, n=400):
        self.frames = series(n, pairs)
        self.now = None
        self.dead = False
        self.no_candles: set[str] = set()
        self.no_quote: set[str] = set()
        self.late: dict[str, int] = {}          # seconds after `now` at which a pair's request lands
        self.first = 0                          # the feed only reaches back to this candle

    def closed(self, pair):
        df = self.frames[pair].iloc[self.first:]
        return df[df["time"] + 3600 <= self.now + self.late.get(pair, 0)]

    def ohlc(self, pair, since=None):
        if self.dead or pair in self.no_candles:
            raise RuntimeError("EService:Unavailable")
        df = self.closed(pair)
        if since:
            df = df[df["time"] > since]
        return df.reset_index(drop=True)

    def quote_for(self, pair):
        if self.dead or pair in self.no_quote:
            raise RuntimeError("EService:Unavailable")
        last = float(self.closed(pair)["close"].iloc[-1])
        return data.Quote(bid=last * 0.9995, ask=last * 1.0005, last=last)


@pytest.fixture
def live(sandbox, monkeypatch):
    feed = Feed(["BTC", "ETH"])
    monkeypatch.setattr(data, "get_source", lambda pairs, quote="USD": feed)
    out = sandbox / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(out))

    def hour(n, minute=7):
        """Run the entry point as the workflow would n hours into the series. Returns (exit code, skipped)."""
        feed.now = int(START + n * 3600 + minute * 60)
        out.write_text("")
        code = run.main(["--now", str(feed.now)])
        return code, dict(line.split("=") for line in out.read_text().split()).get("skipped")
    return feed, hour


def counts(root, names=("champion", "challenger1")):
    return {n: len(rows(root, n, "equity.csv")) for n in names}


def test_main_skips_a_duplicate_trigger_and_says_so(sandbox, live):
    feed, hour = live
    assert hour(200) == (0, "0")
    assert counts(sandbox) == {"champion": 1, "challenger1": 1}
    def records():
        return {p: p.read_bytes() for p in (sandbox / "state").rglob("*")
                if p.is_file() and p.parent.name != "candles"}
    before = records()
    assert len(before) >= 8                                               # two accounts: account, decisions, trades, equity
    assert hour(200, minute=12) == (0, "1")                               # the outside scheduler arrives second
    assert records() == before
    assert hour(201) == (0, "0")                                          # and the next hour runs as usual
    assert counts(sandbox) == {"champion": 2, "challenger1": 2}
    # a verdict resets a slot between two triggers: the second one is not a duplicate for that slot
    for f in (sandbox / "state" / "challenger1").iterdir():
        f.unlink()
    assert hour(201, minute=12) == (0, "0")
    assert counts(sandbox) == {"champion": 2, "challenger1": 1}           # only the new account acted
    assert hour(201, minute=20) == (0, "1")


def test_main_fails_loudly_on_a_dead_feed_and_catches_up_afterwards(sandbox, live, capsys):
    """Kraken down for two hours. Before this check the run found no new candle,
    took it for a duplicate trigger and exited green having done nothing."""
    feed, hour = live
    assert hour(200) == (0, "0")
    # a slot was reset in that hour (a verdict): its account starts again from nothing
    for f in (sandbox / "state" / "challenger1").iterdir():
        f.unlink()
    feed.dead = True
    capsys.readouterr()
    assert hour(201) == (1, None)                                         # red, and not reported as skipped
    assert "feed is down or behind" in capsys.readouterr().out
    assert hour(202) == (1, None)
    assert counts(sandbox) == {"champion": 1, "challenger1": 0}           # nobody decided on a stale candle
    feed.dead = False
    assert hour(203) == (0, "0")
    eq = rows(sandbox, "champion", "equity.csv")
    assert list(eq["ts"]) == [START + 200 * 3600 + 420, START + 201 * 3600, START + 202 * 3600,
                              START + 203 * 3600 + 420]                    # both lost hours replayed, then live
    assert counts(sandbox)["challenger1"] == 1                            # the new account starts on the current candle
    assert in_order(sandbox) and in_order(sandbox, "challenger1")
    assert account(sandbox)["last_bar"] == account(sandbox, "challenger1")["last_bar"] == START + 202 * 3600


def test_main_carries_on_when_one_pair_has_no_candle_and_no_quote(sandbox, live):
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "HA", "strategy": "hold_all", "params": {}})
    feed, hour = live
    assert hour(200) == (0, "0")
    held = account(sandbox)["positions"]
    assert set(held) == {"BTC", "ETH"}
    feed.no_candles, feed.no_quote = {"BTC"}, {"BTC"}
    assert hour(201) == (0, "0")                                          # ETH has the candle, so the hour is decided
    st = account(sandbox)
    assert st["halted_day"] is None and st["positions"] == held
    dec = rows(sandbox, "champion", "decisions.csv")
    last = dec[dec["ts"] == dec["ts"].max()]
    assert last[last["pair"] == "BTC"]["reason"].iloc[0] == SITS_OUT
    feed.no_candles, feed.no_quote = set(), set()
    assert hour(202) == (0, "0")                                          # BTC is back and decided on again
    dec = rows(sandbox, "champion", "decisions.csv")
    last = dec[dec["ts"] == dec["ts"].max()]
    assert not last["reason"].str.contains("sits this hour out").any()
    eq = rows(sandbox, "champion", "equity.csv")["equity"]
    assert (eq / eq.iloc[0] - 1).abs().max() < 0.03 and in_order(sandbox)


def test_a_run_that_straddles_the_hour_decides_the_candle_that_was_due(sandbox, live):
    """A run starts two seconds before the hour and its last request lands after
    it, so that pair already holds the next candle. Deciding on that one would
    leave the other pair undecided for two candles and make the next run look
    like a duplicate."""
    feed, hour = live
    assert hour(200) == (0, "0")
    feed.late = {"ETH": 5}
    assert hour(201, minute=59.97) == (0, "0")                            # 201:59:58
    feed.late = {}
    assert account(sandbox)["last_bar"] == START + 200 * 3600             # the candle that was due, not ETH's newer one
    assert hour(202, minute=20) == (0, "0")                               # so this is not a duplicate
    assert account(sandbox)["last_bar"] == START + 201 * 3600
    dec = rows(sandbox, "champion", "decisions.csv")
    assert not dec["reason"].str.contains("sits this hour out").any()
    for pair in ("BTC", "ETH"):
        assert len(dec[dec["pair"] == pair]) == 3                         # each pair decided once per run
    assert in_order(sandbox)


def test_main_hands_strategies_history_plus_live_and_no_more_than_history_hours(sandbox, live, monkeypatch):
    """The hourly loop once read the live cache only (2026-09-21), so a lookback
    longer than the cache could pass the gate and never fire live."""
    feed, hour = live
    feed.first = 150                                                       # Kraken only reaches back so far
    (sandbox / "state" / "history").mkdir(parents=True)
    for pair, df in feed.frames.items():
        df.iloc[:150].to_csv(sandbox / "state" / "history" / f"{pair}.csv", index=False)
    seen = []

    def needs_180(c, params, w):
        seen.append({len(df) for df in c.values()})
        return {p: strategy.Target(0.25, "enough") if len(df) >= 180
                else strategy.Target(0.0, f"flat: only {len(df)} candles, need 180") for p, df in c.items()}
    monkeypatch.setitem(strategy.STRATEGIES, "needs_180", needs_180)
    config.dump_yaml(sandbox / "configs" / "champion.yaml", {"hypothesis": "HN", "strategy": "needs_180", "params": {}})
    config.dump_yaml(sandbox / "configs" / "risk.yaml", {**RCFG, "history_hours": 190, "challenger": {"slots": 1}})
    assert hour(200) == (0, "0")
    assert len(rows(sandbox, "champion", "decisions.csv")) == 2
    assert set(account(sandbox)["positions"]) == {"BTC", "ETH"}           # 150 from history plus 50 live
    assert seen and all(lengths == {190} for lengths in seen)             # and only the trailing history_hours


def test_deep_history_is_fetched_after_the_accounts_decide_and_cannot_fail_the_run(sandbox, live, monkeypatch):
    """Five years of history is for backtests. Fetched first, a slow venue could
    run the job into its timeout before any account acted, every hour."""
    feed, hour = live
    config.dump_yaml(sandbox / "configs" / "risk.yaml",
                     {**RCFG, "history_target_hours": 5000, "challenger": {"slots": 1}})
    calls = []

    class Venue:
        def candles(self, pair, start, end):
            calls.append((pair, len(rows(sandbox, "champion", "equity.csv")), len(rows(sandbox, "challenger1", "equity.csv"))))
            return pd.DataFrame(columns=data.CANDLE_COLUMNS)
    monkeypatch.setattr(data, "get_history_source", lambda pairs, quote="USD": Venue())
    assert hour(200) == (0, "0")
    assert [c[0] for c in calls] == ["BTC", "ETH"]
    assert all(c[1:] == (1, 1) for c in calls)                            # both accounts had already recorded the hour
    calls.clear()
    assert hour(200, minute=12) == (0, "1") and calls == []               # a duplicate trigger fetches nothing
    feed.dead = True
    assert hour(201)[0] == 1 and calls == []                              # and neither does a run with no candles

    def broken(pairs, quote="USD"):
        raise RuntimeError("venue changed its API")
    feed.dead = False
    monkeypatch.setattr(data, "get_history_source", broken)
    (sandbox / "state" / "history" / "_backfill.json").unlink()            # so it would ask again
    assert hour(202) == (0, "0")                                          # the hour is decided all the same
    assert counts(sandbox) == {"champion": 3, "challenger1": 3}


# --- a new strategy never adopts a position it could not decide on ---------------

def keeps_what_it_holds(c, params, w):
    """Never enters, keeps anything it holds: the shape of any strategy with an exit rule of its own."""
    return {p: strategy.Target(0.2 if w.get(p, 0.0) > 0 else 0.0, "stay long" if w.get(p, 0.0) > 0 else "flat")
            for p in c}


def test_a_position_that_sat_out_the_first_hour_of_a_new_strategy_is_not_adopted():
    frames = upto(series(), 100)
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 2000.0, 100.0, 1, "opened by the previous strategy")
    acct.trade("ETH", 2000.0, 50.0, 1, "opened by the previous strategy")
    t0 = START + 100 * 3600
    d, fills, _ = step(acct, {"params": {}}, keeps_what_it_holds, frames, {"ETH": 50.0}, t0, RCFG, fresh=True,
                       marks={"BTC": (100.0, t0)})
    assert [(f.pair, f.side) for f in fills] == [("ETH", "sell")]           # decided as if flat
    assert acct.state["inherited"] == ["BTC"]                               # BTC had no price: it waits
    d, fills, _ = step(acct, {"params": {}}, keeps_what_it_holds, frames, {"BTC": 100.0, "ETH": 50.0}, t0 + 3600, RCFG)
    assert [(f.pair, f.side) for f in fills] == [("BTC", "sell")] and not acct.positions
    assert "held over from the previous strategy" in next(x for x in d if x["pair"] == "BTC")["reason"]
    assert "inherited" not in acct.state
    # a position the strategy opened itself is its own from then on
    acct.trade("ETH", 2000.0, 50.0, t0 + 3600, "its own")
    d, fills, _ = step(acct, {"params": {}}, keeps_what_it_holds, frames, {"BTC": 100.0, "ETH": 50.0}, t0 + 7200, RCFG)
    assert not fills and "ETH" in acct.positions


def test_a_zero_price_is_no_price():
    frames = upto(series(), 100)
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 2500.0, 100.0, 1, "seed")
    acct.trade("ETH", 2500.0, 50.0, 1, "seed")
    t0 = START + 100 * 3600
    hold = lambda c, p, w: {pair: strategy.Target(0.25, "hold") for pair in c}   # noqa: E731
    step(acct, {"params": {}}, hold, frames, {"BTC": 100.0, "ETH": 50.0}, t0, RCFG)
    d, fills, equity = step(acct, {"params": {}}, hold, frames, {"BTC": 0.0, "ETH": 50.0}, t0 + 3600, RCFG)
    assert not fills and acct.state["halted_day"] is None and equity == pytest.approx(10_000, rel=0.01)
    assert next(x for x in d if x["pair"] == "BTC")["reason"] == SITS_OUT
    assert acct.state["marks"]["BTC"][0] == 100.0


# --- the fill cap ---------------------------------------------------------------

def flip(c, params, w):
    """Enter when flat, exit when long: the loop H3 fell into."""
    return {"BTC": strategy.Target(0.0, "exit") if w.get("BTC", 0) > 0 else strategy.Target(0.2, "enter")}


def test_the_fill_cap_stops_a_loop_but_never_blocks_a_sell():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    frames = upto(series(), 100)
    prices = {"BTC": 100.0, "ETH": 50.0}
    day = 1_700_006_400 // 86400 * 86400 + 86400              # midnight UTC
    actions = []
    for h in range(8):
        d, _, _ = step(acct, {"params": {}}, flip, frames, prices, day + h * 3600, RCFG)
        actions.append(next(x for x in d if x["pair"] == "BTC")["action"])
    assert actions[:4] == ["buy", "sell", "buy", "sell"]
    assert actions[4:] == ["none"] * 4                         # the fifth fill would be a buy: capped
    d, _, _ = step(acct, {"params": {}}, flip, frames, prices, day + 8 * 3600, RCFG)
    assert "capped" in next(x for x in d if x["pair"] == "BTC")["reason"]
    # the words themselves, and that they come first: bot/report.py and bot/backtest.py find a stopped buy by them
    assert next(x for x in d if x["pair"] == "BTC")["reason"] == (
        "capped: 4 fills in BTC today, the limit is 4 a day, so no new buys until the next UTC day (sells are never "
        "capped) | enter") and run.CAPPED == "capped: "
    # next UTC day the count starts again
    d, _, _ = step(acct, {"params": {}}, flip, frames, prices, day + 86400, RCFG)
    assert next(x for x in d if x["pair"] == "BTC")["action"] == "buy"
    # at the cap while holding: the exit still goes through
    acct2 = paper.PaperAccount("t2", 10_000, 10, 5)
    acct2.trade("BTC", 2000.0, 100.0, 1, "seed")
    acct2.state["fills_day"] = {"day": "2023-11-16", "counts": {"BTC": 4}}
    out = lambda c, p, w: {"BTC": strategy.Target(0.0, "exit")}   # noqa: E731
    d, fills, _ = step(acct2, {"params": {}}, out, frames, prices, day + 3600, RCFG)
    assert [f.side for f in fills] == ["sell"] and "BTC" not in acct2.positions


# --- the account counts its readings, as it counts its fills ------------------------------

def test_the_account_counts_its_readings_and_its_files_agree_with_its_counts(sandbox):
    """bot/promote.py sets an account's files against the account's own counts
    before it rules on anything (record_fault). The engine's side of that:
    every reading written is counted, replayed hours included, and what the
    engine writes passes every one of those checks."""
    config.dump_yaml(sandbox / "configs" / "champion.yaml", BUSY)        # quick enough to hold fills
    full = series()
    first = upto(full, 200)
    run_account("champion", first, last_close(first), START + 200 * 3600 + 600, RCFG)
    assert account(sandbox)["equity_rows"] == 1
    for n in range(201, 240):
        frames = upto(full, n)
        run_account("champion", frames, last_close(frames), START + n * 3600 + 600, RCFG)
    late = upto(full, 244)                                               # four runs dropped: replayed, then the live one
    run_account("champion", late, last_close(late), START + 244 * 3600 + 600, RCFG)
    run_account("champion", late, last_close(late), START + 244 * 3600 + 1500, RCFG)     # a second trigger adds nothing
    st = account(sandbox)
    assert st["equity_rows"] == 45 == len(rows(sandbox, "champion", "equity.csv"))
    assert st["n_trades"] == len(rows(sandbox, "champion", "trades.csv")) >= 2
    assert promote.record_fault("champion") is None
    # a reading cut from the middle of the file: its first row, its last row and its order are as they were
    p = sandbox / "state" / "champion" / "equity.csv"
    lines = p.read_text().strip().split("\n")
    p.write_text("\n".join(lines[:20] + lines[21:]) + "\n")
    assert promote.record_fault("champion") == ("champion/equity.csv has 44 rows and the account has taken 45 "
                                                "readings: rows have been lost or added")
    # and the count is the account's own, not a count of the file: the next run does not forget what was lost
    nxt = upto(full, 245)
    run_account("champion", nxt, last_close(nxt), START + 245 * 3600 + 600, RCFG)
    assert account(sandbox)["equity_rows"] == 46
    assert promote.record_fault("champion").startswith("champion/equity.csv has 45 rows and the account has taken 46 ")


def test_the_count_of_readings_starts_from_the_file_as_it_stands(sandbox):
    """Every account that was running when the count arrived has no count yet.
    Its first run under this code takes the file as it finds it."""
    full = series()
    for n in (200, 201):
        frames = upto(full, n)
        run_account("champion", frames, last_close(frames), START + n * 3600 + 600, RCFG)
    st = account(sandbox)
    del st["equity_rows"]                                                # as the live accounts are today
    (sandbox / "state" / "champion" / "account.json").write_text(json.dumps(st))
    assert promote.record_fault("champion") is None                      # no count to set the file against yet
    late = upto(full, 203)                                               # one hour replayed and the live one
    run_account("champion", late, last_close(late), START + 203 * 3600 + 600, RCFG)
    assert account(sandbox)["equity_rows"] == 4 == len(rows(sandbox, "champion", "equity.csv"))
    assert promote.record_fault("champion") is None


def test_a_new_account_counts_from_nothing(sandbox, live):
    feed, hour = live
    assert hour(200) == (0, "0") and hour(201) == (0, "0")
    assert account(sandbox, "challenger1")["equity_rows"] == 2
    for f in (sandbox / "state" / "challenger1").iterdir():              # a verdict resets the slot: a fresh account
        f.unlink()
    assert hour(202) == (0, "0")
    assert account(sandbox, "challenger1")["equity_rows"] == 1 and account(sandbox)["equity_rows"] == 3
    assert promote.record_fault("challenger1") is None and promote.record_fault("champion") is None


# --- what stops the hourly run, and what does not ---------------------------------------

def test_a_slot_record_that_cannot_be_read_does_not_cost_every_account_its_hour(sandbox, live, capsys):
    """slot.maybe_start read every slot's record with nothing round it, after
    the accounts had traded: one meta.json cut short failed the run, so the
    hour of every account went uncommitted, and the next, until it was
    mended by hand. Nothing is started or ended in that slot, it is said,
    and the hour is kept."""
    feed, hour = live
    assert hour(200) == (0, "0")
    meta = sandbox / "state" / "challenger1" / "meta.json"
    config.dump_yaml(sandbox / "configs" / "challenger1.yaml", BUSY)     # a config that would start a test
    for damaged in ("{cut", "[]", "null", json.dumps({"hypothesis": "HB"})):
        meta.write_text(damaged)
        capsys.readouterr()
        n = counts(sandbox)["champion"]
        assert hour(200 + n) == (0, "0")
        assert "[slot] WARNING: challenger1: its slot record (meta.json) could not be read (" in capsys.readouterr().out
        assert meta.read_text() == damaged                                   # left as it was found, for a person to mend
        assert counts(sandbox) == {"champion": n + 1, "challenger1": n + 1}  # and every account kept its hour
    meta.unlink()                                                        # mended (no record is an idle slot): the test starts
    assert hour(210) == (0, "0")
    assert json.loads(meta.read_text())["status"] == "testing"


def test_an_idle_slot_whose_record_cannot_be_read_is_written_afresh(sandbox, live, capsys):
    """A slot whose config is the champion's holds no test, whatever its
    record says or cannot say. Left damaged it was not free for the agent
    until a person mended the file by hand."""
    feed, hour = live
    assert hour(200) == (0, "0")
    meta = sandbox / "state" / "challenger1" / "meta.json"
    meta.write_text("{cut")
    capsys.readouterr()
    assert hour(201) == (0, "0")
    assert ("[slot] challenger1: its slot record (meta.json) could not be read (JSONDecodeError: " in capsys.readouterr().out)
    assert json.loads(meta.read_text()) == {"status": "idle", "hypothesis": None, "started_at": None, "start_equity": {}}
    assert counts(sandbox) == {"champion": 2, "challenger1": 2}


def test_a_record_that_does_not_begin_with_its_header_stops_the_run(sandbox, live):
    """The one kind of damaged record the run does not carry on past: a file
    it would have to write to. Adding rows under a first line that is not
    the header would bury the damage, so the run stops, loudly, with nothing
    committed, and the file is left exactly as it was found."""
    feed, hour = live
    assert hour(200) == (0, "0")
    p = sandbox / "state" / "champion" / "equity.csv"
    damaged = p.read_text().split("\n", 1)[1]
    p.write_text(damaged)
    with pytest.raises(ValueError, match="champion/equity.csv does not begin with a header this code wrote"):
        hour(201)
    assert p.read_text() == damaged
