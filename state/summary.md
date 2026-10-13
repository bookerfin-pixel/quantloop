# quantloop summary — generated 2026-10-13 20:11Z

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

- challenger1: testing H1 since 2026-09-16 05:21Z, day 27.6 of 60, 32.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +2.26% (max drawdown -18.60%, 243 fills) vs challenger1 -1.74% (max drawdown -9.09%, 59 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.35% (usual 0.54, this window 0.63) vs challenger1 -7.68% (usual 0.37, this window 0.29); the rule compares on skill, daily edge t -0.17 over 28 days
  trades: its 18 finished trades made -0.25% of its starting equity after costs (11 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.28 over 28 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +9.71%, equal weight basket of 10 pairs +16.00%, basket max drawdown -14%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 22.5 of 60, 37.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -11.00% (max drawdown -18.60%, 205 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.86% (usual 0.54, this window 0.62) vs challenger2 -1.12% (usual 0.29, this window 0.16); the rule compares on skill, daily edge t +1.06 over 22 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.38 over 22 days)
  fills: 4 in 22.5 days; at this pace about 21 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +0.81%, equal weight basket of 10 pairs -2.12%, basket max drawdown -14%, basket realised vol 58% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 7.9 of 60, 52.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.97% (max drawdown -8.76%, 54 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.26% (usual 0.55, this window 0.41) vs challenger3 -1.03% (usual 0.03, this window 0.04); the rule compares on skill, daily edge t +0.77 over 8 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  fills: 10 in 7.9 days, 8 of them in the hour it began; at this pace about 23 by day 60, under the 30 a promotion there needs, and about 38 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.17%, equal weight basket of 10 pairs -8.59%, basket max drawdown -14%, basket realised vol 60% annualised
- challenger4: idle, holds cash (free for a hypothesis)
- free slots: challenger4
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,225.69 (started 10,000 at 2026-09-16 03:55Z), net +2.26% since start
- 24h -1.47%, 7d -7.59%, 30d +2.26%, max drawdown -18.60%
- fills 243 total, 50 in the last 7d
- costs 559.51 (fees 370.93 + slippage 188.58); gross pnl 785.20; cost coverage 1.40
- cash 5,115.89; positions: BTC 0.030713, ETH 1.01751
- last run 2026-10-13 20:11Z; halted today: False

last decisions (newest last):

- 2026-10-13 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.23% not above entry band +1.0%
- 2026-10-13 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.08% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.87% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.99% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.27% not above entry band +1.0%
- 2026-10-13 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.82% not above entry band +1.0%
- 2026-10-13 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.96% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.59% not above entry band +1.0%
- 2026-10-13 20:11Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.25% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-13 20:11Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return -0.22% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-13 20:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.65% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 20:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.22% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 20:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.99% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 20:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.14% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 20:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.39% not above entry band +1.0%
- 2026-10-13 20:11Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.76% not above entry band +1.0%
- 2026-10-13 20:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.23% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 20:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.42% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 23 fills (10 buy / 13 sell), traded 32,622, gross pnl +2.68, +2 bps per round trip, avg half spread 2.2 bps
- AVAX: 33 fills (15 buy / 18 sell), traded 57,758, gross pnl +447.02, +155 bps per round trip, avg half spread 1.2 bps
- BTC: 21 fills (11 buy / 10 sell), traded 30,368, gross pnl +74.69, +49 bps per round trip, avg half spread 0.1 bps, open 0.030713
- DOGE: 23 fills (12 buy / 11 sell), traded 30,681, gross pnl -208.37, -136 bps per round trip, avg half spread 1.0 bps
- DOT: 27 fills (13 buy / 14 sell), traded 35,702, gross pnl +123.63, +69 bps per round trip, avg half spread 2.3 bps
- ETH: 21 fills (10 buy / 11 sell), traded 32,798, gross pnl -115.40, -70 bps per round trip, avg half spread 0.1 bps, open 1.01751
- LINK: 27 fills (12 buy / 15 sell), traded 48,873, gross pnl -158.14, -65 bps per round trip, avg half spread 2.1 bps
- LTC: 25 fills (11 buy / 14 sell), traded 36,923, gross pnl +523.66, +284 bps per round trip, avg half spread 1.8 bps
- SOL: 23 fills (12 buy / 11 sell), traded 36,631, gross pnl -9.75, -5 bps per round trip, avg half spread 0.5 bps
- XRP: 20 fills (10 buy / 10 sell), traded 28,575, gross pnl +105.18, +74 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-12 17:10Z buy BTC 852 @ 82532.1 fee 0.85 slip 0.43 (half spread 0.0 bps)
- 2026-10-12 17:10Z buy ETH 858 @ 2515.22 fee 0.86 slip 0.43 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell ETH 2,537 @ 2457.8 fee 2.54 slip 1.27 (half spread 0.0 bps)
- 2026-10-13 01:10Z sell BTC 2,568 @ 81615.4 fee 2.57 slip 1.28 (half spread 0.0 bps)
- 2026-10-13 05:10Z buy LINK 2,570 @ 13.0362 fee 2.57 slip 1.28 (half spread 0.0 bps)
- 2026-10-13 06:10Z buy ETH 2,572 @ 2527.96 fee 2.57 slip 1.29 (half spread 0.0 bps)
- 2026-10-13 07:10Z buy BTC 2,569 @ 83644.1 fee 2.57 slip 1.28 (half spread 0.0 bps)
- 2026-10-13 14:10Z sell LINK 2,557 @ 12.9669 fee 2.56 slip 1.31 (half spread 3.1 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,814.53 (started 10,000 at 2026-09-16 03:55Z), net -1.85% since start
- 24h +0.59%, 7d -5.61%, 30d -1.85%, max drawdown -9.09%
- fills 59 total, 49 in the last 7d
- costs 128.95 (fees 85.88 + slippage 43.07); gross pnl -56.52; cost coverage -0.44
- cash 1,420.08; positions: ADA 5922, AVAX 135.761, DOGE 16645.1, LTC 22.3568, SOL 13.0958, XRP 1018.86
- last run 2026-10-13 20:11Z; halted today: False

last decisions (newest last):

- 2026-10-13 19:10Z SOL hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -1.21 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 19:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -1.18 vs 240h mean (entry -2.0, exit -0.5); vol 94% -> weight 0.25
- 2026-10-13 19:10Z AVAX hold target 0.17 (held 0.14) — hold: weight change +0.025 below threshold 0.05 | stay long: z -1.22 vs 240h mean (entry -2.0, exit -0.5); vol 94% -> weight 0.25
- 2026-10-13 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.81 not below -2.0
- 2026-10-13 19:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.11 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 19:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -1.00 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-13 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.27 not below -2.0
- 2026-10-13 19:10Z LTC hold target 0.17 (held 0.14) — hold: weight change +0.026 below threshold 0.05 | stay long: z -1.31 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-10-13 20:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.43 not below -2.0
- 2026-10-13 20:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.79 not below -2.0
- 2026-10-13 20:11Z SOL hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -1.26 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 20:11Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.19 vs 240h mean (entry -2.0, exit -0.5); vol 94% -> weight 0.25
- 2026-10-13 20:11Z AVAX hold target 0.17 (held 0.14) — hold: weight change +0.025 below threshold 0.05 | stay long: z -1.21 vs 240h mean (entry -2.0, exit -0.5); vol 94% -> weight 0.25
- 2026-10-13 20:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.84 not below -2.0
- 2026-10-13 20:11Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: z -1.11 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-13 20:11Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: z -0.99 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-13 20:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.30 not below -2.0
- 2026-10-13 20:11Z LTC hold target 0.17 (held 0.14) — hold: weight change +0.026 below threshold 0.05 | stay long: z -1.27 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (2 buy / 1 sell), traded 6,485, gross pnl +178.34, +550 bps per round trip, avg half spread 2.3 bps, open 5922
- AVAX: 3 fills (2 buy / 1 sell), traded 3,863, gross pnl +134.38, +696 bps per round trip, avg half spread 0.7 bps, open 135.761
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 9 fills (5 buy / 4 sell), traded 13,747, gross pnl -91.99, -134 bps per round trip, avg half spread 0.3 bps, open 16645.1
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 9 fills (4 buy / 5 sell), traded 14,136, gross pnl +8.34, +12 bps per round trip, avg half spread 0.2 bps
- LINK: 6 fills (3 buy / 3 sell), traded 7,237, gross pnl +61.02, +169 bps per round trip, avg half spread 1.2 bps
- LTC: 6 fills (4 buy / 2 sell), traded 7,571, gross pnl +27.98, +74 bps per round trip, avg half spread 1.3 bps, open 22.3568
- SOL: 8 fills (5 buy / 3 sell), traded 11,777, gross pnl -111.80, -190 bps per round trip, avg half spread 0.5 bps, open 13.0958
- XRP: 8 fills (4 buy / 4 sell), traded 8,558, gross pnl -207.61, -485 bps per round trip, avg half spread 0.3 bps, open 1018.86

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
- 24h +0.00%, 7d -1.36%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-13 20:11Z; halted today: False

last decisions (newest last):

- 2026-10-13 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 107.7 not above 120h high 113
- 2026-10-13 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.94 not above 120h high 13.47
- 2026-10-13 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.371 not above 120h high 1.424
- 2026-10-13 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 61.75 not above 120h high 65.77
- 2026-10-13 20:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.32e+04 not above 120h high 8.413e+04
- 2026-10-13 20:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 20:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 107.4 not above 120h high 113
- 2026-10-13 20:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 20:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 20:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.92 not above 120h high 13.47
- 2026-10-13 20:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.371 not above 120h high 1.424
- 2026-10-13 20:11Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 20:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 20:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 61.83 not above 120h high 65.77

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
- 24h +0.00%, 7d -0.92%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 1 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-13 20:11Z; halted today: False

last decisions (newest last):

- 2026-10-13 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 102.8 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-13 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-13 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-13 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-13 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.319 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-13 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08091 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-13 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-13 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 59.58 not a higher low vs prior low 60.91 (need +10.0%)
- 2026-10-13 20:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.067e+04 not a higher low vs prior low 8.263e+04 (need +10.0%)
- 2026-10-13 20:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2415 not a higher low vs prior low 2640 (need +10.0%)
- 2026-10-13 20:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 102.8 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-13 20:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-13 20:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-13 20:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-13 20:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.319 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-13 20:11Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08091 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-13 20:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-13 20:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 59.58 not a higher low vs prior low 60.91 (need +10.0%)

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

## challenger4: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-10-13 17:26Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-10-13 20:11Z; halted today: False

last decisions (newest last):

- 2026-10-13 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-10-13 20:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1385 candles, 2026-08-17 03:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1385 candles, 2026-08-17 03:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1385 candles, 2026-08-17 03:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1385 candles, 2026-08-17 03:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.6 bps
- AVAX: live 1385 candles, 2026-08-17 03:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- LINK: live 1385 candles, 2026-08-17 03:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1357 candles, 2026-08-18 07:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1357 candles, 2026-08-18 07:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- DOT: live 1357 candles, 2026-08-18 07:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1357 candles, 2026-08-18 07:00Z to 2026-10-13 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.1 bps
