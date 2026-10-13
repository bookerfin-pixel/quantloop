# quantloop summary — generated 2026-10-13 00:10Z

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

- challenger1: testing H1 since 2026-09-16 05:21Z, day 26.8 of 60, 33.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +2.75% (max drawdown -17.84%, 238 fills) vs challenger1 -4.72% (max drawdown -8.81%, 51 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.74% (usual 0.54, this window 0.64) vs challenger1 -9.89% (usual 0.37, this window 0.27); the rule compares on skill, daily edge t -0.46 over 27 days
  trades: its 17 finished trades made -0.87% of its starting equity after costs (10 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.54 over 27 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +7.78%, equal weight basket of 10 pairs +13.93%, basket max drawdown -14%, basket realised vol 57% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 21.7 of 60, 38.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -10.57% (max drawdown -17.84%, 200 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.47% (usual 0.54, this window 0.62) vs challenger2 -0.61% (usual 0.29, this window 0.16); the rule compares on skill, daily edge t +0.99 over 22 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.22 over 22 days)
  fills: 4 in 21.7 days; at this pace about 22 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -0.96%, equal weight basket of 10 pairs -3.90%, basket max drawdown -14%, basket realised vol 57% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 7.1 of 60, 52.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.52% (max drawdown -7.91%, 49 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.89% (usual 0.55, this window 0.40) vs challenger3 -0.98% (usual 0.03, this window 0.04); the rule compares on skill, daily edge t +0.34 over 7 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  fills: 10 in 7.1 days, 8 of them in the hour it began; at this pace about 24 by day 60, under the 30 a promotion there needs, and about 41 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -4.88%, equal weight basket of 10 pairs -10.25%, basket max drawdown -14%, basket realised vol 57% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 17.1 of 60, 42.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -15.95% (max drawdown -17.84%, 172 fills) vs challenger4 -13.93% (max drawdown -15.40%, 42 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.85% (usual 0.55, this window 0.58) vs challenger4 -9.50% (usual 0.48, this window 0.86); the rule compares on skill, daily edge t +0.22 over 17 days
  trades: its 15 finished trades made -13.74% of its starting equity after costs (0 won, 15 lost, 8 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -2.05 over 17 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -2.57%, equal weight basket of 10 pairs -9.30%, basket max drawdown -14%, basket realised vol 55% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3, H4 in challenger4), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,275.45 (started 10,000 at 2026-09-16 03:55Z), net +2.75% since start
- 24h -3.67%, 7d -7.21%, 30d +2.75%, max drawdown -17.84%
- fills 238 total, 48 in the last 7d
- costs 540.22 (fees 358.09 + slippage 182.13); gross pnl 815.67; cost coverage 1.51
- cash 7,716.05; positions: BTC 0.0314588
- last run 2026-10-13 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.61% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.78% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.71% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.22% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.41% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-12 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.35% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return -1.00% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-13 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.66% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.26% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.85% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.91% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.71% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.48% not above entry band +1.0% and price below 24h EMA
- 2026-10-13 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.91% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 23 fills (10 buy / 13 sell), traded 32,622, gross pnl +2.68, +2 bps per round trip, avg half spread 2.2 bps
- AVAX: 33 fills (15 buy / 18 sell), traded 57,758, gross pnl +447.02, +155 bps per round trip, avg half spread 1.2 bps
- BTC: 19 fills (10 buy / 9 sell), traded 25,231, gross pnl +76.38, +61 bps per round trip, avg half spread 0.1 bps, open 0.0314588
- DOGE: 23 fills (12 buy / 11 sell), traded 30,681, gross pnl -208.37, -136 bps per round trip, avg half spread 1.0 bps
- DOT: 27 fills (13 buy / 14 sell), traded 35,702, gross pnl +123.63, +69 bps per round trip, avg half spread 2.3 bps
- ETH: 20 fills (9 buy / 11 sell), traded 30,226, gross pnl -97.68, -65 bps per round trip, avg half spread 0.1 bps
- LINK: 25 fills (11 buy / 14 sell), traded 43,746, gross pnl -147.08, -67 bps per round trip, avg half spread 2.2 bps
- LTC: 25 fills (11 buy / 14 sell), traded 36,923, gross pnl +523.66, +284 bps per round trip, avg half spread 1.8 bps
- SOL: 23 fills (12 buy / 11 sell), traded 36,631, gross pnl -9.75, -5 bps per round trip, avg half spread 0.5 bps
- XRP: 20 fills (10 buy / 10 sell), traded 28,575, gross pnl +105.18, +74 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-12 15:10Z buy LTC 697 @ 63.2016 fee 0.70 slip 0.35 (half spread 1.6 bps)
- 2026-10-12 16:10Z sell LTC 1,734 @ 63.1484 fee 1.73 slip 0.87 (half spread 1.6 bps)
- 2026-10-12 17:10Z sell AVAX 1,711 @ 10.4798 fee 1.71 slip 0.86 (half spread 1.0 bps)
- 2026-10-12 17:10Z sell DOGE 1,737 @ 0.0846449 fee 1.74 slip 0.87 (half spread 0.1 bps)
- 2026-10-12 17:10Z sell DOT 1,718 @ 1.21804 fee 1.72 slip 0.86 (half spread 1.2 bps)
- 2026-10-12 17:10Z buy BTC 852 @ 82532.1 fee 0.85 slip 0.43 (half spread 0.0 bps)
- 2026-10-12 17:10Z buy ETH 858 @ 2515.22 fee 0.86 slip 0.43 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell ETH 2,537 @ 2457.8 fee 2.54 slip 1.27 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,517.27 (started 10,000 at 2026-09-16 03:55Z), net -4.83% since start
- 24h -4.14%, 7d -8.46%, 30d -4.83%, max drawdown -8.81%
- fills 51 total, 41 in the last 7d
- costs 114.30 (fees 76.11 + slippage 38.19); gross pnl -368.43; cost coverage -3.22
- cash 2,500.76; positions: DOGE 28603.9, SOL 22.2866, XRP 1771.71
- last run 2026-10-13 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 23:10Z SOL hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: z -1.79 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-12 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.35 not below -2.0
- 2026-10-12 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.39 not below -2.0
- 2026-10-12 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.26 not below -2.0
- 2026-10-12 23:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.79 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-10-12 23:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.49 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25
- 2026-10-12 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.10 not below -2.0
- 2026-10-12 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.69 not below -2.0
- 2026-10-13 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.57 not below -2.0
- 2026-10-13 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.60 not below -2.0
- 2026-10-13 00:10Z SOL hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: z -1.90 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-13 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.71 not below -2.0
- 2026-10-13 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.74 not below -2.0
- 2026-10-13 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.58 not below -2.0
- 2026-10-13 00:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.94 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-10-13 00:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: z -1.74 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25
- 2026-10-13 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.44 not below -2.0
- 2026-10-13 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.85 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- AVAX: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +96.37, +769 bps per round trip, avg half spread 0.7 bps
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 8 fills (5 buy / 3 sell), traded 12,773, gross pnl -138.90, -217 bps per round trip, avg half spread 0.2 bps, open 28603.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 9 fills (4 buy / 5 sell), traded 14,136, gross pnl +8.34, +12 bps per round trip, avg half spread 0.2 bps
- LINK: 4 fills (2 buy / 2 sell), traded 4,459, gross pnl -4.74, -21 bps per round trip, avg half spread 1.1 bps
- LTC: 5 fills (3 buy / 2 sell), traded 6,222, gross pnl -6.00, -19 bps per round trip, avg half spread 1.3 bps
- SOL: 7 fills (5 buy / 2 sell), traded 10,826, gross pnl -150.18, -277 bps per round trip, avg half spread 0.5 bps, open 22.2866
- XRP: 7 fills (4 buy / 3 sell), traded 7,556, gross pnl -248.56, -658 bps per round trip, avg half spread 0.4 bps, open 1771.71

last fills:

- 2026-10-11 16:10Z buy XRP 759 @ 1.41868 fee 0.76 slip 0.38 (half spread 0.2 bps)
- 2026-10-11 16:10Z buy DOGE 745 @ 0.0871362 fee 0.75 slip 0.37 (half spread 0.6 bps)
- 2026-10-11 16:10Z buy LTC 762 @ 64.5523 fee 0.76 slip 0.38 (half spread 1.5 bps)
- 2026-10-12 05:10Z sell ETH 2,020 @ 2565.53 fee 2.02 slip 1.01 (half spread 0.0 bps)
- 2026-10-12 05:10Z buy XRP 521 @ 1.41911 fee 0.52 slip 0.26 (half spread 0.0 bps)
- 2026-10-12 05:10Z buy DOGE 504 @ 0.0878991 fee 0.50 slip 0.25 (half spread 0.1 bps)
- 2026-10-12 08:10Z sell LTC 2,012 @ 65.4822 fee 2.01 slip 1.01 (half spread 0.8 bps)
- 2026-10-12 08:10Z buy SOL 501 @ 112.316 fee 0.50 slip 0.25 (half spread 0.9 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h +0.00%, 7d -1.60%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-13 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 106.3 not above 120h high 116.4
- 2026-10-12 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.79 not above 120h high 13.47
- 2026-10-12 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.349 not above 120h high 1.425
- 2026-10-12 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 61.54 not above 120h high 66.09
- 2026-10-13 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.174e+04 not above 120h high 8.413e+04
- 2026-10-13 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 105.6 not above 120h high 116.4
- 2026-10-13 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.61 not above 120h high 13.47
- 2026-10-13 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.34 not above 120h high 1.425
- 2026-10-13 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-13 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 60.98 not above 120h high 66.09

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
- last run 2026-10-13 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-12 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-12 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-12 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-12 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-12 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-12 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-12 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 59.46 (need +10.0%)
- 2026-10-13 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.067e+04 not a higher low vs prior low 8.263e+04 (need +10.0%)
- 2026-10-13 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2415 not a higher low vs prior low 2640 (need +10.0%)
- 2026-10-13 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-13 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-13 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-13 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-13 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-13 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.09105 (need +10.0%)
- 2026-10-13 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-13 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 59.46 (need +10.0%)

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

- equity 8,825.63 (started 10,000 at 2026-09-25 04:23Z), net -11.74% since start
- 24h -4.91%, 7d -14.43%, 30d -11.68%, max drawdown -15.40%
- fills 55 total, 32 in the last 7d
- costs 106.90 (fees 71.03 + slippage 35.87); gross pnl -1,067.47; cost coverage -9.99
- cash 8,825.63; positions: none
- last run 2026-10-13 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z ADA sell target 0.00 (held 0.19) — daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z AVAX sell target 0.00 (held 0.20) — daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z LINK sell target 0.00 (held 0.20) — daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z DOT sell target 0.00 (held 0.20) — daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-12 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt: equity 8839.07 is down 5.2% from the day's open 9328.81
- 2026-10-13 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -3.22% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +3.80% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -1.93% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -3.17% not above entry band +5.0% and price below 168h EMA
- 2026-10-13 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-13 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (4 buy / 5 sell), traded 12,190, gross pnl -275.47, -452 bps per round trip, avg half spread 2.1 bps
- AVAX: 6 fills (4 buy / 2 sell), traded 8,290, gross pnl -237.69, -573 bps per round trip, avg half spread 0.8 bps
- BTC: 6 fills (4 buy / 2 sell), traded 8,469, gross pnl -94.58, -223 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 7 fills (3 buy / 4 sell), traded 8,649, gross pnl -49.97, -116 bps per round trip, avg half spread 1.9 bps
- ETH: 4 fills (3 buy / 1 sell), traded 4,849, gross pnl -68.19, -281 bps per round trip, avg half spread 0.0 bps
- LINK: 6 fills (2 buy / 4 sell), traded 8,682, gross pnl -39.59, -91 bps per round trip, avg half spread 1.6 bps
- LTC: 5 fills (2 buy / 3 sell), traded 6,271, gross pnl -87.08, -278 bps per round trip, avg half spread 1.7 bps
- SOL: 5 fills (3 buy / 2 sell), traded 4,625, gross pnl -80.22, -347 bps per round trip, avg half spread 0.4 bps
- XRP: 5 fills (2 buy / 3 sell), traded 7,043, gross pnl -34.06, -97 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-11 16:10Z buy BTC 1,870 @ 83751.7 fee 1.87 slip 0.93 (half spread 0.0 bps)
- 2026-10-11 16:10Z buy AVAX 1,870 @ 10.8829 fee 1.87 slip 0.93 (half spread 0.5 bps)
- 2026-10-11 16:10Z buy LINK 1,863 @ 13.3274 fee 1.86 slip 0.93 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell BTC 1,827 @ 81832.2 fee 1.83 slip 0.91 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell ADA 1,721 @ 0.234702 fee 1.72 slip 1.04 (half spread 4.1 bps)
- 2026-10-12 23:10Z sell AVAX 1,754 @ 10.2089 fee 1.75 slip 0.88 (half spread 1.0 bps)
- 2026-10-12 23:10Z sell LINK 1,776 @ 12.7071 fee 1.78 slip 0.89 (half spread 0.0 bps)
- 2026-10-12 23:10Z sell DOT 1,757 @ 1.18351 fee 1.76 slip 0.88 (half spread 2.5 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1365 candles, 2026-08-17 03:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1365 candles, 2026-08-17 03:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1365 candles, 2026-08-17 03:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1365 candles, 2026-08-17 03:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- AVAX: live 1365 candles, 2026-08-17 03:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- LINK: live 1365 candles, 2026-08-17 03:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1337 candles, 2026-08-18 07:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1337 candles, 2026-08-18 07:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- DOT: live 1337 candles, 2026-08-18 07:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LTC: live 1337 candles, 2026-08-18 07:00Z to 2026-10-12 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.1 bps
