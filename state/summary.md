# quantloop summary — generated 2026-10-12 14:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168 (2 of them replayed after a missed run)
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-05 (today and the 7 UTC days before it): the cap stopped a buy in 3 hours, on 1 pair day; a pair filled 4 times or more in one UTC day on 3 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, AVAX, 2026-10-07: 4 fills (buy 02:24, sell 03:25, buy 08:28, sell 10:27); a buy stopped by the cap in 3 hours (14:27, 17:26, 18:29), each an entry from flat
- champion, DOT, 2026-10-05: 4 fills (sell 05:28, buy 19:00, sell 20:00, sell 21:32); no buy stopped
- champion, LTC, 2026-10-05: 4 fills (buy 05:28, sell 16:27, buy 18:30, sell 21:32); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 26.4 of 60, 33.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +6.16% (max drawdown -15.47%, 221 fills) vs challenger1 -1.00% (max drawdown -7.73%, 51 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.44% (usual 0.54, this window 0.64) vs challenger1 -8.31% (usual 0.37, this window 0.27); the rule compares on skill, daily edge t -0.36 over 26 days
  trades: its 17 finished trades made -0.87% of its starting equity after costs (10 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.43 over 26 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +9.29%, equal weight basket of 10 pairs +19.69%, basket max drawdown -14%, basket realised vol 57% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 21.2 of 60, 38.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.61% (max drawdown -15.47%, 183 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.07% (usual 0.54, this window 0.62) vs challenger2 -1.97% (usual 0.29, this window 0.17); the rule compares on skill, daily edge t +0.79 over 21 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.70 over 21 days)
  fills: 4 in 21.2 days; at this pace about 22 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +0.42%, equal weight basket of 10 pairs +0.85%, basket max drawdown -14%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 6.7 of 60, 53.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.46% (max drawdown -5.25%, 32 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.26% (usual 0.55, this window 0.39) vs challenger3 -1.10% (usual 0.03, this window 0.05); the rule compares on skill, daily edge t +0.08 over 7 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.54%, equal weight basket of 10 pairs -5.83%, basket max drawdown -14%, basket realised vol 56% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 16.7 of 60, 43.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.16% (max drawdown -15.47%, 155 fills) vs challenger4 -9.72% (max drawdown -11.85%, 37 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.53% (usual 0.55, this window 0.58) vs challenger4 -7.43% (usual 0.48, this window 0.86); the rule compares on skill, daily edge t +0.44 over 17 days
  trades: its 10 finished trades made -9.65% of its starting equity after costs (0 won, 10 lost, 3 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.73 over 17 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -1.20%, equal weight basket of 10 pairs -4.81%, basket max drawdown -14%, basket realised vol 54% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3, H4 in challenger4), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,615.82 (started 10,000 at 2026-09-16 03:55Z), net +6.16% since start
- 24h -0.01%, 7d -4.86%, 30d +6.16%, max drawdown -15.47%
- fills 221 total, 46 in the last 7d
- costs 511.06 (fees 338.65 + slippage 172.41); gross pnl 1,126.88; cost coverage 2.20
- cash 0.00; positions: ADA 4207.46, AVAX 98.5991, BTC 0.0128091, DOGE 12314.6, DOT 851.334, ETH 0.42386, LINK 80.494, LTC 16.431, SOL 9.59699, XRP 756.369
- last run 2026-10-12 14:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 13:10Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return -0.23% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 13:10Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +4.31% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 13:10Z AVAX hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +6.14% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-12 13:10Z LINK hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +2.98% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 13:10Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return -0.06% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 13:10Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.46% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 13:10Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +7.28% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-10-12 13:10Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.44% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.40% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.29% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.77% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +4.80% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z AVAX hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +6.85% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-12 14:10Z LINK hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +3.34% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.82% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.82% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-12 14:10Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +7.73% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-10-12 14:10Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.52% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 22 fills (10 buy / 12 sell), traded 31,601, gross pnl +25.61, +16 bps per round trip, avg half spread 2.2 bps, open 4207.46
- AVAX: 31 fills (14 buy / 17 sell), traded 55,355, gross pnl +498.71, +180 bps per round trip, avg half spread 1.2 bps, open 98.5991
- BTC: 17 fills (8 buy / 9 sell), traded 23,691, gross pnl +119.44, +101 bps per round trip, avg half spread 0.1 bps, open 0.0128091
- DOGE: 21 fills (11 buy / 10 sell), traded 28,246, gross pnl -188.59, -134 bps per round trip, avg half spread 1.1 bps, open 12314.6
- DOT: 25 fills (12 buy / 13 sell), traded 33,291, gross pnl +170.23, +102 bps per round trip, avg half spread 2.4 bps, open 851.334
- ETH: 17 fills (7 buy / 10 sell), traded 26,155, gross pnl -27.13, -21 bps per round trip, avg half spread 0.1 bps, open 0.42386
- LINK: 24 fills (11 buy / 13 sell), traded 42,700, gross pnl -132.08, -62 bps per round trip, avg half spread 2.2 bps, open 80.494
- LTC: 23 fills (10 buy / 13 sell), traded 34,491, gross pnl +537.92, +312 bps per round trip, avg half spread 1.8 bps, open 16.431
- SOL: 22 fills (12 buy / 10 sell), traded 35,586, gross pnl +3.40, +2 bps per round trip, avg half spread 0.5 bps, open 9.59699
- XRP: 19 fills (10 buy / 9 sell), traded 27,536, gross pnl +119.37, +87 bps per round trip, avg half spread 0.5 bps, open 756.369

last fills:

- 2026-10-11 16:10Z sell DOT 1,670 @ 1.25882 fee 1.67 slip 0.84 (half spread 0.4 bps)
- 2026-10-11 16:10Z buy ETH 1,073 @ 2531.61 fee 1.07 slip 0.54 (half spread 0.0 bps)
- 2026-10-11 16:10Z buy SOL 1,073 @ 111.811 fee 1.07 slip 0.54 (half spread 0.4 bps)
- 2026-10-11 16:10Z buy ADA 1,073 @ 0.255035 fee 1.07 slip 0.54 (half spread 2.1 bps)
- 2026-10-11 16:10Z buy AVAX 1,073 @ 10.8829 fee 1.07 slip 0.54 (half spread 0.5 bps)
- 2026-10-11 16:10Z buy XRP 1,073 @ 1.41868 fee 1.07 slip 0.54 (half spread 0.2 bps)
- 2026-10-11 16:10Z buy DOGE 1,073 @ 0.0871362 fee 1.07 slip 0.54 (half spread 0.6 bps)
- 2026-10-11 16:10Z buy LTC 1,061 @ 64.5523 fee 1.06 slip 0.53 (half spread 1.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,888.78 (started 10,000 at 2026-09-16 03:55Z), net -1.11% since start
- 24h +0.74%, 7d -4.89%, 30d -1.11%, max drawdown -7.73%
- fills 51 total, 41 in the last 7d
- costs 114.30 (fees 76.11 + slippage 38.19); gross pnl 3.08; cost coverage 0.03
- cash 2,500.76; positions: DOGE 28603.9, SOL 22.2866, XRP 1771.71
- last run 2026-10-12 14:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 13:10Z SOL hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.15 vs 240h mean (entry -2.0, exit -0.5); vol 52% -> weight 0.25
- 2026-10-12 13:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.37 not below -2.0
- 2026-10-12 13:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-10-12 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.60 not below -2.0
- 2026-10-12 13:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.17 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-12 13:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -0.96 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-10-12 13:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.28 not below -2.0
- 2026-10-12 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.95 not below -2.0
- 2026-10-12 14:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.83 not below -2.0
- 2026-10-12 14:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.67 not below -2.0
- 2026-10-12 14:10Z SOL hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.09 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-12 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.41 not below -2.0
- 2026-10-12 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.11 not below -2.0
- 2026-10-12 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.61 not below -2.0
- 2026-10-12 14:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.14 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-12 14:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -0.96 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-10-12 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-10-12 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.97 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- AVAX: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +96.37, +769 bps per round trip, avg half spread 0.7 bps
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 8 fills (5 buy / 3 sell), traded 12,773, gross pnl -12.38, -19 bps per round trip, avg half spread 0.2 bps, open 28603.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 9 fills (4 buy / 5 sell), traded 14,136, gross pnl +8.34, +12 bps per round trip, avg half spread 0.2 bps
- LINK: 4 fills (2 buy / 2 sell), traded 4,459, gross pnl -4.74, -21 bps per round trip, avg half spread 1.1 bps
- LTC: 5 fills (3 buy / 2 sell), traded 6,222, gross pnl -6.00, -19 bps per round trip, avg half spread 1.3 bps
- SOL: 7 fills (5 buy / 2 sell), traded 10,826, gross pnl -12.90, -24 bps per round trip, avg half spread 0.5 bps, open 22.2866
- XRP: 7 fills (4 buy / 3 sell), traded 7,556, gross pnl -140.84, -373 bps per round trip, avg half spread 0.4 bps, open 1771.71

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
- 24h +0.00%, 7d -1.68%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-12 14:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 110.1 not above 120h high 116.8
- 2026-10-12 13:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 13:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.18 not above 120h high 13.47
- 2026-10-12 13:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.389 not above 120h high 1.445
- 2026-10-12 13:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 13:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 64.14 not above 120h high 66.83
- 2026-10-12 14:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.288e+04 not above 120h high 8.413e+04
- 2026-10-12 14:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 110.4 not above 120h high 116.8
- 2026-10-12 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.17 not above 120h high 13.47
- 2026-10-12 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.39 not above 120h high 1.434
- 2026-10-12 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-12 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 64.05 not above 120h high 66.8

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
- 24h +0.00%, 7d -1.82%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 24 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-12 14:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-12 13:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-12 13:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-12 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-12 13:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-12 13:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.09188 (need +10.0%)
- 2026-10-12 13:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-12 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 59.46 (need +10.0%)
- 2026-10-12 14:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.067e+04 not a higher low vs prior low 8.263e+04 (need +10.0%)
- 2026-10-12 14:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2415 not a higher low vs prior low 2640 (need +10.0%)
- 2026-10-12 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 113.1 (need +10.0%)
- 2026-10-12 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2341 (need +10.0%)
- 2026-10-12 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.83 not a higher low vs prior low 10.07 (need +10.0%)
- 2026-10-12 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-12 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.457 (need +10.0%)
- 2026-10-12 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.09188 (need +10.0%)
- 2026-10-12 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.094 (need +10.0%)
- 2026-10-12 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 59.46 (need +10.0%)

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

- equity 9,256.48 (started 10,000 at 2026-09-25 04:23Z), net -7.44% since start
- 24h +0.10%, 7d -10.25%, 30d -7.37%, max drawdown -11.85%
- fills 50 total, 27 in the last 7d
- costs 93.46 (fees 62.19 + slippage 31.27); gross pnl -650.05; cost coverage -6.96
- cash -0.00; positions: ADA 7333.37, AVAX 171.789, BTC 0.0223227, DOT 1484.21, LINK 139.783
- last run 2026-10-12 14:10Z; halted today: False

last decisions (newest last):

- 2026-10-12 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-12 13:10Z ADA hold target 0.20 (held 0.20) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +18.94% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-12 13:10Z AVAX hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +46.60% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-12 13:10Z LINK hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +14.16% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-12 13:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.37% not above entry band +5.0% and price below 168h EMA
- 2026-10-12 13:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.07% not above entry band +5.0% and price below 168h EMA
- 2026-10-12 13:10Z DOT hold target 0.20 (held 0.20) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +21.00% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-12 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-12 14:10Z BTC hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +7.16% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-12 14:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -0.20% not above entry band +5.0% and price below 168h EMA
- 2026-10-12 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-12 14:10Z ADA hold target 0.20 (held 0.20) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +18.91% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-12 14:10Z AVAX hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +46.33% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-12 14:10Z LINK hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +13.97% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-12 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.63% not above entry band +5.0% and price below 168h EMA
- 2026-10-12 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.14% not above entry band +5.0% and price below 168h EMA
- 2026-10-12 14:10Z DOT hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +21.64% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-12 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 8 fills (4 buy / 4 sell), traded 10,469, gross pnl -177.88, -340 bps per round trip, avg half spread 1.9 bps, open 7333.37
- AVAX: 5 fills (4 buy / 1 sell), traded 6,536, gross pnl -123.79, -379 bps per round trip, avg half spread 0.8 bps, open 171.789
- BTC: 5 fills (4 buy / 1 sell), traded 6,642, gross pnl -69.28, -209 bps per round trip, avg half spread 0.0 bps, open 0.0223227
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 6 fills (3 buy / 3 sell), traded 6,893, gross pnl +64.46, +187 bps per round trip, avg half spread 1.7 bps, open 1484.21
- ETH: 4 fills (3 buy / 1 sell), traded 4,849, gross pnl -68.19, -281 bps per round trip, avg half spread 0.0 bps
- LINK: 5 fills (2 buy / 3 sell), traded 6,906, gross pnl +26.61, +77 bps per round trip, avg half spread 1.9 bps, open 139.783
- LTC: 5 fills (2 buy / 3 sell), traded 6,271, gross pnl -87.08, -278 bps per round trip, avg half spread 1.7 bps
- SOL: 5 fills (3 buy / 2 sell), traded 4,625, gross pnl -80.22, -347 bps per round trip, avg half spread 0.4 bps
- XRP: 5 fills (2 buy / 3 sell), traded 7,043, gross pnl -34.06, -97 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-08 16:29Z sell AVAX 2,270 @ 10.089 fee 2.27 slip 1.14 (half spread 1.0 bps)
- 2026-10-09 17:23Z buy DOT 2,311 @ 1.20135 fee 2.31 slip 1.16 (half spread 2.1 bps)
- 2026-10-10 02:24Z buy ADA 2,348 @ 0.255383 fee 2.35 slip 1.17 (half spread 1.5 bps)
- 2026-10-11 16:10Z sell ADA 474 @ 0.25478 fee 0.47 slip 0.24 (half spread 2.1 bps)
- 2026-10-11 16:10Z sell DOT 553 @ 1.25882 fee 0.55 slip 0.28 (half spread 0.4 bps)
- 2026-10-11 16:10Z buy BTC 1,870 @ 83751.7 fee 1.87 slip 0.93 (half spread 0.0 bps)
- 2026-10-11 16:10Z buy AVAX 1,870 @ 10.8829 fee 1.87 slip 0.93 (half spread 0.5 bps)
- 2026-10-11 16:10Z buy LINK 1,863 @ 13.3274 fee 1.86 slip 0.93 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1355 candles, 2026-08-17 03:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1355 candles, 2026-08-17 03:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1355 candles, 2026-08-17 03:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1355 candles, 2026-08-17 03:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- AVAX: live 1355 candles, 2026-08-17 03:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- LINK: live 1355 candles, 2026-08-17 03:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- XRP: live 1327 candles, 2026-08-18 07:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1327 candles, 2026-08-18 07:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- DOT: live 1327 candles, 2026-08-18 07:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1327 candles, 2026-08-18 07:00Z to 2026-10-12 13:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.1 bps
