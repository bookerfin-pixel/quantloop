# quantloop summary — generated 2026-10-29 02:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-22 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 42.9 of 60, 17.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -10.67% (max drawdown -28.57%, 354 fills) vs challenger1 -6.79% (max drawdown -12.36%, 105 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.99% (usual 0.54, this window 0.53) vs challenger1 -8.39% (usual 0.37, this window 0.45); the rule compares on skill, daily edge t +0.29 over 43 days
  trades: its 34 finished trades made -3.82% of its starting equity after costs (20 won, 14 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.15 over 43 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +5.39%, equal weight basket of 10 pairs +4.31%, basket max drawdown -19%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 37.7 of 60, 22.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -22.26% (max drawdown -28.57%, 316 fills) vs challenger2 -8.41% (max drawdown -8.86%, 16 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -15.94% (usual 0.54, this window 0.50) vs challenger2 -5.06% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +1.45 over 38 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.09 over 38 days)
  fills: 16 in 37.7 days; at this pace about 25 by day 60, under the 30 a promotion there needs, and about 50 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.16%, equal weight basket of 10 pairs -11.70%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 23.2 of 60, 36.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -19.61% (max drawdown -19.95%, 165 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.98% (usual 0.55, this window 0.36) vs challenger3 -0.78% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.12 over 23 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.72 over 23 days)
  fills: 10 in 23.2 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -6.99%, equal weight basket of 10 pairs -17.54%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 13.1 of 120, 106.9 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -6.23% (max drawdown -9.98%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -2.17% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.62 over 13 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.74% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.62 over 13 days)
  market over the window: BTC -2.91%, equal weight basket of 10 pairs -7.68%, basket max drawdown -10%, basket realised vol 47% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,932.84 (started 10,000 at 2026-09-16 03:55Z), net -10.67% since start
- 24h -3.03%, 7d -5.78%, 30d -23.13%, max drawdown -28.57%
- fills 354 total, 62 in the last 7d
- costs 799.76 (fees 530.06 + slippage 269.70); gross pnl -267.40; cost coverage -0.33
- cash -0.00; positions: BTC 0.0186516, DOGE 19175.7, ETH 0.646361, LINK 130.85, LTC 25.529, XRP 1150.86
- last run 2026-10-29 02:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 01:10Z SOL hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.32% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 01:10Z ADA hold target 0.11 (held 0.09) — hold: weight change +0.020 below threshold 0.05 | stay long: 72h return +0.59% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 01:10Z AVAX hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +0.12% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 01:10Z LINK hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +3.18% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-29 01:10Z XRP hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +1.92% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 01:10Z DOGE hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +3.19% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.17% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 01:10Z LTC hold target 0.11 (held 0.12) — hold: weight change -0.004 below threshold 0.05 | stay long: 72h return +4.58% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-29 02:10Z BTC buy target 0.17 (held 0.11) — stay long: 72h return +0.34% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 28% -> weight 0.25
- 2026-10-29 02:10Z ETH buy target 0.17 (held 0.11) — stay long: 72h return -0.00% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 40% -> weight 0.25
- 2026-10-29 02:10Z SOL sell target 0.00 (held 0.11) — exit: 72h return -1.26% fell below exit band -1.0%
- 2026-10-29 02:10Z ADA sell target 0.00 (held 0.09) — exit: 72h return -2.16% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-10-29 02:10Z AVAX sell target 0.00 (held 0.12) — exit: 72h return -1.78% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-10-29 02:10Z LINK buy target 0.17 (held 0.11) — stay long: 72h return +0.59% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 55% -> weight 0.25
- 2026-10-29 02:10Z XRP buy target 0.17 (held 0.11) — stay long: 72h return +0.53% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 41% -> weight 0.25
- 2026-10-29 02:10Z DOGE buy target 0.17 (held 0.11) — stay long: 72h return +1.99% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 44% -> weight 0.25
- 2026-10-29 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.12% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 02:10Z LTC buy target 0.17 (held 0.12) — stay long: 72h return +3.57% vs exit band -1.0% and price above 24h EMA; realised vol 48% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 31 fills (14 buy / 17 sell), traded 41,277, gross pnl -90.33, -44 bps per round trip, avg half spread 2.1 bps
- AVAX: 41 fills (19 buy / 22 sell), traded 68,763, gross pnl +308.22, +90 bps per round trip, avg half spread 1.1 bps
- BTC: 33 fills (19 buy / 14 sell), traded 47,986, gross pnl -38.10, -16 bps per round trip, avg half spread 0.1 bps, open 0.0186516
- DOGE: 31 fills (16 buy / 15 sell), traded 41,424, gross pnl -215.64, -104 bps per round trip, avg half spread 0.8 bps, open 19175.7
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 35 fills (18 buy / 17 sell), traded 49,895, gross pnl -225.17, -90 bps per round trip, avg half spread 0.1 bps, open 0.646361
- LINK: 39 fills (20 buy / 19 sell), traded 66,298, gross pnl -309.35, -93 bps per round trip, avg half spread 1.9 bps, open 130.85
- LTC: 37 fills (18 buy / 19 sell), traded 52,918, gross pnl +506.98, +192 bps per round trip, avg half spread 1.6 bps, open 25.529
- SOL: 36 fills (19 buy / 17 sell), traded 57,028, gross pnl -95.11, -33 bps per round trip, avg half spread 0.5 bps
- XRP: 32 fills (17 buy / 15 sell), traded 44,709, gross pnl +30.96, +14 bps per round trip, avg half spread 0.3 bps, open 1150.86

last fills:

- 2026-10-29 02:10Z sell ADA 807 @ 0.196751 fee 0.81 slip 0.49 (half spread 4.0 bps)
- 2026-10-29 02:10Z sell AVAX 1,101 @ 8.61819 fee 1.10 slip 0.55 (half spread 1.7 bps)
- 2026-10-29 02:10Z buy BTC 482 @ 79928.3 fee 0.48 slip 0.24 (half spread 0.0 bps)
- 2026-10-29 02:10Z buy ETH 490 @ 2306.43 fee 0.49 slip 0.24 (half spread 0.4 bps)
- 2026-10-29 02:10Z buy LINK 498 @ 11.3947 fee 0.50 slip 0.35 (half spread 5.1 bps)
- 2026-10-29 02:10Z buy XRP 490 @ 1.29537 fee 0.49 slip 0.24 (half spread 0.2 bps)
- 2026-10-29 02:10Z buy DOGE 493 @ 0.0777436 fee 0.49 slip 0.25 (half spread 1.3 bps)
- 2026-10-29 02:10Z buy LTC 447 @ 58.109 fee 0.45 slip 0.22 (half spread 1.7 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,310.06 (started 10,000 at 2026-09-16 03:55Z), net -6.90% since start
- 24h -1.53%, 7d -3.47%, 30d -9.52%, max drawdown -12.36%
- fills 105 total, 30 in the last 7d
- costs 207.78 (fees 138.43 + slippage 69.35); gross pnl -482.16; cost coverage -2.32
- cash 4,719.90; positions: ADA 11493.5, DOT 2399.07
- last run 2026-10-29 02:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.66 not below -2.0
- 2026-10-29 01:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -0.93 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-29 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.73 not below -2.0
- 2026-10-29 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0
- 2026-10-29 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.30 not below -2.0
- 2026-10-29 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.25 not below -2.0
- 2026-10-29 01:10Z DOT hold target 0.25 (held 0.20) — hold: weight change +0.050 below threshold 0.05 | stay long: z -1.15 vs 240h mean (entry -2.0, exit -0.5); vol 76% -> weight 0.25
- 2026-10-29 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.56 not below -2.0
- 2026-10-29 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.19 not below -2.0
- 2026-10-29 02:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.36 not below -2.0
- 2026-10-29 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.54 not below -2.0
- 2026-10-29 02:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.007 below threshold 0.05 | stay long: z -1.85 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-29 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.46 not below -2.0
- 2026-10-29 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.04 not below -2.0
- 2026-10-29 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.67 not below -2.0
- 2026-10-29 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.60 not below -2.0
- 2026-10-29 02:10Z DOT buy target 0.25 (held 0.20) — stay long: z -1.61 vs 240h mean (entry -2.0, exit -0.5); vol 79% -> weight 0.25
- 2026-10-29 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.09 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (5 buy / 4 sell), traded 12,256, gross pnl -27.69, -45 bps per round trip, avg half spread 1.2 bps, open 11493.5
- AVAX: 12 fills (7 buy / 5 sell), traded 14,748, gross pnl +93.32, +127 bps per round trip, avg half spread 0.9 bps
- BTC: 7 fills (4 buy / 3 sell), traded 10,144, gross pnl +88.82, +175 bps per round trip, avg half spread 0.1 bps
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 7 fills (4 buy / 3 sell), traded 9,531, gross pnl -303.43, -637 bps per round trip, avg half spread 1.4 bps, open 2399.07
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

- equity 10,043.63 (started 10,000 at 2026-09-16 23:20Z), net +0.44% since start
- 24h -2.56%, 7d -5.40%, 30d -8.41%, max drawdown -9.58%
- fills 48 total, 8 in the last 7d
- costs 142.17 (fees 94.35 + slippage 47.82); gross pnl 185.80; cost coverage 1.31
- cash 6.44; positions: BTC 0.0316816, DOGE 32060, LTC 43.0817, XRP 1940.8
- last run 2026-10-29 02:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 101.7 not above 120h high 103
- 2026-10-29 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.205 not above 120h high 0.2117
- 2026-10-29 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.936 not above 120h high 9.059
- 2026-10-29 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.76 not above 120h high 11.88
- 2026-10-29 01:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 1.319 still above 72h low 1.276; realised vol 39% -> weight 0.25
- 2026-10-29 01:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 0.0794 still above 72h low 0.07616; realised vol 42% -> weight 0.25
- 2026-10-29 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.006 not above 120h high 1.09
- 2026-10-29 01:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 59.39 still above 72h low 56.05; realised vol 47% -> weight 0.25
- 2026-10-29 02:10Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 7.992e+04 still above 72h low 7.948e+04; realised vol 28% -> weight 0.25
- 2026-10-29 02:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2312 not above 120h high 2382
- 2026-10-29 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 99.71 not above 120h high 103
- 2026-10-29 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.1977 not above 120h high 0.2117
- 2026-10-29 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.679 not above 120h high 9.059
- 2026-10-29 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.44 not above 120h high 11.88
- 2026-10-29 02:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 1.297 still above 72h low 1.276; realised vol 41% -> weight 0.25
- 2026-10-29 02:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.07794 still above 72h low 0.07616; realised vol 44% -> weight 0.25
- 2026-10-29 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9749 not above 120h high 1.09
- 2026-10-29 02:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 58.54 still above 72h low 56.05; realised vol 48% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 8 fills (5 buy / 3 sell), traded 18,711, gross pnl -164.73, -176 bps per round trip, avg half spread 0.0 bps, open 0.0316816
- DOGE: 6 fills (4 buy / 2 sell), traded 10,813, gross pnl -173.46, -321 bps per round trip, avg half spread 0.6 bps, open 32060
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 5 fills (3 buy / 2 sell), traded 9,981, gross pnl +30.36, +61 bps per round trip, avg half spread 2.5 bps, open 43.0817
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 5 fills (3 buy / 2 sell), traded 9,039, gross pnl -190.75, -422 bps per round trip, avg half spread 0.2 bps, open 1940.8

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
- last run 2026-10-29 02:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-29 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-29 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-29 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-29 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.267 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-29 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-29 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-29 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)
- 2026-10-29 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-29 02:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2335 (need +10.0%)
- 2026-10-29 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-29 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-29 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-29 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-29 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.267 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-29 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-29 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-29 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)

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

