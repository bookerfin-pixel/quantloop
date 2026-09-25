# Findings

What this system has learned, distilled. LEDGER.md is the raw record of every
hypothesis and verdict; this file is the short version a person reads to know
what works, what does not, and what is still open. The agent updates it after
every verdict appears under `## Results` in the ledger, and may reorganise it,
but never deletes a finding: something that stopped being true moves to
"Overturned" with the ledger id that overturned it.

Each finding cites the ledger ids it rests on. One verdict is one data point,
not a law. A finding earns "confirmed" only when more than one verdict, or one
verdict plus prior evidence, points the same way.

## Confirmed

- Short horizon mean reversion cannot pay Binance costs (P1, real money, 2025).

## Suggested by one verdict

(none yet)

## Killed ideas and what the kill taught

(none yet)

## Calibration

How the ledger's "Expected gross bps per round trip" compared with the
realised figure promote.py records in each verdict. If expectations run high
across several verdicts, the arithmetic behind them needs fixing, not the
hypotheses.

(none yet)

## Open questions

- Does the momentum family work at all on this universe at hourly resolution
  with a 30 bps round trip, or only at horizons of a week or more? (H0 lost
  on its first 23 days in a falling market; that is one window, not an answer.)
- Is a ≥2 sigma, 240 hour dip rare enough that mean reversion at that horizon
  cannot reach 30 fills in 60 days across ten pairs? (H1 will say.)
- What do the four added pairs (XRP, DOGE, DOT, LTC) really cost to trade? The
  paper loop now pays the observed Kraken half spread plus 2 bps impact whenever
  that exceeds the 5 bps floor; the Data section of state/summary.md shows the
  7 day average per pair. If an alt runs well above the floor, a hypothesis that
  leans on it needs the extra cost in its arithmetic.
- Can any long-only hypothesis clear backtest_gate's plausibility bar right now?
  `bot/run.py` and `bot/backtest.py` capped every strategy call to the trailing 720
  hours (30 days) of candles until 2026-09-20, when Fin raised history_hours to
  2160 (90 days); see notes/2026-09-19.md for why that mattered. Over the trailing 365 days every pair in the universe
  fell 46-81% peak to trough (notes/2026-09-17.md, reproduced 2026-09-19). Six
  backtest-only variants across both running families (momentum and mean
  reversion) — a vol regime filter, an EMA regime filter, a standalone and an
  overlay cross-sectional top-3 ranker, and a z-score stop-loss at two settings
  — all failed backtest_gate's cost coverage and/or drawdown bounds over that
  window (see hypotheses/backlog.md for the numbers). This is backtest evidence
  only, not a verdict, and backtests here can reject an idea but not confirm
  one either way — but if the pattern holds, no new hypothesis may be able to
  enter a slot until the trailing-365-day window rolls past this period, which
  matters for what gets proposed next and is worth Fin knowing about
  independent of any single hypothesis.
  Update 2026-09-20 (Fin): the gate no longer requires in sample profit or an
  absolute 30% drawdown; it is a regime independent sanity filter (cost drag,
  fill rate, drawdown relative to the basket, minimum trades) and the skill
  figure is recorded, not enforced. Over the last 365 days H1's config passes
  it (cost drag 13.5%/yr, drawdown -45% against a -53.6% limit) and H0's does
  not (cost drag 26.1%/yr, drawdown -78%). Both show negative in sample skill
  against the exposure matched basket (-9.9% and -38.3%), which is now the
  first calibration data point to test against their prospective results.
- RESOLVED 2026-09-21, no longer true: "H2 cannot fire until about
  2026-10-22 because the live candle cache is too short" (notes/2026-09-20.md).
  The hourly loop now hands every strategy history plus live candles (see the
  2026-09-21 calibration entry below) and H2's clock was restarted on the
  fixed code. Since then H2 has been flat because no pair has had a
  volatility squeeze: the basket's realised vol has run 61-68% annualised
  through this rally, and the backtest engine replaying the same hours from
  the same data also makes 0 trades (checked 2026-09-25). A flat H2 is a
  reading of the market now, not a data artifact; notes that call it "the
  ramp-up issue" are out of date.

- Calibration of the loop itself, 2026-09-21: the hourly loop and the backtest
  handed strategies different candle frames for four days (live cache only vs
  history plus live), so a lookback that passed the gate could not fire live.
  Fixed in bot/run.py via data.strategy_frames, which both paths now share.
  Lesson for the record: any place the live loop and the backtest diverge is a
  place a hypothesis can pass the gate and still do nothing, so a challenger
  that logs the same "flat: only N candles" reason for a whole day is a bug
  report, not a market observation.

