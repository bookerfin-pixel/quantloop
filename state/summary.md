# quantloop summary — generated 2026-10-29 12:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-22 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 43.3 of 60, 16.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -10.42% (max drawdown -29.04%, 363 fills) vs challenger1 -6.22% (max drawdown -12.36%, 105 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -13.04% (usual 0.54, this window 0.53) vs challenger1 -8.02% (usual 0.37, this window 0.45); the rule compares on skill, daily edge t +0.31 over 43 days
  trades: its 34 finished trades made -3.82% of its starting equity after costs (20 won, 14 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.10 over 43 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +5.57%, equal weight basket of 10 pairs +4.86%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 38.2 of 60, 21.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -22.04% (max drawdown -29.04%, 325 fills) vs challenger2 -8.34% (max drawdown -9.55%, 16 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -15.96% (usual 0.54, this window 0.51) vs challenger2 -5.12% (usual 0.29, this window 0.16); the rule compares on skill, daily edge t +1.44 over 38 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.10 over 38 days)
  fills: 16 in 38.2 days; at this pace about 25 by day 60, under the 30 a promotion there needs, and about 50 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.00%, equal weight basket of 10 pairs -11.26%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 23.6 of 60, 36.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -19.38% (max drawdown -20.47%, 174 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.98% (usual 0.55, this window 0.37) vs challenger3 -0.79% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.16 over 24 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.74 over 24 days)
  fills: 10 in 23.6 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -6.83%, equal weight basket of 10 pairs -17.12%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 13.5 of 120, 106.5 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -5.53% (max drawdown -10.24%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -1.72% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.51 over 14 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.84% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.51 over 14 days)
  market over the window: BTC -2.75%, equal weight basket of 10 pairs -7.21%, basket max drawdown -10%, basket realised vol 47% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,957.92 (started 10,000 at 2026-09-16 03:55Z), net -10.42% since start
- 24h -1.71%, 7d -3.32%, 30d -24.36%, max drawdown -29.04%
- fills 363 total, 53 in the last 7d
- costs 811.38 (fees 537.81 + slippage 273.58); gross pnl -230.70; cost coverage -0.28
- cash 0.00; positions: BTC 0.0278542, DOGE 22825.3, ETH 0.96407, LINK 78.2972, LTC 31.0344
- last run 2026-10-29 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.64% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.42% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 11:10Z LINK buy target 0.20 (held 0.00) — enter long: 72h return +1.30% vs entry band +1.0% and price above 24h EMA; realised vol 55% -> weight 0.25
- 2026-10-29 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.46% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 11:10Z DOGE sell target 0.20 (held 0.25) — stay long: 72h return +1.94% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 44% -> weight 0.25
- 2026-10-29 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.74% not above entry band +1.0%
- 2026-10-29 11:10Z LTC sell target 0.20 (held 0.25) — stay long: 72h return +2.48% vs exit band -1.0% and price above 24h EMA; realised vol 50% -> weight 0.25
- 2026-10-29 12:10Z BTC hold target 0.20 (held 0.25) — hold: weight change -0.049 below threshold 0.05 | stay long: 72h return -0.28% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 12:10Z ETH hold target 0.20 (held 0.25) — hold: weight change -0.050 below threshold 0.05 | stay long: 72h return -0.36% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.31% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.02% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.17% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 12:10Z LINK none target 0.20 (held 0.10) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-29 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 12:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.84% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.01% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 12:10Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.33% vs exit band -1.0% and price above 24h EMA; realised vol 5...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 31 fills (14 buy / 17 sell), traded 41,277, gross pnl -90.33, -44 bps per round trip, avg half spread 2.1 bps
- AVAX: 41 fills (19 buy / 22 sell), traded 68,763, gross pnl +308.22, +90 bps per round trip, avg half spread 1.1 bps
- BTC: 34 fills (20 buy / 14 sell), traded 48,720, gross pnl -32.82, -13 bps per round trip, avg half spread 0.1 bps, open 0.0278542
- DOGE: 33 fills (17 buy / 16 sell), traded 42,615, gross pnl -192.08, -90 bps per round trip, avg half spread 0.7 bps, open 22825.3
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 36 fills (19 buy / 17 sell), traded 50,627, gross pnl -210.31, -83 bps per round trip, avg half spread 0.1 bps, open 0.96407
- LINK: 41 fills (21 buy / 20 sell), traded 68,694, gross pnl -315.25, -92 bps per round trip, avg half spread 1.9 bps, open 78.2972
- LTC: 39 fills (19 buy / 20 sell), traded 54,133, gross pnl +515.24, +190 bps per round trip, avg half spread 1.6 bps, open 31.0344
- SOL: 36 fills (19 buy / 17 sell), traded 57,028, gross pnl -95.11, -33 bps per round trip, avg half spread 0.5 bps
- XRP: 33 fills (17 buy / 16 sell), traded 46,189, gross pnl +21.60, +9 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-29 04:10Z sell XRP 1,480 @ 1.28594 fee 1.48 slip 0.74 (half spread 0.0 bps)
- 2026-10-29 04:10Z buy BTC 734 @ 79738.5 fee 0.73 slip 0.37 (half spread 0.0 bps)
- 2026-10-29 04:10Z buy ETH 732 @ 2303.83 fee 0.73 slip 0.37 (half spread 0.0 bps)
- 2026-10-29 04:10Z buy DOGE 734 @ 0.0775475 fee 0.73 slip 0.37 (half spread 0.2 bps)
- 2026-10-29 04:10Z buy LTC 761 @ 56.9885 fee 0.76 slip 0.38 (half spread 1.8 bps)
- 2026-10-29 11:10Z sell DOGE 457 @ 0.0786025 fee 0.46 slip 0.23 (half spread 0.1 bps)
- 2026-10-29 11:10Z sell LTC 454 @ 57.8111 fee 0.45 slip 0.23 (half spread 1.7 bps)
- 2026-10-29 11:10Z buy LINK 909 @ 11.6099 fee 0.91 slip 0.45 (half spread 2.6 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,367.95 (started 10,000 at 2026-09-16 03:55Z), net -6.32% since start
- 24h -0.18%, 7d -2.74%, 30d -8.96%, max drawdown -12.36%
- fills 105 total, 29 in the last 7d
- costs 207.78 (fees 138.43 + slippage 69.35); gross pnl -424.27; cost coverage -2.04
- cash 4,719.90; positions: ADA 11493.5, DOT 2399.07
- last run 2026-10-29 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.07 not below -2.0
- 2026-10-29 11:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: z -1.29 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-29 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.07 not below -2.0
- 2026-10-29 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.62 not below -2.0
- 2026-10-29 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.80 not below -2.0
- 2026-10-29 11:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.26 not below -2.0
- 2026-10-29 11:10Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -1.22 vs 240h mean (entry -2.0, exit -0.5); vol 79% -> weight 0.25
- 2026-10-29 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-10-29 12:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.98 not below -2.0
- 2026-10-29 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.04 not below -2.0
- 2026-10-29 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.19 not below -2.0
- 2026-10-29 12:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: z -1.30 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-10-29 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.09 not below -2.0
- 2026-10-29 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.49 not below -2.0
- 2026-10-29 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.91 not below -2.0
- 2026-10-29 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.20 not below -2.0
- 2026-10-29 12:10Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.35 vs 240h mean (entry -2.0, exit -0.5); vol 79% -> weight 0.25
- 2026-10-29 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (5 buy / 4 sell), traded 12,256, gross pnl +8.61, +14 bps per round trip, avg half spread 1.2 bps, open 11493.5
- AVAX: 12 fills (7 buy / 5 sell), traded 14,748, gross pnl +93.32, +127 bps per round trip, avg half spread 0.9 bps
- BTC: 7 fills (4 buy / 3 sell), traded 10,144, gross pnl +88.82, +175 bps per round trip, avg half spread 0.1 bps
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 7 fills (4 buy / 3 sell), traded 9,531, gross pnl -281.83, -591 bps per round trip, avg half spread 1.4 bps, open 2399.07
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 12 fills (7 buy / 5 sell), traded 13,123, gross pnl +52.42, +80 bps per round trip, avg half spread 1.1 bps
- LTC: 12 fills (6 buy / 6 sell), traded 14,725, gross pnl +11.39, +15 bps per round trip, avg half spread 1.2 bps
- SOL: 12 fills (7 buy / 5 sell), traded 16,951, gross pnl -123.88, -146 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-28 03:10Z buy DOT 612 @ 1.00045 fee 0.61 slip 0.31 (half spread 0.5 bps)
- 2026-10-28 03:10Z buy LTC 505 @ 57.4137 fee 0.51 slip 0.25 (half spread 0.9 bps)
- 2026-10-28 08:10Z sell SOL 1,905 @ 102.184 fee 1.90 slip 0.95 (half spread 0.5 bps)
- 2026-10-28 08:10Z sell LTC 1,895 @ 57.6262 fee 1.89 slip 0.95 (half spread 0.9 bps)
- 2026-10-28 08:10Z buy ADA 480 @ 0.206689 fee 0.48 slip 0.24 (half spread 0.7 bps)
- 2026-10-28 08:10Z buy AVAX 481 @ 9.02001 fee 0.48 slip 0.24 (half spread 0.6 bps)
- 2026-10-28 20:10Z sell AVAX 2,381 @ 9.03998 fee 2.38 slip 1.19 (half spread 0.6 bps)
- 2026-10-29 02:10Z buy DOT 492 @ 0.970635 fee 0.49 slip 0.25 (half spread 0.5 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,051.15 (started 10,000 at 2026-09-16 23:20Z), net +0.51% since start
- 24h -1.78%, 7d -3.53%, 30d -8.31%, max drawdown -10.27%
- fills 48 total, 7 in the last 7d
- costs 142.17 (fees 94.35 + slippage 47.82); gross pnl 193.32; cost coverage 1.36
- cash 6.44; positions: BTC 0.0316816, DOGE 32060, LTC 43.0817, XRP 1940.8
- last run 2026-10-29 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 100.5 not above 120h high 103
- 2026-10-29 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.201 not above 120h high 0.2087
- 2026-10-29 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.781 not above 120h high 9.042
- 2026-10-29 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.57 not above 120h high 11.88
- 2026-10-29 11:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 1.293 still above 72h low 1.283; realised vol 40% -> weight 0.25
- 2026-10-29 11:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 0.07846 still above 72h low 0.0767; realised vol 44% -> weight 0.25
- 2026-10-29 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.992 not above 120h high 1.066
- 2026-10-29 11:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 57.88 still above 72h low 56.05; realised vol 50% -> weight 0.25
- 2026-10-29 12:10Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 8.006e+04 still above 72h low 7.953e+04; realised vol 27% -> weight 0.25
- 2026-10-29 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2322 not above 120h high 2370
- 2026-10-29 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 100.2 not above 120h high 103
- 2026-10-29 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2008 not above 120h high 0.2087
- 2026-10-29 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.772 not above 120h high 9.042
- 2026-10-29 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.61 not above 120h high 11.88
- 2026-10-29 12:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 1.29 still above 72h low 1.283; realised vol 40% -> weight 0.25
- 2026-10-29 12:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 0.07857 still above 72h low 0.0767; realised vol 44% -> weight 0.25
- 2026-10-29 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9824 not above 120h high 1.066
- 2026-10-29 12:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 57.96 still above 72h low 56.05; realised vol 50% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 8 fills (5 buy / 3 sell), traded 18,711, gross pnl -160.70, -172 bps per round trip, avg half spread 0.0 bps, open 0.0316816
- DOGE: 6 fills (4 buy / 2 sell), traded 10,813, gross pnl -150.64, -279 bps per round trip, avg half spread 0.6 bps, open 32060
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 5 fills (3 buy / 2 sell), traded 9,981, gross pnl +23.69, +47 bps per round trip, avg half spread 2.5 bps, open 43.0817
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 5 fills (3 buy / 2 sell), traded 9,039, gross pnl -203.39, -450 bps per round trip, avg half spread 0.2 bps, open 1940.8

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
- last run 2026-10-29 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 11:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-29 11:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1973 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-29 11:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.586 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-29 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-29 11:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.267 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-29 11:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-29 11:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9697 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-29 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)
- 2026-10-29 12:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-29 12:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2335 (need +10.0%)
- 2026-10-29 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-29 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1973 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-29 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.586 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-29 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-29 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.267 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-29 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-29 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9697 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-29 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)

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

- equity 9,443.30 (started 10,000 at 2026-10-13 17:26Z), net -5.57% since start
- 24h -1.34%, 7d -4.38%, 30d -5.57%, max drawdown -10.24%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -527.48; cost coverage -18.05
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-29 12:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 11:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.12 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-29 11:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.66 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-10-29 11:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.61 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-29 11:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.12 not below -2.0
- 2026-10-29 11:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -0.83 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-29 11:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.030 below threshold 0.05 | stay long: ratio to BTC z -0.79 vs 720h mean (entry -2.0, exit -0.25); vol 44% -> weigh...
- 2026-10-29 11:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.035 below threshold 0.05 | stay long: ratio to BTC z -2.04 vs 720h mean (entry -2.0, exit -0.25); vol 79% -> weigh...
- 2026-10-29 11:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.83 not below -2.0
- 2026-10-29 12:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-29 12:10Z ETH hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.17 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-29 12:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.14 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-29 12:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -1.65 vs 720h mean (entry -2.0, exit -0.25); vol 59% -> weigh...
- 2026-10-29 12:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.60 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-29 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.03 not below -2.0
- 2026-10-29 12:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.84 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-29 12:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.030 below threshold 0.05 | stay long: ratio to BTC z -0.74 vs 720h mean (entry -2.0, exit -0.25); vol 44% -> weigh...
- 2026-10-29 12:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.18 vs 720h mean (entry -2.0, exit -0.25); vol 79% -> weigh...
- 2026-10-29 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.77 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -128.50, -1711 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -79.03, -1110 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -100.46, -616 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl +9.24, +69 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -107.42, -607 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -72.87, -413 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -48.44, -272 bps per round trip, avg half spread 0.6 bps, open 1066.7

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

- BTC: live 1761 candles, 2026-08-17 03:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1761 candles, 2026-08-17 03:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1761 candles, 2026-08-17 03:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1761 candles, 2026-08-17 03:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- AVAX: live 1761 candles, 2026-08-17 03:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LINK: live 1761 candles, 2026-08-17 03:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- XRP: live 1733 candles, 2026-08-18 07:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1733 candles, 2026-08-18 07:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 1733 candles, 2026-08-18 07:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1733 candles, 2026-08-18 07:00Z to 2026-10-29 11:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
