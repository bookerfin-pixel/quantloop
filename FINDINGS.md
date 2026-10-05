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
  In sample answer, 2026-09-25, backtests only: at 72h the signal is a coin
  flip before costs (mean gross move per round trip +4 bps long, -16 bps
  short, in a fixed size screen over two years), at 168h +58 bps long, at 720h
  +294 bps long with an eighth as many round trips. The real engine gives the 720h
  version (entry and exit bands of 5%, 168h EMA) +35% over 700 days against
  a basket of +1.4%, and -13.5% over the last 365 days against -50.1%. One
  parameter set on the data it was chosen from; the prospective test is still
  the answer. See the top of hypotheses/backlog.md.
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
  through this rally. A flat H2 is a reading of the market now, not a data
  artifact; notes that call it "the ramp-up issue" are out of date.
  Correction 2026-10-04: this entry used to add that a backtest over the same
  hours "also makes 0 trades (checked 2026-09-25)". That check proved
  nothing, because short backtests then starved strategies of history (see
  the 2026-10-04 calibration entry). The live reason text was the evidence.
  With the engine fixed the backtest does reproduce live H2: 2 fills against
  2 over 25 Sep to 4 Oct.

- Calibration of the loop itself, 2026-09-21: the hourly loop and the backtest
  handed strategies different candle frames for four days (live cache only vs
  history plus live), so a lookback that passed the gate could not fire live.
  Fixed in bot/run.py: both paths now build a strategy's frames from the same
  merge of history and live candles (tests/gate/test_replay.py checks it
  through the hourly entry point).
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
  have been flat, 0 trades (first checked on a short backtest that starved
  the strategy of history, so that check proved nothing; rerun 2026-10-04 on
  the fixed engine, the answer is the same). Fixed in bot/run.py: an account's first hour
  under a new strategy decides as if flat and trades from the book it really
  holds. The same thing would have happened after every verdict (an idle slot
  runs the champion's config and builds its book) and after every promotion
  (the champion account keeps its positions), so it is fixed at the root.
  Lesson: before reading a challenger's first days, check that its first
  fills carry its own entry reasons.

- Calibration of the loop itself, 2026-10-04: short backtests starved
  strategies of history. run_backtest cut the candles handed to a strategy
  to the replayed window plus the largest single `*_hours` parameter, so a
  strategy needing more (swing_reversal needs two recent_hours, vol_breakout
  needs compression plus lookback) sat flat on "only N candles" for a whole
  short run: `--days 9` of H3 showed 0 trades while the live account made
  124. Two live against backtest checks made on 2026-09-25 rested on such
  runs and proved nothing (both conclusions survive the rerun). Fixed in
  bot/backtest.py: the strategy is always handed the trailing history_hours
  of real candles, as the hourly loop hands it. The gate now fails a config
  that says "only N candles" on more than 2% of its decisions, and
  tests/gate/test_replay.py holds the replay and the backtest to the same
  fills. Lesson: a check that returns "nothing happened" has to show it
  could have returned something. This is the fourth bug in the measuring
  code in three weeks (candle frames, inherited book, skill basis, this);
  the measuring code deserves more suspicion than the strategies.

- Calibration of the loop itself, 2026-10-04: GitHub's scheduler is best
  effort. From 2026-10-03 10:22Z it dropped scheduled runs for hours at a
  time (gaps of 4.2, 4.5 and 6.7 hours) and skipped that night's agent run;
  nothing failed, the runs were never created, and nobody was told. The loop
  no longer depends on it: an outside scheduler also starts both workflows,
  each account remembers the last candle it decided on, a duplicate trigger
  does nothing, and missed hours are replayed in order at the next candle's
  open (rows marked "replayed after a missed run"). The hours dropped on
  2026-10-03 between the old loop's runs were not replayed (the accounts held
  their books through them); hours dropped after its last run were, by the
  first run of the new loop. The daily review missed all of it: it checked
  the candle files for missing hours, and Kraken backfills candles, so its
  notes said "no missing hours" while 26 of 40 hourly runs had not happened
  (the weekly digest caught it by counting commits). The summary now opens
  with a Runs section, hours on record against hours due, from the champion's
  own equity log. Lesson: check that a thing ran by looking at what it wrote,
  not at its inputs.