- Calibration of the loop itself, 2026-09-25: a new strategy inherited the
  book of the one before it. challenger3 ran the champion's config while
  idle, so when H3 landed on 2026-09-21 it held ten champion positions, and
  swing_reversal's "stay long until the 48h low breaks" treated them as its
  own. For 40 hours H3's account was the champion's book with a different
  exit rule: all 11 fills in its window were exits of that book, one top-up
  of it, and a daily halt, and the window read -4.66% against the champion's
  -0.66%. The backtest engine replaying the same hours says H3 itself would
  have been flat, 0 trades. Fixed in bot/run.py: an account's first hour
  under a new strategy decides as if flat and trades from the book it really
  holds. The same thing would have happened after every verdict (an idle slot
  runs the champion's config and builds its book) and after every promotion
  (the champion account keeps its positions), so it is fixed at the root.
  Lesson: before reading a challenger's first days, check that its first
  fills carry its own entry reasons.

## How the machinery shapes results

- In sample, none of the four live configs shows skill over two years
  (2026-09-25). Replayed over the last 700 days and read in 89 overlapping 60
  day windows (weekly steps, Nov 2024 to Sep 2026), skill (net return minus
  the equal weight basket held at the same average exposure) was positive in
  1% of windows for H0 (average -14.3% per window), 45% for H1 (-0.8%), 44%
  for H2 (-1.5%) and 18% for H3 (-2.8%). These are the data the ideas were
  designed on, so this is the kindest reading they will get. Each challenger
  beat H0 on raw return in 84-98% of those windows, so beating H0 says little.
  One strategy's 60 day skill varies by 7-9 points from window to window, so
  one verdict cannot tell an edge of a few points from none; the ledger over
  many verdicts can. And a raw return verdict is partly a bet on the market:
  for H3 against H0, the basket's own move explained 54% of the variance of
  the raw edge across windows (H3 holds less, so it wins falls and loses
  rallies) and 4% of the variance of the skill edge.

Not findings about markets: findings about how this system turns a signal
into fills, which every verdict passes through. The backtests below replay
the live configs over the history they were designed on, so they describe
the machinery, not edge.

- The paper loop and the backtest agree (2026-09-25). Replaying the
  champion's first nine live days with the backtest engine from the same
  10,000 cash gave +20.99% against +19.95% live, with the same 58 fills and
  costs of 132 against 135. The gap is fill timing (the backtest fills at the
  candle open on the hour, the live loop at the quote about 20 minutes later)
  and observed spreads. H1's replay differed (27 fills against 8) only because
  live H1 ran on six pairs and the live candle cache until 2026-09-21; on the
  shared pairs the entries and exits match.
- The 5% daily halt is part of every hypothesis, and for the mean reversion
  family it can decide the result. H1's config over the last 365 days:
  -28.1% with the halt, -36.4% without. Over the last 700 days: -39.3% with,
  -18.7% without. H2 over 365 days: -19.2% with, -27.6% without. The halt
  sells at the day's low: it saved the dip buyer and the breakout in the
  falling year and cost the dip buyer far more by selling dips just before
  they recovered in the year before. It made no difference to H0 (-64.4%
  against -64.2% over 365 days). A soft halt (stop adding for the day, sell
  nothing) did not dominate either: over 700 days it was best for H1 (-13.2%)
  and H3 (+30.1% against +23.0%) and worst for H2 (-13.9% against -7.5%), and
  over 365 days the hard halt was best for H1 and H2. Kept as it is. Read a
  mean reversion verdict as "mean reversion plus a 5% daily stop".
- Resizes are a large share of all fills. Over the last 365 days 40% of H0's
  fills, 42% of H2's, 27% of H1's and 14% of H3's were "stay long" weight
  changes (the gross cap rescaling every position when one pair enters or
  exits, or vol targeting drifting), not entries or exits. They were 4-23% of
  each strategy's costs. They count toward min_trades and dilute realised
  bps per round trip, so a verdict's fill count overstates how many decisions
  it rests on.
- H0 is a fees treadmill by today's gate. Its config would fail
  backtest_gate on cost drag: about 26% of equity a year over the last 365
  days (2,782 fills). Over 700 days its gross pnl was +19% of starting equity and
  costs took 90%, net -71%. Its live start (+20% in nine days) is a trend
  follower in the best regime it can have. It is the bar every challenger is
  measured against, which makes that bar low in a choppy market and high in
  a trend.
- Blocked entries. When the book is fully invested and every position sits
  inside the 5 point rebalance threshold, a new entry finds no cash and waits
  (champion: a blocked buy in 111 of its first 216 hourly runs; BTC and ETH
  underweight for two days, DOT for four). Trimming overweight positions to
  fund entries cut the average shortfall from 5.4 to 2.1 points in backtest
  but added 40% more fills and moved the one year result by -0.1 points, so
  it was not adopted. The loop now fills reductions before additions within
  an hour (2026-09-25), which was worth +0.6 to +1.3 points a year on H0, H1
  and H2 in backtest with no extra fills.

## Overturned

(none yet)
