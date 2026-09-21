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
- H2's live test may not have 60 days of real runway: vol_breakout needs
  ~1610 live candles (compression_hours + lookback_hours) before it can fire
  at all, but live candle collection only began 2026-08-17, so the pairs
  needing the most candles don't clear that bar until roughly 2026-10-22 —
  about a month into H2's 60 day window (notes/2026-09-20.md). The 365 day
  backtest that passed the gate used the two-year Coinbase history and never
  saw this ramp-up. If H2 comes back "killed: too few fills," read it the
  way H1's own kill criteria already treats that outcome — a test-design
  artifact, not evidence against the mechanism.

- Calibration of the loop itself, 2026-09-21: the hourly loop and the backtest
  handed strategies different candle frames for four days (live cache only vs
  history plus live), so a lookback that passed the gate could not fire live.
  Fixed in bot/run.py via data.strategy_frames, which both paths now share.
  Lesson for the record: any place the live loop and the backtest diverge is a
  place a hypothesis can pass the gate and still do nothing, so a challenger
  that logs the same "flat: only N candles" reason for a whole day is a bug
  report, not a market observation.

## Overturned

(none yet)
