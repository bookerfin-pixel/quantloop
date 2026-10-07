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

- The skill figure carries a compounding term of its own (raised 2026-10-05 in review, not yet acted on). Skill is a total return minus exposure times the basket's total return. A holder who keeps a steady half of his equity in the ten pairs, rebalanced daily, does not score zero on it. Over the 60 day windows since all ten pairs have traded (July 2023 on, one window a week), his skill figure ran from -21% to +2%: a little above zero in most windows (median +0.3%), and well below it where the market ran hard one way (median -1.7% in the windows where the basket moved more than 30%), because the basket is bought once and held, so it ends up mostly in whatever rose. Both sides of a comparison carry a similar term and the daily skill t does not have it (it is built on daily differences), so it bears mostly on the floor at zero under a challenger's skill. A candidate for the next ruleset: measure skill as the sum of the daily differences, so that the figure and its t are the same quantity.

- The basket and the account are read up to an hour apart (raised 2026-10-05 in review, not yet acted on). An account is valued at the quotes of the minute the bot runs; the basket is read from hourly closes. At a test's start that is now corrected by reading between the two closes either side of it, which is nearer and not exact: on 5 October, 9.8 days after H4 began, its basket read -0.9% from the first close after the start (the old reading), 0.0% between the closes, and -0.3% from the quotes the accounts were valued at in that minute (four hours later the three read +0.1%, +1.0% and +0.7%: the gaps between them stay, about 0.9 and 0.3 of a point). At the window's end the basket is the last hourly close, some minutes older than the account's own reading. Over 60 days this is noise of a few tenths of a point, not a lean either way. A candidate for the next ruleset: read the basket from the same quotes the accounts are valued at, which the decision log already holds for every pair every hour.

- A test's return leaves out the cost of its first hour (seen 2026-10-05 in review, not changed). A test's start equity is its equity after the fills of the hour it began in, and in that hour a new strategy trades from the book the idle slot held to its own. So that one off cost is in the costs a result shows, and in the cost kill, and not in the return, the skill or the gross pnl. H4's was 13.71 and H5's 14.74, about 0.14% of the account each. The champion side leaves out only what it happened to trade in that same hour (nothing in H4's, 0.39 in H5's). It has been the convention since the first test and it leans towards the challenger by about 0.14 of a point a test, small against a bar that asks for a daily skill t of 1.0. The result's line now says the amount. The fills of that hour also count towards the 30 a promotion needs (H4's ten, H5's eight). A sell in that hour of what the slot was handed can never be a finished trade of the test's own; what the test buys in that hour is its own from then on. A candidate for the next ruleset: start a test's return, and its count of fills, from before that hour's fills.

