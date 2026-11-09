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
How the rules, the engine, the paper loop and the bench were measured is
not here: it is in MACHINERY.md, which changes only with the patch that
changes what it describes, and is cited as MACHINERY with the date of its
entry. This file is what the system has learned about markets and ideas,
and it stays under 30,000 characters, so that it can be read whole every
day: the gate fails a pull request that grows it past that, and CLAUDE.md
says how to condense it first.

## Confirmed

- Short horizon mean reversion cannot pay Binance costs (P1, real money, 2025).

## Suggested by one verdict

(none yet)

## Killed ideas and what the kill taught

- How to read a kill: 60 days is short for slow strategies. A strategy whose value comes from
  sitting out a crash shows it in the windows that contain one; in the rest
  its skill is noise around zero. Read a slow strategy's verdict with its
  Market line, and do not treat one kill as the end of the family.

- H4, the champion's signal slowed to a 30 day lookback (killed 2026-10-13, day 17.8, early kill on losses; LEDGER Result H4). It lost 15.04% against a basket that lost 7.85%, with 15 finished trades, 0 won and 15 lost (-13.74% of starting equity after costs), average exposure 0.84, daily skill t -2.36 over 18 days. Confidence 5%. Market line: basket -7.85%, BTC -0.70%, max drawdown -14%, a falling window, which is the kind the slow long-only trend follower is weakest in, so the kill says little about trend persistence over a full cycle. What it does say: the in-sample lead (+294 bps per round trip, positive skill in every quarter of the last year) did not carry into the first prospective window; the fast champion lost almost as much (-16.43%) over the same days, so a slower horizon did not buy protection against a fall. One early kill is one data point: do not close slow trend following on it, but the next entry in this family needs a reason this window does not cover (an exit that cuts a fall faster than a 5% band, or a flat-by-construction regime).

- H2, breakout after a volatility squeeze (killed 2026-11-05, day 45.3, early kill on losses; LEDGER Result H2). It lost 16.67% against a basket that lost 14.80%, with 11 finished trades, 0 won and 11 lost (-11.67% of starting equity after costs), 30 fills, average exposure 0.17, daily skill t -1.75 over 45 days. Confidence 4%. Market line: basket -14.80%, BTC -5.26%, max drawdown -24%, a falling window, so a long-only breakout buyer was in the weak regime; but the squeeze was meant to keep it out of falls, and it still bought breakouts that failed (every finished trade lost). The champion lost 30.19% over the same days, so it did less badly, which is not skill (skill -12.44%). The bench's in-sample reading (timing +17.0%, t +0.6) did not carry over. The test began 2026-09-21 after the candle-feed fix (see the ledger note).

## Calibration

How the ledger's "Expected gross bps per round trip" compared with the
realised figure promote.py records in each verdict. If expectations run high
across several verdicts, the arithmetic behind them needs fixing, not the
hypotheses.

- H4: expected +294 bps per round trip, realised -516 (15 finished trades, all lost, 17.8 days). Expectation ran far high, and the sign was wrong, on a small sample in a falling window. H3 was voided and is not counted.
- H2: expected +200 bps per round trip, realised -510 (11 finished trades, all lost, 45.3 days). Expectation ran high and the sign was wrong again, in a falling window; two of two counted verdicts now read about 700 bps below the ledger. Entries written from a plausible mechanism plus the basket's volatility overstate what long-only entries earn in a fall.

## Open questions

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

## What history says of each idea (in sample)

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


- What the bench read of each config in use, on about five years of history (2026-10-07 for H0, H1, H2, H5
  and H4, and each later test's whole reading after it; in sample, every figure). For each: what it made after
  costs; what its timing was worth a year before costs, which is the book as it last traded each pair less its
  average twin; what its costs took a year; what is left a year, with its t; the share of its twins it beats;
  how often a book with no timing does as well; and the share over the last 365 days alone. Over H0's 1,820
  days to 2026-10-07 the equal weight basket of the ten pairs lost 41.8%. How the readings are taken and how exact one
  is: MACHINERY, 2026-10-07.
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
    weak spot: at double costs nothing is left (-3.1%). Its null check (the whole reading of 2026-11-04,
    which put its own book at 90%): on the four tossed markets its books beat 70%, 71%, 83% and 84% of
    their twins, 77% on average, so the bench leans toward books like it and its share reads against about
    77%, not half. Live it was killed on 2026-11-05 with all 11 finished trades lost (Killed, H2).
  - H5, swing reversal: made +79.2% over 1,807 days; timing +16.2%, costs 3.9%, left +13.2% (t +1.7); beats 99%
    of its twins, luck does as well 2% of the time; 41% over the last 365 days. Its weak spots: ahead after
    costs in only 3 of 6 years, and under half its twins over the last year. It holds 9% of its equity on
    average and makes about 20 fills in 60 days, where a promotion asks for 30.
  - H4, ts_momentum over 720 hours: made +77.7% over 1,797 days; timing +23.3%, costs 9.0%, left +15.3% (t
    +1.0); beats 96% of its twins, luck does as well 6% of the time; 81% over the last 365 days. Ahead in 4 of 6
    years; 84% to 96% at the settings nearby and 94% to over 99% on the halves; no weak spot named. It is a slow
    book, so its twins are worth only 62 separate ones.
  - H6, relative reversion against BTC (whole reading, 2026-10-23; in sample): made -73.2% over 1,813 days
    while the basket made -61.3%; timing -11.2% a year, costs 8.5%, left -19.5% (t -1.3); beats 28% of its
    twins, luck does as well 72% of the time; 80% over the last 365 days. Nearby settings beat 23% to 50% and
    the halves of the coins 24% and 34%, so the quick reading's "no sign of timing" holds at every setting and
    half; ahead after costs in only 2 of 6 years (2021 and 2026). With the clock moved it beats 35% to 90%,
    so the 90% is one phase of the clock, not an edge. The one good year is the live window's year.
  What to take from it, and what not to. H0 and H1 show nothing on history; whether that agrees with what they
  do live is for their verdicts to say. That H2, H5 and H4 beat most of their twins says they are worth the
  slots they have and no more: all three were written with these years in view, "left a year" is measured
  against the same positions at other times and not against cash, a t under about 2 either way cannot be told
  from noise, and none of the three reaches it. The readings are here so that each test's verdict, when it
  comes, can be set beside what its history said: that comparison, over many tests, is what will say whether the
  bench is worth reading at all.

## Overturned

- Weekly cross sectional momentum on the ten pairs (a first look of 2026-10-05 by Fin's maintainer session, written into the backlog as a candidate; not a ledger verdict, so there is no ledger id). Claimed: all 18 variants beat the equal weight basket over five years, skill Sharpe 0.48 on average, 7 of 18 beating 95% of their twins. Overturned 2026-10-06 by the same session's own recheck while planning the wider universe: the study had rebalanced at Friday's close and nowhere else, and over the seven possible days the family averages +0.05. The twins could not catch it, because a twin is slid in time and so samples every weekday, while the rule under test sat on the one day that happened to work. What changed: the backlog entry moved to the ideas not to bother with, and CLAUDE.md now asks for every phase of a rhythm to be tried. No slot was spent on it.
