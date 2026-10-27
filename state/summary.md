# quantloop summary — generated 2026-10-27 01:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-20 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 40.8 of 60, 19.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -9.03% (max drawdown -27.26%, 320 fills) vs challenger1 -5.98% (max drawdown -12.36%, 89 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.80% (usual 0.54, this window 0.51) vs challenger1 -7.89% (usual 0.37, this window 0.43); the rule compares on skill, daily edge t +0.24 over 41 days
  trades: its 28 finished trades made -3.56% of its starting equity after costs (15 won, 13 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.10 over 41 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +5.60%, equal weight basket of 10 pairs +5.15%, basket max drawdown -19%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 35.7 of 60, 24.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.83% (max drawdown -27.26%, 282 fills) vs challenger2 -6.06% (max drawdown -6.53%, 12 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.85% (usual 0.54, this window 0.49) vs challenger2 -2.90% (usual 0.29, this window 0.14); the rule compares on skill, daily edge t +1.57 over 36 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.68 over 36 days)
  fills: 12 in 35.7 days; at this pace about 20 by day 60, under the 30 a promotion there needs, and about 40 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -2.96%, equal weight basket of 10 pairs -11.07%, basket max drawdown -19%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 21.1 of 60, 38.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -18.13% (max drawdown -18.47%, 131 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.84% (usual 0.55, this window 0.32) vs challenger3 -0.79% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.93 over 21 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.74 over 21 days)
  fills: 10 in 21.1 days, 8 of them in the hour it began; at this pace about 19 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -6.80%, equal weight basket of 10 pairs -16.91%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 11.1 of 120, 108.9 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -4.31% (max drawdown -9.60%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -0.62% (usual 0.53, this window 0.96); the rule compares on skill, daily edge t -0.19 over 11 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.60% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.19 over 11 days)
  market over the window: BTC -2.72%, equal weight basket of 10 pairs -6.99%, basket max drawdown -10%, basket realised vol 48% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,097.27 (started 10,000 at 2026-09-16 03:55Z), net -9.03% since start
- 24h -0.05%, 7d -5.03%, 30d -25.66%, max drawdown -27.26%
- fills 320 total, 39 in the last 7d
- costs 751.31 (fees 497.88 + slippage 253.43); gross pnl -151.42; cost coverage -0.20
- cash 6,823.93; positions: XRP 1738.76
- last run 2026-10-27 01:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.90% not above entry band +1.0% and price below 24h EMA
- 2026-10-27 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.04% not above entry band +1.0%
- 2026-10-27 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.97% not above entry band +1.0%
- 2026-10-27 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.65% not above entry band +1.0% and price below 24h EMA
- 2026-10-27 00:10Z XRP buy target 0.25 (held 0.00) — enter long: 72h return +1.04% vs entry band +1.0% and price above 24h EMA; realised vol 47% -> weight 0.25
- 2026-10-27 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.14% not above entry band +1.0%
- 2026-10-27 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.98% not above entry band +1.0% and price below 24h EMA
- 2026-10-27 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.89% not above entry band +1.0%
- 2026-10-27 01:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.55% not above entry band +1.0%
- 2026-10-27 01:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.04% not above entry band +1.0%
- 2026-10-27 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.44% not above entry band +1.0% and price below 24h EMA
- 2026-10-27 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.84% not above entry band +1.0%
- 2026-10-27 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.68% not above entry band +1.0%
- 2026-10-27 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.94% not above entry band +1.0% and price below 24h EMA
- 2026-10-27 01:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.70% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-27 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.81% not above entry band +1.0%
- 2026-10-27 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.60% not above entry band +1.0% and price below 24h EMA
- 2026-10-27 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.39% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 27 fills (12 buy / 15 sell), traded 37,592, gross pnl -30.48, -16 bps per round trip, avg half spread 2.0 bps
- AVAX: 37 fills (17 buy / 20 sell), traded 64,485, gross pnl +381.31, +118 bps per round trip, avg half spread 1.1 bps
- BTC: 31 fills (17 buy / 14 sell), traded 46,476, gross pnl -18.60, -8 bps per round trip, avg half spread 0.1 bps
- DOGE: 27 fills (14 buy / 13 sell), traded 37,349, gross pnl -242.09, -130 bps per round trip, avg half spread 0.9 bps
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 30 fills (15 buy / 15 sell), traded 45,825, gross pnl -221.92, -97 bps per round trip, avg half spread 0.0 bps
- LINK: 35 fills (17 buy / 18 sell), traded 63,192, gross pnl -286.39, -91 bps per round trip, avg half spread 1.8 bps
- LTC: 33 fills (16 buy / 17 sell), traded 48,903, gross pnl +455.37, +186 bps per round trip, avg half spread 1.6 bps
- SOL: 32 fills (17 buy / 15 sell), traded 51,357, gross pnl -71.41, -28 bps per round trip, avg half spread 0.5 bps
- XRP: 29 fills (16 buy / 13 sell), traded 42,939, gross pnl +22.64, +11 bps per round trip, avg half spread 0.3 bps, open 1738.76

last fills:

- 2026-10-23 03:10Z buy LINK 2,310 @ 12.1923 fee 2.31 slip 1.15 (half spread 0.0 bps)
- 2026-10-23 06:10Z buy XRP 2,317 @ 1.32625 fee 2.32 slip 1.16 (half spread 0.0 bps)
- 2026-10-23 09:10Z buy DOGE 2,289 @ 0.0803815 fee 2.29 slip 1.14 (half spread 0.0 bps)
- 2026-10-23 14:10Z sell DOT 2,272 @ 1.13687 fee 2.27 slip 1.15 (half spread 3.1 bps)
- 2026-10-23 15:00Z sell LINK 2,276 @ 12.0133 fee 2.28 slip 1.14 (half spread 1.7 bps)
- 2026-10-23 15:00Z sell XRP 2,291 @ 1.31097 fee 2.29 slip 1.15 (half spread 0.0 bps)
- 2026-10-23 15:00Z sell DOGE 2,273 @ 0.0798346 fee 2.27 slip 1.14 (half spread 0.0 bps)
- 2026-10-27 00:10Z buy XRP 2,275 @ 1.30863 fee 2.28 slip 1.14 (half spread 0.1 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,391.30 (started 10,000 at 2026-09-16 03:55Z), net -6.09% since start
- 24h +0.49%, 7d -0.32%, 30d -8.73%, max drawdown -12.36%
- fills 89 total, 20 in the last 7d
- costs 183.47 (fees 122.23 + slippage 61.24); gross pnl -425.23; cost coverage -2.32
- cash 0.00; positions: ADA 6514.27, AVAX 152.521, BTC 0.00426951, DOGE 17505.6, DOT 1280.66, LINK 86.9977, LTC 24.0795, SOL 13.3337
- last run 2026-10-27 01:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 00:10Z SOL hold target 0.12 (held 0.14) — hold: weight change -0.018 below threshold 0.05 | stay long: z -1.46 vs 240h mean (entry -2.0, exit -0.5); vol 45% -> weight 0.25
- 2026-10-27 00:10Z ADA hold target 0.12 (held 0.14) — hold: weight change -0.018 below threshold 0.05 | stay long: z -1.23 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-27 00:10Z AVAX hold target 0.12 (held 0.15) — hold: weight change -0.020 below threshold 0.05 | stay long: z -1.07 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-10-27 00:10Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.020 below threshold 0.05 | stay long: z -1.55 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-10-27 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.03 not below -2.0
- 2026-10-27 00:10Z DOGE hold target 0.12 (held 0.14) — hold: weight change -0.020 below threshold 0.05 | stay long: z -0.86 vs 240h mean (entry -2.0, exit -0.5); vol 47% -> weight 0.25
- 2026-10-27 00:10Z DOT hold target 0.12 (held 0.14) — hold: weight change -0.013 below threshold 0.05 | stay long: z -1.80 vs 240h mean (entry -2.0, exit -0.5); vol 80% -> weight 0.25
- 2026-10-27 00:10Z LTC hold target 0.12 (held 0.15) — hold: weight change -0.020 below threshold 0.05 | stay long: z -1.18 vs 240h mean (entry -2.0, exit -0.5); vol 50% -> weight 0.25
- 2026-10-27 01:10Z BTC none target 0.12 (held 0.04) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-27 01:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.50 not below -2.0
- 2026-10-27 01:10Z SOL hold target 0.12 (held 0.14) — hold: weight change -0.018 below threshold 0.05 | stay long: z -1.48 vs 240h mean (entry -2.0, exit -0.5); vol 45% -> weight 0.25
- 2026-10-27 01:10Z ADA hold target 0.12 (held 0.14) — hold: weight change -0.018 below threshold 0.05 | stay long: z -1.31 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-27 01:10Z AVAX hold target 0.12 (held 0.14) — hold: weight change -0.020 below threshold 0.05 | stay long: z -1.14 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-10-27 01:10Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.020 below threshold 0.05 | stay long: z -1.57 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-10-27 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.03 not below -2.0
- 2026-10-27 01:10Z DOGE hold target 0.12 (held 0.15) — hold: weight change -0.020 below threshold 0.05 | stay long: z -0.83 vs 240h mean (entry -2.0, exit -0.5); vol 47% -> weight 0.25
- 2026-10-27 01:10Z DOT hold target 0.12 (held 0.14) — hold: weight change -0.012 below threshold 0.05 | stay long: z -1.87 vs 240h mean (entry -2.0, exit -0.5); vol 80% -> weight 0.25
- 2026-10-27 01:10Z LTC hold target 0.12 (held 0.15) — hold: weight change -0.020 below threshold 0.05 | stay long: z -1.20 vs 240h mean (entry -2.0, exit -0.5); vol 50% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 7 fills (3 buy / 4 sell), traded 11,227, gross pnl +80.01, +143 bps per round trip, avg half spread 1.3 bps, open 6514.27
- AVAX: 9 fills (5 buy / 4 sell), traded 11,368, gross pnl +71.67, +126 bps per round trip, avg half spread 1.0 bps, open 152.521
- BTC: 5 fills (3 buy / 2 sell), traded 7,807, gross pnl +81.86, +210 bps per round trip, avg half spread 0.1 bps, open 0.00426951
- DOGE: 11 fills (6 buy / 5 sell), traded 16,452, gross pnl -133.99, -163 bps per round trip, avg half spread 0.3 bps, open 17505.6
- DOT: 5 fills (2 buy / 3 sell), traded 8,427, gross pnl -240.77, -571 bps per round trip, avg half spread 1.7 bps, open 1280.66
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 10 fills (6 buy / 4 sell), traded 10,977, gross pnl +24.32, +44 bps per round trip, avg half spread 1.1 bps, open 86.9977
- LTC: 10 fills (5 buy / 5 sell), traded 12,325, gross pnl -15.67, -25 bps per round trip, avg half spread 1.2 bps, open 24.0795
- SOL: 10 fills (6 buy / 4 sell), traded 14,508, gross pnl -147.70, -204 bps per round trip, avg half spread 0.5 bps, open 13.3337
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-24 09:10Z buy LINK 1,009 @ 11.5926 fee 1.01 slip 0.50 (half spread 0.8 bps)
- 2026-10-24 10:10Z sell ADA 547 @ 0.207395 fee 0.55 slip 0.27 (half spread 0.2 bps)
- 2026-10-24 10:10Z sell AVAX 967 @ 8.85657 fee 0.97 slip 0.48 (half spread 2.3 bps)
- 2026-10-24 10:10Z sell DOT 997 @ 1.05477 fee 1.00 slip 0.50 (half spread 1.9 bps)
- 2026-10-24 10:10Z sell LTC 540 @ 56.1069 fee 0.54 slip 0.27 (half spread 0.9 bps)
- 2026-10-24 10:10Z buy SOL 1,352 @ 101.396 fee 1.35 slip 0.68 (half spread 0.5 bps)
- 2026-10-24 10:10Z buy DOGE 1,352 @ 0.0772311 fee 1.35 slip 0.68 (half spread 0.5 bps)
- 2026-10-24 15:10Z buy BTC 341 @ 79791.2 fee 0.34 slip 0.17 (half spread 0.5 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,300.76 (started 10,000 at 2026-09-16 23:20Z), net +3.01% since start
- 24h +0.00%, 7d -4.41%, 30d -6.06%, max drawdown -7.26%
- fills 44 total, 8 in the last 7d
- costs 126.75 (fees 84.07 + slippage 42.68); gross pnl 427.51; cost coverage 3.37
- cash 10,300.76; positions: none
- last run 2026-10-27 01:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 100.8 not above 120h high 107.1
- 2026-10-27 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2064 not above 120h high 0.2258
- 2026-10-27 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.962 not above 120h high 9.662
- 2026-10-27 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.39 not above 120h high 12.56
- 2026-10-27 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.307 not above 120h high 1.364
- 2026-10-27 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07762 not above 120h high 0.08189
- 2026-10-27 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.009 not above 120h high 1.197
- 2026-10-27 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 56.71 not above 120h high 61.62
- 2026-10-27 01:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.009e+04 not above 120h high 8.415e+04
- 2026-10-27 01:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-27 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 100.7 not above 120h high 107.1
- 2026-10-27 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2057 not above 120h high 0.2258
- 2026-10-27 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.931 not above 120h high 9.662
- 2026-10-27 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.38 not above 120h high 12.56
- 2026-10-27 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.307 not above 120h high 1.363
- 2026-10-27 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07767 not above 120h high 0.08186
- 2026-10-27 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.004 not above 120h high 1.197
- 2026-10-27 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 56.66 not above 120h high 61.62

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
- XRP: 4 fills (2 buy / 2 sell), traded 6,464, gross pnl -129.64, -401 bps per round trip, avg half spread 0.2 bps

last fills:

- 2026-10-20 15:10Z buy BTC 2,694 @ 82967.9 fee 2.69 slip 1.35 (half spread 0.0 bps)
- 2026-10-21 08:10Z buy XRP 2,694 @ 1.34334 fee 2.69 slip 1.35 (half spread 0.2 bps)
- 2026-10-21 14:10Z buy DOGE 2,706 @ 0.0820032 fee 2.71 slip 1.35 (half spread 0.0 bps)
- 2026-10-21 16:10Z buy ADA 2,672 @ 0.228184 fee 2.67 slip 1.34 (half spread 0.9 bps)
- 2026-10-22 09:10Z sell ADA 2,515 @ 0.21479 fee 2.51 slip 1.26 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell BTC 2,632 @ 81047.4 fee 2.63 slip 1.32 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell DOGE 2,584 @ 0.0783045 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-23 23:06Z sell XRP 2,581 @ 1.28694 fee 2.58 slip 1.29 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-27 01:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 00:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.66 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-27 00:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2187 (need +10.0%)
- 2026-10-27 00:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.773 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-27 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.3 not a higher low vs prior low 11.88 (need +10.0%)
- 2026-10-27 00:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.287 (need +10.0%)
- 2026-10-27 00:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07826 (need +10.0%)
- 2026-10-27 00:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.004 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-27 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)
- 2026-10-27 01:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-27 01:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2338 (need +10.0%)
- 2026-10-27 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.66 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-27 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2187 (need +10.0%)
- 2026-10-27 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.773 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-27 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.3 not a higher low vs prior low 11.88 (need +10.0%)
- 2026-10-27 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.287 (need +10.0%)
- 2026-10-27 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07826 (need +10.0%)
- 2026-10-27 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.004 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-27 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)

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

- equity 9,565.49 (started 10,000 at 2026-10-13 17:26Z), net -4.35% since start
- 24h +0.85%, 7d -3.19%, 30d -4.35%, max drawdown -9.60%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -405.29; cost coverage -13.87
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-27 01:10Z; halted today: False

last decisions (newest last):

- 2026-10-27 00:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.19 vs 720h mean (entry -2.0, exit -0.25); vol 45% -> weigh...
- 2026-10-27 00:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.005 below threshold 0.05 | stay long: ratio to BTC z -1.56 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-10-27 00:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.60 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-10-27 00:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.51 not below -2.0
- 2026-10-27 00:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.63 vs 720h mean (entry -2.0, exit -0.25); vol 47% -> weigh...
- 2026-10-27 00:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.026 below threshold 0.05 | stay long: ratio to BTC z -1.07 vs 720h mean (entry -2.0, exit -0.25); vol 47% -> weigh...
- 2026-10-27 00:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.034 below threshold 0.05 | stay long: ratio to BTC z -2.31 vs 720h mean (entry -2.0, exit -0.25); vol 80% -> weigh...
- 2026-10-27 00:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.31 not below -2.0
- 2026-10-27 01:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-27 01:10Z ETH hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.35 vs 720h mean (entry -2.0, exit -0.25); vol 44% -> weigh...
- 2026-10-27 01:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.22 vs 720h mean (entry -2.0, exit -0.25); vol 45% -> weigh...
- 2026-10-27 01:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.005 below threshold 0.05 | stay long: ratio to BTC z -1.63 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-10-27 01:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.66 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-10-27 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.53 not below -2.0
- 2026-10-27 01:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.65 vs 720h mean (entry -2.0, exit -0.25); vol 47% -> weigh...
- 2026-10-27 01:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.027 below threshold 0.05 | stay long: ratio to BTC z -1.07 vs 720h mean (entry -2.0, exit -0.25); vol 47% -> weigh...
- 2026-10-27 01:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.035 below threshold 0.05 | stay long: ratio to BTC z -2.43 vs 720h mean (entry -2.0, exit -0.25); vol 80% -> weigh...
- 2026-10-27 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.34 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -86.87, -1157 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -46.17, -648 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -112.39, -689 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl +35.72, +267 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -103.35, -584 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -64.34, -365 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -27.91, -157 bps per round trip, avg half spread 0.6 bps, open 1066.7

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

- BTC: live 1702 candles, 2026-08-17 03:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1702 candles, 2026-08-17 03:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1702 candles, 2026-08-17 03:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1702 candles, 2026-08-17 03:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- AVAX: live 1702 candles, 2026-08-17 03:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.2 bps
- LINK: live 1702 candles, 2026-08-17 03:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- XRP: live 1674 candles, 2026-08-18 07:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1674 candles, 2026-08-18 07:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.2 bps
- DOT: live 1674 candles, 2026-08-18 07:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1674 candles, 2026-08-18 07:00Z to 2026-10-27 00:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.2 bps
