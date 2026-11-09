# quantloop summary — generated 2026-11-09 06:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-02 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 2 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, AVAX, 2026-11-02: 4 fills (buy 00:10, sell 02:10, buy 07:10, sell 18:10); no buy stopped
- champion, DOT, 2026-11-02: 4 fills (buy 00:10, sell 02:10, buy 07:10, sell 13:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 54.0 of 60, 6.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.39% (max drawdown -36.34%, 438 fills) vs challenger1 -8.57% (max drawdown -15.05%, 152 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -16.56% (usual 0.54, this window 0.49) vs challenger1 -5.94% (usual 0.37, this window 0.53); the rule compares on skill, daily edge t +0.70 over 54 days
  trades: its 45 finished trades made -4.42% of its starting equity after costs (28 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.69 over 54 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -1.92%, equal weight basket of 10 pairs -7.11%, basket max drawdown -28%, basket realised vol 57% annualised
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 34.3 of 60, 25.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -28.35% (max drawdown -28.65%, 249 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -13.77% (usual 0.55, this window 0.35) vs challenger3 -0.52% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.45 over 34 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.41 over 34 days)
  fills: 10 in 34.3 days, 8 of them in the hour it began; at this pace about 14 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -13.44%, equal weight basket of 10 pairs -26.55%, basket max drawdown -28%, basket realised vol 56% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 24.3 of 120, 95.7 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -10.93% (max drawdown -14.50%, 42 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -1.52% (usual 0.53, this window 0.85); the rule compares on skill, daily edge t -0.13 over 24 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -19.87% so far
  trades: its 13 finished trades made -8.65% of its starting equity after costs (2 won, 11 lost, 11 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.13 over 24 days)
  market over the window: BTC -9.65%, equal weight basket of 10 pairs -17.83%, basket max drawdown -20%, basket realised vol 54% annualised
- free slots: challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,961.12 (started 10,000 at 2026-09-16 03:55Z), net -20.39% since start
- 24h +0.00%, 7d -6.80%, 30d -25.28%, max drawdown -36.34%
- fills 438 total, 43 in the last 7d
- costs 948.23 (fees 627.38 + slippage 320.85); gross pnl -1,090.64; cost coverage -1.15
- cash 7,961.12; positions: none
- last run 2026-11-09 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-09 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.40% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.35% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.41% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.71% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.13% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.83% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.13% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.20% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.61% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.32% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.17% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.90% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.23% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.81% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.73% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.46% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.50% not above entry band +1.0% and price below 24h EMA
- 2026-11-09 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.24% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 36 fills (16 buy / 20 sell), traded 45,961, gross pnl -172.72, -75 bps per round trip, avg half spread 2.2 bps
- AVAX: 52 fills (24 buy / 28 sell), traded 85,193, gross pnl +92.15, +22 bps per round trip, avg half spread 1.5 bps
- BTC: 43 fills (24 buy / 19 sell), traded 60,178, gross pnl -158.33, -53 bps per round trip, avg half spread 0.1 bps
- DOGE: 39 fills (19 buy / 20 sell), traded 49,043, gross pnl -313.08, -128 bps per round trip, avg half spread 1.0 bps
- DOT: 47 fills (22 buy / 25 sell), traded 69,133, gross pnl -174.48, -50 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 49 fills (25 buy / 24 sell), traded 81,140, gross pnl -448.58, -111 bps per round trip, avg half spread 2.1 bps
- LTC: 45 fills (21 buy / 24 sell), traded 60,527, gross pnl +373.93, +124 bps per round trip, avg half spread 1.6 bps
- SOL: 40 fills (21 buy / 19 sell), traded 60,786, gross pnl -147.60, -49 bps per round trip, avg half spread 0.5 bps
- XRP: 43 fills (21 buy / 22 sell), traded 57,249, gross pnl -5.63, -2 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-11-05 15:10Z sell AVAX 889 @ 8.37432 fee 0.89 slip 0.66 (half spread 5.4 bps)
- 2026-11-05 15:10Z sell LINK 875 @ 10.9274 fee 0.87 slip 0.75 (half spread 6.6 bps)
- 2026-11-05 15:10Z sell DOGE 891 @ 0.0728598 fee 0.89 slip 0.45 (half spread 2.8 bps)
- 2026-11-05 15:10Z sell LTC 889 @ 53.1884 fee 0.89 slip 0.44 (half spread 2.8 bps)
- 2026-11-05 15:10Z buy BTC 1,100 @ 77074.5 fee 1.10 slip 0.55 (half spread 0.0 bps)
- 2026-11-05 15:10Z buy XRP 1,100 @ 1.26162 fee 1.10 slip 0.55 (half spread 2.3 bps)
- 2026-11-05 16:10Z sell BTC 1,975 @ 75762.1 fee 1.97 slip 0.99 (half spread 0.0 bps)
- 2026-11-05 16:10Z sell XRP 1,985 @ 1.24647 fee 1.98 slip 0.99 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,132.40 (started 10,000 at 2026-09-16 03:55Z), net -8.68% since start
- 24h -3.49%, 7d -0.61%, 30d -6.62%, max drawdown -15.05%
- fills 152 total, 29 in the last 7d
- costs 287.84 (fees 188.99 + slippage 98.85); gross pnl -579.76; cost coverage -2.01
- cash -0.00; positions: ADA 5226.63, AVAX 115.396, BTC 0.0122833, DOGE 13255.7, DOT 1063.05, ETH 0.430747, LINK 88.4303, LTC 18.2152, SOL 10.5703, XRP 813.358
- last run 2026-11-09 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-09 05:10Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.94 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-11-09 05:10Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: z -2.25 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-11-09 05:10Z AVAX hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.14 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-11-09 05:10Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.65 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-11-09 05:10Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: z -2.49 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-11-09 05:10Z DOGE hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.18 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-11-09 05:10Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.50 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-11-09 05:10Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.91 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25
- 2026-11-09 06:10Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.94 vs 240h mean (entry -2.0, exit -0.5); vol 41% -> weight 0.25
- 2026-11-09 06:10Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.31 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-11-09 06:10Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.18 vs 240h mean (entry -2.0, exit -0.5); vol 61% -> weight 0.25
- 2026-11-09 06:10Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: z -2.37 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-11-09 06:10Z AVAX hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: z -2.40 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-11-09 06:10Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: z -2.00 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-11-09 06:10Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: z -2.66 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-11-09 06:10Z DOGE hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.40 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-11-09 06:10Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.68 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-11-09 06:10Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: z -2.05 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 14 fills (7 buy / 7 sell), traded 17,768, gross pnl -95.79, -108 bps per round trip, avg half spread 2.2 bps, open 5226.63
- AVAX: 16 fills (9 buy / 7 sell), traded 19,041, gross pnl +79.78, +84 bps per round trip, avg half spread 1.6 bps, open 115.396
- BTC: 11 fills (7 buy / 4 sell), traded 14,145, gross pnl +79.19, +112 bps per round trip, avg half spread 0.1 bps, open 0.0122833
- DOGE: 17 fills (9 buy / 8 sell), traded 23,156, gross pnl -151.66, -131 bps per round trip, avg half spread 0.9 bps, open 13255.7
- DOT: 12 fills (6 buy / 6 sell), traded 14,947, gross pnl -461.94, -618 bps per round trip, avg half spread 3.2 bps, open 1063.05
- ETH: 16 fills (8 buy / 8 sell), traded 22,188, gross pnl +128.00, +115 bps per round trip, avg half spread 0.4 bps, open 0.430747
- LINK: 19 fills (11 buy / 8 sell), traded 21,160, gross pnl +169.04, +160 bps per round trip, avg half spread 2.1 bps, open 88.4303
- LTC: 17 fills (9 buy / 8 sell), traded 20,048, gross pnl +23.27, +23 bps per round trip, avg half spread 1.4 bps, open 18.2152
- SOL: 17 fills (11 buy / 6 sell), traded 22,622, gross pnl -112.08, -99 bps per round trip, avg half spread 0.6 bps, open 10.5703
- XRP: 13 fills (7 buy / 6 sell), traded 13,921, gross pnl -237.56, -341 bps per round trip, avg half spread 0.8 bps, open 813.358

last fills:

- 2026-11-08 22:10Z sell LINK 617 @ 10.3154 fee 0.62 slip 0.43 (half spread 4.9 bps)
- 2026-11-08 22:10Z sell DOGE 612 @ 0.0688335 fee 0.61 slip 0.33 (half spread 3.3 bps)
- 2026-11-08 22:10Z sell DOT 596 @ 0.857728 fee 0.60 slip 0.57 (half spread 7.6 bps)
- 2026-11-08 22:10Z sell LTC 609 @ 50.0949 fee 0.61 slip 0.30 (half spread 2.0 bps)
- 2026-11-08 22:10Z buy BTC 913 @ 74349.1 fee 0.91 slip 0.46 (half spread 0.0 bps)
- 2026-11-08 22:10Z buy ETH 913 @ 2120.15 fee 0.91 slip 0.46 (half spread 1.4 bps)
- 2026-11-08 22:10Z buy SOL 913 @ 86.3982 fee 0.91 slip 0.46 (half spread 1.7 bps)
- 2026-11-08 22:10Z buy XRP 906 @ 1.11384 fee 0.91 slip 0.45 (half spread 2.0 bps)

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-09 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-09 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-09 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-09 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-09 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 85.87 not a higher low vs prior low 93.78 (need +10.0%)
- 2026-11-09 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1726 not a higher low vs prior low 0.1868 (need +10.0%)
- 2026-11-09 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.841 not a higher low vs prior low 8.186 (need +10.0%)
- 2026-11-09 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.2 not a higher low vs prior low 10.49 (need +10.0%)
- 2026-11-09 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.109 not a higher low vs prior low 1.207 (need +10.0%)
- 2026-11-09 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.06829 not a higher low vs prior low 0.07388 (need +10.0%)
- 2026-11-09 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8546 not a higher low vs prior low 0.8971 (need +10.0%)
- 2026-11-09 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 49.8 not a higher low vs prior low 54.24 (need +10.0%)
- 2026-11-09 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.409e+04 not a higher low vs prior low 7.664e+04 (need +10.0%)
- 2026-11-09 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2124 not a higher low vs prior low 2191 (need +10.0%)
- 2026-11-09 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 85.87 not a higher low vs prior low 93.78 (need +10.0%)
- 2026-11-09 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1726 not a higher low vs prior low 0.1868 (need +10.0%)
- 2026-11-09 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.841 not a higher low vs prior low 8.186 (need +10.0%)
- 2026-11-09 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.2 not a higher low vs prior low 10.49 (need +10.0%)
- 2026-11-09 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.105 not a higher low vs prior low 1.207 (need +10.0%)
- 2026-11-09 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.06829 not a higher low vs prior low 0.07388 (need +10.0%)
- 2026-11-09 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8546 not a higher low vs prior low 0.8971 (need +10.0%)
- 2026-11-09 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 49.8 not a higher low vs prior low 54.24 (need +10.0%)

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

- equity 8,903.46 (started 10,000 at 2026-10-13 17:26Z), net -10.97% since start
- 24h -2.02%, 7d -7.18%, 30d -10.97%, max drawdown -14.50%
- fills 42 total, 12 in the last 7d
- costs 97.82 (fees 62.42 + slippage 35.40); gross pnl -998.72; cost coverage -10.21
- cash -0.00; positions: DOGE 25813.1, ETH 0.466071, LTC 35.5795, SOL 25.4938, XRP 1943.04
- last run 2026-11-09 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-09 05:10Z SOL hold target 0.20 (held 0.25) — hold: weight change -0.048 below threshold 0.05 | stay long: ratio to BTC z -2.03 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-11-09 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.56 not below -2.0
- 2026-11-09 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.26 not below -2.0
- 2026-11-09 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.17 not below -2.0
- 2026-11-09 05:10Z XRP hold target 0.20 (held 0.24) — hold: weight change -0.040 below threshold 0.05 | stay long: ratio to BTC z -3.74 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-11-09 05:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.90 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-11-09 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.54 not below -2.0
- 2026-11-09 05:10Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.76 vs 720h mean (entry -2.0, exit -0.25); vol 63% -> weigh...
- 2026-11-09 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-09 06:10Z ETH none target 0.20 (held 0.11) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-11-09 06:10Z SOL hold target 0.20 (held 0.25) — hold: weight change -0.048 below threshold 0.05 | stay long: ratio to BTC z -2.14 vs 720h mean (entry -2.0, exit -0.25); vol 61% -> weigh...
- 2026-11-09 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.57 not below -2.0
- 2026-11-09 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.33 not below -2.0
- 2026-11-09 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.39 not below -2.0
- 2026-11-09 06:10Z XRP hold target 0.20 (held 0.24) — hold: weight change -0.039 below threshold 0.05 | stay long: ratio to BTC z -3.96 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-11-09 06:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -2.03 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-11-09 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.57 not below -2.0
- 2026-11-09 06:10Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.79 vs 720h mean (entry -2.0, exit -0.25); vol 63% -> weigh...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 5 fills (2 buy / 3 sell), traded 7,535, gross pnl -142.22, -378 bps per round trip, avg half spread 1.9 bps, open 25813.1
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 5 fills (2 buy / 3 sell), traded 5,853, gross pnl -148.27, -507 bps per round trip, avg half spread 0.9 bps, open 0.466071
- LINK: 2 fills (1 buy / 1 sell), traded 4,797, gross pnl +245.83, +1025 bps per round trip, avg half spread 2.6 bps
- LTC: 2 fills (1 buy / 1 sell), traded 2,682, gross pnl +17.93, +134 bps per round trip, avg half spread 1.5 bps, open 35.5795
- SOL: 7 fills (3 buy / 4 sell), traded 11,735, gross pnl -215.91, -368 bps per round trip, avg half spread 0.9 bps, open 25.4938
- XRP: 5 fills (2 buy / 3 sell), traded 7,173, gross pnl -247.97, -691 bps per round trip, avg half spread 1.4 bps, open 1943.04

last fills:

- 2026-11-05 23:10Z sell DOT 2,257 @ 0.89712 fee 2.26 slip 1.96 (half spread 6.7 bps)
- 2026-11-06 00:10Z buy SOL 2,284 @ 89.5798 fee 2.28 slip 1.14 (half spread 0.6 bps)
- 2026-11-06 21:10Z buy XRP 2,285 @ 1.17624 fee 2.29 slip 1.14 (half spread 0.0 bps)
- 2026-11-08 22:10Z buy DOGE 2,231 @ 0.0689068 fee 2.23 slip 1.19 (half spread 3.3 bps)
- 2026-11-08 22:10Z buy LTC 2,231 @ 50.1451 fee 2.23 slip 1.12 (half spread 2.0 bps)
- 2026-11-08 23:10Z sell DOGE 457 @ 0.0695648 fee 0.46 slip 0.23 (half spread 2.0 bps)
- 2026-11-08 23:10Z sell LTC 450 @ 50.4698 fee 0.45 slip 0.23 (half spread 1.0 bps)
- 2026-11-08 23:10Z buy ETH 999 @ 2143.75 fee 1.00 slip 0.50 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 2019 candles, 2026-08-17 03:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 2019 candles, 2026-08-17 03:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 2019 candles, 2026-08-17 03:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 2019 candles, 2026-08-17 03:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- AVAX: live 2019 candles, 2026-08-17 03:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- LINK: live 2019 candles, 2026-08-17 03:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- XRP: live 1991 candles, 2026-08-18 07:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1991 candles, 2026-08-18 07:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- DOT: live 1991 candles, 2026-08-18 07:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.6 bps
- LTC: live 1991 candles, 2026-08-18 07:00Z to 2026-11-09 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
