# quantloop summary — generated 2026-10-28 00:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-21 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 41.8 of 60, 18.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -8.22% (max drawdown -27.50%, 327 fills) vs challenger1 -5.71% (max drawdown -12.36%, 91 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.45% (usual 0.54, this window 0.51) vs challenger1 -7.94% (usual 0.37, this window 0.44); the rule compares on skill, daily edge t +0.21 over 42 days
  trades: its 29 finished trades made -3.42% of its starting equity after costs (16 won, 13 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.09 over 42 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +6.54%, equal weight basket of 10 pairs +6.01%, basket max drawdown -19%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 36.7 of 60, 23.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.12% (max drawdown -27.50%, 289 fills) vs challenger2 -6.10% (max drawdown -6.56%, 13 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.55% (usual 0.54, this window 0.49) vs challenger2 -3.15% (usual 0.29, this window 0.14); the rule compares on skill, daily edge t +1.48 over 37 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.74 over 37 days)
  fills: 13 in 36.7 days; at this pace about 21 by day 60, under the 30 a promotion there needs, and about 42 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -2.10%, equal weight basket of 10 pairs -10.31%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 22.1 of 60, 37.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -17.40% (max drawdown -18.74%, 138 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.50% (usual 0.55, this window 0.33) vs challenger3 -0.81% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.82 over 22 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.77 over 22 days)
  fills: 10 in 22.1 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.97%, equal weight basket of 10 pairs -16.21%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 12.0 of 120, 108.0 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -3.85% (max drawdown -9.87%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -0.58% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.17 over 12 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.74% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.17 over 12 days)
  market over the window: BTC -1.85%, equal weight basket of 10 pairs -6.19%, basket max drawdown -10%, basket realised vol 47% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,178.12 (started 10,000 at 2026-09-16 03:55Z), net -8.22% since start
- 24h +0.89%, 7d -3.92%, 30d -25.72%, max drawdown -27.50%
- fills 327 total, 35 in the last 7d
- costs 765.68 (fees 507.46 + slippage 258.22); gross pnl -56.20; cost coverage -0.07
- cash -0.00; positions: DOGE 23412.4, ETH 0.779375, LTC 32.2637, SOL 18.0659, XRP 1383.97
- last run 2026-10-28 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 23:10Z SOL hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return -0.32% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-27 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.53% not above entry band +1.0%
- 2026-10-27 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.06% not above entry band +1.0%
- 2026-10-27 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.20% not above entry band +1.0%
- 2026-10-27 23:10Z XRP hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.56% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-27 23:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.84% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-27 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.78% not above entry band +1.0%
- 2026-10-27 23:10Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.46% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.04% not above entry band +1.0%
- 2026-10-28 00:10Z ETH hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return -0.35% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-28 00:10Z SOL hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return -1.00% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-28 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.03% not above entry band +1.0%
- 2026-10-28 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-10-28 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.38% not above entry band +1.0%
- 2026-10-28 00:10Z XRP hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +2.47% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 00:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.80% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.49% not above entry band +1.0%
- 2026-10-28 00:10Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.32% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 27 fills (12 buy / 15 sell), traded 37,592, gross pnl -30.48, -16 bps per round trip, avg half spread 2.0 bps
- AVAX: 37 fills (17 buy / 20 sell), traded 64,485, gross pnl +381.31, +118 bps per round trip, avg half spread 1.1 bps
- BTC: 31 fills (17 buy / 14 sell), traded 46,476, gross pnl -18.60, -8 bps per round trip, avg half spread 0.1 bps
- DOGE: 29 fills (15 buy / 14 sell), traded 40,083, gross pnl -213.92, -107 bps per round trip, avg half spread 0.8 bps, open 23412.4
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 31 fills (16 buy / 15 sell), traded 47,650, gross pnl -219.29, -92 bps per round trip, avg half spread 0.0 bps, open 0.779375
- LINK: 35 fills (17 buy / 18 sell), traded 63,192, gross pnl -286.39, -91 bps per round trip, avg half spread 1.8 bps
- LTC: 35 fills (17 buy / 18 sell), traded 51,640, gross pnl +481.63, +187 bps per round trip, avg half spread 1.6 bps, open 32.2637
- SOL: 33 fills (18 buy / 15 sell), traded 53,177, gross pnl -63.10, -24 bps per round trip, avg half spread 0.5 bps, open 18.0659
- XRP: 30 fills (16 buy / 14 sell), traded 43,406, gross pnl +52.50, +24 bps per round trip, avg half spread 0.3 bps, open 1383.97

last fills:

- 2026-10-27 00:10Z buy XRP 2,275 @ 1.30863 fee 2.28 slip 1.14 (half spread 0.1 bps)
- 2026-10-27 15:10Z buy DOGE 2,277 @ 0.0777607 fee 2.28 slip 1.14 (half spread 0.0 bps)
- 2026-10-27 15:10Z buy LTC 2,277 @ 56.3682 fee 2.28 slip 1.14 (half spread 1.8 bps)
- 2026-10-27 16:10Z sell XRP 468 @ 1.31778 fee 0.47 slip 0.23 (half spread 0.0 bps)
- 2026-10-27 16:10Z sell DOGE 457 @ 0.0778974 fee 0.46 slip 0.23 (half spread 0.0 bps)
- 2026-10-27 16:10Z sell LTC 460 @ 56.5267 fee 0.46 slip 0.23 (half spread 0.9 bps)
- 2026-10-27 16:10Z buy ETH 1,825 @ 2341.5 fee 1.82 slip 0.91 (half spread 0.0 bps)
- 2026-10-27 16:10Z buy SOL 1,820 @ 100.735 fee 1.82 slip 0.91 (half spread 0.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,418.58 (started 10,000 at 2026-09-16 03:55Z), net -5.81% since start
- 24h +0.29%, 7d -2.34%, 30d -8.47%, max drawdown -12.36%
- fills 91 total, 16 in the last 7d
- costs 187.02 (fees 124.59 + slippage 62.43); gross pnl -394.40; cost coverage -2.11
- cash 371.02; positions: ADA 6514.27, AVAX 152.521, BTC 0.0166116, DOT 1280.66, LINK 86.9977, LTC 24.0795, SOL 13.3337
- last run 2026-10-28 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 23:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: z -0.97 vs 240h mean (entry -2.0, exit -0.5); vol 39% -> weight 0.25
- 2026-10-27 23:10Z ADA hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.11 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-27 23:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.002 below threshold 0.05 | stay long: z -0.95 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-27 23:10Z LINK hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: z -0.89 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-27 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.71 not below -2.0
- 2026-10-27 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.11 not below -2.0
- 2026-10-27 23:10Z DOT hold target 0.14 (held 0.14) — hold: weight change +0.007 below threshold 0.05 | stay long: z -1.52 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-10-27 23:10Z LTC hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.80 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-28 00:10Z BTC hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: z -0.51 vs 240h mean (entry -2.0, exit -0.5); vol 27% -> weight 0.25
- 2026-10-28 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.75 not below -2.0
- 2026-10-28 00:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: z -0.95 vs 240h mean (entry -2.0, exit -0.5); vol 39% -> weight 0.25
- 2026-10-28 00:10Z ADA hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.03 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-28 00:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.002 below threshold 0.05 | stay long: z -0.84 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-28 00:10Z LINK hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: z -0.76 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-28 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.88 not below -2.0
- 2026-10-28 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.06 not below -2.0
- 2026-10-28 00:10Z DOT hold target 0.14 (held 0.14) — hold: weight change +0.007 below threshold 0.05 | stay long: z -1.48 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-10-28 00:10Z LTC hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.71 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 7 fills (3 buy / 4 sell), traded 11,227, gross pnl +74.69, +133 bps per round trip, avg half spread 1.3 bps, open 6514.27
- AVAX: 9 fills (5 buy / 4 sell), traded 11,368, gross pnl +73.58, +129 bps per round trip, avg half spread 1.0 bps, open 152.521
- BTC: 6 fills (4 buy / 2 sell), traded 8,801, gross pnl +85.75, +195 bps per round trip, avg half spread 0.1 bps, open 0.0166116
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 5 fills (2 buy / 3 sell), traded 8,427, gross pnl -249.73, -593 bps per round trip, avg half spread 1.7 bps, open 1280.66
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 10 fills (6 buy / 4 sell), traded 10,977, gross pnl +41.01, +75 bps per round trip, avg half spread 1.1 bps, open 86.9977
- LTC: 10 fills (5 buy / 5 sell), traded 12,325, gross pnl -4.35, -7 bps per round trip, avg half spread 1.2 bps, open 24.0795
- SOL: 10 fills (6 buy / 4 sell), traded 14,508, gross pnl -142.23, -196 bps per round trip, avg half spread 0.5 bps, open 13.3337
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-24 10:10Z sell AVAX 967 @ 8.85657 fee 0.97 slip 0.48 (half spread 2.3 bps)
- 2026-10-24 10:10Z sell DOT 997 @ 1.05477 fee 1.00 slip 0.50 (half spread 1.9 bps)
- 2026-10-24 10:10Z sell LTC 540 @ 56.1069 fee 0.54 slip 0.27 (half spread 0.9 bps)
- 2026-10-24 10:10Z buy SOL 1,352 @ 101.396 fee 1.35 slip 0.68 (half spread 0.5 bps)
- 2026-10-24 10:10Z buy DOGE 1,352 @ 0.0772311 fee 1.35 slip 0.68 (half spread 0.5 bps)
- 2026-10-24 15:10Z buy BTC 341 @ 79791.2 fee 0.34 slip 0.17 (half spread 0.5 bps)
- 2026-10-27 17:10Z sell DOGE 1,368 @ 0.0781397 fee 1.37 slip 0.68 (half spread 0.1 bps)
- 2026-10-27 17:10Z buy BTC 994 @ 80577.9 fee 0.99 slip 0.50 (half spread 0.0 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,296.90 (started 10,000 at 2026-09-16 23:20Z), net +2.97% since start
- 24h -0.04%, 7d -4.35%, 30d -6.10%, max drawdown -7.30%
- fills 45 total, 8 in the last 7d
- costs 130.61 (fees 86.64 + slippage 43.97); gross pnl 427.51; cost coverage 3.27
- cash 7,723.00; positions: XRP 1940.8
- last run 2026-10-28 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 101.2 not above 120h high 104.9
- 2026-10-27 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2052 not above 120h high 0.2179
- 2026-10-27 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.917 not above 120h high 9.314
- 2026-10-27 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.52 not above 120h high 12.23
- 2026-10-27 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.326 not above 120h high 1.328
- 2026-10-27 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07869 not above 120h high 0.08035
- 2026-10-27 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9985 not above 120h high 1.197
- 2026-10-27 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 57.01 not above 120h high 59.69
- 2026-10-28 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.08e+04 not above 120h high 8.19e+04
- 2026-10-28 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2347 not above 120h high 2413
- 2026-10-28 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 101.2 not above 120h high 104.9
- 2026-10-28 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2057 not above 120h high 0.2179
- 2026-10-28 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.954 not above 120h high 9.314
- 2026-10-28 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.57 not above 120h high 12.23
- 2026-10-28 00:10Z XRP buy target 0.25 (held 0.00) — enter long: squeeze in last 72h (168h vol at or below its own 25% percentile over 1440h) then broke above 120h high 1.328 at 1.33; realis...
- 2026-10-28 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07898 not above 120h high 0.08035
- 2026-10-28 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1 not above 120h high 1.197
- 2026-10-28 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 57.16 not above 120h high 59.69

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 7 fills (4 buy / 3 sell), traded 16,132, gross pnl -117.78, -146 bps per round trip, avg half spread 0.0 bps
- DOGE: 5 fills (3 buy / 2 sell), traded 8,238, gross pnl -90.86, -221 bps per round trip, avg half spread 0.7 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 5 fills (3 buy / 2 sell), traded 9,039, gross pnl -129.64, -287 bps per round trip, avg half spread 0.2 bps, open 1940.8

last fills:

- 2026-10-21 08:10Z buy XRP 2,694 @ 1.34334 fee 2.69 slip 1.35 (half spread 0.2 bps)
- 2026-10-21 14:10Z buy DOGE 2,706 @ 0.0820032 fee 2.71 slip 1.35 (half spread 0.0 bps)
- 2026-10-21 16:10Z buy ADA 2,672 @ 0.228184 fee 2.67 slip 1.34 (half spread 0.9 bps)
- 2026-10-22 09:10Z sell ADA 2,515 @ 0.21479 fee 2.51 slip 1.26 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell BTC 2,632 @ 81047.4 fee 2.63 slip 1.32 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell DOGE 2,584 @ 0.0783045 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-23 23:06Z sell XRP 2,581 @ 1.28694 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 00:10Z buy XRP 2,575 @ 1.32687 fee 2.58 slip 1.29 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-28 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 23:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-27 23:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2166 (need +10.0%)
- 2026-10-27 23:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-27 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.86 (need +10.0%)
- 2026-10-27 23:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.286 (need +10.0%)
- 2026-10-27 23:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07815 (need +10.0%)
- 2026-10-27 23:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-27 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)
- 2026-10-28 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-28 00:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2338 (need +10.0%)
- 2026-10-28 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-28 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2166 (need +10.0%)
- 2026-10-28 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-28 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.86 (need +10.0%)
- 2026-10-28 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.286 (need +10.0%)
- 2026-10-28 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07815 (need +10.0%)
- 2026-10-28 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-28 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)

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

- equity 9,611.38 (started 10,000 at 2026-10-13 17:26Z), net -3.89% since start
- 24h +0.48%, 7d -5.14%, 30d -3.89%, max drawdown -9.87%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -359.40; cost coverage -12.30
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-28 00:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 23:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.24 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-27 23:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -1.68 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-10-27 23:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.69 vs 720h mean (entry -2.0, exit -0.25); vol 54% -> weigh...
- 2026-10-27 23:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.37 not below -2.0
- 2026-10-27 23:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -0.48 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-27 23:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.028 below threshold 0.05 | stay long: ratio to BTC z -0.95 vs 720h mean (entry -2.0, exit -0.25); vol 42% -> weigh...
- 2026-10-27 23:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.44 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-10-27 23:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.32 not below -2.0
- 2026-10-28 00:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-28 00:10Z ETH hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.23 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 00:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.23 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 00:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -1.63 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-10-28 00:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.62 vs 720h mean (entry -2.0, exit -0.25); vol 54% -> weigh...
- 2026-10-28 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.31 not below -2.0
- 2026-10-28 00:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -0.40 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-28 00:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.028 below threshold 0.05 | stay long: ratio to BTC z -0.88 vs 720h mean (entry -2.0, exit -0.25); vol 43% -> weigh...
- 2026-10-28 00:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.39 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-10-28 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.27 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -92.47, -1231 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -44.24, -621 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -90.99, -558 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl +28.51, +213 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -93.51, -529 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -58.78, -333 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -7.90, -44 bps per round trip, avg half spread 0.6 bps, open 1066.7

last fills:

- 2026-10-18 20:10Z buy DOT 761 @ 1.05068 fee 0.76 slip 0.38 (half spread 1.4 bps)
- 2026-10-19 16:10Z sell DOT 836 @ 1.15392 fee 0.84 slip 0.42 (half spread 2.6 bps)
- 2026-10-19 16:10Z buy AVAX 834 @ 9.5953 fee 0.83 slip 0.42 (half spread 1.6 bps)
- 2026-10-24 15:10Z sell ETH 544 @ 2316.84 fee 0.54 slip 0.27 (half spread 1.6 bps)
- 2026-10-24 15:10Z sell SOL 552 @ 99.6651 fee 0.55 slip 0.28 (half spread 0.5 bps)
- 2026-10-24 15:10Z sell XRP 573 @ 1.2657 fee 0.57 slip 0.29 (half spread 0.0 bps)
- 2026-10-24 15:10Z buy AVAX 590 @ 8.76038 fee 0.59 slip 0.29 (half spread 2.3 bps)
- 2026-10-24 15:10Z buy DOT 1,076 @ 1.04407 fee 1.08 slip 0.54 (half spread 2.4 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1725 candles, 2026-08-17 03:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1725 candles, 2026-08-17 03:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1725 candles, 2026-08-17 03:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1725 candles, 2026-08-17 03:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- AVAX: live 1725 candles, 2026-08-17 03:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LINK: live 1725 candles, 2026-08-17 03:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- XRP: live 1697 candles, 2026-08-18 07:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1697 candles, 2026-08-18 07:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 1697 candles, 2026-08-18 07:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1697 candles, 2026-08-18 07:00Z to 2026-10-27 23:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.2 bps