- equity 9,373.73 (started 10,000 at 2026-10-13 17:26Z), net -6.26% since start
- 24h -2.94%, 7d -6.73%, 30d -6.26%, max drawdown -9.98%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -597.05; cost coverage -20.43
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-29 02:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 01:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.11 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-29 01:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -1.59 vs 720h mean (entry -2.0, exit -0.25); vol 54% -> weigh...
- 2026-10-29 01:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.56 vs 720h mean (entry -2.0, exit -0.25); vol 52% -> weigh...
- 2026-10-29 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.03 not below -2.0
- 2026-10-29 01:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.60 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-29 01:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.029 below threshold 0.05 | stay long: ratio to BTC z -0.79 vs 720h mean (entry -2.0, exit -0.25); vol 42% -> weigh...
- 2026-10-29 01:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.035 below threshold 0.05 | stay long: ratio to BTC z -2.08 vs 720h mean (entry -2.0, exit -0.25); vol 76% -> weigh...
- 2026-10-29 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.57 not below -2.0
- 2026-10-29 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-29 02:10Z ETH hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.28 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-29 02:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.25 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-29 02:10Z ADA hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.92 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-10-29 02:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.79 vs 720h mean (entry -2.0, exit -0.25); vol 55% -> weigh...
- 2026-10-29 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.26 not below -2.0
- 2026-10-29 02:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -0.69 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-29 02:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.030 below threshold 0.05 | stay long: ratio to BTC z -0.87 vs 720h mean (entry -2.0, exit -0.25); vol 44% -> weigh...
- 2026-10-29 02:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.42 vs 720h mean (entry -2.0, exit -0.25); vol 79% -> weigh...
- 2026-10-29 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.59 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -150.18, -2000 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -93.14, -1308 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -115.31, -707 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl -0.03, -0 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -115.90, -655 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -81.00, -459 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -41.49, -233 bps per round trip, avg half spread 0.6 bps, open 1066.7

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

- BTC: live 1751 candles, 2026-08-17 03:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1751 candles, 2026-08-17 03:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1751 candles, 2026-08-17 03:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1751 candles, 2026-08-17 03:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.2 bps
- AVAX: live 1751 candles, 2026-08-17 03:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LINK: live 1751 candles, 2026-08-17 03:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- XRP: live 1723 candles, 2026-08-18 07:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1723 candles, 2026-08-18 07:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 1723 candles, 2026-08-18 07:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1723 candles, 2026-08-18 07:00Z to 2026-10-29 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
