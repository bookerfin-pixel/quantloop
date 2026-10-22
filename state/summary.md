# quantloop summary — generated 2026-10-22 07:11Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-15 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 2 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, ETH, 2026-10-18: 4 fills (buy 03:10, sell 04:10, buy 15:10, sell 16:10); no buy stopped
- champion, DOT, 2026-10-16: 5 fills (buy 01:10, buy 02:10, sell 04:10, buy 15:10, sell 19:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 36.1 of 60, 23.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -6.13% (max drawdown -24.95%, 302 fills) vs challenger1 -3.44% (max drawdown -12.36%, 75 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.84% (usual 0.54, this window 0.57) vs challenger1 -7.38% (usual 0.37, this window 0.39); the rule compares on skill, daily edge t +0.27 over 36 days
  trades: its 28 finished trades made -3.56% of its starting equity after costs (15 won, 13 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.02 over 36 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +8.65%, equal weight basket of 10 pairs +10.61%, basket max drawdown -17%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 30.9 of 60, 29.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -18.31% (max drawdown -24.95%, 264 fills) vs challenger2 -4.03% (max drawdown -4.50%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.79% (usual 0.54, this window 0.54) vs challenger2 -2.17% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +1.62 over 31 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.56 over 31 days)
  fills: 8 in 30.9 days; at this pace about 15 by day 60, under the 30 a promotion there needs, and about 31 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -0.17%, equal weight basket of 10 pairs -6.51%, basket max drawdown -17%, basket realised vol 58% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 16.4 of 60, 43.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -15.52% (max drawdown -15.88%, 113 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.56% (usual 0.55, this window 0.38) vs challenger3 -0.91% (usual 0.03, this window 0.02); the rule compares on skill, daily edge t +2.36 over 16 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.89 over 16 days)
  fills: 10 in 16.4 days, 8 of them in the hour it began; at this pace about 22 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -4.11%, equal weight basket of 10 pairs -12.68%, basket max drawdown -17%, basket realised vol 58% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 6.3 of 120, 113.7 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -0.27% (max drawdown -4.99%, 13 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +0.93% (usual 0.53, this window 0.94); the rule compares on skill, daily edge t +0.62 over 6 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -7.17% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  market over the window: BTC +0.09%, equal weight basket of 10 pairs -2.27%, basket max drawdown -7%, basket realised vol 51% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,386.69 (started 10,000 at 2026-09-16 03:55Z), net -6.13% since start
- 24h -2.12%, 7d -6.80%, 30d -20.20%, max drawdown -24.95%
- fills 302 total, 55 in the last 7d
- costs 699.54 (fees 463.38 + slippage 236.16); gross pnl 86.23; cost coverage 0.12
- cash 1,560.89; positions: BTC 0.0190144, ETH 0.645533, LINK 129.067, LTC 25.9796, XRP 1169.96
- last run 2026-10-22 07:10Z; halted today: False

last decisions (newest last):

- 2026-10-22 06:10Z SOL buy target 0.17 (held 0.11) — stay long: 72h return -0.59% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 55% -> weight 0.25
- 2026-10-22 06:10Z ADA sell target 0.00 (held 0.11) — exit: price more than 2.0% below 24h EMA
- 2026-10-22 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.78% not above entry band +1.0% and price below 24h EMA
- 2026-10-22 06:10Z LINK buy target 0.17 (held 0.11) — stay long: 72h return +0.38% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 64% -> weight 0.25
- 2026-10-22 06:10Z XRP buy target 0.17 (held 0.11) — stay long: 72h return +2.40% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 52% -> weight 0.25
- 2026-10-22 06:10Z DOGE sell target 0.00 (held 0.11) — exit: price more than 2.0% below 24h EMA
- 2026-10-22 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.12% not above entry band +1.0% and price below 24h EMA
- 2026-10-22 06:10Z LTC buy target 0.17 (held 0.11) — stay long: 72h return +0.58% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 60% -> weight 0.25
- 2026-10-22 07:10Z BTC hold target 0.20 (held 0.17) — hold: weight change +0.033 below threshold 0.05 | stay long: 72h return -0.43% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-22 07:10Z ETH hold target 0.20 (held 0.17) — hold: weight change +0.033 below threshold 0.05 | stay long: 72h return +0.11% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-22 07:10Z SOL sell target 0.00 (held 0.17) — exit: 72h return -1.09% fell below exit band -1.0%
- 2026-10-22 07:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.13% not above entry band +1.0% and price below 24h EMA
- 2026-10-22 07:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.12% not above entry band +1.0% and price below 24h EMA
- 2026-10-22 07:10Z LINK hold target 0.20 (held 0.17) — hold: weight change +0.033 below threshold 0.05 | stay long: 72h return -0.22% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-22 07:10Z XRP hold target 0.20 (held 0.17) — hold: weight change +0.033 below threshold 0.05 | stay long: 72h return +2.07% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-22 07:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.06% not above entry band +1.0% and price below 24h EMA
- 2026-10-22 07:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.67% not above entry band +1.0% and price below 24h EMA
- 2026-10-22 07:10Z LTC hold target 0.20 (held 0.17) — hold: weight change +0.034 below threshold 0.05 | stay long: 72h return +0.45% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 27 fills (12 buy / 15 sell), traded 37,592, gross pnl -30.48, -16 bps per round trip, avg half spread 2.0 bps
- AVAX: 37 fills (17 buy / 20 sell), traded 64,485, gross pnl +381.31, +118 bps per round trip, avg half spread 1.1 bps
- BTC: 29 fills (16 buy / 13 sell), traded 43,372, gross pnl -5.64, -3 bps per round trip, avg half spread 0.1 bps, open 0.0190144
- DOGE: 25 fills (13 buy / 12 sell), traded 32,788, gross pnl -228.80, -140 bps per round trip, avg half spread 0.9 bps
- DOT: 37 fills (18 buy / 19 sell), traded 55,180, gross pnl -105.48, -38 bps per round trip, avg half spread 2.3 bps
- ETH: 28 fills (14 buy / 14 sell), traded 42,725, gross pnl -202.22, -95 bps per round trip, avg half spread 0.0 bps, open 0.645533
- LINK: 31 fills (15 buy / 16 sell), traded 55,516, gross pnl -230.88, -83 bps per round trip, avg half spread 2.0 bps, open 129.067
- LTC: 32 fills (16 buy / 16 sell), traded 47,360, gross pnl +472.51, +200 bps per round trip, avg half spread 1.6 bps, open 25.9796
- SOL: 32 fills (17 buy / 15 sell), traded 51,357, gross pnl -71.41, -28 bps per round trip, avg half spread 0.5 bps
- XRP: 24 fills (13 buy / 11 sell), traded 33,008, gross pnl +107.30, +65 bps per round trip, avg half spread 0.4 bps, open 1169.96

last fills:

- 2026-10-22 06:10Z sell DOGE 1,043 @ 0.0797341 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-10-22 06:10Z buy BTC 512 @ 82764 fee 0.51 slip 0.26 (half spread 0.0 bps)
- 2026-10-22 06:10Z buy ETH 520 @ 2437.83 fee 0.52 slip 0.26 (half spread 0.0 bps)
- 2026-10-22 06:10Z buy SOL 529 @ 104.947 fee 0.53 slip 0.26 (half spread 0.5 bps)
- 2026-10-22 06:10Z buy LINK 520 @ 12.1929 fee 0.52 slip 0.26 (half spread 0.5 bps)
- 2026-10-22 06:10Z buy XRP 496 @ 1.3451 fee 0.50 slip 0.25 (half spread 0.0 bps)
- 2026-10-22 06:10Z buy LTC 516 @ 60.3352 fee 0.52 slip 0.26 (half spread 0.8 bps)
- 2026-10-22 07:10Z sell SOL 1,562 @ 104.198 fee 1.56 slip 0.78 (half spread 1.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,644.74 (started 10,000 at 2026-09-16 03:55Z), net -3.55% since start
- 24h +0.00%, 7d +3.34%, 30d -6.27%, max drawdown -12.36%
- fills 75 total, 14 in the last 7d
- costs 157.01 (fees 104.58 + slippage 52.42); gross pnl -198.25; cost coverage -1.26
- cash 9,644.74; positions: none
- last run 2026-10-22 07:10Z; halted today: False

last decisions (newest last):

- 2026-10-22 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-10-22 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.94 not below -2.0
- 2026-10-22 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.54 not below -2.0
- 2026-10-22 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-10-22 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.43 not below -2.0
- 2026-10-22 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.68 not below -2.0
- 2026-10-22 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.63 not below -2.0
- 2026-10-22 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.04 not below -2.0
- 2026-10-22 07:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.12 not below -2.0
- 2026-10-22 07:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-10-22 07:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-10-22 07:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.01 not below -2.0
- 2026-10-22 07:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.61 not below -2.0
- 2026-10-22 07:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.52 not below -2.0
- 2026-10-22 07:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.35 not below -2.0
- 2026-10-22 07:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.74 not below -2.0
- 2026-10-22 07:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.85 not below -2.0
- 2026-10-22 07:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.10 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 7,809, gross pnl +98.89, +253 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (4 buy / 3 sell), traded 7,990, gross pnl +152.80, +382 bps per round trip, avg half spread 0.8 bps
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 10 fills (5 buy / 5 sell), traded 15,100, gross pnl -145.41, -193 bps per round trip, avg half spread 0.3 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 9 fills (5 buy / 4 sell), traded 9,969, gross pnl +43.86, +88 bps per round trip, avg half spread 1.2 bps
- LTC: 7 fills (4 buy / 3 sell), traded 8,915, gross pnl -8.69, -19 bps per round trip, avg half spread 1.4 bps
- SOL: 9 fills (5 buy / 4 sell), traded 13,156, gross pnl -139.56, -212 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-19 03:10Z buy AVAX 1,200 @ 9.77939 fee 1.20 slip 0.60 (half spread 1.5 bps)
- 2026-10-19 13:10Z sell LTC 1,345 @ 60.1499 fee 1.34 slip 0.67 (half spread 1.7 bps)
- 2026-10-20 15:10Z sell ETH 1,378 @ 2458.62 fee 1.38 slip 0.69 (half spread 0.0 bps)
- 2026-10-20 15:10Z sell ADA 1,324 @ 0.223619 fee 1.32 slip 0.66 (half spread 1.3 bps)
- 2026-10-20 15:10Z sell AVAX 1,369 @ 9.80509 fee 1.37 slip 0.68 (half spread 1.0 bps)
- 2026-10-20 15:10Z sell LINK 1,357 @ 12.2995 fee 1.36 slip 0.68 (half spread 1.0 bps)
- 2026-10-20 15:10Z sell XRP 1,352 @ 1.32697 fee 1.35 slip 0.68 (half spread 0.0 bps)
- 2026-10-20 15:10Z sell DOGE 1,353 @ 0.0812951 fee 1.35 slip 0.68 (half spread 0.1 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,523.57 (started 10,000 at 2026-09-16 23:20Z), net +5.24% since start
- 24h -2.31%, 7d -2.34%, 30d -4.03%, max drawdown -5.26%
- fills 40 total, 4 in the last 7d
- costs 111.28 (fees 73.75 + slippage 37.53); gross pnl 634.85; cost coverage 5.70
- cash -0.00; positions: ADA 11708.7, BTC 0.0324709, DOGE 32993.8, XRP 2005.46
- last run 2026-10-22 07:10Z; halted today: False

last decisions (newest last):

- 2026-10-22 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 06:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.008 below threshold 0.05 | stay long: price 0.2186 still above 72h low 0.2152; realised vol 65% -> weight 0.25
- 2026-10-22 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 06:10Z XRP hold target 0.25 (held 0.26) — hold: weight change -0.005 below threshold 0.05 | stay long: price 1.343 still above 72h low 1.292; realised vol 52% -> weight 0.25
- 2026-10-22 06:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 0.07983 still above 72h low 0.0788; realised vol 57% -> weight 0.25
- 2026-10-22 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 07:10Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: price 8.24e+04 still above 72h low 8.138e+04; realised vol 32% -> weight 0.25
- 2026-10-22 07:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 07:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 07:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.008 below threshold 0.05 | stay long: price 0.2181 still above 72h low 0.2152; realised vol 65% -> weight 0.25
- 2026-10-22 07:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 07:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 07:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.005 below threshold 0.05 | stay long: price 1.34 still above 72h low 1.292; realised vol 51% -> weight 0.25
- 2026-10-22 07:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 0.07971 still above 72h low 0.0788; realised vol 57% -> weight 0.25
- 2026-10-22 07:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-22 07:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 7,563, gross pnl -79.02, -209 bps per round trip, avg half spread 1.7 bps, open 11708.7
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 6 fills (4 buy / 2 sell), traded 13,500, gross pnl -80.06, -119 bps per round trip, avg half spread 0.0 bps, open 0.0324709
- DOGE: 4 fills (3 buy / 1 sell), traded 5,655, gross pnl -52.28, -185 bps per round trip, avg half spread 0.9 bps, open 32993.8
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 3 fills (2 buy / 1 sell), traded 3,883, gross pnl -29.01, -149 bps per round trip, avg half spread 0.3 bps, open 2005.46

last fills:

- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)
- 2026-09-30 13:27Z buy BTC 2,737 @ 85327.3 fee 2.74 slip 1.37 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell BTC 2,689 @ 83812.2 fee 2.69 slip 1.34 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell ETH 2,611 @ 2609.08 fee 2.61 slip 1.31 (half spread 0.0 bps)
- 2026-10-20 15:10Z buy BTC 2,694 @ 82967.9 fee 2.69 slip 1.35 (half spread 0.0 bps)
- 2026-10-21 08:10Z buy XRP 2,694 @ 1.34334 fee 2.69 slip 1.35 (half spread 0.2 bps)
- 2026-10-21 14:10Z buy DOGE 2,706 @ 0.0820032 fee 2.71 slip 1.35 (half spread 0.0 bps)
- 2026-10-21 16:10Z buy ADA 2,672 @ 0.228184 fee 2.67 slip 1.34 (half spread 0.9 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-22 07:10Z; halted today: False

last decisions (newest last):

- 2026-10-22 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 100.7 not a higher low vs prior low 106.3 (need +10.0%)
- 2026-10-22 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2117 not a higher low vs prior low 0.2251 (need +10.0%)
- 2026-10-22 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.315 not a higher low vs prior low 9.83 (need +10.0%)
- 2026-10-22 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.56 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-22 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.326 (need +10.0%)
- 2026-10-22 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07626 not a higher low vs prior low 0.08144 (need +10.0%)
- 2026-10-22 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.048 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-22 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 56.77 not a higher low vs prior low 61.36 (need +10.0%)
- 2026-10-22 07:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.011e+04 not a higher low vs prior low 8.067e+04 (need +10.0%)
- 2026-10-22 07:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2335 not a higher low vs prior low 2415 (need +10.0%)
- 2026-10-22 07:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 100.7 not a higher low vs prior low 106.3 (need +10.0%)
- 2026-10-22 07:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2117 not a higher low vs prior low 0.2251 (need +10.0%)
- 2026-10-22 07:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.315 not a higher low vs prior low 9.83 (need +10.0%)
- 2026-10-22 07:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.56 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-22 07:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.326 (need +10.0%)
- 2026-10-22 07:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07626 not a higher low vs prior low 0.08144 (need +10.0%)
- 2026-10-22 07:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.048 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-22 07:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 56.77 not a higher low vs prior low 61.36 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 4 fills (2 buy / 2 sell), traded 7,389, gross pnl -111.53, -302 bps per round trip, avg half spread 0.7 bps
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)
- 2026-10-06 15:25Z buy AVAX 2,503 @ 11.5663 fee 2.50 slip 1.25 (half spread 0.4 bps)
- 2026-10-07 22:22Z sell AVAX 2,381 @ 11.0025 fee 2.38 slip 1.19 (half spread 0.9 bps)

## challenger4: relative_reversion (H6)

params: {"entry_z": 2.0, "exit_z": 0.25, "max_weight": 0.25, "ratio_hours": 720, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,969.27 (started 10,000 at 2026-10-13 17:26Z), net -0.31% since start
- 24h -1.98%, 7d -0.31%, 30d -0.31%, max drawdown -4.99%
- fills 13 total, 13 in the last 7d
- costs 24.22 (fees 16.15 + slippage 8.07); gross pnl -6.51; cost coverage -0.27
- cash -0.00; positions: ADA 6863.3, AVAX 86.9342, DOGE 20854.4, ETH 0.817638, SOL 19.0822, XRP 1519.34
- last run 2026-10-22 07:10Z; halted today: False

last decisions (newest last):

- 2026-10-22 06:10Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: ratio to BTC z -1.43 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-22 06:10Z ADA hold target 0.17 (held 0.15) — hold: weight change +0.017 below threshold 0.05 | stay long: ratio to BTC z -1.93 vs 720h mean (entry -2.0, exit -0.25); vol 65% -> weigh...
- 2026-10-22 06:10Z AVAX none target 0.17 (held 0.08) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-22 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.25 not below -2.0
- 2026-10-22 06:10Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.037 below threshold 0.05 | stay long: ratio to BTC z -1.10 vs 720h mean (entry -2.0, exit -0.25); vol 52% -> weigh...
- 2026-10-22 06:10Z DOGE hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.57 vs 720h mean (entry -2.0, exit -0.25); vol 57% -> weigh...
- 2026-10-22 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.96 not below -2.0
- 2026-10-22 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.13 not below -2.0
- 2026-10-22 07:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-22 07:10Z ETH hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: ratio to BTC z -1.33 vs 720h mean (entry -2.0, exit -0.25); vol 48% -> weigh...
- 2026-10-22 07:10Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: ratio to BTC z -1.43 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-22 07:10Z ADA hold target 0.17 (held 0.15) — hold: weight change +0.017 below threshold 0.05 | stay long: ratio to BTC z -1.88 vs 720h mean (entry -2.0, exit -0.25); vol 65% -> weigh...
- 2026-10-22 07:10Z AVAX none target 0.17 (held 0.08) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-22 07:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.21 not below -2.0
- 2026-10-22 07:10Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.037 below threshold 0.05 | stay long: ratio to BTC z -1.06 vs 720h mean (entry -2.0, exit -0.25); vol 51% -> weigh...
- 2026-10-22 07:10Z DOGE hold target 0.17 (held 0.17) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.52 vs 720h mean (entry -2.0, exit -0.25); vol 57% -> weigh...
- 2026-10-22 07:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.05 not below -2.0
- 2026-10-22 07:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.10 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -8.62, -115 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 1 fill (1 buy / 0 sell), traded 834, gross pnl -21.73, -521 bps per round trip, avg half spread 1.6 bps, open 86.9342
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -77.60, -476 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 2 fills (1 buy / 1 sell), traded 1,597, gross pnl +75.58, +947 bps per round trip, avg half spread 2.0 bps
- ETH: 2 fills (1 buy / 1 sell), traded 2,992, gross pnl -19.28, -129 bps per round trip, avg half spread 0.0 bps, open 0.817638
- SOL: 2 fills (1 buy / 1 sell), traded 2,976, gross pnl +8.38, +56 bps per round trip, avg half spread 0.5 bps, open 19.0822
- XRP: 2 fills (1 buy / 1 sell), traded 2,984, gross pnl +36.76, +246 bps per round trip, avg half spread 0.9 bps, open 1519.34

last fills:

- 2026-10-17 22:10Z sell XRP 494 @ 1.28916 fee 0.49 slip 0.25 (half spread 1.8 bps)
- 2026-10-17 22:10Z buy ADA 1,009 @ 0.218646 fee 1.01 slip 0.50 (half spread 2.2 bps)
- 2026-10-18 06:10Z sell ETH 494 @ 2407.93 fee 0.49 slip 0.25 (half spread 0.0 bps)
- 2026-10-18 06:10Z buy ADA 493 @ 0.219297 fee 0.49 slip 0.25 (half spread 1.0 bps)
- 2026-10-18 20:10Z sell DOGE 763 @ 0.0763131 fee 0.76 slip 0.38 (half spread 0.3 bps)
- 2026-10-18 20:10Z buy DOT 761 @ 1.05068 fee 0.76 slip 0.38 (half spread 1.4 bps)
- 2026-10-19 16:10Z sell DOT 836 @ 1.15392 fee 0.84 slip 0.42 (half spread 2.6 bps)
- 2026-10-19 16:10Z buy AVAX 834 @ 9.5953 fee 0.83 slip 0.42 (half spread 1.6 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1588 candles, 2026-08-17 03:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1588 candles, 2026-08-17 03:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1588 candles, 2026-08-17 03:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1588 candles, 2026-08-17 03:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- AVAX: live 1588 candles, 2026-08-17 03:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- LINK: live 1588 candles, 2026-08-17 03:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- XRP: live 1560 candles, 2026-08-18 07:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1560 candles, 2026-08-18 07:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.2 bps
- DOT: live 1560 candles, 2026-08-18 07:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LTC: live 1560 candles, 2026-08-18 07:00Z to 2026-10-22 06:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.2 bps