- Calibration of the loop itself, 2026-10-04: a held pair with no price
  counted as zero. Equity summed only the positions that had a price that
  hour, so one failed quote, or one pair's candles missing from a replayed or
  backtested hour, read as that position vanishing: a quarter of the book
  gone, the 5% daily halt fired, the rest was sold, and in a challenger the
  15% early kill followed. It had been in the live path since the first day
  and never fired, because Kraken has not failed a quote on a held pair yet;
  the replay made it likely (one pair's request failing during a catch up),
  and an independent review of the replay found it before it shipped. A held
  pair now keeps the last price known for it, sits the hour out, and says so
  in the decision log. Backtests over the last 365 and 700 days are identical
  before and after for all five live configs, because Coinbase's history has
  no gap in a single pair, only two venue wide ones of five hours. The same
  review found that a replay would have run a new strategy over hours from
  before it existed, and that a dead candle feed would have passed for a
  duplicate trigger and exited green; both are closed (a changed strategy
  starts fresh on the current candle, a run that cannot get the candle that
  just closed fails). Lesson: test what a new path does when its inputs fail,
  not only when they arrive, and have someone who did not write it try to
  break it. Fifth bug in the measuring code in three weeks.

## How the machinery shapes results

- What skill means in a verdict (2026-09-25). Skill is net return minus the
  equal weight basket held at the strategy's usual exposure, its average
  exposure in a backtest over the year before its test began. Measured
  against the window's own average exposure instead, a strategy gets no
  credit for timing slower than the window: in sample the slow trend
  follower's 60 day skill was positive in 25% of windows that way and 54% on
  the usual basis. Either way the market's own move explains little of the
  skill edge between two strategies (R2 0.00 to 0.16 across the live configs,
  against up to 0.63 for raw return), which is why verdicts use it.
- 60 days is short for slow strategies. A strategy whose value comes from
  sitting out a crash shows it in the windows that contain one; in the rest
  its skill is noise around zero. Read a slow strategy's verdict with its
  Market line, and do not treat one kill as the end of the family.

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

- A loop the gate did not see (H3, 2026-10-04). swing_reversal enters on a
  level test and exits on a new 48h low, so a fading rally above the reaction
  high loops exit, re-enter, exit within hours. Live: 124 fills in 8.9 days,
  1.39 per pair per day against the 0.05 its ledger entry reported, costs at
  116% of starting equity a year against the gate's 15% limit. The gate
  passed it because it bounded only the average fill rate over 365 days
  (0.09) while the same backtest showed 12 fills in one pair in one day; the
  loop is rare in falling months and constant in a rally (2 to 6 fills a month
  in seven of the last twelve months, 123 in September 2026). The agent diagnosed it on
  2026-10-02 and left it running so as not to confound the test, which would
  have spent 51 more days measuring the bug. Fin voided the test. Three rules
  came out of it: buys in a pair stop after 4 fills in a UTC day (it never
  binds on H1, H2 or H4 over the last 365 days and binds on 4 pair days for
  H0, so it changes nothing that is not a loop); the gate fails a config
  whose buys the cap had to stop on more than 12 pair days a year (H3: 16);
  and a challenger whose live costs after 14 days run past three times the
  gate's limit is killed.
- The treadmill, live (week to 2026-10-04). In a flat week (basket -1.5%,
  BTC +0.4%) H0 made 81 fills, paid 205 in costs (1.9% of equity) and lost
  10.9%. H4, the same signal at ten times the horizon, made no fills and lost
  1.9%. This is the in sample finding below showing up prospectively; it is
  one week.
- The paper loop and the backtest agree (2026-09-25). Replaying the
  champion's first nine live days with the backtest engine from the same
  10,000 cash gave +20.99% against +19.95% live, with the same 58 fills and
  costs of 132 against 135. The gap is fill timing (the backtest fills at the
  candle open on the hour, the live loop at the quote about 20 minutes later)
  and observed spreads. H1's replay differed (27 fills against 8) only because
  live H1 ran on six pairs and the live candle cache until 2026-09-21; on the
  shared pairs the entries and exits match. With the 2026-10-04 history fix
  the engine also reproduces live H3 (125 fills against 124 over its window,
  with the fill cap switched off as it was live; 96 with the cap on) and live
  H2 (2 against 2).
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
  and H2 in backtest with no extra fills. Retested 2026-09-27 on the live
  code with H4 included, over 365 and 700 days (H0 / H4 net return):
  current rule -62.5% / -7.9% and -68.8% / +43.8%; sharing scarce cash pro
  rata -61.6% / -10.4% and -68.0% / +35.2%; trimming to fund new entries only
  -63.7% / -6.2% and -72.5% / +42.4%, with 40-47% more fills. No variant beat
  the current rule across the board, so blocked buys stay as they are and the
  log now says "waits for cash" instead of "no fill possible". Since sells
  started filling first, the champion had a blocked buy in 12 of 51 hourly
  runs (it was 111 of 216 before), and the longest wait for a new entry was
  two hours.

- How easy is it to be promoted by luck? (raised 2026-10-04, rule under
  review by Fin.) The bar is skill above zero and above the champion's, and
  H0's skill is positive in about 3% of historical windows, so the real bar
  is skill above zero. In sample, 60 day skill was positive in 46% of windows
  for H1, 58% for H2, 35% for H3 and 54% for the slow trend, none of which
  has shown an edge. So a strategy with no edge clears the bar about half the
  time, and a promotion in November would say little. Until the rule changes,
  read "promoted" as "not ruled out", and look at the daily edge t in the
  verdict: under about 2 it is noise.
  Measured the same day with twins that have no skill: each live config's
  hour by hour weights slid against the market by a random offset of at least
  30 days, so the exposure, turnover and costs are the strategy's own and its
  timing is gone. Against H0 over the last 687 days the rule as it stands
  promotes such a twin 40% of the time. Two passes in a row: 16%. A pass at
  day 60 and then 120 days with skill above zero, above the champion's and a
  daily skill t of at least 1.0: 8%; at 1.5: 3%; at 2.0: under 1%. The price
  is power. A strategy whose skill truly has a yearly Sharpe ratio of 2
  clears those five bars 81%, 65%, 57%, 38% and 20% of the time, so no rule
  over 60 or 120 days separates an edge of ordinary size from luck: t grows
  with the square root of time, and a skill Sharpe of 2 needs about a year to
  show a t of 2. In sample over those 687 days the skill Sharpe of the live
  configs is -0.6 (H1), 0.0 (H2) and +0.2 (H4). H4's +43% over 715 days is
  mostly its first four weeks, the rally of late 2024 (+40%, the basket
  +45%); from then on it made +3% while the basket fell 27%. That is skill of
  the useful kind (it stepped aside) and far too little to prove in a year.

## Overturned

(none yet)
