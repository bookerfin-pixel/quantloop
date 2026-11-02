# quantloop summary — generated 2026-11-02 00:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-26 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 6 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, BTC, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 16:10, sell 21:10); no buy stopped
- champion, DOGE, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 11:10, sell 21:10); no buy stopped
- champion, ETH, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 16:10, sell 21:10); no buy stopped
- champion, LINK, 2026-10-29: 5 fills (buy 02:10, sell 03:10, buy 11:10, buy 16:10, sell 21:10); no buy stopped
- champion, LTC, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 11:10, sell 21:10); no buy stopped
- champion, XRP, 2026-10-29: 4 fills (buy 02:10, sell 04:10, buy 16:10, sell 21:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 46.8 of 60, 13.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -14.09% (max drawdown -31.31%, 385 fills) vs challenger1 -7.69% (max drawdown -15.05%, 116 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.95% (usual 0.54, this window 0.50) vs challenger1 -8.28% (usual 0.37, this window 0.48); the rule compares on skill, daily edge t +0.45 over 47 days
  trades: its 36 finished trades made -2.99% of its starting equity after costs (22 won, 14 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.15 over 47 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +3.17%, equal weight basket of 10 pairs +1.59%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 41.7 of 60, 18.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -25.24% (max drawdown -31.31%, 347 fills) vs challenger2 -11.67% (max drawdown -12.10%, 26 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -17.64% (usual 0.54, this window 0.48) vs challenger2 -7.65% (usual 0.29, this window 0.16); the rule compares on skill, daily edge t +1.39 over 42 days
  trades: its 11 finished trades made -11.67% of its starting equity after costs (0 won, 11 lost, 4 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 4% that this is a real edge (every idea starts at 10%; the daily skill t is -1.48 over 42 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.20%, equal weight basket of 10 pairs -14.07%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 27.1 of 60, 32.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -22.69% (max drawdown -23.01%, 196 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.86% (usual 0.55, this window 0.35) vs challenger3 -0.72% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.40 over 27 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.65 over 27 days)
  fills: 10 in 27.1 days, 8 of them in the hour it began; at this pace about 16 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -8.95%, equal weight basket of 10 pairs -19.72%, basket max drawdown -23%, basket realised vol 56% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 17.0 of 120, 103.0 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -3.40% (max drawdown -12.71%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +1.96% (usual 0.53, this window 0.95); the rule compares on skill, daily edge t +0.38 over 17 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -14.83% so far
  trades: its 9 finished trades made -6.54% of its starting equity after costs (2 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 11% that this is a real edge (every idea starts at 10%; the daily skill t is +0.38 over 17 days)
  market over the window: BTC -4.96%, equal weight basket of 10 pairs -10.14%, basket max drawdown -15%, basket realised vol 52% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,590.53 (started 10,000 at 2026-09-16 03:55Z), net -14.09% since start
- 24h -0.69%, 7d -5.62%, 30d -22.00%, max drawdown -31.31%
- fills 385 total, 66 in the last 7d
- costs 861.97 (fees 571.01 + slippage 290.95); gross pnl -547.50; cost coverage -0.64
- cash -0.00; positions: ADA 7386.57, AVAX 165.392, DOT 1507.61, ETH 0.631081, LTC 25.6088, XRP 1149.17
- last run 2026-11-02 00:10Z; halted today: False

last decisions (newest last):

- 2026-11-01 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.42% not above entry band +1.0% and price below 24h EMA
- 2026-11-01 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.15% not above entry band +1.0% and price below 24h EMA
- 2026-11-01 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-11-01 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-11-01 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.02% not above entry band +1.0% and price below 24h EMA
- 2026-11-01 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.49% not above entry band +1.0% and price below 24h EMA
- 2026-11-01 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-11-01 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.54% not above entry band +1.0% and price below 24h EMA
- 2026-11-02 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.56% not above entry band +1.0%
- 2026-11-02 00:10Z ETH buy target 0.17 (held 0.00) — enter long: 72h return +1.04% vs entry band +1.0% and price above 24h EMA; realised vol 46% -> weight 0.25
- 2026-11-02 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.04% not above entry band +1.0% and price below 24h EMA
- 2026-11-02 00:10Z ADA buy target 0.17 (held 0.00) — enter long: 72h return +1.51% vs entry band +1.0% and price above 24h EMA; realised vol 71% -> weight 0.25
- 2026-11-02 00:10Z AVAX buy target 0.17 (held 0.00) — enter long: 72h return +5.09% vs entry band +1.0% and price above 24h EMA; realised vol 76% -> weight 0.25
- 2026-11-02 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-11-02 00:10Z XRP buy target 0.17 (held 0.00) — enter long: 72h return +1.18% vs entry band +1.0% and price above 24h EMA; realised vol 53% -> weight 0.25
- 2026-11-02 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.50% not above entry band +1.0%
- 2026-11-02 00:10Z DOT buy target 0.17 (held 0.00) — enter long: 72h return +4.80% vs entry band +1.0% and price above 24h EMA; realised vol 88% -> weight 0.25
- 2026-11-02 00:10Z LTC buy target 0.17 (held 0.00) — enter long: 72h return +1.35% vs entry band +1.0% and price above 24h EMA; realised vol 68% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 32 fills (15 buy / 17 sell), traded 42,711, gross pnl -90.33, -42 bps per round trip, avg half spread 2.1 bps, open 7386.57
- AVAX: 44 fills (21 buy / 23 sell), traded 74,493, gross pnl +282.00, +76 bps per round trip, avg half spread 1.2 bps, open 165.392
- BTC: 36 fills (20 buy / 16 sell), traded 50,945, gross pnl -35.30, -14 bps per round trip, avg half spread 0.1 bps
- DOGE: 34 fills (17 buy / 17 sell), traded 44,348, gross pnl -247.89, -112 bps per round trip, avg half spread 0.8 bps
- DOT: 40 fills (20 buy / 20 sell), traded 61,194, gross pnl -139.84, -46 bps per round trip, avg half spread 2.3 bps, open 1507.61
- ETH: 39 fills (20 buy / 19 sell), traded 54,274, gross pnl -231.91, -85 bps per round trip, avg half spread 0.1 bps, open 0.631081
- LINK: 47 fills (24 buy / 23 sell), traded 79,344, gross pnl -403.27, -102 bps per round trip, avg half spread 2.0 bps
- LTC: 41 fills (20 buy / 21 sell), traded 57,277, gross pnl +437.19, +153 bps per round trip, avg half spread 1.6 bps, open 25.6088
- SOL: 36 fills (19 buy / 17 sell), traded 57,028, gross pnl -95.11, -33 bps per round trip, avg half spread 0.5 bps
- XRP: 36 fills (19 buy / 17 sell), traded 49,401, gross pnl -23.04, -9 bps per round trip, avg half spread 0.4 bps, open 1149.17

last fills:

- 2026-11-01 15:01Z sell AVAX 2,134 @ 8.75112 fee 2.13 slip 1.07 (half spread 0.6 bps)
- 2026-11-01 15:01Z sell LINK 2,153 @ 11.5739 fee 2.15 slip 1.08 (half spread 1.6 bps)
- 2026-11-02 00:10Z buy ETH 1,434 @ 2272.17 fee 1.43 slip 0.72 (half spread 0.2 bps)
- 2026-11-02 00:10Z buy ADA 1,434 @ 0.194126 fee 1.43 slip 0.84 (half spread 3.9 bps)
- 2026-11-02 00:10Z buy AVAX 1,434 @ 8.66983 fee 1.43 slip 0.72 (half spread 1.7 bps)
- 2026-11-02 00:10Z buy XRP 1,434 @ 1.24779 fee 1.43 slip 0.72 (half spread 0.0 bps)
- 2026-11-02 00:10Z buy DOT 1,434 @ 0.951125 fee 1.43 slip 0.72 (half spread 0.5 bps)
- 2026-11-02 00:10Z buy LTC 1,425 @ 55.6578 fee 1.43 slip 0.71 (half spread 1.8 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,220.40 (started 10,000 at 2026-09-16 03:55Z), net -7.80% since start
- 24h +0.35%, 7d -1.76%, 30d -10.90%, max drawdown -15.05%
- fills 116 total, 27 in the last 7d
- costs 227.08 (fees 150.07 + slippage 77.01); gross pnl -552.52; cost coverage -2.43
- cash 2,120.33; positions: ADA 5280.14, BTC 0.0128711, DOGE 13261, DOT 1095.71, ETH 0.449834, SOL 10.5172, XRP 814.617
- last run 2026-11-02 00:10Z; halted today: False

last decisions (newest last):

- 2026-11-01 23:10Z SOL hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: z -2.00 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-11-01 23:10Z ADA hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: z -1.44 vs 240h mean (entry -2.0, exit -0.5); vol 70% -> weight 0.25
- 2026-11-01 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.79 not below -2.0
- 2026-11-01 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.81 not below -2.0
- 2026-11-01 23:10Z XRP hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: z -1.42 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-11-01 23:10Z DOGE hold target 0.14 (held 0.11) — hold: weight change +0.034 below threshold 0.05 | stay long: z -1.47 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-11-01 23:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.030 below threshold 0.05 | stay long: z -1.01 vs 240h mean (entry -2.0, exit -0.5); vol 88% -> weight 0.25
- 2026-11-01 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.32 not below -2.0
- 2026-11-02 00:10Z BTC hold target 0.14 (held 0.11) — hold: weight change +0.034 below threshold 0.05 | stay long: z -0.91 vs 240h mean (entry -2.0, exit -0.5); vol 38% -> weight 0.25
- 2026-11-02 00:10Z ETH hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: z -0.81 vs 240h mean (entry -2.0, exit -0.5); vol 46% -> weight 0.25
- 2026-11-02 00:10Z SOL hold target 0.14 (held 0.11) — hold: weight change +0.035 below threshold 0.05 | stay long: z -1.71 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-11-02 00:10Z ADA hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: z -1.21 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-11-02 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.48 not below -2.0
- 2026-11-02 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.51 not below -2.0
- 2026-11-02 00:10Z XRP hold target 0.14 (held 0.11) — hold: weight change +0.033 below threshold 0.05 | stay long: z -1.24 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-11-02 00:10Z DOGE hold target 0.14 (held 0.11) — hold: weight change +0.034 below threshold 0.05 | stay long: z -1.15 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-11-02 00:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.030 below threshold 0.05 | stay long: z -0.92 vs 240h mean (entry -2.0, exit -0.5); vol 88% -> weight 0.25
- 2026-11-02 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.92 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 10 fills (5 buy / 5 sell), traded 13,452, gross pnl -69.53, -103 bps per round trip, avg half spread 1.6 bps, open 5280.14
- AVAX: 14 fills (8 buy / 6 sell), traded 16,832, gross pnl +143.39, +170 bps per round trip, avg half spread 1.5 bps
- BTC: 8 fills (5 buy / 3 sell), traded 11,161, gross pnl +77.47, +139 bps per round trip, avg half spread 0.1 bps, open 0.0128711
- DOGE: 13 fills (7 buy / 6 sell), traded 18,828, gross pnl -136.16, -145 bps per round trip, avg half spread 0.5 bps, open 13261
- DOT: 8 fills (4 buy / 4 sell), traded 10,739, gross pnl -380.45, -709 bps per round trip, avg half spread 2.3 bps, open 1095.71
- ETH: 14 fills (7 buy / 7 sell), traded 20,243, gross pnl +113.64, +112 bps per round trip, avg half spread 0.4 bps, open 0.449834
- LINK: 14 fills (8 buy / 6 sell), traded 15,196, gross pnl +92.34, +122 bps per round trip, avg half spread 1.5 bps
- LTC: 12 fills (6 buy / 6 sell), traded 14,725, gross pnl +11.39, +15 bps per round trip, avg half spread 1.2 bps
- SOL: 13 fills (8 buy / 5 sell), traded 17,969, gross pnl -149.64, -167 bps per round trip, avg half spread 0.5 bps, open 10.5172
- XRP: 10 fills (5 buy / 5 sell), traded 10,928, gross pnl -254.98, -467 bps per round trip, avg half spread 0.8 bps, open 814.617

last fills:

- 2026-10-29 21:10Z buy ETH 1,018 @ 2262.1 fee 1.02 slip 0.51 (half spread 2.7 bps)
- 2026-10-29 21:10Z buy SOL 1,018 @ 96.7534 fee 1.02 slip 0.51 (half spread 0.5 bps)
- 2026-10-29 21:10Z buy AVAX 1,018 @ 8.45469 fee 1.02 slip 0.93 (half spread 7.1 bps)
- 2026-10-29 21:10Z buy LINK 1,018 @ 11.1368 fee 1.02 slip 0.67 (half spread 4.6 bps)
- 2026-10-29 21:10Z buy XRP 1,018 @ 1.24914 fee 1.02 slip 0.71 (half spread 5.0 bps)
- 2026-10-29 21:10Z buy DOGE 1,008 @ 0.0760162 fee 1.01 slip 0.59 (half spread 3.8 bps)
- 2026-10-31 01:10Z sell LINK 1,056 @ 11.5604 fee 1.06 slip 0.55 (half spread 3.2 bps)
- 2026-11-01 05:10Z sell AVAX 1,066 @ 8.85857 fee 1.07 slip 0.53 (half spread 2.3 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 9,686.16 (started 10,000 at 2026-09-16 23:20Z), net -3.14% since start
- 24h +0.00%, 7d -5.97%, 30d -10.88%, max drawdown -12.80%
- fills 58 total, 14 in the last 7d
- costs 166.60 (fees 110.15 + slippage 56.45); gross pnl -147.24; cost coverage -0.88
- cash 9,686.16; positions: none
- last run 2026-11-02 00:10Z; halted today: False

last decisions (newest last):

- 2026-11-01 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-01 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.1913 not above 120h high 0.2075
- 2026-11-01 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-01 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-01 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.244 not above 120h high 1.337
- 2026-11-01 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-01 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9467 not above 120h high 1.029
- 2026-11-01 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.1929 not above 120h high 0.2075
- 2026-11-02 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.249 not above 120h high 1.337
- 2026-11-02 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-02 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.952 not above 120h high 1.029
- 2026-11-02 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 10 fills (5 buy / 5 sell), traded 21,231, gross pnl -174.17, -164 bps per round trip, avg half spread 0.0 bps
- DOGE: 9 fills (5 buy / 4 sell), traded 14,280, gross pnl -214.67, -301 bps per round trip, avg half spread 1.0 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 5 fills (3 buy / 2 sell), traded 7,935, gross pnl -94.34, -238 bps per round trip, avg half spread 2.9 bps
- LTC: 6 fills (3 buy / 3 sell), traded 12,367, gross pnl -84.66, -137 bps per round trip, avg half spread 2.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 6 fills (3 buy / 3 sell), traded 11,524, gross pnl -217.79, -378 bps per round trip, avg half spread 0.1 bps

last fills:

- 2026-10-29 16:10Z buy LINK 1,086 @ 11.9832 fee 1.09 slip 0.54 (half spread 2.1 bps)
- 2026-10-29 19:10Z sell XRP 2,485 @ 1.28014 fee 2.48 slip 1.24 (half spread 0.0 bps)
- 2026-10-29 19:10Z buy LINK 1,458 @ 11.6425 fee 1.46 slip 0.73 (half spread 2.2 bps)
- 2026-10-29 19:10Z buy DOGE 509 @ 0.0791227 fee 0.51 slip 0.25 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell BTC 1,984 @ 78979.6 fee 1.98 slip 0.99 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell LINK 2,401 @ 11.1222 fee 2.40 slip 1.58 (half spread 4.6 bps)
- 2026-10-29 21:10Z sell DOGE 2,412 @ 0.0759279 fee 2.41 slip 1.40 (half spread 3.8 bps)
- 2026-10-29 21:10Z sell LTC 2,386 @ 55.3789 fee 2.39 slip 1.34 (half spread 3.6 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-02 00:10Z; halted today: False

last decisions (newest last):

- 2026-11-01 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 93.78 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-11-01 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1868 not a higher low vs prior low 0.2109 (need +10.0%)
- 2026-11-01 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 9.09 (need +10.0%)
- 2026-11-01 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-11-01 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-01 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07388 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-11-01 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-11-01 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 54.24 not a higher low vs prior low 56.77 (need +10.0%)
- 2026-11-02 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.65e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-11-02 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2335 (need +10.0%)
- 2026-11-02 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 93.59 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-11-02 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1868 not a higher low vs prior low 0.2109 (need +10.0%)
- 2026-11-02 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 9.09 (need +10.0%)
- 2026-11-02 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-11-02 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-02 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07388 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-11-02 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-11-02 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 54.24 not a higher low vs prior low 56.77 (need +10.0%)

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

- equity 9,656.61 (started 10,000 at 2026-10-13 17:26Z), net -3.43% since start
- 24h +0.54%, 7d +1.40%, 30d -3.43%, max drawdown -12.71%
- fills 30 total, 12 in the last 7d
- costs 62.94 (fees 40.22 + slippage 22.72); gross pnl -280.45; cost coverage -4.46
- cash 2,517.83; positions: ADA 12106.8, AVAX 276.724, DOT 2516.14
- last run 2026-11-02 00:10Z; halted today: False

last decisions (newest last):

- 2026-11-01 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.75 not below -2.0
- 2026-11-01 23:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.008 below threshold 0.05 | stay long: ratio to BTC z -1.49 vs 720h mean (entry -2.0, exit -0.25); vol 70% -> weigh...
- 2026-11-01 23:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.10 vs 720h mean (entry -2.0, exit -0.25); vol 75% -> weigh...
- 2026-11-01 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.87 not below -2.0
- 2026-11-01 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.86 not below -2.0
- 2026-11-01 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.92 not below -2.0
- 2026-11-01 23:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.68 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-01 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.97 not below -2.0
- 2026-11-02 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-02 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.94 not below -2.0
- 2026-11-02 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.70 not below -2.0
- 2026-11-02 00:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.007 below threshold 0.05 | stay long: ratio to BTC z -1.45 vs 720h mean (entry -2.0, exit -0.25); vol 71% -> weigh...
- 2026-11-02 00:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.07 vs 720h mean (entry -2.0, exit -0.25); vol 76% -> weigh...
- 2026-11-02 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.84 not below -2.0
- 2026-11-02 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.93 not below -2.0
- 2026-11-02 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.91 not below -2.0
- 2026-11-02 00:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.69 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-02 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.93 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (3 buy / 1 sell), traded 5,091, gross pnl -97.17, -382 bps per round trip, avg half spread 3.3 bps, open 12106.8
- AVAX: 4 fills (3 buy / 1 sell), traded 5,003, gross pnl +1.82, +7 bps per round trip, avg half spread 3.5 bps, open 276.724
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 5 fills (3 buy / 2 sell), traded 5,904, gross pnl +72.23, +245 bps per round trip, avg half spread 3.9 bps, open 2516.14
- ETH: 4 fills (1 buy / 3 sell), traded 4,854, gross pnl -141.72, -584 bps per round trip, avg half spread 1.1 bps
- LINK: 2 fills (1 buy / 1 sell), traded 4,797, gross pnl +245.83, +1025 bps per round trip, avg half spread 2.6 bps
- SOL: 4 fills (1 buy / 3 sell), traded 4,837, gross pnl -118.93, -492 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (1 buy / 3 sell), traded 4,888, gross pnl -91.04, -373 bps per round trip, avg half spread 1.7 bps

last fills:

- 2026-10-29 21:10Z sell XRP 1,331 @ 1.24739 fee 1.33 slip 0.93 (half spread 5.0 bps)
- 2026-10-29 21:10Z sell DOGE 1,583 @ 0.0759279 fee 1.58 slip 0.92 (half spread 3.8 bps)
- 2026-10-29 21:10Z sell DOT 954 @ 0.926415 fee 0.95 slip 1.07 (half spread 9.2 bps)
- 2026-10-30 00:10Z buy AVAX 2,277 @ 8.22864 fee 2.28 slip 1.15 (half spread 3.0 bps)
- 2026-10-30 00:10Z buy LINK 2,277 @ 10.5579 fee 2.28 slip 1.27 (half spread 3.6 bps)
- 2026-10-30 00:10Z buy DOT 2,277 @ 0.904981 fee 2.28 slip 1.34 (half spread 3.9 bps)
- 2026-10-30 01:10Z buy ADA 2,268 @ 0.187329 fee 2.27 slip 1.65 (half spread 5.3 bps)
- 2026-10-31 18:10Z sell LINK 2,520 @ 11.6859 fee 2.52 slip 1.26 (half spread 1.5 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1845 candles, 2026-08-17 03:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1845 candles, 2026-08-17 03:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1845 candles, 2026-08-17 03:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1845 candles, 2026-08-17 03:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 1845 candles, 2026-08-17 03:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LINK: live 1845 candles, 2026-08-17 03:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- XRP: live 1817 candles, 2026-08-18 07:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.3 bps
- DOGE: live 1817 candles, 2026-08-18 07:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 1817 candles, 2026-08-18 07:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1817 candles, 2026-08-18 07:00Z to 2026-11-01 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
