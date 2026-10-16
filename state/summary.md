# quantloop summary — generated 2026-10-16 16:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-09 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 1 pair day (the cap is 4 fills in one pair in one UTC day)
- champion, DOT, 2026-10-16: 4 fills (buy 01:10, buy 02:10, sell 04:10, buy 15:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 30.5 of 60, 29.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -0.31% (max drawdown -20.29%, 266 fills) vs challenger1 -4.32% (max drawdown -11.24%, 64 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.82% (usual 0.54, this window 0.59) vs challenger1 -8.82% (usual 0.37, this window 0.35); the rule compares on skill, daily edge t -0.19 over 30 days
  trades: its 20 finished trades made +0.63% of its starting equity after costs (13 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.34 over 30 days)
  two look rule (measured, not applied to this test): on today's numbers it would be kept at day 60 on the value of its trades without passing the rule, the same as under its own rule. From there the two rules are one: 60 more days, and a promotion asks for a daily skill t of 1.0 over all 120 (its daily skill t is -1.34 so far)
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be kept on value at day 60, the same as against the champion
  market over the window: BTC +7.13%, equal weight basket of 10 pairs +12.11%, basket max drawdown -16%, basket realised vol 59% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 25.3 of 60, 34.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.24% (max drawdown -20.29%, 228 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.29% (usual 0.54, this window 0.57) vs challenger2 -0.17% (usual 0.29, this window 0.14); the rule compares on skill, daily edge t +1.27 over 25 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.09 over 25 days)
  fills: 4 in 25.3 days; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -1.56%, equal weight basket of 10 pairs -5.46%, basket max drawdown -16%, basket realised vol 59% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 10.7 of 60, 49.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -10.28% (max drawdown -10.66%, 77 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.87% (usual 0.55, this window 0.36) vs challenger3 -0.94% (usual 0.03, this window 0.03); the rule compares on skill, daily edge t +1.03 over 11 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.92 over 11 days)
  fills: 10 in 10.7 days, 8 of them in the hour it began; at this pace about 19 by day 60, under the 30 a promotion there needs, and about 30 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.45%, equal weight basket of 10 pairs -11.68%, basket max drawdown -16%, basket realised vol 61% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 0.7 of 120, 119.3 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -0.37% (max drawdown -0.95%, 3 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +0.25% (usual 0.53, this window 0.49); the rule compares on skill
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -2.19% so far
  trades: it has finished no trade of its own: none of its 3 fills closed a position it had bought or had chosen to keep, so the -0.37% it shows is not from an exit it chose. A test that has finished no trade of its own by its look is killed
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  market over the window: BTC -1.31%, equal weight basket of 10 pairs -1.16%, basket max drawdown -2%, basket realised vol 43% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,969.41 (started 10,000 at 2026-09-16 03:55Z), net -0.31% since start
- 24h -1.01%, 7d -5.74%, 30d -0.31%, max drawdown -20.29%
- fills 266 total, 58 in the last 7d
- costs 621.95 (fees 412.13 + slippage 209.82); gross pnl 591.36; cost coverage 0.95
- cash 7,478.23; positions: DOT 2113.14
- last run 2026-10-16 16:10Z; halted today: False

last decisions (newest last):

- 2026-10-16 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.75% not above entry band +1.0%
- 2026-10-16 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.66% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.01% not above entry band +1.0%
- 2026-10-16 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.61% not above entry band +1.0%
- 2026-10-16 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.31% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.68% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 15:10Z DOT buy target 0.25 (held 0.00) — enter long: 72h return +1.17% vs entry band +1.0% and price above 24h EMA; realised vol 97% -> weight 0.25
- 2026-10-16 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.00% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.51% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.40% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.38% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.10% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.20% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.43% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.51% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.54% not above entry band +1.0% and price below 24h EMA
- 2026-10-16 16:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.27% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-16 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.77% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 25 fills (11 buy / 14 sell), traded 35,491, gross pnl -4.51, -3 bps per round trip, avg half spread 2.1 bps
- AVAX: 35 fills (16 buy / 19 sell), traded 60,625, gross pnl +437.92, +144 bps per round trip, avg half spread 1.1 bps
- BTC: 25 fills (13 buy / 12 sell), traded 37,898, gross pnl +24.20, +13 bps per round trip, avg half spread 0.1 bps
- DOGE: 23 fills (12 buy / 11 sell), traded 30,681, gross pnl -208.37, -136 bps per round trip, avg half spread 1.0 bps
- DOT: 31 fills (16 buy / 15 sell), traded 43,151, gross pnl +91.67, +42 bps per round trip, avg half spread 2.5 bps, open 2113.14
- ETH: 22 fills (10 buy / 12 sell), traded 35,319, gross pnl -146.87, -83 bps per round trip, avg half spread 0.1 bps
- LINK: 29 fills (13 buy / 16 sell), traded 53,932, gross pnl -216.41, -80 bps per round trip, avg half spread 2.0 bps
- LTC: 28 fills (13 buy / 15 sell), traded 41,924, gross pnl +515.74, +246 bps per round trip, avg half spread 1.7 bps
- SOL: 26 fills (14 buy / 12 sell), traded 41,663, gross pnl -3.65, -2 bps per round trip, avg half spread 0.5 bps
- XRP: 22 fills (11 buy / 11 sell), traded 31,447, gross pnl +101.64, +65 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-16 02:10Z buy SOL 1,075 @ 105.198 fee 1.08 slip 0.54 (half spread 0.5 bps)
- 2026-10-16 02:10Z buy DOT 1,056 @ 1.16538 fee 1.06 slip 0.53 (half spread 1.7 bps)
- 2026-10-16 02:10Z buy LTC 1,077 @ 60.9154 fee 1.08 slip 0.54 (half spread 0.8 bps)
- 2026-10-16 03:10Z sell BTC 2,510 @ 82028.3 fee 2.51 slip 1.26 (half spread 0.0 bps)
- 2026-10-16 03:10Z sell SOL 2,518 @ 105.502 fee 2.52 slip 1.26 (half spread 0.5 bps)
- 2026-10-16 04:10Z sell DOT 2,461 @ 1.14227 fee 2.46 slip 1.35 (half spread 3.5 bps)
- 2026-10-16 04:10Z sell LTC 2,496 @ 60.8096 fee 2.50 slip 1.25 (half spread 1.6 bps)
- 2026-10-16 15:10Z buy DOT 2,494 @ 1.18004 fee 2.49 slip 1.77 (half spread 5.1 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,556.87 (started 10,000 at 2026-09-16 03:55Z), net -4.43% since start
- 24h -0.53%, 7d -1.34%, 30d -3.74%, max drawdown -11.24%
- fills 64 total, 26 in the last 7d
- costs 136.69 (fees 91.04 + slippage 45.65); gross pnl -306.44; cost coverage -2.24
- cash 1,489.75; positions: ADA 5922, DOGE 16645.1, LINK 110.29, LTC 22.3568, SOL 13.0958, XRP 1018.86
- last run 2026-10-16 16:10Z; halted today: False

last decisions (newest last):

- 2026-10-16 15:10Z SOL hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -0.94 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-16 15:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.028 below threshold 0.05 | stay long: z -1.25 vs 240h mean (entry -2.0, exit -0.5); vol 81% -> weight 0.25
- 2026-10-16 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.37 not below -2.0
- 2026-10-16 15:10Z LINK hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -0.96 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-16 15:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.33 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-16 15:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.23 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-10-16 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.41 not below -2.0
- 2026-10-16 15:10Z LTC hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.02 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-16 16:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.61 not below -2.0
- 2026-10-16 16:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.13 not below -2.0
- 2026-10-16 16:10Z SOL hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.36 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-10-16 16:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.53 vs 240h mean (entry -2.0, exit -0.5); vol 81% -> weight 0.25
- 2026-10-16 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.81 not below -2.0
- 2026-10-16 16:10Z LINK hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.45 vs 240h mean (entry -2.0, exit -0.5); vol 69% -> weight 0.25
- 2026-10-16 16:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.77 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-16 16:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.58 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-16 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.04 not below -2.0
- 2026-10-16 16:10Z LTC hold target 0.17 (held 0.14) — hold: weight change +0.026 below threshold 0.05 | stay long: z -1.27 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (2 buy / 1 sell), traded 6,485, gross pnl +104.75, +323 bps per round trip, avg half spread 2.3 bps, open 5922
- AVAX: 4 fills (2 buy / 2 sell), traded 5,263, gross pnl +140.49, +534 bps per round trip, avg half spread 0.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 9 fills (5 buy / 4 sell), traded 13,747, gross pnl -160.37, -233 bps per round trip, avg half spread 0.3 bps, open 16645.1
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 11 fills (5 buy / 6 sell), traded 16,518, gross pnl +59.49, +72 bps per round trip, avg half spread 0.2 bps
- LINK: 8 fills (5 buy / 3 sell), traded 8,612, gross pnl +48.03, +112 bps per round trip, avg half spread 1.2 bps, open 110.29
- LTC: 6 fills (4 buy / 2 sell), traded 7,571, gross pnl -12.60, -33 bps per round trip, avg half spread 1.3 bps, open 22.3568
- SOL: 8 fills (5 buy / 3 sell), traded 11,777, gross pnl -157.77, -268 bps per round trip, avg half spread 0.5 bps, open 13.0958
- XRP: 8 fills (4 buy / 4 sell), traded 8,558, gross pnl -273.29, -639 bps per round trip, avg half spread 0.3 bps, open 1018.86

last fills:

- 2026-10-13 01:10Z buy LINK 1,357 @ 12.4903 fee 1.36 slip 0.68 (half spread 2.2 bps)
- 2026-10-13 01:10Z buy LTC 1,349 @ 60.3302 fee 1.35 slip 0.67 (half spread 1.7 bps)
- 2026-10-13 06:10Z sell LINK 1,422 @ 13.0827 fee 1.42 slip 0.71 (half spread 0.5 bps)
- 2026-10-15 04:10Z buy ETH 1,166 @ 2364.79 fee 1.17 slip 0.58 (half spread 0.3 bps)
- 2026-10-15 04:10Z buy LINK 253 @ 12.0834 fee 0.25 slip 0.13 (half spread 1.1 bps)
- 2026-10-16 10:10Z sell AVAX 1,400 @ 10.3113 fee 1.40 slip 0.70 (half spread 0.5 bps)
- 2026-10-16 10:10Z buy LINK 1,122 @ 12.5572 fee 1.12 slip 0.56 (half spread 1.5 bps)
- 2026-10-16 12:10Z sell ETH 1,216 @ 2466.12 fee 1.22 slip 0.61 (half spread 0.0 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h +0.00%, 7d +0.00%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 0 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-16 16:10Z; halted today: False

last decisions (newest last):

- 2026-10-16 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.327 not above 120h high 1.424
- 2026-10-16 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.08137 not above 120h high 0.08785
- 2026-10-16 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.125e+04 not above 120h high 8.413e+04
- 2026-10-16 16:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.307 not above 120h high 1.424
- 2026-10-16 16:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.08029 not above 120h high 0.08785
- 2026-10-16 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-16 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-16 16:10Z; halted today: False

last decisions (newest last):

- 2026-10-16 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 101.3 not a higher low vs prior low 116.9 (need +10.0%)
- 2026-10-16 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2187 not a higher low vs prior low 0.2392 (need +10.0%)
- 2026-10-16 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.496 not a higher low vs prior low 10.23 (need +10.0%)
- 2026-10-16 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.88 not a higher low vs prior low 13.56 (need +10.0%)
- 2026-10-16 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.287 not a higher low vs prior low 1.464 (need +10.0%)
- 2026-10-16 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07826 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-16 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.142 (need +10.0%)
- 2026-10-16 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 57.36 not a higher low vs prior low 66.15 (need +10.0%)
- 2026-10-16 16:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.011e+04 not a higher low vs prior low 8.263e+04 (need +10.0%)
- 2026-10-16 16:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2338 not a higher low vs prior low 2640 (need +10.0%)
- 2026-10-16 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 101.3 not a higher low vs prior low 116.9 (need +10.0%)
- 2026-10-16 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2187 not a higher low vs prior low 0.2392 (need +10.0%)
- 2026-10-16 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.496 not a higher low vs prior low 10.23 (need +10.0%)
- 2026-10-16 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.88 not a higher low vs prior low 13.56 (need +10.0%)
- 2026-10-16 16:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.287 not a higher low vs prior low 1.464 (need +10.0%)
- 2026-10-16 16:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07826 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-16 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.142 (need +10.0%)
- 2026-10-16 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 57.36 not a higher low vs prior low 66.15 (need +10.0%)

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

- equity 9,959.69 (started 10,000 at 2026-10-13 17:26Z), net -0.40% since start
- 24h -0.40%, 7d -0.40%, 30d -0.40%, max drawdown -0.95%
- fills 3 total, 3 in the last 7d
- costs 11.23 (fees 7.49 + slippage 3.74); gross pnl -29.07; cost coverage -2.59
- cash 2,502.79; positions: DOGE 30847, ETH 1.02263, XRP 1902.23
- last run 2026-10-16 16:10Z; halted today: False

last decisions (newest last):

- 2026-10-16 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.62 not below -2.0
- 2026-10-16 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.01 not below -2.0
- 2026-10-16 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.09 not below -2.0
- 2026-10-16 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.70 not below -2.0
- 2026-10-16 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.93 not below -2.0
- 2026-10-16 15:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.87 vs 720h mean (entry -2.0, exit -0.25); vol 58% -> weigh...
- 2026-10-16 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +1.00 not below -2.0
- 2026-10-16 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.70 not below -2.0
- 2026-10-16 16:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-16 16:10Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.70 vs 720h mean (entry -2.0, exit -0.25); vol 47% -> weigh...
- 2026-10-16 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.90 not below -2.0
- 2026-10-16 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.18 not below -2.0
- 2026-10-16 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.07 not below -2.0
- 2026-10-16 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.88 not below -2.0
- 2026-10-16 16:10Z XRP buy target 0.25 (held 0.00) — enter long: ratio to BTC z -2.12 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weight 0.25
- 2026-10-16 16:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.98 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-10-16 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.59 not below -2.0
- 2026-10-16 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.75 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- DOGE: 1 fill (1 buy / 0 sell), traded 2,500, gross pnl -17.51, -140 bps per round trip, avg half spread 0.0 bps, open 30847
- ETH: 1 fill (1 buy / 0 sell), traded 2,499, gross pnl -11.57, -93 bps per round trip, avg half spread 0.0 bps, open 1.02263
- XRP: 1 fill (1 buy / 0 sell), traded 2,491, gross pnl -0.00, -0 bps per round trip, avg half spread 0.0 bps, open 1902.23

last fills:

- 2026-10-15 23:10Z buy DOGE 2,500 @ 0.081045 fee 2.50 slip 1.25 (half spread 0.0 bps)
- 2026-10-16 00:10Z buy ETH 2,499 @ 2443.58 fee 2.50 slip 1.25 (half spread 0.0 bps)
- 2026-10-16 16:10Z buy XRP 2,491 @ 1.30944 fee 2.49 slip 1.24 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1453 candles, 2026-08-17 03:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1453 candles, 2026-08-17 03:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1453 candles, 2026-08-17 03:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1453 candles, 2026-08-17 03:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- AVAX: live 1453 candles, 2026-08-17 03:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- LINK: live 1453 candles, 2026-08-17 03:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1425 candles, 2026-08-18 07:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1425 candles, 2026-08-18 07:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.2 bps
- DOT: live 1425 candles, 2026-08-18 07:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LTC: live 1425 candles, 2026-08-18 07:00Z to 2026-10-16 15:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.1 bps
