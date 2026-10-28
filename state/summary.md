# quantloop summary — generated 2026-10-28 17:11Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-21 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 42.5 of 60, 17.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -8.75% (max drawdown -27.50%, 342 fills) vs challenger1 -6.38% (max drawdown -12.36%, 103 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.83% (usual 0.54, this window 0.52) vs challenger1 -8.50% (usual 0.37, this window 0.45); the rule compares on skill, daily edge t +0.20 over 42 days
  trades: its 33 finished trades made -3.12% of its starting equity after costs (20 won, 13 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.18 over 42 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +6.15%, equal weight basket of 10 pairs +5.71%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 37.4 of 60, 22.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.59% (max drawdown -27.50%, 304 fills) vs challenger2 -6.85% (max drawdown -7.31%, 15 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.89% (usual 0.54, this window 0.50) vs challenger2 -3.84% (usual 0.29, this window 0.14); the rule compares on skill, daily edge t +1.44 over 37 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.87 over 37 days)
  fills: 15 in 37.4 days; at this pace about 24 by day 60, under the 30 a promotion there needs, and about 48 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -2.46%, equal weight basket of 10 pairs -10.55%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 22.8 of 60, 37.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -17.88% (max drawdown -18.74%, 153 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.85% (usual 0.55, this window 0.35) vs challenger3 -0.81% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.91 over 23 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.76 over 23 days)
  fills: 10 in 22.8 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -6.32%, equal weight basket of 10 pairs -16.46%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 12.8 of 120, 107.2 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -4.61% (max drawdown -9.87%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -1.20% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.37 over 13 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.74% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.37 over 13 days)
  market over the window: BTC -2.21%, equal weight basket of 10 pairs -6.46%, basket max drawdown -10%, basket realised vol 46% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,124.51 (started 10,000 at 2026-09-16 03:55Z), net -8.75% since start
- 24h +0.11%, 7d -6.81%, 30d -22.12%, max drawdown -27.50%
- fills 342 total, 50 in the last 7d
- costs 786.37 (fees 521.25 + slippage 265.12); gross pnl -89.12; cost coverage -0.11
- cash 1,004.00; positions: AVAX 113.085, BTC 0.0126241, DOGE 12831.6, ETH 0.434103, LINK 87.1889, LTC 17.8352, SOL 10.026, XRP 772.576
- last run 2026-10-28 17:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 16:10Z SOL hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return -0.57% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.29% not above entry band +1.0% and price below 24h EMA
- 2026-10-28 16:10Z AVAX hold target 0.12 (held 0.11) — hold: weight change +0.015 below threshold 0.05 | stay long: 72h return -0.33% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 16:10Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.015 below threshold 0.05 | stay long: 72h return +1.19% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 16:10Z XRP hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +0.85% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 16:10Z DOGE hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +2.68% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.44% not above entry band +1.0%
- 2026-10-28 16:10Z LTC hold target 0.12 (held 0.11) — hold: weight change +0.011 below threshold 0.05 | stay long: 72h return +2.44% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 17:10Z BTC hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return -0.24% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z ETH hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return -0.92% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z SOL hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return -0.75% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-28 17:10Z AVAX hold target 0.12 (held 0.11) — hold: weight change +0.015 below threshold 0.05 | stay long: 72h return -0.93% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.015 below threshold 0.05 | stay long: 72h return +0.31% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z XRP hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +0.50% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z DOGE hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +2.07% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-28 17:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.88% not above entry band +1.0% and price below 24h EMA
- 2026-10-28 17:10Z LTC hold target 0.12 (held 0.12) — hold: weight change +0.009 below threshold 0.05 | stay long: 72h return +3.54% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 29 fills (13 buy / 16 sell), traded 39,626, gross pnl -52.98, -27 bps per round trip, avg half spread 2.0 bps
- AVAX: 38 fills (18 buy / 20 sell), traded 65,505, gross pnl +360.73, +110 bps per round trip, avg half spread 1.2 bps, open 113.085
- BTC: 32 fills (18 buy / 14 sell), traded 47,504, gross pnl -31.76, -13 bps per round trip, avg half spread 0.1 bps, open 0.0126241
- DOGE: 30 fills (15 buy / 15 sell), traded 40,931, gross pnl -200.81, -98 bps per round trip, avg half spread 0.8 bps, open 12831.6
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 34 fills (17 buy / 17 sell), traded 49,405, gross pnl -214.63, -87 bps per round trip, avg half spread 0.0 bps, open 0.434103
- LINK: 38 fills (19 buy / 19 sell), traded 65,801, gross pnl -300.93, -91 bps per round trip, avg half spread 1.8 bps, open 87.1889
- LTC: 36 fills (17 buy / 19 sell), traded 52,471, gross pnl +528.11, +201 bps per round trip, avg half spread 1.6 bps, open 17.8352
- SOL: 35 fills (19 buy / 16 sell), traded 56,030, gross pnl -80.57, -29 bps per round trip, avg half spread 0.5 bps, open 10.026
- XRP: 31 fills (16 buy / 15 sell), traded 44,219, gross pnl +43.57, +20 bps per round trip, avg half spread 0.3 bps, open 772.576

last fills:

- 2026-10-28 09:10Z sell XRP 813 @ 1.3301 fee 0.81 slip 0.41 (half spread 0.2 bps)
- 2026-10-28 09:10Z sell DOGE 847 @ 0.0800829 fee 0.85 slip 0.42 (half spread 0.0 bps)
- 2026-10-28 09:10Z sell LTC 831 @ 57.6162 fee 0.83 slip 0.42 (half spread 0.9 bps)
- 2026-10-28 09:10Z buy BTC 1,029 @ 81473.6 fee 1.03 slip 0.51 (half spread 0.0 bps)
- 2026-10-28 09:10Z buy SOL 1,029 @ 102.586 fee 1.03 slip 0.51 (half spread 0.5 bps)
- 2026-10-28 09:10Z buy ADA 1,029 @ 0.207016 fee 1.03 slip 0.51 (half spread 1.9 bps)
- 2026-10-28 09:10Z buy AVAX 1,020 @ 9.02251 fee 1.02 slip 0.51 (half spread 2.2 bps)
- 2026-10-28 15:10Z sell ADA 1,005 @ 0.202281 fee 1.01 slip 0.50 (half spread 2.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,351.89 (started 10,000 at 2026-09-16 03:55Z), net -6.48% since start
- 24h -0.03%, 7d -3.04%, 30d -9.11%, max drawdown -12.36%
- fills 103 total, 28 in the last 7d
- costs 203.47 (fees 135.56 + slippage 67.91); gross pnl -444.64; cost coverage -2.19
- cash 2,834.03; positions: ADA 11493.5, AVAX 263.367, DOT 1892.09
- last run 2026-10-28 17:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.02 not below -2.0
- 2026-10-28 16:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.29 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-28 16:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -0.98 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-28 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.75 not below -2.0
- 2026-10-28 16:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.04 not below -2.0
- 2026-10-28 16:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.18 not below -2.0
- 2026-10-28 16:10Z DOT hold target 0.25 (held 0.20) — hold: weight change +0.048 below threshold 0.05 | stay long: z -1.26 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-10-28 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.01 not below -2.0
- 2026-10-28 17:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.72 not below -2.0
- 2026-10-28 17:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.96 not below -2.0
- 2026-10-28 17:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.94 not below -2.0
- 2026-10-28 17:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.40 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-28 17:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.00 vs 240h mean (entry -2.0, exit -0.5); vol 51% -> weight 0.25
- 2026-10-28 17:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.83 not below -2.0
- 2026-10-28 17:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.09 not below -2.0
- 2026-10-28 17:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.07 not below -2.0
- 2026-10-28 17:10Z DOT hold target 0.25 (held 0.20) — hold: weight change +0.049 below threshold 0.05 | stay long: z -1.40 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-10-28 17:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.43 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (5 buy / 4 sell), traded 12,256, gross pnl +22.17, +36 bps per round trip, avg half spread 1.2 bps, open 11493.5
- AVAX: 11 fills (7 buy / 4 sell), traded 12,368, gross pnl +38.41, +62 bps per round trip, avg half spread 1.0 bps, open 263.367
- BTC: 7 fills (4 buy / 3 sell), traded 10,144, gross pnl +88.82, +175 bps per round trip, avg half spread 0.1 bps
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 6 fills (3 buy / 3 sell), traded 9,039, gross pnl -260.85, -577 bps per round trip, avg half spread 1.5 bps, open 1892.09
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 12 fills (7 buy / 5 sell), traded 13,123, gross pnl +52.42, +80 bps per round trip, avg half spread 1.1 bps
- LTC: 12 fills (6 buy / 6 sell), traded 14,725, gross pnl +11.39, +15 bps per round trip, avg half spread 1.2 bps
- SOL: 12 fills (7 buy / 5 sell), traded 16,951, gross pnl -123.88, -146 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-28 03:10Z buy ADA 548 @ 0.206398 fee 0.55 slip 0.27 (half spread 1.4 bps)
- 2026-10-28 03:10Z buy AVAX 519 @ 9.011 fee 0.52 slip 0.26 (half spread 0.6 bps)
- 2026-10-28 03:10Z buy DOT 612 @ 1.00045 fee 0.61 slip 0.31 (half spread 0.5 bps)
- 2026-10-28 03:10Z buy LTC 505 @ 57.4137 fee 0.51 slip 0.25 (half spread 0.9 bps)
- 2026-10-28 08:10Z sell SOL 1,905 @ 102.184 fee 1.90 slip 0.95 (half spread 0.5 bps)
- 2026-10-28 08:10Z sell LTC 1,895 @ 57.6262 fee 1.89 slip 0.95 (half spread 0.9 bps)
- 2026-10-28 08:10Z buy ADA 480 @ 0.206689 fee 0.48 slip 0.24 (half spread 0.7 bps)
- 2026-10-28 08:10Z buy AVAX 481 @ 9.02001 fee 0.48 slip 0.24 (half spread 0.6 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,214.23 (started 10,000 at 2026-09-16 23:20Z), net +2.14% since start
- 24h -0.84%, 7d -6.86%, 30d -6.85%, max drawdown -8.04%
- fills 47 total, 7 in the last 7d
- costs 138.30 (fees 91.77 + slippage 46.53); gross pnl 352.53; cost coverage 2.55
- cash 2,588.24; positions: DOGE 32060, LTC 43.0817, XRP 1940.8
- last run 2026-10-28 17:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 100.9 not above 120h high 104.7
- 2026-10-28 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2027 not above 120h high 0.2162
- 2026-10-28 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.869 not above 120h high 9.148
- 2026-10-28 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.55 not above 120h high 12.04
- 2026-10-28 16:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 1.31 still above 72h low 1.276; realised vol 39% -> weight 0.25
- 2026-10-28 16:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.07922 still above 72h low 0.07616; realised vol 42% -> weight 0.25
- 2026-10-28 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.003 not above 120h high 1.128
- 2026-10-28 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 58.36 not above 120h high 58.87
- 2026-10-28 17:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.05e+04 not above 120h high 8.162e+04
- 2026-10-28 17:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2332 not above 120h high 2407
- 2026-10-28 17:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 101.1 not above 120h high 104.5
- 2026-10-28 17:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2019 not above 120h high 0.2159
- 2026-10-28 17:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.859 not above 120h high 9.148
- 2026-10-28 17:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.52 not above 120h high 12.04
- 2026-10-28 17:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 1.313 still above 72h low 1.276; realised vol 39% -> weight 0.25
- 2026-10-28 17:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 0.07903 still above 72h low 0.07616; realised vol 42% -> weight 0.25
- 2026-10-28 17:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9933 not above 120h high 1.128
- 2026-10-28 17:10Z LTC buy target 0.25 (held 0.00) — enter long: squeeze in last 72h (168h vol at or below its own 25% percentile over 1440h) then broke above 120h high 58.87 at 59.11; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 7 fills (4 buy / 3 sell), traded 16,132, gross pnl -117.78, -146 bps per round trip, avg half spread 0.0 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 10,813, gross pnl -136.40, -252 bps per round trip, avg half spread 0.6 bps, open 32060
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 5 fills (3 buy / 2 sell), traded 9,981, gross pnl +81.42, +163 bps per round trip, avg half spread 2.5 bps, open 43.0817
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 5 fills (3 buy / 2 sell), traded 9,039, gross pnl -159.08, -352 bps per round trip, avg half spread 0.2 bps, open 1940.8

last fills:

- 2026-10-21 16:10Z buy ADA 2,672 @ 0.228184 fee 2.67 slip 1.34 (half spread 0.9 bps)
- 2026-10-22 09:10Z sell ADA 2,515 @ 0.21479 fee 2.51 slip 1.26 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell BTC 2,632 @ 81047.4 fee 2.63 slip 1.32 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell DOGE 2,584 @ 0.0783045 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-23 23:06Z sell XRP 2,581 @ 1.28694 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 00:10Z buy XRP 2,575 @ 1.32687 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 10:10Z buy DOGE 2,575 @ 0.0803216 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 17:10Z buy LTC 2,555 @ 59.2946 fee 2.55 slip 1.28 (half spread 0.8 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-28 17:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 16:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-28 16:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2161 (need +10.0%)
- 2026-10-28 16:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-28 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.76 (need +10.0%)
- 2026-10-28 16:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.274 (need +10.0%)
- 2026-10-28 16:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07781 (need +10.0%)
- 2026-10-28 16:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-28 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)
- 2026-10-28 17:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-28 17:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2338 (need +10.0%)
- 2026-10-28 17:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-28 17:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.216 (need +10.0%)
- 2026-10-28 17:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-28 17:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.75 (need +10.0%)
- 2026-10-28 17:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.272 (need +10.0%)
- 2026-10-28 17:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07741 (need +10.0%)
- 2026-10-28 17:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-28 17:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)

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

- equity 9,534.93 (started 10,000 at 2026-10-13 17:26Z), net -4.65% since start
- 24h -0.12%, 7d -8.44%, 30d -4.65%, max drawdown -9.87%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -435.85; cost coverage -14.92
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-28 17:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 16:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.15 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 16:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.70 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-10-28 16:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.61 vs 720h mean (entry -2.0, exit -0.25); vol 51% -> weigh...
- 2026-10-28 16:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.21 not below -2.0
- 2026-10-28 16:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.62 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 16:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.030 below threshold 0.05 | stay long: ratio to BTC z -0.72 vs 720h mean (entry -2.0, exit -0.25); vol 42% -> weigh...
- 2026-10-28 16:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.035 below threshold 0.05 | stay long: ratio to BTC z -2.07 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-10-28 16:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.78 not below -2.0
- 2026-10-28 17:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-28 17:10Z ETH hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.26 vs 720h mean (entry -2.0, exit -0.25); vol 38% -> weigh...
- 2026-10-28 17:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.13 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 17:10Z ADA hold target 0.14 (held 0.14) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.77 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-10-28 17:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.63 vs 720h mean (entry -2.0, exit -0.25); vol 51% -> weigh...
- 2026-10-28 17:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.26 not below -2.0
- 2026-10-28 17:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -0.58 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 17:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.030 below threshold 0.05 | stay long: ratio to BTC z -0.77 vs 720h mean (entry -2.0, exit -0.25); vol 42% -> weigh...
- 2026-10-28 17:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.28 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-10-28 17:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.56 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -120.40, -1603 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -60.20, -846 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -91.20, -559 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl +23.15, +173 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -101.75, -575 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -61.36, -348 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -24.08, -135 bps per round trip, avg half spread 0.6 bps, open 1066.7

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

- BTC: live 1742 candles, 2026-08-17 03:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1742 candles, 2026-08-17 03:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1742 candles, 2026-08-17 03:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1742 candles, 2026-08-17 03:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- AVAX: live 1742 candles, 2026-08-17 03:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LINK: live 1742 candles, 2026-08-17 03:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1714 candles, 2026-08-18 07:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1714 candles, 2026-08-18 07:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 1714 candles, 2026-08-18 07:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1714 candles, 2026-08-18 07:00Z to 2026-10-28 16:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.2 bps