- Does choosing between coins carry skill here where timing the market has not? (raised 2026-10-05, corrected 2026-10-06.) Not on the ten pairs, as far as five years of daily closes can say. The first look of 2026-10-05 held the strongest two to five by trailing return, rebalanced weekly, and reported that all 18 variants beat the equal weight basket (skill Sharpe 0.48 on average) and that 7 beat 95% of their own twins. It rebalanced on Fridays only. On each of the seven days the same 18 rules average +0.05 (Friday +0.47, Sunday -0.38), and 2026 is negative on every day. The details are in hypotheses/backlog.md, under the ideas not to bother with, and under Overturned below. Published work points the same way: CF Benchmarks' momentum factor on the top 50 coins (two week lookback, weekly, long the stronger half and short the weaker) made 13.41% a year from 2015 to November 2024 and has lost 14.66% in 2026 to 25 September. The same question on a wide list is what state/wide/ is for, and it has to be asked on every rebalance day. First look on the wide list, 2026-10-07, the collector's first day (by Fin's maintainer session; a lead and not a finding, for the two reasons at the end). The hundred most traded USD pairs on Kraken, 1,825 days of daily closes, a coin counted from the day its median dollar volume over the 30 days before reached $250,000 (47 coins at the median). Long only, fully invested in the strongest k by trailing return at equal weight, rebalanced weekly, costed at a 10 bps fee plus the coin's own half spread, set against all the coins then in the universe at equal weight, and run on each of the seven rebalance days. The strongest five beat the universe on every one of the seven days at every lookback tried, from 3 to 90 days: a yearly information ratio of +0.57 to +1.09 on average over the seven days and never under +0.14 on any one. The strongest ten are weaker (+0.30 to +0.93) and the strongest twenty show nothing (-0.49 to +0.47). All 18 settings on all seven days average +0.42, with 79% above nothing; with the volume floor at $1,000,000 they average +0.24, with 68% above nothing, and the strongest five still +0.49 to +1.09. The weakest k lose on nearly every setting and day (-0.51 on average), the same thing seen from the other side, and the last two years read like the whole (+0.45). So the answer on the ten pairs, nothing once every rebalance day is tried, does not carry over as it stands: on a wide list there is something to chase, and it sits in the top handful of coins. Why it is only a lead. One: the list is the hundred most traded coins today, so every coin in it is one that survived and grew, and the coins a momentum rule would have bought on the way up and held into nothing are not in it. That leans the result upward by an amount this data cannot put a figure on (a coin's `since` date in state/wide/universe.json marks where its history stops being a survivor's). Two: it is in sample, eighteen settings tried at once. What would make it a finding: the same rule on the days after each coin's `since` date as the collector's own list grows, the bench's twins on the wide data, and a history that keeps the coins that died. On that last, the collector's first run found that GitHub's runners can reach Binance's public archive of candles (both of its probes answered 200), which keeps the files of pairs that were later delisted; nothing reads it yet.

- Is there skill in anything we run? (2026-10-06.) Each live config was replayed by the engine over the 687 days to 2026-10-03 (the basket fell 35%) and set against 500 of its own twins: its hour by hour weights slid against the market by 30 days or more, so the same exposure, turnover and costs with no timing. Skill Sharpe over the span, the share of twins beaten, and the same share over the last 365 days alone: H0 -2.22, 40%, 41% (its costs come to 61% of equity a year, four times the gate's limit for a challenger); H1 -0.64, 41%, 59%; H2 +0.03, 76%, 63%; H4 +0.19, 85%, 92%; H5 +1.03, 96%, 24%. A config with no skill beats about half its twins. None beats 95% in both spans; H5's 96% is all from before the last year, as its ledger entry says, and with five configs one at 96% is what luck gives one time in five. H4 is the only one above 80% in both. This is in sample for the challengers only loosely (the agent wrote them having seen recent history) and it took minutes, where a slot takes 60 to 120 days: the case for reading every idea this way before it takes a slot.

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

- What the promotion rule asks, set against what five years of history could give (raised 2026-10-07 by the
  bench's first readings; for ruleset 8). The bench cuts each config's replay into every 120 day window from a
  year in, about 1,300 of them, of which 11 or 12 fit end to end, and counts how often a test begun there would
  have had what a promotion asks for. A daily skill t of 1.0 or more at day 120: H0 in 2% of windows, H1 in 1%,
  H2 in 15%, H4 in 10%, H5 in 27%. All three counts (a trade of its own by day 60, 30 fills, that t): the same
  figures but for H5, 25%, which has fewer than 30 fills by day 120 in 37% of windows. So the config that reads
  best on history, H4, would have been promoted from one window in ten, and the middle window's t is +0.2. Two
  readings are open and they point opposite ways. One: the rule is doing its job. These are in sample figures
  for ideas whose edge, where they have one, is small (what is left after costs against their own twins has a
  yearly Sharpe ratio of 0.3 to 0.8), and by CLAUDE.md's own sum a t of 1.0 at day 120 wants a skill with a
  Sharpe ratio of about 1.75: an edge of this size is not one 120 days can show. Two: a rule that passes the
  best idea on file one time in ten will mostly return `unproven`, and a slot spends four months to learn
  little. What would settle it is not a looser bar but more independent bets per window, which is what the wider
  universe is for, or a longer record for slow ideas, which is what the nursery in the plan is for. Not acted
  on.

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
  Measured with twins that have no skill (2026-10-05, the study behind
  PROMOTION.md; three random seeds within a point and a half of each other
  in every cell): each live config's hour by hour weights, from a replay,
  slid against the market by a random offset of at least 30 days, so the
  exposure and turnover are the strategy's own and its timing is gone. 900
  twins against H0 over 687 days in which the basket fell by a third, a
  test starting each week, every rule read the way the code reads it (the
  early kill asked every hour, 30 fills, the basket held from the test's
  start). The old rule as it ran, one look at day 60 with an early kill at
  15% under the test's own high, promoted such a twin 25 times in 100; with
  no early kill, 38. Two passes in a row: 14. Two looks with a daily skill
  t of 1.0 at day 120: 9; at 1.5: 3; at 2.0: under 1. The price is power. A
  strategy whose skill truly has a yearly Sharpe ratio of 2 is promoted 49,
  77, 57, 56, 37 and 20 times in 100 by those six, so no rule over 60 or
  120 days separates an edge of ordinary size from luck: t grows with the
  square root of time, and a skill Sharpe of 2 needs about a year to show a
  t of 2. In sample over those 687 days the skill Sharpe of the live
  configs is -0.6 (H1), 0.0 (H2) and +0.2 (H4). H4's +43% over its 715 day
  replay is mostly its first four weeks, the rally of late 2024 (+37%, the
  basket +44%); from then on it made about nothing while the basket fell by
  roughly a third (cut after 28 days it made +5% and the basket -27%; over
  the study's 687 days it made -3% and the basket -33%). That is skill of
  the useful kind (it stepped aside) and far too little to prove in a
  year.
  Decided 2026-10-05 (Fin, ruleset 7, PROMOTION.md): two looks with a daily
  skill t of 1.0 at day 120, an `unproven` outcome, and a fast pass. H1, H2,
  H4 and H5 (which began a few hours before the rule) keep their one look
  at day 60 and are otherwise judged the same way; their results also say
  what the new rule makes of the same numbers.
  As built the rule promotes a twin 9 times in 100 (8.5 to 9.0 across the
  seeds) and a Sharpe 2 edge 56. The fast pass, a first look pass with a
  daily skill t of 2.0 or more: a twin 9 times in 1,000, a Sharpe 2 edge 12
  times in 100, a Sharpe 3 edge 23. A Sharpe 2 edge is about 14 times as
  likely as a twin to get a fast pass, about 6 times as likely to be
  promoted under the whole rule, and was about 2 times as likely to pass
  the old rule as it ran. An old rule pass that the new rule does not
  confirm is 0.7 times as likely from the edge as from a twin: evidence the
  wrong way. A twin's test now takes 80 days on average against 43, so four
  slots give about 18 verdicts a year where the old rule gave about 34 (of
  those, 55 in 100 were early kills, 20 kills at day 60 and 25
  promotions). One look at day 60 under today's rules, which is how H1, H2,
  H4 and H5 are judged, would promote 38 twins in 100, against the 25 the
  old rule promoted as it ran: the fairer early kill lets more of them
  reach day 60. What would make proof
  faster for an edge of ordinary size is not a lower bar but more
  independent bets a day (open question for the wider universe).
  An earlier run of this study (the same day) asked the early kills once a
  day at the close, measured against a basket rebalanced every hour, and
  never asked for the 30 fills. Read that way the old rule's row was 32 and
  the old early kill's toll 45 of 100 by day 60. The fifth review reran the
  same twins the way the code reads them; rule 1's own row moved by half a
  point, the old rule's by seven. The figures above are the code's.

- The early kill was ending most tests whatever their skill (found
  2026-10-05, in review; in force since 2026-09-17). It read "more than 15%
  under its high inside the window", asked every hour. Replayed on the same
  687 days it ended 55 of 100 twins and 40 of 100 strategies with a Sharpe
  2 edge before day 60, and the live configs as they are in 60 (H1), 46
  (H2) and 65 (H4) of 100 starts: the basket itself fell far more than 15%
  in that stretch, so anything that held coins hit the limit. Kept on
  through a 120 day test it would have ended 74 and 58 of 100, and the two
  look rule would have promoted a Sharpe 2 edge 31 times in 100, not 56. It
  also measured from the high, so a test that had risen and given back 16%
  was ended while still above where it began, although the sentence it
  printed, and the rules file, said "from its window start".
  Twelve ways of reading it were replayed (once a day at the close, which
  understates each by a few points). Scaling the limit by the test's usual
  exposure still ended 28 of 100 Sharpe 2 edges, a flat 25% ended 11, and
  "more than the basket's own worst fall" from the high ended 2 but took H4
  as it is in 47 of 100 starts, because a trend follower is fully invested
  at the top. From ruleset 7: lost more than 15% since the test began AND
  more than the market itself over the same span. Asked every hour, that
  ends 25 of 100 twins and 5 of 100 Sharpe 2 edges inside 120 days (H1, H2
  and H4 as they are: 36, 14 and 17 of 100 starts), costs under one
  promotion in 100 against having no early kill at all, and frees a twin's
  slot about 8 days sooner on average. It is not only for fully invested
  books: what ends a test is losing more than the whole market, and a book
  of a few coins that fall harder than the rest does that at any exposure
  (H1, which usually holds about a third, is the config it ends most).
  One more change the fifth review forced: the account is valued at this
  hour's quotes, so the basket it is set against must be this hour's too.
  With two of three pairs' candles three hours behind in a falling market,
  a test that had lost less than the market was ended for losing more. The
  limit was six hours; it was made two, and the sixth review showed one
  failed fetch inside two hours doing the same in a market falling 3% an
  hour. The early kill now waits unless every pair has the candle that
  closed at the top of the hour, which the hourly run fetches just before.

- Review of the verdict code before ruleset 7 shipped (2026-10-05 and 06). Seven
  rounds of independent review, each of which ran the rule against random
  states and its own reading of PROMOTION.md, and 449 deliberate breakages
  of the code, each of which a test has to catch. What they found, all
  fixed before the first run:
  measuring: days missing from an account's record bent the daily skill t,
  because the first row back carried the account's whole return for the
  gap and only one day of the basket's (three missing days in a market up
  25% turned a t of +0.4 into +1.1, enough to turn `unproven` into
  `promoted`), and the first fix still bent it when the outage began
  inside a day, so the basket is now read at the account's own readings; a
  test's average exposure was a plain mean of its rows, which left out
  whatever it held through hours the bot did not run; three days were
  enough for a t.
  Numbers that are not numbers: a blank equity cell made a return NaN and
  every comparison with NaN is false, so a losing test passed; a blank cell
  in the hour of a promotion went into the shadow guard's start equity and
  the guard could then never revert.
  Settings: a blank value in the rules file stopped the hourly run; the
  first fix read a mistyped value as zero, which quietly switched the two
  look rule off; `compare_on: Skill` was read as "not skill", so the rule
  compared raw returns without a word; several older settings stopped the
  run only once a test reached day 60. Every challenger setting is now read
  through one checked function.
  Market data: with the candles missing the rule fell back to raw return;
  with two of three pairs' candles missing, the basket was the one pair
  left and a kill became a promotion; candles that stopped three days early
  read those days as flat. A look now waits for candles that are whole.
  Older than the rule, and never fired because nothing has been promoted:
  after a promotion every idle slot kept the old champion's config, so the
  next run would have opened a "test" of the old champion in each; the
  ledger's status flip could run on into the next entry; a test in another
  slot went on being scored against the old champion's usual exposure after
  the champion changed (the review's case: a new champion that usually
  holds 10% read as +12% of skill for sitting through a 30% fall, and a
  good challenger was killed for it). The first live promotion would have
  hit all three.
  And sentences that said what the numbers did not: "bought and held" for a
  test that had sold everything it was handed, "despite better return" for
  a return eight points worse, "passed" on the slot line for a test kept on
  value, a first look on day 119.5 that said the verdict was next.
  The fifth round went at damaged files, the guard, late candles, the names
  of settings and the documents themselves.
  Records: a file that has lost rows still parses, and was read as a
  shorter record. A test that had made forty fills read as one that had
  made one and was killed for having "finished no trade of its own"; a
  champion whose equity rows had gone read as never having had a drawdown,
  which tightened the guard on every challenger. The engine made it worse:
  a file that had lost its header was rewritten with every old row blanked.
  Now each account's files are set against its own counts every hour, and
  the engine stops rather than rewrite a file it did not write.
  The hour: the shadow guard and each slot's own record were read with
  nothing round them, so one damaged file stopped every slot's ruling, the
  summary and the commit. And a test whose record could not be read could
  not be voided, the one state a void is for.
  Candles: a pair whose candles began two days into a window was dropped
  from the basket without a word, and a kill became a promotion again; the
  early kill set an account at this hour's quotes against a basket up to
  six hours old.
  Settings: a slip in a setting's name (`two_looks_from_rulset`) was read
  as the line being left out, which switched the thing off; a blank
  `ruleset:` line stamped a new test as one from before the rule.
  The documents: the first run of the twin study had asked the early kill
  once a day and left out the 30 fills, so the old rule's row and every
  early kill figure were off by seven to fourteen points (rule 1's own row by
  half a point). And some sentences said more than the code does: "a test
  is never killed for the number of its fills" (one under 30 cannot pass a
  look, so at day 60 it is kept only on the value of its trades), "kept ...
  ends unproven" (it can also be killed at day 120).
  Sentences again: "10 fills, costs 0.00", because costs were counted from
  a reading written after a test's first hour; "is due a ruling" on day
  75; "max drawdown 10.00% exceeded the limit 10.00%".
  The sixth round went back over the fifth's fixes and found each of them
  a size too small.
  Records: an equity file was checked by its first row, its last row and
  its order, so rows cut from the middle passed; and a fill whose quantity
  had gone blank was left out of the count of fills while the count of
  rows still agreed, so a test with twenty finished trades read as having
  finished none. An account now counts its readings as it counts its
  fills, and every row of a trades file must be a fill.
  Candles: "late" was measured from the earliest pair, so when every
  pair's candles began ten days in (a candle cache lost and fetched again)
  none was late, and a test that should have been killed passed its first
  look. Late is now measured from the window's start.
  Settings: matching near names missed any name past its cutoff
  (`early_kill` for `early_kill_drawdown`), which still switched the thing
  off without a word; `max_cost_drag: 15` was read as 1,500% and the cost
  kill could never fire; `ruleset: '7'` in quotes was "unreadable";
  `slots: 2.9` ran two slots and a slip in that line's name ran one, the
  run going green every hour while a test stood still. A missing line now
  means its documented value and is named, `off` is how a thing is
  switched off, and a `slots` line that is not a count stops the run.
  The hour: the catch that keeps a damaged record from stopping the hour
  had been put round the whole of a ruling, so a revert that failed with
  half of itself written would have been swallowed and that half
  committed. Only the reading is waited for now; a ruling that cannot be
  written stops the hour. And a slot record that could not be read still
  failed the run itself, after every account had traded, so every account
  lost its hour to one file: it is now waited for like the rest.
  The guard: a promotion during an earlier promotion's guard left no
  `superseded` block when the old shadow's record was damaged, so the
  earlier promotion looked confirmed; and the summary did not say what a
  guard that was due a ruling was waiting for.
  Sentences: "skill +0.00% ... beat champion skill +0.00%"; a limit
  printed "1e-05%"; "1 fills"; a test's first hour read "there are no
  candles for its window", the line for damage, and "-0.00%".
  A seventh, short pass confirmed those fixes and found what they had
  opened. With a slot record that could not be read no longer stopping the
  run, a void request for that slot was dropped without a word, and an idle
  slot in that state did not follow a new champion, so it would have opened
  a "test" of the old one once mended: a void now reads what runs in a slot
  from its config, and idle slots follow by their config. An equity row cut
  short ("2595600,101", an equity of 10,100 read as 101) passed every
  check, and the champion's drawdown then read 99%, which takes the
  drawdown guard off every challenger: every equity row must now be a
  reading in each cell the rule reads. Under `ruleset: '7'` in quotes every
  block said the rules had changed during the test. And H4's ten fills, all
  made in its first hour, read as "on pace" for thirty.
  What the reviews could not break, for the record, in the last pass's own
  runs: the decision table held through 22 made up worlds and 1,524 hourly
  rulings with 243 damaged files and candle gaps thrown in, each hour
  checked against the reviewer's own table from PROMOTION.md; the count of
  finished trades agreed with a second implementation on 8,000 random
  sequences of fills and on 28,490 fills run through the real engine; and
  on the live state every account's files agree with its own counts, as
  does every trade row in the 452 commits of state history.

- What a kill means, and what keeps a test (Fin, 2026-10-05). On day 19 H1
  had 10 fills, on day 14 H2 had 2, and H4 had made its 10 in its first
  hour and held. The rule killed any test under 30 fills at day 60,
  whatever it had made, and promoted on skill against the usual exposure,
  which a bot can show by sitting fully invested through a rise. Fin's
  steer, in two parts. Trading little is no fault if the trades are of
  value; if they are not, kill. And riding a rise and selling at the right
  time is the skill, so kill bots that just buy and hold.
  The first build answered both with one figure, "own decisions": the sum
  of a test's daily returns minus its average exposure in the window times
  the sum of the basket's, with a floor of 1%. A holder scores zero on it,
  which is what it was for. It was dropped before it ran, because it scores
  a style and not a skill. The benchmark's exposure is known only after the
  window, and a strategy's exposure answers the market: a dip buyer holds
  most after falls, so its average exposure is high in just the windows
  where the basket lost, and the figure flatters it; a trend follower the
  other way. On a random walk with nothing to time and no costs, a dip
  buyer with no skill read +3.9% and a trend follower with no skill -3.9%
  (60 day windows, daily volatility 3.5%, a ten day rule, 20,000 windows).
  Measured against a running average known the day before the bias goes,
  and then a strategy with no skill clears a 1% floor 47 times in 100: over
  60 days any figure of this kind is a coin toss for anything that trades.
  So no profit figure can be the test of skill here. That stays with the t
  and the two looks.
  What ruleset 7 does instead is read the record plainly (PROMOTION.md). A
  test that has finished no trade of its own is killed, whatever its
  numbers. A test that does not pass the rule is kept all the same when it
  has finished a trade of its own, its finished trades made money after
  costs, and its drawdown is inside the guard. Kept is not promoted. In
  the twin study a twin with no skill had finished trades in profit at day
  60 in 36 of 100 tests and a Sharpe 2 edge in 69 (64 and 92 in the third
  of windows where the basket rose, 22 and 58 where it fell), so it is a
  weak filter and it is used as one. Two limits. Only finished trades are
  read, so a bot that takes its winners and sits on its losers reads "of
  value" until the drawdown guard or an early kill catches it. And fewer
  than 30 fills still matters: such a test cannot pass a look, so at day 60
  it is kept only if its trades are of value, and one that passes every
  number but the fills with losing trades is killed there (under 2 in 100
  twin tests).
  On 5 October: H1 had finished five trades, all winners, which made +3.98%
  of its starting equity after costs; it was behind the champion on skill
  because holding its usual 37% of a market up 27% would have made more. So
  on that day's numbers: not passing, trades of value, kept. H2 had two
  open buys and nothing finished. H4's ten fills were five buys and five
  trims of the book the idle slot had left it, all in its first hour, and
  nothing finished. Both would be killed at day 60 if that is still so.
  How a finished trade is counted: from the account's whole record of
  fills, so the count knows what a slot held when its test began. A
  position is left when a twentieth or less of its largest size remains, a
  crumb sold afterwards is not a second trade, and a position the daily
  loss halt sold is not an exit the strategy chose. That last matters: in
  the gate's replay of the last year the halt closed 127 of the 307
  positions H1 left, 31 of H4's 101, 19 of H2's 146 and 21 of H0's 862.
  None of the four had a 60 day window without a finished trade of its
  own, so a live test of any of them that reaches day 60 without one is
  doing something its backtest never did. The backtest now prints all
  three numbers for the next idea.
  What this does not catch, and what says so: a bot that trades a little
  and otherwise holds more of a rising market than it usually does. Its
  skill is real money and one bet. The confidence line says "Read it with
  care" when half or more of a test's skill is that standing tilt (in the
  test that pins it, a bot that usually holds half the market and sat fully
  invested through a 19% rise read 27%), and such a first look gets no
  fast pass.

- The market window began up to an hour late (found 2026-10-05). A test's
  basket started at the first hourly close after the test began, so it left
  out whatever the market did between the test's start and that close, for
  the whole length of the test. H4 began 21 minutes into an hour in which
  the basket rose 1.4%. On 5 October, 9.8 days on, its basket read -0.9%
  that way, where the quotes the accounts were valued at in that minute
  give -0.3%. The window now starts at the test's own start time, read
  between the two hourly prices either side of it, which gave 0.0%: nearer,
  and not
  exact, because the price did not move evenly through the hour (open
  question above). The gate's and the backtest's basket cover the same span
  as the equity curve they are set against.

- The wide data collector, and what its review found before it shipped (2026-10-06). bot/wide.py gathers research
  data once a day under state/wide/ (daily candles for the most traded USD pairs on Kraken, a bid and ask reading,
  funding of the perpetuals); no account and nothing in the hourly loop reads it, and a test runs the hourly loop
  with and without a full state/wide to hold that. An independent review of the first version found no way for it
  to disturb the hourly loop and no crash on real answers from the venues, and these faults of its own, all closed
  before the first run: a test that pinned the settings file to the code's defaults, so that any edit of
  configs/wide.yaml would have turned the gate red for every agent PR; rows already on file written back a digit
  off (pandas reads one long number in seven a unit out in its last place unless told to round trip, and a file
  that is read and rewritten daily would drift); a run that went green with half its pairs, all funding and all
  older history failing, with nobody told (the collector's own report now starts such lines with FAILED and the
  agent passes them on); one coin's odd answer stopping the older history of every coin after it; a coin new on
  Kraken marked as asked about and left for 90 days; a damaged quotes file stopping the candles; a setting that
  left no coin on the list giving a green, empty run; a join stamped with a day whose candle began before the
  coin joined (the list now records the moment too); and two smaller slips in how a damaged list file and a run
  by hand that failed were read. A second review, of the mended version, again found no way for it to reach the
  hourly loop, and these, also closed before the first run: the lines about a fault did not begin with the words
  the agent was told to look for, and the agent's run sheet had no step that ran the report, so the alarm would
  have reached nobody; the test on the shipped settings could still have closed agent PRs on a slip in the file;
  an answer whose rows were not candles (times in another unit, say), or funding readings in a shape that could
  not be read, passed for a day with nothing new; a setting that shut every coin out was caught only while the
  list was still empty; a day on which both of the day's asks failed was said nowhere (the report now says STALE
  once the last run is 30 hours old); a coin called NA or NULL would have been read back as no name; and the
  tests that held the collector apart from the hourly loop held less than they said.
  A third review, of the version mended twice, found nothing that could stop the hourly loop, close an agent PR
  on a normal day or write a wrong row, and these, closed as well before the first run. The tests that hold the
  collector apart still ran only about three in five of the loop's lines, leaving out the history backfill and
  the report's own main, and the one file of the loop the agent can change was guarded by a search for a word: a
  strategy could read the collector's files, which in a backtest is reading days not yet reached, and no test
  said so. One odd day at Coinbase ("no such product" for every coin, or rows that were not candles) was
  remembered for 90 days and said nowhere. Funding stopped without a word when the futures venue's list had no
  perpetual in it. A futures venue that hung could run the job into GitHub's 30 minute limit and take the
  day's candles with it; each part of a run now has its own allowance of time. A word in a comment in
  configs/wide.yaml, a number of hundreds of digits there, or the agent's run sheet wrapped differently would
  each have turned the gate red. The workflow's commit step, the one part that makes the data last, had only
  ever been read as text; it is now run as written, against a scratch repo. A list or a ticker from Kraken that
  had been cut off was taken at its word. The report gave the settings as the last run found them, and a line
  break inside a failure's text could start a line of its own. The same reviewer then checked the fixes: sixteen
  of its seventeen findings closed, one partly (an empty answer from Coinbase was still believed at once; it is
  now asked about once more like a "no such product", by the next day's run and not one minutes later), and
  three faults the fixes themselves had brought in, closed as well: the time allowed for candles would have cut
  a healthy list of 600 pairs short every day, always the same coins, the last by name (it now grows with the
  list, and the job's limit with it); the new check on strategies switched every setting of a strategy on, and
  one with a number for a step never came back, which in the gate is a closed pull request (only settings read
  as switches are turned on now, and each call is given ten seconds); and a pin on the Python of the other
  workflows that a change to one of them would have tripped.
  How the collector is held apart now, in layers that each see what the others miss. The loop itself, three
  hours of it as the hourly workflow runs it (accounts, history backfill, rulings, the report written to file,
  across a UTC midnight), with and without a full state/wide beside it: what it prints and every file and
  folder it leaves must come out the same. The same hours watched through Python's audit hook for a single
  file opened or folder listed under a state/wide, and run again in a process where the collector cannot be
  imported. Every line of every module of the loop read for an import of the collector or its folder spelled
  out, because three hours run only some of the lines. And every strategy called beside a full state/wide,
  with the settings of each config in the repo and with each setting its own code asks for switched on.
  The count of deliberate breakages, which is the figure to go by. The first review ran 124 against the first
  version and 48 got past its tests. The second review's fixes were tried with 57, and 4 got past at first. The
  third reviewer wrote 78, most of them aimed at the gaps above, and 50 got past. Against the version that
  ships, 378 were run and 366 are caught. The 12 that are not: three change nothing that can be seen (the next
  page of Coinbase's candles asked for a day later, since a page includes both of its ends; the whole history
  checked out by the job in place of the newest commit; the watch handed a path as an object, which Python
  turns into text before the watch is told), one is harmless (the job pushing the day's data when the pull
  before it failed and the push could still go), one shows only on an older Python than the job runs on, and
  seven are rewordings of the agent's instructions that change their sense (run the report only if there is
  time, pass on only one of the three words). Instructions are prose: a test can hold their shape (the step
  is there, before anything is committed, with the three words, and the command never carries the flag that
  collects) but not their sense.
  Known and left as they are. The watch sees files opened and folders listed, not a file's size or date being
  looked up. Kraken's numbers are read with pandas' fast parser, which can be a unit out in the last place for
  a number of 16 digits or more; Kraken sends fewer, and the same text always reads the same, so nothing
  drifts. And requirements.txt names no upper versions, for this job as for the hourly loop: a new pandas
  could turn the suite red, or change what the loop does, on the day it comes out. Naming them is Fin's call,
  because somebody then has to raise them.
  The same parser quirk sits in bot/data.py: the vwap column of state/history (a mean of three prices from
  Coinbase) would shift by a unit in its last place whenever a history file is rewritten. Nothing reads it to
  that precision and a history file is rewritten only when a backfill adds to it, so it is left as it is.
  What no test here can say is whether the venues answer the first real run the way they answered when their
  answers were read by hand on 2026-10-06; a red first run would cost nothing but the day (it commits nothing).
  Lesson, the same as on 2026-10-04: have someone who did not write a thing try to break it, and count what
  gets past the tests rather than what they cover.

- The bench, and how far a reading of it can be trusted (2026-10-07). bot/bench.py replays a config through the
  engine over all the history on file and sets its book against its twins: the same book slid 30 days or more
  later in time, so the same positions on the same coins for as long, with nothing left of when they were taken.
  A book with no timing lands anywhere among its twins. A reading gives the share of its twins the book beats
  before costs, how often a book with no timing does as well (its chance), what the timing was worth a year,
  what the costs took and what is left. The module's own text says how each is made. This entry is what was
  measured before it went in, so that nobody takes its figures for more than they are.

  How often it cries wolf. Markets were made from the ten pairs' own hours with every hour's direction tossed,
  so that the past says nothing about what comes next, and twelve kinds of book that decide on that past all the
  same were made on them: 300 markets of five years, 200 twins a book. Two of the twelve could not be read in
  any market: a book sized by how quiet each coin has been is never out of a pair, whether it trades every hour
  or, as the account does, only when a target is five points from what is held (below, under what it cannot
  read). Of the other ten kinds, the chance came out at one in ten or less for 170 of the 2,504 books that could
  be read (6.8%), and at one in twenty or less for 54 (2.2%). By kind, at one in ten or less: blind books 35 of
  300; dip buyers that look a month back 34 of 300; trend followers that look three days back 28 of 300; dip
  buyers that look 2,000 hours back 24 of 300; breakouts 22 of 300; month scale trend followers 18 of 300; 2,000
  hour trend followers 5 of 300; books that take an 8% profit and have no stop 4 of 53; books that buy a fall
  and wait for the old high 0 of 51; and trend followers with a 40% trailing stop 0 of 300. The highest of them
  is 11.7%, give or take 1.9, so no kind is clearly above ten in a hundred. On shorter runs it is more cautious,
  because slow books' twins are worth only a handful there: 5.0% of the books read at three years, 4.2% at two,
  2.6% at one and 1.9% at 300 days. So "one time in ten or less" in a reading means about that, for a book
  nobody has tuned.

  The share of twins beaten is not that honest by itself, and is not to be quoted without the chance. With
  nothing in them, slow dip buyers beat nine in ten of their twins in 53 of 300 markets (17.7%) and blind books
  in 39 of 300. And of the 396 books whose twins were worth fewer than nine separate ones, 42 beat nine in ten
  of them, 13 of those beating every one, where none of them could have a chance of one in ten. The gap is the
  number of separate twins. A thousand twins slid a few days apart are nearly one book: of the 200 made for each
  book here, the twins were worth at the median 135 separate ones for the three day trend follower, 35 for the
  month scale one, 12.5 and 14.4 for the two kinds at 2,000 hours and 5.2 for the trailing stop, and a book
  cannot stand out among five. The reading says how many, and takes the chance from that number. Two counts are
  made and the smaller is used: one from how likeness falls away with the distance between two slides, and one
  from likeness wherever it is, without which a book that holds at weekends (the same book again a week further
  on) read 888 separate twins where it has three or four. Its allowance for what twins with nothing in common
  show by chance is reckoned day by day, because a market's days are not of a size and every twin has been
  through the wild ones: reckoned as if each day weighed the same, it cut the live books' twins by up to half.
  On the five configs in use the second count now comes out above the first for four of them and one under it
  for the fifth (390 against 391 for H0). Mirror image books are not treated alike either: on the same markets a
  slow dip buyer gets a chance of one in ten or less 8.0% of the time and a slow trend follower 1.7%. No
  statistic was found that mends that; the measured rates are the mend.

  What it cannot read.

  - A book that is never out of some pair for most of the run. A strategy is told what it holds, so for as long
    as it is in a pair it can be acting on what it saw when it went in, and a twin that holds what such a book
    took later has seen the hours it is scored on: twins that held what a dip buyer was still sitting on half a
    year later scored a quarter of a point of t under the rest. So no twin holds what the book took within its
    longest stay in any one pair, and a book whose stay is most of the run has no twins. On five years that was
    249 of the 300 books that buy a fall and wait for the old high, 247 of the 300 that take an 8% profit, and
    all 600 of the quiet sized books. That is the bench failing to read a timing, not the book having none, and
    the reading says which. Two ways round it were built in review rounds three and four and taken out again in
    round five. One left a position that never changes out of the stay, so that a core holding bought once and
    kept would cost a book nothing. But the strategy is told that position's weight, which moves with its price
    and so carries the whole path since it was bought. In two kinds of book that traded their other pairs on
    that weight (40 tossed markets each, through a copy of the account's rules; the figures are from the 23 and
    the 19 in which the core stood all through) the twins that held later positions in half their hours or more
    scored 0.12 of a point of t under the rest in one kind and 0.23 over in the other (give or take 0.06 and
    0.11), where without the core they scored the same (0.01 under, give or take 0.03). The share itself did not
    visibly move (0.50, give or take 0.06): twins that see ahead a little, not a false reading that was
    measured. The other read a strategy's code for whether it ever names what it holds, and counted its stays
    from one trade to the next when it does not. But ten ordinary ways of keeping something from one hour to the
    next (a counter, a small class, a list kept sorted) still read as keeping nothing, and a strategy wrongly
    taken for one that remembers nothing has twins that see ahead (for a book that sits on its dips, read with
    the short lead, such twins scored 0.26 under the rest). Neither could be made safe for every strategy. All
    four strategies in bot/strategy.py do name what they hold and all of them go flat, so no reading on file
    changed. What is lost: a book that never leaves any position cannot be read, and rule 1 kills such a test at
    its look in any case. Two kinds that rule 1 does not kill cannot be read either: a book that keeps one
    position for good and trades the rest, and one that sells its positions down to a crumb and never to nothing
    (rule 1 counts a position as left at a twentieth of its size, the bench only at nothing; a strategy is told
    that it holds a crumb). Reading those properly means the bench deciding what the strategy is told it holds,
    which is for the bench on the wide data.

  - A short run. On 300 days it could read 78 of 300 slow trend followers and 24 of 300 slow dip buyers, and
    those were the ones whose trends had failed and whose dips had come back: with nothing in them they beat 31%
    and 69% of their twins on average. Twins there are worth 3.3 to 3.5 separate ones at the median, so no claim
    follows, but "a book with no timing beats about half" is not true of what gets read on a short run. At two
    years 243 of 300 trailing stop books, 299 and 299 of 300 of the two kinds at 2,000 hours and every one of
    the two month scale kinds are read, and the average is back near a half (0.47 to 0.53); at five years it is
    0.46 to 0.54, which is the mirror image lean above and not this. `--days` is for trying things out; a
    reading that counts is of all the history.

  - An idea tuned on this history. Every config was written by someone who had seen these five years. How often
    a tuned idea with nothing in it gets a chance under one in ten was not measured, and it is more often than
    the 7 in a hundred above.

  - A strategy with a memory of its own between hours, in its module, on its function or in its params. The
    hourly loop starts afresh every hour, so such a strategy does not do live what it does in a replay, which is
    a fault in the strategy and now a line in its contract (bot/strategy.py, CLAUDE.md). The bench says so when
    a strategy's params are not, at the end of a replay, what it was handed, and it cannot see a memory kept
    anywhere else. And a strategy that enters on one thing and leaves on another carries something through its
    flat stretches too: the rule on how far a twin may be slid is a rule of thumb, held to the rates above, not
    a proof.

  What review found. Two reviewers who had not written it, one on the statistics and one on the engineering,
  went over it five times before it shipped, with mutation runs between. Round one, 20 faults. The worst: twins
  were ranked on a figure with the book's own costs in it, so that a book on the costs treadmill read 83% where
  its timing alone read 73%; a twin could hold positions the book took just after the hour in hand, which piled
  trend followers up at the bottom; and a replay that had failed was counted as a setting that agreed. Round
  two, 16. The worst: a line that split a book's timing into what was made inside the years and between them,
  and gave a trend follower with nothing in it ten points a year either way (the line was dropped); and a
  protected test that needed some config to be named H0, which would have turned the gate red for every proposal
  after the first promotion. Round three, 11. The worst: the rule on stays had begun to refuse every book that
  is never out of a pair, however much it trades; and the weekend count above. Round four, 10. The worst: the
  second count's allowance for chance, above; a core position bought once and kept cost a book all its twins; a
  strategy that kept where it had bought in its params was taken for one that cannot see what it holds; and a
  replay whose process died was waited for as long as anything it had started lived. Round five, 8. The worst
  were two of round four's own mends, the two ways round a book that is never out of a pair, above: one let
  twins see ahead a little and the other could not tell which strategies remember, and both came out. That is 65
  faults in all, and a sixth, short look at the taking out found nine more, all small (the worst: a book that
  holds only pairs too new for any book to be read was told its stay was too long). All were closed but two that
  are stated instead: the mirror image, and the books that are never out of a pair. Lesson, for the third time
  in a month: the figures that looked most finished were the ones a second pair of eyes took apart, and a mend
  is a change like any other, so nothing that scores ideas goes in on its author's word.

- What the five configs in use read on five years (2026-10-07; in sample, every figure of it). The bench's first
  readings, from replays of the candles on file up to the midnight before. Each config is read from the first
  hour it could decide, about 1,800 days; over H0's 1,820 the equal weight basket of the ten pairs lost 41.8%.
  For each: what it made after costs; what its timing was worth a year before costs, which is the book as it
  last traded each pair less its average twin; what its costs took a year; what is left a year, with its t; the
  share of its twins it beats; how often a book with no timing does as well; and the share of its twins it beats
  over the last 365 days alone. Taken again by the real command with a few more hours of candles, the yearly
  figures came out within a tenth of a point and the shares within one point; but the two takes draw the same
  twins, so that says only that a few hours of candles change nothing. How exact a reading is shows when the
  thousand twins are drawn afresh. Over twelve other draws a share moved by 0.4 to 1.3 points either way, book
  by book (H0's ran from 72% to 76%), a share over the last 365 days by 1.2 to 1.9 points, and the yearly
  figures by a quarter to half a point (H0's timing from +8.3% to +10.1%, where the draw the bench keeps gives
  +8.2%); the t of what is left moved by 0.03. H2's chance was one in ten or less in 8 of the 12, so it sits on
  the line the words turn on; H5's and H4's were under it in all 12, and H0's and H1's in none.
  - H0, ts_momentum over 72 hours, the champion: made -92.0%; timing +8.2%, costs 58.2%, left -49.6% (t -3.3);
    beats 72% of its twins, luck does as well 29% of the time; 25% over the last 365 days. Cannot be told from
    luck, and it pays seven times in costs what its timing could be worth.
  - H1, mean reversion over 240 hours: made -87.3% over 1,817 days; timing -21.6%, costs 16.6%, left -38.4% (t
    -2.7); beats 5% of its twins, luck does as well 95% of the time; 67% over the last 365 days. No sign of
    timing: nineteen in twenty of its own twins did better, at every setting nearby (1% to 6%) and on every half
    of the coins (3% to 14%).
  - H2, volatility breakout: made +41.2% over 1,760 days; timing +17.0%, costs 10.5%, left +7.5% (t +0.6); beats
    91% of its twins, luck does as well 9% of the time; 64% over the last 365 days. Ahead of its average twin
    after costs in 5 of 5 years, at 84% to 96% at the settings nearby and 89% to over 99% on the halves. Its
    weak spot: at double costs nothing is left (-3.1%).
  - H5, swing reversal: made +79.2% over 1,807 days; timing +16.2%, costs 3.9%, left +13.2% (t +1.7); beats 99%
    of its twins, luck does as well 2% of the time; 41% over the last 365 days. Its weak spots: ahead after
    costs in only 3 of 6 years, and under half its twins over the last year. It holds 9% of its equity on
    average and makes about 20 fills in 60 days, where a promotion asks for 30.
  - H4, ts_momentum over 720 hours: made +77.7% over 1,797 days; timing +23.3%, costs 9.0%, left +15.3% (t
    +1.0); beats 96% of its twins, luck does as well 6% of the time; 81% over the last 365 days. Ahead in 4 of 6
    years; 84% to 96% at the settings nearby and 94% to over 99% on the halves; no weak spot named. It is a slow
    book, so its twins are worth only 62 separate ones.
  What to take from it, and what not to. H0 and H1 show nothing on history; whether that agrees with what they
  do live is for their verdicts to say. That H2, H5 and H4 beat most of their twins says they are worth the
  slots they have and no more: all three were written with these years in view, "left a year" is measured
  against the same positions at other times and not against cash, a t under about 2 either way cannot be told
  from noise, and none of the three reaches it. The readings are here so that each test's verdict, when it
  comes, can be set beside what its history said: that comparison, over many tests, is what will say whether the
  bench is worth reading at all.

## Overturned

- Weekly cross sectional momentum on the ten pairs (a first look of 2026-10-05 by Fin's maintainer session, written into the backlog as a candidate; not a ledger verdict, so there is no ledger id). Claimed: all 18 variants beat the equal weight basket over five years, skill Sharpe 0.48 on average, 7 of 18 beating 95% of their twins. Overturned 2026-10-06 by the same session's own recheck while planning the wider universe: the study had rebalanced at Friday's close and nowhere else, and over the seven possible days the family averages +0.05. The twins could not catch it, because a twin is slid in time and so samples every weekday, while the rule under test sat on the one day that happened to work. What changed: the backlog entry moved to the ideas not to bother with, and CLAUDE.md now asks for every phase of a rhythm to be tried. No slot was spent on it.
