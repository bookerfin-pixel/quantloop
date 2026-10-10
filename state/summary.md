# quantloop summary — generated 2026-10-10 04:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 142 of the last 168 (2 of them replayed after a missed run)
- 26 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-03 (today and the 7 UTC days before it): the cap stopped a buy in 3 hours, on 1 pair day; a pair filled 4 times or more in one UTC day on 3 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, AVAX, 2026-10-07: 4 fills (buy 02:24, sell 03:25, buy 08:28, sell 10:27); a buy stopped by the cap in 3 hours (14:27, 17:26, 18:29), each an entry from flat
- champion, DOT, 2026-10-05: 4 fills (sell 05:28, buy 19:00, sell 20:00, sell 21:32); no buy stopped
- champion, LTC, 2026-10-05: 4 fills (buy 05:28, sell 16:27, buy 18:30, sell 21:32); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it runs the champion's config. The champion's lines from before a promotion or a revert are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 24.0 of 60, 36.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +6.82% (max drawdown -15.47%, 209 fills) vs challenger1 -2.34% (max drawdown -7.73%, 38 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.18% (usual 0.54, this window 0.65) vs challenger1 -9.23% (usual 0.37, this window 0.19); the rule compares on skill, daily edge t -0.53 over 24 days
  trades: its 12 finished trades made -3.56% of its starting equity after costs (5 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.66 over 24 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +8.81%, equal weight basket of 10 pairs +18.58%, basket max drawdown -14%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 18.8 of 60, 41.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.04% (max drawdown -15.47%, 171 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.04% (usual 0.54, this window 0.63) vs challenger2 -1.73% (usual 0.29, this window 0.19); the rule compares on skill, daily edge t +0.68 over 19 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.63 over 19 days)
  fills: 4 in 18.8 days; at this pace about 25 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -0.01%, equal weight basket of 10 pairs +0.01%, basket max drawdown -14%, basket realised vol 59% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 4.2 of 60, 55.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -3.87% (max drawdown -5.25%, 20 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -0.22% (usual 0.55, this window 0.30) vs challenger3 -1.08% (usual 0.03, this window 0.07); the rule compares on skill, daily edge t -0.31 over 4 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -3.96%, equal weight basket of 10 pairs -6.64%, basket max drawdown -14%, basket realised vol 64% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 14.2 of 60, 45.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -12.62% (max drawdown -15.47%, 143 fills) vs challenger4 -9.11% (max drawdown -11.46%, 32 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.53% (usual 0.55, this window 0.58) vs challenger4 -6.42% (usual 0.48, this window 0.89); the rule compares on skill, daily edge t +0.44 over 14 days
  trades: its 10 finished trades made -9.65% of its starting equity after costs (0 won, 10 lost, 3 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.47 over 14 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -1.63%, equal weight basket of 10 pairs -5.64%, basket max drawdown -14%, basket realised vol 57% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,681.70 (started 10,000 at 2026-09-16 03:55Z), net +6.82% since start
- 24h +1.00%, 7d -2.25%, 30d +6.82%, max drawdown -15.47%
- fills 209 total, 55 in the last 7d
- costs 484.51 (fees 320.95 + slippage 163.56); gross pnl 1,166.21; cost coverage 2.41
- cash 7,929.53; positions: DOT 2177.69
- last run 2026-10-10 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-10 03:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.14% not above entry band +1.0%
- 2026-10-10 03:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.13% not above entry band +1.0%
- 2026-10-10 03:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.12% not above entry band +1.0%
- 2026-10-10 03:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.40% not above entry band +1.0%
- 2026-10-10 03:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.80% not above entry band +1.0%
- 2026-10-10 03:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.85% not above entry band +1.0%
- 2026-10-10 03:24Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.009 below threshold 0.05 | stay long: 72h return +13.63% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-10-10 03:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.88% not above entry band +1.0%
- 2026-10-10 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.91% not above entry band +1.0%
- 2026-10-10 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.66% not above entry band +1.0% and price below 24h EMA
- 2026-10-10 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.30% not above entry band +1.0% and price below 24h EMA
- 2026-10-10 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-10-10 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.91% not above entry band +1.0%
- 2026-10-10 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.93% not above entry band +1.0% and price below 24h EMA
- 2026-10-10 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.26% not above entry band +1.0%
- 2026-10-10 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.34% not above entry band +1.0%
- 2026-10-10 04:10Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +12.84% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-10-10 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.40% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (9 buy / 12 sell), traded 30,528, gross pnl +54.04, +35 bps per round trip, avg half spread 2.2 bps
- AVAX: 30 fills (13 buy / 17 sell), traded 54,282, gross pnl +498.76, +184 bps per round trip, avg half spread 1.2 bps
- BTC: 15 fills (7 buy / 8 sell), traded 19,440, gross pnl +105.45, +108 bps per round trip, avg half spread 0.2 bps
- DOGE: 20 fills (10 buy / 10 sell), traded 27,173, gross pnl -175.84, -129 bps per round trip, avg half spread 1.1 bps
- DOT: 24 fills (12 buy / 12 sell), traded 31,622, gross pnl +178.21, +113 bps per round trip, avg half spread 2.5 bps, open 2177.69
- ETH: 16 fills (6 buy / 10 sell), traded 25,082, gross pnl -30.95, -25 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 22 fills (9 buy / 13 sell), traded 33,431, gross pnl +545.56, +326 bps per round trip, avg half spread 1.8 bps
- SOL: 21 fills (11 buy / 10 sell), traded 34,513, gross pnl +17.41, +10 bps per round trip, avg half spread 0.5 bps
- XRP: 18 fills (9 buy / 9 sell), traded 26,463, gross pnl +138.10, +104 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-07 02:24Z buy XRP 1,310 @ 1.4578 fee 1.31 slip 0.65 (half spread 0.2 bps)
- 2026-10-07 03:25Z sell BTC 2,663 @ 84007.1 fee 2.66 slip 1.33 (half spread 0.0 bps)
- 2026-10-07 03:25Z sell SOL 2,671 @ 118.276 fee 2.67 slip 1.34 (half spread 0.4 bps)
- 2026-10-07 03:25Z sell AVAX 2,630 @ 10.985 fee 2.63 slip 1.32 (half spread 0.5 bps)
- 2026-10-07 03:25Z sell XRP 2,656 @ 1.46281 fee 2.66 slip 1.33 (half spread 0.0 bps)
- 2026-10-07 08:28Z buy AVAX 2,652 @ 11.2336 fee 2.65 slip 1.33 (half spread 0.9 bps)
- 2026-10-07 10:27Z sell AVAX 2,625 @ 11.1159 fee 2.62 slip 1.31 (half spread 1.3 bps)
- 2026-10-09 22:25Z buy DOT 2,644 @ 1.21416 fee 2.64 slip 1.32 (half spread 1.2 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,755.43 (started 10,000 at 2026-09-16 03:55Z), net -2.45% since start
- 24h +0.34%, 7d -5.63%, 30d -2.45%, max drawdown -7.73%
- fills 38 total, 29 in the last 7d
- costs 94.59 (fees 62.97 + slippage 31.62); gross pnl -149.99; cost coverage -1.59
- cash -0.00; positions: AVAX 119.636, BTC 0.0147423, DOGE 14318.8, ETH 0.486166, LINK 94.6674, LTC 18.9301, SOL 11.0391, XRP 869.779
- last run 2026-10-10 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-10 03:24Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.01 vs 240h mean (entry -2.0, exit -0.5); vol 48% -> weight 0.25
- 2026-10-10 03:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.07 not below -2.0
- 2026-10-10 03:24Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.003 below threshold 0.05 | stay long: z -1.42 vs 240h mean (entry -2.0, exit -0.5); vol 81% -> weight 0.25
- 2026-10-10 03:24Z LINK hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.69 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-10 03:24Z XRP hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.38 vs 240h mean (entry -2.0, exit -0.5); vol 52% -> weight 0.25
- 2026-10-10 03:24Z DOGE hold target 0.12 (held 0.13) — hold: weight change -0.002 below threshold 0.05 | stay long: z -1.38 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-10 03:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.97 not below -2.0
- 2026-10-10 03:24Z LTC hold target 0.12 (held 0.12) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.63 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-10 04:10Z BTC hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.32 vs 240h mean (entry -2.0, exit -0.5); vol 31% -> weight 0.25
- 2026-10-10 04:10Z ETH hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.82 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-10 04:10Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.04 vs 240h mean (entry -2.0, exit -0.5); vol 48% -> weight 0.25
- 2026-10-10 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.10 not below -2.0
- 2026-10-10 04:10Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.003 below threshold 0.05 | stay long: z -1.54 vs 240h mean (entry -2.0, exit -0.5); vol 81% -> weight 0.25
- 2026-10-10 04:10Z LINK hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.72 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-10 04:10Z XRP hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.44 vs 240h mean (entry -2.0, exit -0.5); vol 52% -> weight 0.25
- 2026-10-10 04:10Z DOGE hold target 0.12 (held 0.13) — hold: weight change -0.002 below threshold 0.05 | stay long: z -1.46 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-10 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.74 not below -2.0
- 2026-10-10 04:10Z LTC hold target 0.12 (held 0.12) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.70 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- AVAX: 1 fill (1 buy / 0 sell), traded 1,206, gross pnl +39.96, +663 bps per round trip, avg half spread 1.0 bps, open 119.636
- BTC: 3 fills (2 buy / 1 sell), traded 6,233, gross pnl +63.78, +205 bps per round trip, avg half spread 0.0 bps, open 0.0147423
- DOGE: 6 fills (3 buy / 3 sell), traded 11,524, gross pnl +10.16, +18 bps per round trip, avg half spread 0.2 bps, open 14318.8
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 7 fills (3 buy / 4 sell), traded 11,354, gross pnl -39.48, -70 bps per round trip, avg half spread 0.3 bps, open 0.486166
- LINK: 3 fills (2 buy / 1 sell), traded 3,198, gross pnl -53.27, -333 bps per round trip, avg half spread 1.4 bps, open 94.6674
- LTC: 3 fills (2 buy / 1 sell), traded 3,448, gross pnl -56.26, -326 bps per round trip, avg half spread 1.3 bps, open 18.9301
- SOL: 5 fills (3 buy / 2 sell), traded 9,566, gross pnl -0.85, -2 bps per round trip, avg half spread 0.5 bps, open 11.0391
- XRP: 5 fills (2 buy / 3 sell), traded 6,277, gross pnl -109.22, -348 bps per round trip, avg half spread 0.5 bps, open 869.779

last fills:

- 2026-10-09 00:37Z buy BTC 1,206 @ 81776.6 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy ETH 1,206 @ 2479.75 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy SOL 1,206 @ 109.21 fee 1.21 slip 0.60 (half spread 0.5 bps)
- 2026-10-09 00:37Z buy AVAX 1,206 @ 10.077 fee 1.21 slip 0.60 (half spread 1.0 bps)
- 2026-10-09 00:37Z buy LINK 1,206 @ 12.7348 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy XRP 1,206 @ 1.38607 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy DOGE 1,206 @ 0.0841954 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy LTC 1,196 @ 63.1766 fee 1.20 slip 0.60 (half spread 0.8 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h +0.00%, 7d -0.88%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-10 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-10 03:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 109.8 not above 120h high 121.7
- 2026-10-10 03:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 03:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 03:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.83 not above 120h high 14.25
- 2026-10-10 03:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.406 not above 120h high 1.523
- 2026-10-10 03:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.08659 not above 120h high 0.09674
- 2026-10-10 03:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 03:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.252e+04 not above 120h high 8.66e+04
- 2026-10-10 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2489 not above 120h high 2725
- 2026-10-10 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 109.6 not above 120h high 121.7
- 2026-10-10 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.8 not above 120h high 14.25
- 2026-10-10 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.403 not above 120h high 1.523
- 2026-10-10 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.08622 not above 120h high 0.09674
- 2026-10-10 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-10 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- 24h +0.00%, 7d -1.13%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 26 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-10 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-10 03:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 107.7 (need +10.0%)
- 2026-10-10 03:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2191 (need +10.0%)
- 2026-10-10 03:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 9.517 (need +10.0%)
- 2026-10-10 03:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 11.95 (need +10.0%)
- 2026-10-10 03:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.37 (need +10.0%)
- 2026-10-10 03:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.08471 (need +10.0%)
- 2026-10-10 03:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.075 (need +10.0%)
- 2026-10-10 03:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 56.67 (need +10.0%)
- 2026-10-10 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.067e+04 not a higher low vs prior low 8.023e+04 (need +10.0%)
- 2026-10-10 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2415 not a higher low vs prior low 2571 (need +10.0%)
- 2026-10-10 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 108 (need +10.0%)
- 2026-10-10 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2191 (need +10.0%)
- 2026-10-10 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 9.562 (need +10.0%)
- 2026-10-10 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 11.95 (need +10.0%)
- 2026-10-10 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.376 (need +10.0%)
- 2026-10-10 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.08471 (need +10.0%)
- 2026-10-10 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.081 (need +10.0%)
- 2026-10-10 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 56.68 (need +10.0%)

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

- equity 9,319.87 (started 10,000 at 2026-09-25 04:23Z), net -6.80% since start
- 24h +0.81%, 7d -7.07%, 30d -6.73%, max drawdown -11.46%
- fills 45 total, 22 in the last 7d
- costs 83.52 (fees 55.56 + slippage 27.95); gross pnl -596.61; cost coverage -7.14
- cash 4,581.41; positions: ADA 9193.07, DOT 1923.9
- last run 2026-10-10 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-10 03:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 03:24Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +18.51% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-10 03:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 03:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 03:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.02% not above entry band +5.0% and price below 168h EMA
- 2026-10-10 03:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.69% not above entry band +5.0% and price below 168h EMA
- 2026-10-10 03:24Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.012 below threshold 0.05 | stay long: 720h return +14.47% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-10 03:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.58% not above entry band +5.0% and price below 168h EMA
- 2026-10-10 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 04:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +17.23% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-10 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-10 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.85% not above entry band +5.0% and price below 168h EMA
- 2026-10-10 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.30% not above entry band +5.0% and price below 168h EMA
- 2026-10-10 04:10Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.011 below threshold 0.05 | stay long: 720h return +14.38% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-10 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 7 fills (4 buy / 3 sell), traded 9,995, gross pnl -164.68, -330 bps per round trip, avg half spread 1.9 bps, open 9193.07
- AVAX: 4 fills (3 buy / 1 sell), traded 4,667, gross pnl -123.70, -530 bps per round trip, avg half spread 0.8 bps
- BTC: 4 fills (3 buy / 1 sell), traded 4,772, gross pnl -53.58, -225 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 5 fills (3 buy / 2 sell), traded 6,339, gross pnl +70.23, +222 bps per round trip, avg half spread 2.0 bps, open 1923.9
- ETH: 4 fills (3 buy / 1 sell), traded 4,849, gross pnl -68.19, -281 bps per round trip, avg half spread 0.0 bps
- LINK: 4 fills (1 buy / 3 sell), traded 5,043, gross pnl +45.28, +180 bps per round trip, avg half spread 2.4 bps
- LTC: 5 fills (2 buy / 3 sell), traded 6,271, gross pnl -87.08, -278 bps per round trip, avg half spread 1.7 bps
- SOL: 5 fills (3 buy / 2 sell), traded 4,625, gross pnl -80.22, -347 bps per round trip, avg half spread 0.4 bps
- XRP: 5 fills (2 buy / 3 sell), traded 7,043, gross pnl -34.06, -97 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-08 13:29Z buy ADA 809 @ 0.247799 fee 0.81 slip 0.40 (half spread 1.6 bps)
- 2026-10-08 13:29Z buy AVAX 799 @ 10.6048 fee 0.80 slip 0.40 (half spread 1.4 bps)
- 2026-10-08 14:29Z sell ETH 2,389 @ 2531.68 fee 2.39 slip 1.20 (half spread 0.0 bps)
- 2026-10-08 16:29Z sell BTC 2,358 @ 81224.3 fee 2.36 slip 1.18 (half spread 0.0 bps)
- 2026-10-08 16:29Z sell ADA 2,236 @ 0.231688 fee 2.24 slip 1.12 (half spread 1.1 bps)
- 2026-10-08 16:29Z sell AVAX 2,270 @ 10.089 fee 2.27 slip 1.14 (half spread 1.0 bps)
- 2026-10-09 17:23Z buy DOT 2,311 @ 1.20135 fee 2.31 slip 1.16 (half spread 2.1 bps)
- 2026-10-10 02:24Z buy ADA 2,348 @ 0.255383 fee 2.35 slip 1.17 (half spread 1.5 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1297 candles, 2026-08-17 03:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1297 candles, 2026-08-17 03:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1297 candles, 2026-08-17 03:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- ADA: live 1297 candles, 2026-08-17 03:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- AVAX: live 1297 candles, 2026-08-17 03:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- LINK: live 1297 candles, 2026-08-17 03:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1269 candles, 2026-08-18 07:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1269 candles, 2026-08-18 07:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.2 bps
- DOT: live 1269 candles, 2026-08-18 07:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.6 bps
- LTC: live 1269 candles, 2026-08-18 07:00Z to 2026-10-10 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.1 bps
