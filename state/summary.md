# quantloop summary — generated 2026-10-20 09:11Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-13 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 2 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, ETH, 2026-10-18: 4 fills (buy 03:10, sell 04:10, buy 15:10, sell 16:10); no buy stopped
- champion, DOT, 2026-10-16: 5 fills (buy 01:10, buy 02:10, sell 04:10, buy 15:10, sell 19:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 34.2 of 60, 25.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.21% (max drawdown -23.41%, 281 fills) vs challenger1 -6.11% (max drawdown -12.36%, 69 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.29% (usual 0.54, this window 0.55) vs challenger1 -9.62% (usual 0.37, this window 0.41); the rule compares on skill, daily edge t -0.07 over 34 days
  trades: its 22 finished trades made -0.84% of its starting equity after costs (13 won, 9 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.37 over 34 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +7.37%, equal weight basket of 10 pairs +9.45%, basket max drawdown -17%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 29.0 of 60, 31.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -16.63% (max drawdown -23.41%, 243 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.55% (usual 0.54, this window 0.52) vs challenger2 +0.43% (usual 0.29, this window 0.12); the rule compares on skill, daily edge t +1.64 over 29 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is +0.07 over 29 days)
  fills: 4 in 29.0 days; at this pace about 16 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -1.34%, equal weight basket of 10 pairs -7.56%, basket max drawdown -17%, basket realised vol 57% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 14.4 of 60, 45.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.79% (max drawdown -14.15%, 92 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.30% (usual 0.55, this window 0.31) vs challenger3 -0.89% (usual 0.03, this window 0.02); the rule compares on skill, daily edge t +1.72 over 14 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.86 over 14 days)
  fills: 10 in 14.4 days, 8 of them in the hour it began; at this pace about 24 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.24%, equal weight basket of 10 pairs -13.65%, basket max drawdown -17%, basket realised vol 58% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 4.4 of 120, 115.6 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -1.72% (max drawdown -4.99%, 13 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +0.06% (usual 0.53, this window 0.91); the rule compares on skill, daily edge t +0.10 over 4 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -7.17% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  market over the window: BTC -1.09%, equal weight basket of 10 pairs -3.38%, basket max drawdown -7%, basket realised vol 48% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,579.18 (started 10,000 at 2026-09-16 03:55Z), net -4.21% since start
- 24h +0.00%, 7d -6.39%, 30d -10.95%, max drawdown -23.41%
- fills 281 total, 39 in the last 7d
- costs 664.86 (fees 440.73 + slippage 224.12); gross pnl 244.04; cost coverage 0.37
- cash 9,579.18; positions: none
- last run 2026-10-20 09:10Z; halted today: False

last decisions (newest last):

- 2026-10-20 08:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.66% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.11% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.30% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.34% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.87% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.74% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.54% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 08:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.05% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.22% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.08% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.87% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.63% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.84% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.88% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.01% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.92% not above entry band +1.0% and price below 24h EMA
- 2026-10-20 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.73% not above entry band +1.0%
- 2026-10-20 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.61% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 25 fills (11 buy / 14 sell), traded 35,491, gross pnl -4.51, -3 bps per round trip, avg half spread 2.1 bps
- AVAX: 37 fills (17 buy / 20 sell), traded 64,485, gross pnl +381.31, +118 bps per round trip, avg half spread 1.1 bps
- BTC: 27 fills (14 buy / 13 sell), traded 41,796, gross pnl +5.97, +3 bps per round trip, avg half spread 0.1 bps
- DOGE: 23 fills (12 buy / 11 sell), traded 30,681, gross pnl -208.37, -136 bps per round trip, avg half spread 1.0 bps
- DOT: 34 fills (17 buy / 17 sell), traded 50,430, gross pnl -68.89, -27 bps per round trip, avg half spread 2.3 bps
- ETH: 26 fills (12 buy / 14 sell), traded 41,141, gross pnl -186.03, -90 bps per round trip, avg half spread 0.1 bps
- LINK: 29 fills (13 buy / 16 sell), traded 53,932, gross pnl -216.41, -80 bps per round trip, avg half spread 2.0 bps
- LTC: 30 fills (14 buy / 16 sell), traded 45,789, gross pnl +480.93, +210 bps per round trip, avg half spread 1.7 bps
- SOL: 28 fills (15 buy / 13 sell), traded 45,542, gross pnl -41.60, -18 bps per round trip, avg half spread 0.5 bps
- XRP: 22 fills (11 buy / 11 sell), traded 31,447, gross pnl +101.64, +65 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-18 04:10Z buy AVAX 1,959 @ 9.82941 fee 1.96 slip 0.98 (half spread 1.5 bps)
- 2026-10-18 04:10Z buy LTC 1,951 @ 59.1346 fee 1.95 slip 0.98 (half spread 0.8 bps)
- 2026-10-18 15:10Z sell SOL 1,919 @ 102.144 fee 1.92 slip 0.96 (half spread 0.5 bps)
- 2026-10-18 15:10Z sell AVAX 1,901 @ 9.53573 fee 1.90 slip 0.95 (half spread 0.5 bps)
- 2026-10-18 15:10Z buy ETH 483 @ 2379.01 fee 0.48 slip 0.24 (half spread 0.0 bps)
- 2026-10-18 16:10Z sell BTC 1,939 @ 80999.6 fee 1.94 slip 0.97 (half spread 0.0 bps)
- 2026-10-18 16:10Z sell ETH 2,399 @ 2369.85 fee 2.40 slip 1.20 (half spread 0.0 bps)
- 2026-10-18 16:10Z sell LTC 1,914 @ 58.021 fee 1.91 slip 0.96 (half spread 1.7 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,378.37 (started 10,000 at 2026-09-16 03:55Z), net -6.22% since start
- 24h -1.68%, 7d -4.02%, 30d -8.86%, max drawdown -12.36%
- fills 69 total, 10 in the last 7d
- costs 144.80 (fees 96.45 + slippage 48.36); gross pnl -476.83; cost coverage -3.29
- cash 1,519.81; positions: ADA 5922, AVAX 139.618, DOGE 16645.1, ETH 0.56054, LINK 110.29, XRP 1018.86
- last run 2026-10-20 09:10Z; halted today: False

last decisions (newest last):

- 2026-10-20 08:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.69 not below -2.0
- 2026-10-20 08:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.031 below threshold 0.05 | stay long: z -1.21 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-10-20 08:10Z AVAX hold target 0.17 (held 0.14) — hold: weight change +0.026 below threshold 0.05 | stay long: z -1.53 vs 240h mean (entry -2.0, exit -0.5); vol 70% -> weight 0.25
- 2026-10-20 08:10Z LINK hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.21 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25
- 2026-10-20 08:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.026 below threshold 0.05 | stay long: z -1.07 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-20 08:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.07 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-10-20 08:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.59 not below -2.0
- 2026-10-20 08:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.78 not below -2.0
- 2026-10-20 09:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.01 not below -2.0
- 2026-10-20 09:10Z ETH hold target 0.17 (held 0.14) — hold: weight change +0.025 below threshold 0.05 | stay long: z -1.29 vs 240h mean (entry -2.0, exit -0.5); vol 47% -> weight 0.25
- 2026-10-20 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.77 not below -2.0
- 2026-10-20 09:10Z ADA hold target 0.17 (held 0.14) — hold: weight change +0.031 below threshold 0.05 | stay long: z -1.32 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-10-20 09:10Z AVAX hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.57 vs 240h mean (entry -2.0, exit -0.5); vol 70% -> weight 0.25
- 2026-10-20 09:10Z LINK hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.31 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25
- 2026-10-20 09:10Z XRP hold target 0.17 (held 0.14) — hold: weight change +0.026 below threshold 0.05 | stay long: z -1.12 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-20 09:10Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.027 below threshold 0.05 | stay long: z -1.19 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-10-20 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.53 not below -2.0
- 2026-10-20 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.90 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (2 buy / 1 sell), traded 6,485, gross pnl +47.69, +147 bps per round trip, avg half spread 2.3 bps, open 5922
- AVAX: 6 fills (4 buy / 2 sell), traded 6,621, gross pnl +96.95, +293 bps per round trip, avg half spread 0.8 bps, open 139.618
- BTC: 4 fills (2 buy / 2 sell), traded 7,466, gross pnl +80.04, +214 bps per round trip, avg half spread 0.0 bps
- DOGE: 9 fills (5 buy / 4 sell), traded 13,747, gross pnl -188.27, -274 bps per round trip, avg half spread 0.3 bps, open 16645.1
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 12 fills (6 buy / 6 sell), traded 17,848, gross pnl +63.53, +71 bps per round trip, avg half spread 0.2 bps, open 0.56054
- LINK: 8 fills (5 buy / 3 sell), traded 8,612, gross pnl -1.81, -4 bps per round trip, avg half spread 1.2 bps, open 110.29
- LTC: 7 fills (4 buy / 3 sell), traded 8,915, gross pnl -8.69, -19 bps per round trip, avg half spread 1.4 bps
- SOL: 9 fills (5 buy / 4 sell), traded 13,156, gross pnl -139.56, -212 bps per round trip, avg half spread 0.5 bps
- XRP: 8 fills (4 buy / 4 sell), traded 8,558, gross pnl -291.50, -681 bps per round trip, avg half spread 0.3 bps, open 1018.86

last fills:

- 2026-10-16 10:10Z sell AVAX 1,400 @ 10.3113 fee 1.40 slip 0.70 (half spread 0.5 bps)
- 2026-10-16 10:10Z buy LINK 1,122 @ 12.5572 fee 1.12 slip 0.56 (half spread 1.5 bps)
- 2026-10-16 12:10Z sell ETH 1,216 @ 2466.12 fee 1.22 slip 0.61 (half spread 0.0 bps)
- 2026-10-18 17:10Z buy ETH 1,330 @ 2372.51 fee 1.33 slip 0.66 (half spread 0.0 bps)
- 2026-10-18 20:10Z buy AVAX 158 @ 9.34517 fee 0.16 slip 0.08 (half spread 0.5 bps)
- 2026-10-19 03:10Z sell SOL 1,379 @ 105.272 fee 1.38 slip 0.69 (half spread 0.5 bps)
- 2026-10-19 03:10Z buy AVAX 1,200 @ 9.77939 fee 1.20 slip 0.60 (half spread 1.5 bps)
- 2026-10-19 13:10Z sell LTC 1,345 @ 60.1499 fee 1.34 slip 0.67 (half spread 1.7 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h +0.00%, 7d +0.00%, 30d +0.18%, max drawdown -3.54%
- fills 36 total, 0 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-20 09:10Z; halted today: False

last decisions (newest last):

- 2026-10-20 08:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 08:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2167 not above 120h high 0.2316
- 2026-10-20 08:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 08:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 08:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.295 not above 120h high 1.345
- 2026-10-20 08:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07916 not above 120h high 0.08234
- 2026-10-20 08:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 08:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 09:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.143e+04 not above 120h high 8.275e+04
- 2026-10-20 09:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2152 not above 120h high 0.2316
- 2026-10-20 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.293 not above 120h high 1.345
- 2026-10-20 09:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.0788 not above 120h high 0.08234
- 2026-10-20 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-20 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- last run 2026-10-20 09:10Z; halted today: False

last decisions (newest last):

- 2026-10-20 08:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 100.7 not a higher low vs prior low 106.3 (need +10.0%)
- 2026-10-20 08:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2117 not a higher low vs prior low 0.2251 (need +10.0%)
- 2026-10-20 08:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.315 not a higher low vs prior low 9.83 (need +10.0%)
- 2026-10-20 08:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.56 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-20 08:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.326 (need +10.0%)
- 2026-10-20 08:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07626 not a higher low vs prior low 0.08144 (need +10.0%)
- 2026-10-20 08:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.048 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-20 08:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 56.77 not a higher low vs prior low 61.36 (need +10.0%)
- 2026-10-20 09:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.011e+04 not a higher low vs prior low 8.067e+04 (need +10.0%)
- 2026-10-20 09:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2335 not a higher low vs prior low 2415 (need +10.0%)
- 2026-10-20 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 100.7 not a higher low vs prior low 106.3 (need +10.0%)
- 2026-10-20 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2117 not a higher low vs prior low 0.2251 (need +10.0%)
- 2026-10-20 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.315 not a higher low vs prior low 9.83 (need +10.0%)
- 2026-10-20 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.56 not a higher low vs prior low 12.18 (need +10.0%)
- 2026-10-20 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.326 (need +10.0%)
- 2026-10-20 09:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07626 not a higher low vs prior low 0.08144 (need +10.0%)
- 2026-10-20 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.048 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-20 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 56.77 not a higher low vs prior low 61.36 (need +10.0%)

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

- equity 9,824.47 (started 10,000 at 2026-10-13 17:26Z), net -1.76% since start
- 24h -1.40%, 7d -1.76%, 30d -1.76%, max drawdown -4.99%
- fills 13 total, 13 in the last 7d
- costs 24.22 (fees 16.15 + slippage 8.07); gross pnl -151.31; cost coverage -6.25
- cash -0.00; positions: ADA 6863.3, AVAX 86.9342, DOGE 20854.4, ETH 0.817638, SOL 19.0822, XRP 1519.34
- last run 2026-10-20 09:10Z; halted today: False

last decisions (newest last):

- 2026-10-20 08:10Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.035 below threshold 0.05 | stay long: ratio to BTC z -1.40 vs 720h mean (entry -2.0, exit -0.25); vol 56% -> weigh...
- 2026-10-20 08:10Z ADA hold target 0.17 (held 0.15) — hold: weight change +0.016 below threshold 0.05 | stay long: ratio to BTC z -2.00 vs 720h mean (entry -2.0, exit -0.25); vol 67% -> weigh...
- 2026-10-20 08:10Z AVAX none target 0.17 (held 0.08) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-20 08:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.41 not below -2.0
- 2026-10-20 08:10Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: ratio to BTC z -1.70 vs 720h mean (entry -2.0, exit -0.25); vol 51% -> weigh...
- 2026-10-20 08:10Z DOGE hold target 0.17 (held 0.17) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.65 vs 720h mean (entry -2.0, exit -0.25); vol 58% -> weigh...
- 2026-10-20 08:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.34 not below -2.0
- 2026-10-20 08:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.09 not below -2.0
- 2026-10-20 09:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-20 09:10Z ETH hold target 0.17 (held 0.20) — hold: weight change -0.031 below threshold 0.05 | stay long: ratio to BTC z -1.78 vs 720h mean (entry -2.0, exit -0.25); vol 47% -> weigh...
- 2026-10-20 09:10Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.035 below threshold 0.05 | stay long: ratio to BTC z -1.45 vs 720h mean (entry -2.0, exit -0.25); vol 56% -> weigh...
- 2026-10-20 09:10Z ADA hold target 0.17 (held 0.15) — hold: weight change +0.016 below threshold 0.05 | stay long: ratio to BTC z -2.13 vs 720h mean (entry -2.0, exit -0.25); vol 67% -> weigh...
- 2026-10-20 09:10Z AVAX none target 0.17 (held 0.08) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-20 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.49 not below -2.0
- 2026-10-20 09:10Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: ratio to BTC z -1.73 vs 720h mean (entry -2.0, exit -0.25); vol 51% -> weigh...
- 2026-10-20 09:10Z DOGE hold target 0.17 (held 0.17) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.71 vs 720h mean (entry -2.0, exit -0.25); vol 58% -> weigh...
- 2026-10-20 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.25 not below -2.0
- 2026-10-20 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.17 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -25.15, -335 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 1 fill (1 buy / 0 sell), traded 834, gross pnl -15.69, -376 bps per round trip, avg half spread 1.6 bps, open 86.9342
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -93.29, -572 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 2 fills (1 buy / 1 sell), traded 1,597, gross pnl +75.58, +947 bps per round trip, avg half spread 2.0 bps
- ETH: 2 fills (1 buy / 1 sell), traded 2,992, gross pnl -59.01, -394 bps per round trip, avg half spread 0.0 bps, open 0.817638
- SOL: 2 fills (1 buy / 1 sell), traded 2,976, gross pnl +0.65, +4 bps per round trip, avg half spread 0.5 bps, open 19.0822
- XRP: 2 fills (1 buy / 1 sell), traded 2,984, gross pnl -34.42, -231 bps per round trip, avg half spread 0.9 bps, open 1519.34

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

- BTC: live 1542 candles, 2026-08-17 03:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1542 candles, 2026-08-17 03:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1542 candles, 2026-08-17 03:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1542 candles, 2026-08-17 03:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- AVAX: live 1542 candles, 2026-08-17 03:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- LINK: live 1542 candles, 2026-08-17 03:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- XRP: live 1514 candles, 2026-08-18 07:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1514 candles, 2026-08-18 07:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.2 bps
- DOT: live 1514 candles, 2026-08-18 07:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.6 bps
- LTC: live 1514 candles, 2026-08-18 07:00Z to 2026-10-20 08:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.2 bps
