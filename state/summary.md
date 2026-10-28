# quantloop summary — generated 2026-10-28 21:00Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-21 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 42.7 of 60, 17.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.95% (max drawdown -27.50%, 344 fills) vs challenger1 -4.73% (max drawdown -12.36%, 104 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.89% (usual 0.54, this window 0.52) vs challenger1 -7.45% (usual 0.37, this window 0.45); the rule compares on skill, daily edge t +0.27 over 43 days
  trades: its 34 finished trades made -3.82% of its starting equity after costs (20 won, 14 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.00 over 43 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +7.15%, equal weight basket of 10 pairs +7.33%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 37.5 of 60, 22.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -19.89% (max drawdown -27.50%, 306 fills) vs challenger2 -6.42% (max drawdown -7.54%, 16 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.92% (usual 0.54, this window 0.50) vs challenger2 -3.79% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +1.43 over 38 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.88 over 38 days)
  fills: 16 in 37.5 days; at this pace about 25 by day 60, under the 30 a promotion there needs, and about 51 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -1.54%, equal weight basket of 10 pairs -9.20%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 22.9 of 60, 37.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -17.16% (max drawdown -18.74%, 155 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.82% (usual 0.55, this window 0.35) vs challenger3 -0.84% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.89 over 23 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.80 over 23 days)
  fills: 10 in 22.9 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.43%, equal weight basket of 10 pairs -15.18%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 12.9 of 120, 107.1 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -2.89% (max drawdown -9.87%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -0.23% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.05 over 13 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.74% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 10% that this is a real edge (every idea starts at 10%; the daily skill t is -0.05 over 13 days)
  market over the window: BTC -1.29%, equal weight basket of 10 pairs -5.04%, basket max drawdown -10%, basket realised vol 46% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,205.07 (started 10,000 at 2026-09-16 03:55Z), net -7.95% since start
- 24h +0.74%, 7d -5.48%, 30d -21.43%, max drawdown -27.50%
- fills 344 total, 52 in the last 7d
- costs 789.60 (fees 523.41 + slippage 266.20); gross pnl -5.33; cost coverage -0.01
- cash 845.61; positions: AVAX 127.789, BTC 0.0126241, DOGE 12831.6, ETH 0.434103, LINK 87.1889, LTC 17.8352, SOL 10.026, XRP 772.576
- last run 2026-10-28 21:00Z; halted today: False

last decisions (newest last):

- 2026-10-28 20:10Z SOL hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +1.28% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.66% not above entry band +1.0%
- 2026-10-28 20:10Z AVAX buy target 0.12 (held 0.00) — enter long: 72h return +1.13% vs entry band +1.0% and price above 24h EMA; realised vol 52% -> weight 0.25
- 2026-10-28 20:10Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +3.16% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-28 20:10Z XRP hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +2.72% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 20:10Z DOGE hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +3.75% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-10-28 20:10Z LTC hold target 0.12 (held 0.11) — hold: weight change +0.010 below threshold 0.05 | stay long: 72h return +4.33% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 21:00Z BTC hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +1.08% vs exit band -1.0% and price above 24h EMA; realised vol 2...
- 2026-10-28 21:00Z ETH hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +0.64% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-28 21:00Z SOL hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +0.88% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 21:00Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.57% not above entry band +1.0%
- 2026-10-28 21:00Z AVAX hold target 0.12 (held 0.12) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.77% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-28 21:00Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +2.93% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-28 21:00Z XRP hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +2.43% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 21:00Z DOGE hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +3.99% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 21:00Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.86% not above entry band +1.0%
- 2026-10-28 21:00Z LTC hold target 0.12 (held 0.11) — hold: weight change +0.011 below threshold 0.05 | stay long: 72h return +3.26% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 29 fills (13 buy / 16 sell), traded 39,626, gross pnl -52.98, -27 bps per round trip, avg half spread 2.0 bps
- AVAX: 40 fills (19 buy / 21 sell), traded 67,662, gross pnl +357.03, +106 bps per round trip, avg half spread 1.1 bps, open 127.789
- BTC: 32 fills (18 buy / 14 sell), traded 47,504, gross pnl -21.20, -9 bps per round trip, avg half spread 0.1 bps, open 0.0126241
- DOGE: 30 fills (15 buy / 15 sell), traded 40,931, gross pnl -184.27, -90 bps per round trip, avg half spread 0.8 bps, open 12831.6
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 34 fills (17 buy / 17 sell), traded 49,405, gross pnl -202.42, -82 bps per round trip, avg half spread 0.0 bps, open 0.434103
- LINK: 38 fills (19 buy / 19 sell), traded 65,801, gross pnl -272.37, -83 bps per round trip, avg half spread 1.8 bps, open 87.1889
- LTC: 36 fills (17 buy / 19 sell), traded 52,471, gross pnl +519.91, +198 bps per round trip, avg half spread 1.6 bps, open 17.8352
- SOL: 35 fills (19 buy / 16 sell), traded 56,030, gross pnl -66.43, -24 bps per round trip, avg half spread 0.5 bps, open 10.026
- XRP: 31 fills (16 buy / 15 sell), traded 44,219, gross pnl +57.25, +26 bps per round trip, avg half spread 0.3 bps, open 772.576

last fills:

- 2026-10-28 09:10Z sell LTC 831 @ 57.6162 fee 0.83 slip 0.42 (half spread 0.9 bps)
- 2026-10-28 09:10Z buy BTC 1,029 @ 81473.6 fee 1.03 slip 0.51 (half spread 0.0 bps)
- 2026-10-28 09:10Z buy SOL 1,029 @ 102.586 fee 1.03 slip 0.51 (half spread 0.5 bps)
- 2026-10-28 09:10Z buy ADA 1,029 @ 0.207016 fee 1.03 slip 0.51 (half spread 1.9 bps)
- 2026-10-28 09:10Z buy AVAX 1,020 @ 9.02251 fee 1.02 slip 0.51 (half spread 2.2 bps)
- 2026-10-28 15:10Z sell ADA 1,005 @ 0.202281 fee 1.01 slip 0.50 (half spread 2.0 bps)
- 2026-10-28 18:10Z sell AVAX 1,000 @ 8.84408 fee 1.00 slip 0.50 (half spread 0.6 bps)
- 2026-10-28 20:10Z buy AVAX 1,156 @ 9.04902 fee 1.16 slip 0.58 (half spread 0.6 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,516.70 (started 10,000 at 2026-09-16 03:55Z), net -4.83% since start
- 24h +1.48%, 7d -1.33%, 30d -7.51%, max drawdown -12.36%
- fills 104 total, 29 in the last 7d
- costs 207.04 (fees 137.94 + slippage 69.10); gross pnl -276.26; cost coverage -1.33
- cash 5,212.48; positions: ADA 11493.5, DOT 1892.09
- last run 2026-10-28 21:00Z; halted today: False

last decisions (newest last):

- 2026-10-28 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.11 not below -2.0
- 2026-10-28 20:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: z -0.72 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-28 20:10Z AVAX sell target 0.00 (held 0.25) — flat: z -0.49 not below -0.5
- 2026-10-28 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.03 not below -2.0
- 2026-10-28 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.95 not below -2.0
- 2026-10-28 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.67 not below -2.0
- 2026-10-28 20:10Z DOT hold target 0.25 (held 0.20) — hold: weight change +0.045 below threshold 0.05 | stay long: z -0.83 vs 240h mean (entry -2.0, exit -0.5); vol 76% -> weight 0.25
- 2026-10-28 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.63 not below -2.0
- 2026-10-28 21:00Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.08 not below -2.0
- 2026-10-28 21:00Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.44 not below -2.0
- 2026-10-28 21:00Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.34 not below -2.0
- 2026-10-28 21:00Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -0.76 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-28 21:00Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.55 not below -2.0
- 2026-10-28 21:00Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.04 not below -2.0
- 2026-10-28 21:00Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.79 not below -2.0
- 2026-10-28 21:00Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-10-28 21:00Z DOT hold target 0.25 (held 0.20) — hold: weight change +0.047 below threshold 0.05 | stay long: z -0.90 vs 240h mean (entry -2.0, exit -0.5); vol 76% -> weight 0.25
- 2026-10-28 21:00Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.29 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (5 buy / 4 sell), traded 12,256, gross pnl +80.77, +132 bps per round trip, avg half spread 1.2 bps, open 11493.5
- AVAX: 12 fills (7 buy / 5 sell), traded 14,748, gross pnl +93.32, +127 bps per round trip, avg half spread 0.9 bps
- BTC: 7 fills (4 buy / 3 sell), traded 10,144, gross pnl +88.82, +175 bps per round trip, avg half spread 0.1 bps
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 6 fills (3 buy / 3 sell), traded 9,039, gross pnl -205.98, -456 bps per round trip, avg half spread 1.5 bps, open 1892.09
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 12 fills (7 buy / 5 sell), traded 13,123, gross pnl +52.42, +80 bps per round trip, avg half spread 1.1 bps
- LTC: 12 fills (6 buy / 6 sell), traded 14,725, gross pnl +11.39, +15 bps per round trip, avg half spread 1.2 bps
- SOL: 12 fills (7 buy / 5 sell), traded 16,951, gross pnl -123.88, -146 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-28 03:10Z buy AVAX 519 @ 9.011 fee 0.52 slip 0.26 (half spread 0.6 bps)
- 2026-10-28 03:10Z buy DOT 612 @ 1.00045 fee 0.61 slip 0.31 (half spread 0.5 bps)
- 2026-10-28 03:10Z buy LTC 505 @ 57.4137 fee 0.51 slip 0.25 (half spread 0.9 bps)
- 2026-10-28 08:10Z sell SOL 1,905 @ 102.184 fee 1.90 slip 0.95 (half spread 0.5 bps)
- 2026-10-28 08:10Z sell LTC 1,895 @ 57.6262 fee 1.89 slip 0.95 (half spread 0.9 bps)
- 2026-10-28 08:10Z buy ADA 480 @ 0.206689 fee 0.48 slip 0.24 (half spread 0.7 bps)
- 2026-10-28 08:10Z buy AVAX 481 @ 9.02001 fee 0.48 slip 0.24 (half spread 0.6 bps)
- 2026-10-28 20:10Z sell AVAX 2,381 @ 9.03998 fee 2.38 slip 1.19 (half spread 0.6 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,261.71 (started 10,000 at 2026-09-16 23:20Z), net +2.62% since start
- 24h -0.38%, 7d -6.07%, 30d -6.42%, max drawdown -8.27%
- fills 48 total, 8 in the last 7d
- costs 142.17 (fees 94.35 + slippage 47.82); gross pnl 403.88; cost coverage 2.84
- cash 6.44; positions: BTC 0.0316816, DOGE 32060, LTC 43.0817, XRP 1940.8
- last run 2026-10-28 21:00Z; halted today: False

last decisions (newest last):

- 2026-10-28 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 103 not above 120h high 103.8
- 2026-10-28 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2069 not above 120h high 0.2138
- 2026-10-28 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 9.03 not above 120h high 9.111
- 2026-10-28 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.84 not above 120h high 11.92
- 2026-10-28 20:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 1.334 still above 72h low 1.276; realised vol 40% -> weight 0.25
- 2026-10-28 20:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 0.08009 still above 72h low 0.07616; realised vol 43% -> weight 0.25
- 2026-10-28 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.029 not above 120h high 1.119
- 2026-10-28 20:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 59.49 still above 72h low 56.05; realised vol 46% -> weight 0.25
- 2026-10-28 21:00Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 8.126e+04 still above 72h low 7.948e+04; realised vol 27% -> weight 0.25
- 2026-10-28 21:00Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2359 not above 120h high 2399
- 2026-10-28 21:00Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 102.5 not above 120h high 103.8
- 2026-10-28 21:00Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2065 not above 120h high 0.2138
- 2026-10-28 21:00Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 9.006 not above 120h high 9.111
- 2026-10-28 21:00Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.82 not above 120h high 11.92
- 2026-10-28 21:00Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 1.33 still above 72h low 1.276; realised vol 40% -> weight 0.25
- 2026-10-28 21:00Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 0.08023 still above 72h low 0.07616; realised vol 43% -> weight 0.25
- 2026-10-28 21:00Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.024 not above 120h high 1.119
- 2026-10-28 21:00Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 58.88 still above 72h low 56.05; realised vol 47% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 8 fills (5 buy / 3 sell), traded 18,711, gross pnl -122.30, -131 bps per round trip, avg half spread 0.0 bps, open 0.0316816
- DOGE: 6 fills (4 buy / 2 sell), traded 10,813, gross pnl -95.08, -176 bps per round trip, avg half spread 0.6 bps, open 32060
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 5 fills (3 buy / 2 sell), traded 9,981, gross pnl +61.60, +123 bps per round trip, avg half spread 2.5 bps, open 43.0817
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 5 fills (3 buy / 2 sell), traded 9,039, gross pnl -124.72, -276 bps per round trip, avg half spread 0.2 bps, open 1940.8

last fills:

- 2026-10-22 09:10Z sell ADA 2,515 @ 0.21479 fee 2.51 slip 1.26 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell BTC 2,632 @ 81047.4 fee 2.63 slip 1.32 (half spread 0.0 bps)
- 2026-10-22 17:10Z sell DOGE 2,584 @ 0.0783045 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-23 23:06Z sell XRP 2,581 @ 1.28694 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 00:10Z buy XRP 2,575 @ 1.32687 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 10:10Z buy DOGE 2,575 @ 0.0803216 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-28 17:10Z buy LTC 2,555 @ 59.2946 fee 2.55 slip 1.28 (half spread 0.8 bps)
- 2026-10-28 20:10Z buy BTC 2,579 @ 81410.7 fee 2.58 slip 1.29 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-28 21:00Z; halted today: False

last decisions (newest last):

- 2026-10-28 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-28 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2154 (need +10.0%)
- 2026-10-28 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-28 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.75 (need +10.0%)
- 2026-10-28 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.27 (need +10.0%)
- 2026-10-28 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07741 (need +10.0%)
- 2026-10-28 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.046 (need +10.0%)
- 2026-10-28 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)
- 2026-10-28 21:00Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-28 21:00Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2335 (need +10.0%)
- 2026-10-28 21:00Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-28 21:00Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-28 21:00Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-28 21:00Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-28 21:00Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.263 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-28 21:00Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-28 21:00Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-28 21:00Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)

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

- equity 9,707.06 (started 10,000 at 2026-10-13 17:26Z), net -2.93% since start
- 24h +1.43%, 7d -6.14%, 30d -2.93%, max drawdown -9.87%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -263.72; cost coverage -9.02
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-28 21:00Z; halted today: False

last decisions (newest last):

- 2026-10-28 20:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.00 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-28 20:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -1.57 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-28 20:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.52 vs 720h mean (entry -2.0, exit -0.25); vol 52% -> weigh...
- 2026-10-28 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.02 not below -2.0
- 2026-10-28 20:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.50 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-28 20:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.029 below threshold 0.05 | stay long: ratio to BTC z -0.75 vs 720h mean (entry -2.0, exit -0.25); vol 43% -> weigh...
- 2026-10-28 20:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.034 below threshold 0.05 | stay long: ratio to BTC z -1.81 vs 720h mean (entry -2.0, exit -0.25); vol 76% -> weigh...
- 2026-10-28 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.67 not below -2.0
- 2026-10-28 21:00Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-28 21:00Z ETH hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.19 vs 720h mean (entry -2.0, exit -0.25); vol 38% -> weigh...
- 2026-10-28 21:00Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.03 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-28 21:00Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -1.54 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-28 21:00Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.50 vs 720h mean (entry -2.0, exit -0.25); vol 52% -> weigh...
- 2026-10-28 21:00Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.00 not below -2.0
- 2026-10-28 21:00Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.48 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-28 21:00Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.029 below threshold 0.05 | stay long: ratio to BTC z -0.67 vs 720h mean (entry -2.0, exit -0.25); vol 43% -> weigh...
- 2026-10-28 21:00Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.034 below threshold 0.05 | stay long: ratio to BTC z -1.83 vs 720h mean (entry -2.0, exit -0.25); vol 76% -> weigh...
- 2026-10-28 21:00Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.79 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -85.41, -1137 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -34.21, -480 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -64.32, -394 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl +53.02, +397 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -85.36, -483 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -42.26, -240 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -5.20, -29 bps per round trip, avg half spread 0.6 bps, open 1066.7

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

- BTC: live 1746 candles, 2026-08-17 03:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1746 candles, 2026-08-17 03:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1746 candles, 2026-08-17 03:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1746 candles, 2026-08-17 03:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- AVAX: live 1746 candles, 2026-08-17 03:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LINK: live 1746 candles, 2026-08-17 03:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- XRP: live 1718 candles, 2026-08-18 07:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1718 candles, 2026-08-18 07:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 1718 candles, 2026-08-18 07:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1718 candles, 2026-08-18 07:00Z to 2026-10-28 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
