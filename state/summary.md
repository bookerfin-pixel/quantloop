# quantloop summary — generated 2026-11-08 03:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-01 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 2 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, AVAX, 2026-11-02: 4 fills (buy 00:10, sell 02:10, buy 07:10, sell 18:10); no buy stopped
- champion, DOT, 2026-11-02: 4 fills (buy 00:10, sell 02:10, buy 07:10, sell 13:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 52.9 of 60, 7.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.39% (max drawdown -36.34%, 438 fills) vs challenger1 -5.16% (max drawdown -15.05%, 142 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -18.22% (usual 0.54, this window 0.50) vs challenger1 -3.67% (usual 0.37, this window 0.52); the rule compares on skill, daily edge t +0.97 over 53 days
  trades: its 45 finished trades made -4.42% of its starting equity after costs (28 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.43 over 53 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -0.21%, equal weight basket of 10 pairs -4.02%, basket max drawdown -25%, basket realised vol 56% annualised
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 33.2 of 60, 26.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -28.35% (max drawdown -28.65%, 249 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -15.13% (usual 0.55, this window 0.37) vs challenger3 -0.59% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.89 over 33 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.49 over 33 days)
  fills: 10 in 33.2 days, 8 of them in the hour it began; at this pace about 15 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -11.93%, equal weight basket of 10 pairs -24.09%, basket max drawdown -25%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 23.2 of 120, 96.8 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -9.11% (max drawdown -12.99%, 37 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -1.15% (usual 0.53, this window 0.86); the rule compares on skill, daily edge t -0.09 over 23 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -16.66% so far
  trades: its 13 finished trades made -8.65% of its starting equity after costs (2 won, 11 lost, 11 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.09 over 23 days)
  market over the window: BTC -8.07%, equal weight basket of 10 pairs -15.07%, basket max drawdown -17%, basket realised vol 52% annualised
- free slots: challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,961.12 (started 10,000 at 2026-09-16 03:55Z), net -20.39% since start
- 24h +0.00%, 7d -7.62%, 30d -24.73%, max drawdown -36.34%
- fills 438 total, 62 in the last 7d
- costs 948.23 (fees 627.38 + slippage 320.85); gross pnl -1,090.64; cost coverage -1.15
- cash 7,961.12; positions: none
- last run 2026-11-08 03:10Z; halted today: False

last decisions (newest last):

- 2026-11-08 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.29% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.74% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.58% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.08% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.42% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.56% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.63% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.40% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.99% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.99% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.56% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.31% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.34% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.30% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.39% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.86% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.40% not above entry band +1.0% and price below 24h EMA
- 2026-11-08 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.55% not above entry band +1.0% and price below 24h EMA

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

- equity 9,473.43 (started 10,000 at 2026-09-16 03:55Z), net -5.27% since start
- 24h -0.86%, 7d +3.30%, 30d -2.47%, max drawdown -15.05%
- fills 142 total, 27 in the last 7d
- costs 276.38 (fees 181.70 + slippage 94.69); gross pnl -250.19; cost coverage -0.91
- cash -0.00; positions: ADA 8685.54, AVAX 193.232, DOGE 22140, DOT 1758.45, LINK 148.244, LTC 30.3681
- last run 2026-11-08 03:10Z; halted today: False

last decisions (newest last):

- 2026-11-08 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.59 not below -2.0
- 2026-11-08 02:10Z ADA hold target 0.14 (held 0.17) — hold: weight change -0.022 below threshold 0.05 | stay long: z -2.06 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-11-08 02:10Z AVAX hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -1.69 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25
- 2026-11-08 02:10Z LINK hold target 0.14 (held 0.17) — hold: weight change -0.026 below threshold 0.05 | stay long: z -1.34 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25
- 2026-11-08 02:10Z XRP none target 0.14 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-11-08 02:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -1.80 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-11-08 02:10Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -2.11 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-11-08 02:10Z LTC hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -1.58 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-11-08 03:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.26 not below -2.0
- 2026-11-08 03:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.76 not below -2.0
- 2026-11-08 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.58 not below -2.0
- 2026-11-08 03:10Z ADA hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -2.03 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-11-08 03:10Z AVAX hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -1.70 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25
- 2026-11-08 03:10Z LINK hold target 0.14 (held 0.17) — hold: weight change -0.026 below threshold 0.05 | stay long: z -1.33 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25
- 2026-11-08 03:10Z XRP none target 0.14 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-11-08 03:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -1.85 vs 240h mean (entry -2.0, exit -0.5); vol 52% -> weight 0.25
- 2026-11-08 03:10Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -2.11 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-11-08 03:10Z LTC hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -1.58 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 13 fills (7 buy / 6 sell), traded 17,164, gross pnl -43.93, -51 bps per round trip, avg half spread 2.0 bps, open 8685.54
- AVAX: 15 fills (9 buy / 6 sell), traded 18,425, gross pnl +132.28, +144 bps per round trip, avg half spread 1.4 bps, open 193.232
- BTC: 10 fills (6 buy / 4 sell), traded 13,232, gross pnl +77.24, +117 bps per round trip, avg half spread 0.1 bps
- DOGE: 16 fills (9 buy / 7 sell), traded 22,544, gross pnl -101.60, -90 bps per round trip, avg half spread 0.7 bps, open 22140
- DOT: 11 fills (6 buy / 5 sell), traded 14,350, gross pnl -407.98, -569 bps per round trip, avg half spread 2.8 bps, open 1758.45
- ETH: 15 fills (7 buy / 8 sell), traded 21,275, gross pnl +123.89, +116 bps per round trip, avg half spread 0.3 bps
- LINK: 18 fills (11 buy / 7 sell), traded 20,543, gross pnl +229.19, +223 bps per round trip, avg half spread 1.9 bps, open 148.244
- LTC: 16 fills (9 buy / 7 sell), traded 19,439, gross pnl +76.38, +79 bps per round trip, avg half spread 1.3 bps, open 30.3681
- SOL: 16 fills (10 buy / 6 sell), traded 21,709, gross pnl -113.08, -104 bps per round trip, avg half spread 0.5 bps
- XRP: 12 fills (6 buy / 6 sell), traded 13,015, gross pnl -222.60, -342 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-11-04 15:11Z buy SOL 814 @ 97.5588 fee 0.81 slip 0.41 (half spread 1.0 bps)
- 2026-11-04 16:10Z sell SOL 2,383 @ 96.9665 fee 2.38 slip 1.19 (half spread 0.5 bps)
- 2026-11-05 16:10Z buy ADA 1,593 @ 0.183423 fee 1.59 slip 0.85 (half spread 3.4 bps)
- 2026-11-05 16:10Z buy AVAX 1,593 @ 8.24462 fee 1.59 slip 0.80 (half spread 0.6 bps)
- 2026-11-05 16:10Z buy LINK 1,593 @ 10.7466 fee 1.59 slip 0.90 (half spread 3.6 bps)
- 2026-11-05 16:10Z buy DOGE 1,593 @ 0.0719568 fee 1.59 slip 0.80 (half spread 1.4 bps)
- 2026-11-05 16:10Z buy DOT 1,593 @ 0.905981 fee 1.59 slip 1.46 (half spread 7.2 bps)
- 2026-11-05 16:10Z buy LTC 1,584 @ 52.1461 fee 1.58 slip 0.79 (half spread 1.9 bps)

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-08 03:10Z; halted today: False

last decisions (newest last):

- 2026-11-08 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-08 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-08 03:10Z; halted today: False

last decisions (newest last):

- 2026-11-08 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 88.95 not a higher low vs prior low 99.43 (need +10.0%)
- 2026-11-08 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.18 not a higher low vs prior low 0.2015 (need +10.0%)
- 2026-11-08 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.148 not a higher low vs prior low 8.704 (need +10.0%)
- 2026-11-08 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.27 (need +10.0%)
- 2026-11-08 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.154 not a higher low vs prior low 1.267 (need +10.0%)
- 2026-11-08 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07103 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-08 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8884 not a higher low vs prior low 0.9818 (need +10.0%)
- 2026-11-08 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 51.48 not a higher low vs prior low 55.7 (need +10.0%)
- 2026-11-08 03:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.543e+04 not a higher low vs prior low 7.948e+04 (need +10.0%)
- 2026-11-08 03:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2299 (need +10.0%)
- 2026-11-08 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 88.95 not a higher low vs prior low 99.43 (need +10.0%)
- 2026-11-08 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1797 not a higher low vs prior low 0.1977 (need +10.0%)
- 2026-11-08 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.148 not a higher low vs prior low 8.679 (need +10.0%)
- 2026-11-08 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.27 (need +10.0%)
- 2026-11-08 03:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.154 not a higher low vs prior low 1.267 (need +10.0%)
- 2026-11-08 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07103 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-08 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8884 not a higher low vs prior low 0.9749 (need +10.0%)
- 2026-11-08 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 51.48 not a higher low vs prior low 55.7 (need +10.0%)

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

- equity 9,085.86 (started 10,000 at 2026-10-13 17:26Z), net -9.14% since start
- 24h -0.08%, 7d -5.33%, 30d -9.14%, max drawdown -12.99%
- fills 37 total, 7 in the last 7d
- costs 88.19 (fees 56.05 + slippage 32.14); gross pnl -825.95; cost coverage -9.37
- cash 4,561.13; positions: SOL 25.4938, XRP 1943.04
- last run 2026-11-08 03:10Z; halted today: False

last decisions (newest last):

- 2026-11-08 02:10Z SOL hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.99 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-11-08 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.53 not below -2.0
- 2026-11-08 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.15 not below -2.0
- 2026-11-08 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.07 not below -2.0
- 2026-11-08 02:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -2.66 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-11-08 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.57 not below -2.0
- 2026-11-08 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.47 not below -2.0
- 2026-11-08 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.51 not below -2.0
- 2026-11-08 03:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-08 03:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.03 not below -2.0
- 2026-11-08 03:10Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -2.00 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-11-08 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.53 not below -2.0
- 2026-11-08 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.17 not below -2.0
- 2026-11-08 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.08 not below -2.0
- 2026-11-08 03:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -2.70 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-11-08 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.67 not below -2.0
- 2026-11-08 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.48 not below -2.0
- 2026-11-08 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.53 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 4 fills (1 buy / 3 sell), traded 4,854, gross pnl -141.72, -584 bps per round trip, avg half spread 1.1 bps
- LINK: 2 fills (1 buy / 1 sell), traded 4,797, gross pnl +245.83, +1025 bps per round trip, avg half spread 2.6 bps
- SOL: 7 fills (3 buy / 4 sell), traded 11,735, gross pnl -146.56, -250 bps per round trip, avg half spread 0.9 bps, open 25.4938
- XRP: 5 fills (2 buy / 3 sell), traded 7,173, gross pnl -123.93, -346 bps per round trip, avg half spread 1.4 bps, open 1943.04

last fills:

- 2026-10-31 18:10Z sell LINK 2,520 @ 11.6859 fee 2.52 slip 1.26 (half spread 1.5 bps)
- 2026-11-05 18:10Z buy SOL 2,318 @ 89.1596 fee 2.32 slip 1.16 (half spread 0.6 bps)
- 2026-11-05 23:10Z sell SOL 2,297 @ 88.3623 fee 2.30 slip 1.24 (half spread 3.4 bps)
- 2026-11-05 23:10Z sell ADA 2,152 @ 0.177773 fee 2.15 slip 1.65 (half spread 5.7 bps)
- 2026-11-05 23:10Z sell AVAX 2,240 @ 8.09295 fee 2.24 slip 1.12 (half spread 2.5 bps)
- 2026-11-05 23:10Z sell DOT 2,257 @ 0.89712 fee 2.26 slip 1.96 (half spread 6.7 bps)
- 2026-11-06 00:10Z buy SOL 2,284 @ 89.5798 fee 2.28 slip 1.14 (half spread 0.6 bps)
- 2026-11-06 21:10Z buy XRP 2,285 @ 1.17624 fee 2.29 slip 1.14 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1992 candles, 2026-08-17 03:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1992 candles, 2026-08-17 03:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1992 candles, 2026-08-17 03:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 1992 candles, 2026-08-17 03:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 1992 candles, 2026-08-17 03:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- LINK: live 1992 candles, 2026-08-17 03:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- XRP: live 1964 candles, 2026-08-18 07:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1964 candles, 2026-08-18 07:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- DOT: live 1964 candles, 2026-08-18 07:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1964 candles, 2026-08-18 07:00Z to 2026-11-08 02:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
