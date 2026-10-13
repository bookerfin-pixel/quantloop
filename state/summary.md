# quantloop summary — generated 2026-10-13 12:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-06 (today and the 7 UTC days before it): the cap stopped a buy in 3 hours, on 1 pair day; a pair filled 4 times or more in one UTC day on 1 pair day (the cap is 4 fills in one pair in one UTC day)
- champion, AVAX, 2026-10-07: 4 fills (buy 02:24, sell 03:25, buy 08:28, sell 10:27); a buy stopped by the cap in 3 hours (14:27, 17:26, 18:29), each an entry from flat
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 27.3 of 60, 32.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +1.84% (max drawdown -18.60%, 242 fills) vs challenger1 -2.88% (max drawdown -9.09%, 59 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.24% (usual 0.54, this window 0.63) vs challenger1 -8.45% (usual 0.37, this window 0.28); the rule compares on skill, daily edge t -0.24 over 27 days
  trades: its 18 finished trades made -0.25% of its starting equity after costs (11 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.40 over 27 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +9.78%, equal weight basket of 10 pairs +15.02%, basket max drawdown -14%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 22.2 of 60, 37.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -11.37% (max drawdown -18.60%, 204 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.77% (usual 0.54, this window 0.62) vs challenger2 -0.88% (usual 0.29, this window 0.16); the rule compares on skill, daily edge t +1.07 over 22 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.30 over 22 days)
  fills: 4 in 22.2 days; at this pace about 21 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +0.87%, equal weight basket of 10 pairs -2.96%, basket max drawdown -14%, basket realised vol 58% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 7.6 of 60, 52.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -8.35% (max drawdown -8.76%, 53 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.22% (usual 0.55, this window 0.40) vs challenger3 -1.01% (usual 0.03, this window 0.04); the rule compares on skill, daily edge t +0.76 over 8 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  fills: 10 in 7.6 days, 8 of them in the hour it began; at this pace about 23 by day 60, under the 30 a promotion there needs, and about 39 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.11%, equal weight basket of 10 pairs -9.35%, basket max drawdown -14%, basket realised vol 61% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 17.6 of 60, 42.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -16.70% (max drawdown -18.60%, 176 fills) vs challenger4 -14.80% (max drawdown -16.26%, 44 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.10% (usual 0.55, this window 0.57) vs challenger4 -10.81% (usual 0.48, this window 0.84); the rule compares on skill, daily edge t +0.21 over 18 days
  trades: its 15 finished trades made -13.74% of its starting equity after costs (0 won, 15 lost, 8 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -2.35 over 18 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -0.76%, equal weight basket of 10 pairs -8.39%, basket max drawdown -14%, basket realised vol 57% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3, H4 in challenger4), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,183.87 (started 10,000 at 2026-09-16 03:55Z), net +1.84% since start
- 24h -3.91%, 7d -8.58%, 30d +1.84%, max drawdown -18.60%
- fills 242 total, 49 in the last 7d
- costs 555.64 (fees 368.37 + slippage 187.27); gross pnl 739.51; cost coverage 1.33
- cash 2,561.86; positions: BTC 0.030713, ETH 1.01751, LINK 197.162
- last run 2026-10-13 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-13 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.89% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.60% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.13% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 11:10Z LINK hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return -0.33% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-13 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.29% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 11:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.53% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.15% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.06% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.55% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-13 12:10Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.10% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-13 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.39% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.80% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.30% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z LINK hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return -0.74% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-13 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.33% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.78% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.12% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.83% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 23 fills (10 buy / 13 sell), traded 32,622, gross pnl +2.68, +2 bps per round trip, avg half spread 2.2 bps
- AVAX: 33 fills (15 buy / 18 sell), traded 57,758, gross pnl +447.02, +155 bps per round trip, avg half spread 1.2 bps
- BTC: 21 fills (11 buy / 10 sell), traded 30,368, gross pnl +73.62, +48 bps per round trip, avg half spread 0.1 bps, open 0.030713
- DOGE: 23 fills (12 buy / 11 sell), traded 30,681, gross pnl -208.37, -136 bps per round trip, avg half spread 1.0 bps
- DOT: 27 fills (13 buy / 14 sell), traded 35,702, gross pnl +123.63, +69 bps per round trip, avg half spread 2.3 bps
- ETH: 21 fills (10 buy / 11 sell), traded 32,798, gross pnl -128.19, -78 bps per round trip, avg half spread 0.1 bps, open 1.01751
- LINK: 26 fills (12 buy / 14 sell), traded 46,316, gross pnl -189.96, -82 bps per round trip, avg half spread 2.1 bps, open 197.162
- LTC: 25 fills (11 buy / 14 sell), traded 36,923, gross pnl +523.66, +284 bps per round trip, avg half spread 1.8 bps
- SOL: 23 fills (12 buy / 11 sell), traded 36,631, gross pnl -9.75, -5 bps per round trip, avg half spread 0.5 bps
- XRP: 20 fills (10 buy / 10 sell), traded 28,575, gross pnl +105.18, +74 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-12 17:10Z sell DOT 1,718 @ 1.21804 fee 1.72 slip 0.86 (half spread 1.2 bps)
- 2026-10-12 17:10Z buy BTC 852 @ 82532.1 fee 0.85 slip 0.43 (half spread 0.0 bps)
- 2026-10-12 17:10Z buy ETH 858 @ 2515.22 fee 0.86 slip 0.43 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell ETH 2,537 @ 2457.8 fee 2.54 slip 1.27 (half spread 0.0 bps)
- 2026-10-13 01:10Z sell BTC 2,568 @ 81615.4 fee 2.57 slip 1.28 (half spread 0.0 bps)
- 2026-10-13 05:10Z buy LINK 2,570 @ 13.0362 fee 2.57 slip 1.28 (half spread 0.0 bps)
- 2026-10-13 06:10Z buy ETH 2,572 @ 2527.96 fee 2.57 slip 1.29 (half spread 0.0 bps)
- 2026-10-13 07:10Z buy BTC 2,569 @ 83644.1 fee 2.57 slip 1.28 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,701.03 (started 10,000 at 2026-09-16 03:55Z), net -2.99% since start
- 24h -1.77%, 7d -6.70%, 30d -2.99%, max drawdown -9.09%
- fills 59 total, 49 in the last 7d
- costs 128.95 (fees 85.88 + slippage 43.07); gross pnl -170.02; cost coverage -1.32
- cash 1,420.08; positions: ADA 5922, AVAX 135.761, DOGE 16645.1, LTC 22.3568, SOL 13.0958, XRP 1018.86
- last run 2026-10-13 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-13 11:10Z SOL hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.56 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 11:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.025 below threshold 0.05 | stay long: z -1.56 vs 240h mean (entry -2.0, exit -0.5); vol 95% -> weight 0.25
- 2026-10-13 11:10Z AVAX hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.35 vs 240h mean (entry -2.0, exit -0.5); vol 95% -> weight 0.25
- 2026-10-13 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.02 not below -2.0
- 2026-10-13 11:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.43 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 11:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -1.27 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-10-13 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.35 not below -2.0
- 2026-10-13 11:10Z LTC hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.68 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-10-13 12:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.43 not below -2.0
- 2026-10-13 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.93 not below -2.0
- 2026-10-13 12:10Z SOL hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -1.61 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 12:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.025 below threshold 0.05 | stay long: z -1.58 vs 240h mean (entry -2.0, exit -0.5); vol 94% -> weight 0.25
- 2026-10-13 12:10Z AVAX hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.35 vs 240h mean (entry -2.0, exit -0.5); vol 94% -> weight 0.25
- 2026-10-13 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.05 not below -2.0
- 2026-10-13 12:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.46 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 12:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.30 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-10-13 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.38 not below -2.0
- 2026-10-13 12:10Z LTC hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.75 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (2 buy / 1 sell), traded 6,485, gross pnl +150.87, +465 bps per round trip, avg half spread 2.3 bps, open 5922
- AVAX: 3 fills (2 buy / 1 sell), traded 3,863, gross pnl +124.81, +646 bps per round trip, avg half spread 0.7 bps, open 135.761
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 9 fills (5 buy / 4 sell), traded 13,747, gross pnl -111.00, -161 bps per round trip, avg half spread 0.3 bps, open 16645.1
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 9 fills (4 buy / 5 sell), traded 14,136, gross pnl +8.34, +12 bps per round trip, avg half spread 0.2 bps
- LINK: 6 fills (3 buy / 3 sell), traded 7,237, gross pnl +61.02, +169 bps per round trip, avg half spread 1.2 bps
- LTC: 6 fills (4 buy / 2 sell), traded 7,571, gross pnl +3.39, +9 bps per round trip, avg half spread 1.3 bps, open 22.3568
- SOL: 8 fills (5 buy / 3 sell), traded 11,777, gross pnl -129.35, -220 bps per round trip, avg half spread 0.5 bps, open 13.0958
- XRP: 8 fills (4 buy / 4 sell), traded 8,558, gross pnl -222.92, -521 bps per round trip, avg half spread 0.3 bps, open 1018.86

last fills:

- 2026-10-13 01:10Z sell SOL 952 @ 103.543 fee 0.95 slip 0.48 (half spread 0.5 bps)
- 2026-10-13 01:10Z sell XRP 1,002 @ 1.33086 fee 1.00 slip 0.50 (half spread 0.0 bps)
- 2026-10-13 01:10Z sell DOGE 974 @ 0.0814635 fee 0.97 slip 0.49 (half spread 0.5 bps)
- 2026-10-13 01:10Z buy ADA 1,357 @ 0.229169 fee 1.36 slip 0.68 (half spread 2.4 bps)
- 2026-10-13 01:10Z buy AVAX 1,357 @ 9.9965 fee 1.36 slip 0.68 (half spread 0.5 bps)
- 2026-10-13 01:10Z buy LINK 1,357 @ 12.4903 fee 1.36 slip 0.68 (half spread 2.2 bps)
- 2026-10-13 01:10Z buy LTC 1,349 @ 60.3302 fee 1.35 slip 0.67 (half spread 1.7 bps)
- 2026-10-13 06:10Z sell LINK 1,422 @ 13.0827 fee 1.42 slip 0.71 (half spread 0.5 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h +0.00%, 7d -1.63%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-13 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-13 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 106.4 not above 120h high 114.3
- 2026-10-13 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.86 not above 120h high 13.47
- 2026-10-13 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.359 not above 120h high 1.424
- 2026-10-13 11:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 60.96 not above 120h high 65.77
- 2026-10-13 12:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.325e+04 not above 120h high 8.413e+04
- 2026-10-13 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 106.1 not above 120h high 113.1
- 2026-10-13 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.84 not above 120h high 13.47
- 2026-10-13 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.356 not above 120h high 1.424
- 2026-10-13 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 60.67 not above 120h high 65.77

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 5 fills (3 buy / 2 sell), traded 10,806, gross pnl -58.08, -108 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)
- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)
- 2026-09-30 13:27Z buy BTC 2,737 @ 85327.3 fee 2.74 slip 1.37 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell BTC 2,689 @ 83812.2 fee 2.69 slip 1.34 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell ETH 2,611 @ 2609.08 fee 2.61 slip 1.31 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d -1.27%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 2 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-13 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-13 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 102.8 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-13 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-13 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-13 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-13 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.319 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-13 11:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08091 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-13 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-13 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 59.58 not a higher low vs prior low 59.46 (need +10.0%)
- 2026-10-13 12:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.067e+04 not a higher low vs prior low 8.263e+04 (need +10.0%)
- 2026-10-13 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2415 not a higher low vs prior low 2640 (need +10.0%)
- 2026-10-13 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 102.8 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-13 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-13 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-13 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-13 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.319 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-13 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08091 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-13 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-13 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 59.58 not a higher low vs prior low 59.46 (need +10.0%)

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

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,735.62 (started 10,000 at 2026-09-25 04:23Z), net -12.64% since start
- 24h -5.46%, 7d -15.85%, 30d -12.58%, max drawdown -16.26%
- fills 57 total, 34 in the last 7d
- costs 113.52 (fees 75.44 + slippage 38.08); gross pnl -1,150.86; cost coverage -10.14
- cash 4,408.44; positions: BTC 0.0264162, DOT 1817.88
- last run 2026-10-13 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-13 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.41% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 11:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.40% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 11:10Z DOT hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +17.66% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-13 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 12:10Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +8.47% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-13 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.69% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.99% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -0.12% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 12:10Z DOT hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 720h return +16.47% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-13 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (4 buy / 5 sell), traded 12,190, gross pnl -275.47, -452 bps per round trip, avg half spread 2.1 bps
- AVAX: 6 fills (4 buy / 2 sell), traded 8,290, gross pnl -237.69, -573 bps per round trip, avg half spread 0.8 bps
- BTC: 7 fills (5 buy / 2 sell), traded 10,675, gross pnl -101.90, -191 bps per round trip, avg half spread 0.0 bps, open 0.0264162
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 8 fills (4 buy / 4 sell), traded 10,855, gross pnl -126.05, -232 bps per round trip, avg half spread 1.8 bps, open 1817.88
- ETH: 4 fills (3 buy / 1 sell), traded 4,849, gross pnl -68.19, -281 bps per round trip, avg half spread 0.0 bps
- LINK: 6 fills (2 buy / 4 sell), traded 8,682, gross pnl -39.59, -91 bps per round trip, avg half spread 1.6 bps
- LTC: 5 fills (2 buy / 3 sell), traded 6,271, gross pnl -87.08, -278 bps per round trip, avg half spread 1.7 bps
- SOL: 5 fills (3 buy / 2 sell), traded 4,625, gross pnl -80.22, -347 bps per round trip, avg half spread 0.4 bps
- XRP: 5 fills (2 buy / 3 sell), traded 7,043, gross pnl -34.06, -97 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-11 16:10Z buy LINK 1,863 @ 13.3274 fee 1.86 slip 0.93 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell BTC 1,827 @ 81832.2 fee 1.83 slip 0.91 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell ADA 1,721 @ 0.234702 fee 1.72 slip 1.04 (half spread 4.1 bps)
- 2026-10-12 23:10Z sell AVAX 1,754 @ 10.2089 fee 1.75 slip 0.88 (half spread 1.0 bps)
- 2026-10-12 23:10Z sell LINK 1,776 @ 12.7071 fee 1.78 slip 0.89 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell DOT 1,757 @ 1.18351 fee 1.76 slip 0.88 (half spread 2.5 bps)
- 2026-10-13 05:10Z buy BTC 2,206 @ 83524.9 fee 2.21 slip 1.10 (half spread 0.0 bps)
- 2026-10-13 07:10Z buy DOT 2,206 @ 1.21371 fee 2.21 slip 1.10 (half spread 1.6 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1377 candles, 2026-08-17 03:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1377 candles, 2026-08-17 03:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1377 candles, 2026-08-17 03:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1377 candles, 2026-08-17 03:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- AVAX: live 1377 candles, 2026-08-17 03:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- LINK: live 1377 candles, 2026-08-17 03:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1349 candles, 2026-08-18 07:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1349 candles, 2026-08-18 07:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- DOT: live 1349 candles, 2026-08-18 07:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1349 candles, 2026-08-18 07:00Z to 2026-10-13 11:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.1 bps
