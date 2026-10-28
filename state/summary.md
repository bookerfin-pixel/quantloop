# quantloop summary — generated 2026-10-28 04:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-21 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 42.0 of 60, 18.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.87% (max drawdown -27.50%, 330 fills) vs challenger1 -5.30% (max drawdown -12.36%, 99 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.46% (usual 0.54, this window 0.52) vs challenger1 -7.78% (usual 0.37, this window 0.45); the rule compares on skill, daily edge t +0.22 over 42 days
  trades: its 31 finished trades made -3.34% of its starting equity after costs (18 won, 13 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.06 over 42 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +6.84%, equal weight basket of 10 pairs +6.67%, basket max drawdown -19%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 36.8 of 60, 23.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -19.82% (max drawdown -27.50%, 292 fills) vs challenger2 -6.03% (max drawdown -6.58%, 13 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.54% (usual 0.54, this window 0.49) vs challenger2 -3.24% (usual 0.29, this window 0.14); the rule compares on skill, daily edge t +1.46 over 37 days
  trades: its 6 finished trades made -6.06% of its starting equity after costs (0 won, 6 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.76 over 37 days)
  fills: 13 in 36.8 days; at this pace about 21 by day 60, under the 30 a promotion there needs, and about 42 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -1.83%, equal weight basket of 10 pairs -9.76%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 22.2 of 60, 37.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -17.08% (max drawdown -18.74%, 141 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.47% (usual 0.55, this window 0.33) vs challenger3 -0.83% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.80 over 22 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.78 over 22 days)
  fills: 10 in 22.2 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.71%, equal weight basket of 10 pairs -15.69%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 12.2 of 120, 107.8 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -3.34% (max drawdown -9.87%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -0.38% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.09 over 12 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.74% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.09 over 12 days)
  market over the window: BTC -1.58%, equal weight basket of 10 pairs -5.61%, basket max drawdown -10%, basket realised vol 46% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,213.35 (started 10,000 at 2026-09-16 03:55Z), net -7.87% since start
- 24h +1.50%, 7d -3.55%, 30d -24.12%, max drawdown -27.50%
- fills 330 total, 38 in the last 7d
- costs 771.15 (fees 511.11 + slippage 260.04); gross pnl -15.50; cost coverage -0.02
- cash 0.00; positions: DOGE 23412.4, ETH 0.979343, LINK 115.49, LTC 32.2637, XRP 1383.97
- last run 2026-10-28 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.75% not above entry band +1.0%
- 2026-10-28 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.49% not above entry band +1.0%
- 2026-10-28 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.60% not above entry band +1.0%
- 2026-10-28 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.78% not above entry band +1.0%
- 2026-10-28 03:10Z XRP hold target 0.25 (held 0.20) — hold: weight change +0.050 below threshold 0.05 | stay long: 72h return +1.84% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 03:10Z DOGE hold target 0.25 (held 0.20) — hold: weight change +0.048 below threshold 0.05 | stay long: 72h return +2.15% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.67% not above entry band +1.0%
- 2026-10-28 03:10Z LTC hold target 0.25 (held 0.20) — hold: weight change +0.049 below threshold 0.05 | stay long: 72h return +0.88% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.34% not above entry band +1.0%
- 2026-10-28 04:10Z ETH hold target 0.20 (held 0.25) — hold: weight change -0.050 below threshold 0.05 | stay long: 72h return -0.12% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-28 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.45% not above entry band +1.0%
- 2026-10-28 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.33% not above entry band +1.0%
- 2026-10-28 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.64% not above entry band +1.0%
- 2026-10-28 04:10Z LINK buy target 0.20 (held 0.00) — enter long: 72h return +1.42% vs entry band +1.0% and price above 24h EMA; realised vol 51% -> weight 0.25
- 2026-10-28 04:10Z XRP hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.92% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 04:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.45% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-28 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.41% not above entry band +1.0%
- 2026-10-28 04:10Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.88% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 27 fills (12 buy / 15 sell), traded 37,592, gross pnl -30.48, -16 bps per round trip, avg half spread 2.0 bps
- AVAX: 37 fills (17 buy / 20 sell), traded 64,485, gross pnl +381.31, +118 bps per round trip, avg half spread 1.1 bps
- BTC: 31 fills (17 buy / 14 sell), traded 46,476, gross pnl -18.60, -8 bps per round trip, avg half spread 0.1 bps
- DOGE: 29 fills (15 buy / 14 sell), traded 40,083, gross pnl -196.83, -98 bps per round trip, avg half spread 0.8 bps, open 23412.4
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 32 fills (17 buy / 15 sell), traded 48,118, gross pnl -210.13, -87 bps per round trip, avg half spread 0.0 bps, open 0.979343
- LINK: 36 fills (18 buy / 18 sell), traded 64,545, gross pnl -286.39, -89 bps per round trip, avg half spread 1.8 bps, open 115.49
- LTC: 35 fills (17 buy / 18 sell), traded 51,640, gross pnl +492.12, +191 bps per round trip, avg half spread 1.6 bps, open 32.2637
- SOL: 34 fills (18 buy / 16 sell), traded 55,002, gross pnl -64.73, -24 bps per round trip, avg half spread 0.5 bps
- XRP: 30 fills (16 buy / 14 sell), traded 43,406, gross pnl +58.07, +27 bps per round trip, avg half spread 0.3 bps, open 1383.97

last fills:

- 2026-10-27 16:10Z sell XRP 468 @ 1.31778 fee 0.47 slip 0.23 (half spread 0.0 bps)
- 2026-10-27 16:10Z sell DOGE 457 @ 0.0778974 fee 0.46 slip 0.23 (half spread 0.0 bps)
- 2026-10-27 16:10Z sell LTC 460 @ 56.5267 fee 0.46 slip 0.23 (half spread 0.9 bps)
- 2026-10-27 16:10Z buy ETH 1,825 @ 2341.5 fee 1.82 slip 0.91 (half spread 0.0 bps)
- 2026-10-27 16:10Z buy SOL 1,820 @ 100.735 fee 1.82 slip 0.91 (half spread 0.5 bps)
- 2026-10-28 01:10Z sell SOL 1,825 @ 101.004 fee 1.82 slip 0.91 (half spread 0.5 bps)
- 2026-10-28 01:10Z buy ETH 468 @ 2341.45 fee 0.47 slip 0.23 (half spread 0.0 bps)
- 2026-10-28 04:10Z buy LINK 1,353 @ 11.7143 fee 1.35 slip 0.68 (half spread 1.8 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,458.90 (started 10,000 at 2026-09-16 03:55Z), net -5.41% since start
- 24h +1.76%, 7d -1.93%, 30d -8.07%, max drawdown -12.36%
- fills 99 total, 24 in the last 7d
- costs 196.33 (fees 130.80 + slippage 65.53); gross pnl -344.77; cost coverage -1.76
- cash -0.00; positions: ADA 9171.51, AVAX 210.076, DOT 1892.09, LTC 32.8825, SOL 18.638
- last run 2026-10-28 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 03:10Z SOL buy target 0.20 (held 0.14) — stay long: z -0.78 vs 240h mean (entry -2.0, exit -0.5); vol 39% -> weight 0.25
- 2026-10-28 03:10Z ADA buy target 0.20 (held 0.14) — stay long: z -0.90 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-28 03:10Z AVAX buy target 0.20 (held 0.15) — stay long: z -0.63 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-28 03:10Z LINK sell target 0.00 (held 0.17) — flat: z -0.48 not below -0.5
- 2026-10-28 03:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.03 not below -2.0
- 2026-10-28 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.28 not below -2.0
- 2026-10-28 03:10Z DOT buy target 0.20 (held 0.14) — stay long: z -1.40 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-10-28 03:10Z LTC buy target 0.20 (held 0.15) — stay long: z -0.54 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-28 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-10-28 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.53 not below -2.0
- 2026-10-28 04:10Z SOL hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: z -0.64 vs 240h mean (entry -2.0, exit -0.5); vol 39% -> weight 0.25
- 2026-10-28 04:10Z ADA hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: z -0.84 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-28 04:10Z AVAX hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: z -0.65 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-28 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.29 not below -2.0
- 2026-10-28 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.05 not below -2.0
- 2026-10-28 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.47 not below -2.0
- 2026-10-28 04:10Z DOT hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.36 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-10-28 04:10Z LTC hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: z -0.53 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 8 fills (4 buy / 4 sell), traded 11,776, gross pnl +83.96, +143 bps per round trip, avg half spread 1.3 bps, open 9171.51
- AVAX: 10 fills (6 buy / 4 sell), traded 11,887, gross pnl +79.38, +134 bps per round trip, avg half spread 1.0 bps, open 210.076
- BTC: 7 fills (4 buy / 3 sell), traded 10,144, gross pnl +88.82, +175 bps per round trip, avg half spread 0.1 bps
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 6 fills (3 buy / 3 sell), traded 9,039, gross pnl -247.04, -547 bps per round trip, avg half spread 1.5 bps, open 1892.09
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 12 fills (7 buy / 5 sell), traded 13,123, gross pnl +52.42, +80 bps per round trip, avg half spread 1.1 bps
- LTC: 11 fills (6 buy / 5 sell), traded 12,830, gross pnl +3.83, +6 bps per round trip, avg half spread 1.2 bps, open 32.8825
- SOL: 11 fills (7 buy / 4 sell), traded 15,047, gross pnl -133.01, -177 bps per round trip, avg half spread 0.5 bps, open 18.638
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-28 02:10Z sell BTC 1,343 @ 80823.9 fee 1.34 slip 0.67 (half spread 0.0 bps)
- 2026-10-28 02:10Z buy LINK 565 @ 11.6567 fee 0.56 slip 0.28 (half spread 0.0 bps)
- 2026-10-28 03:10Z sell LINK 1,580 @ 11.667 fee 1.58 slip 0.79 (half spread 1.6 bps)
- 2026-10-28 03:10Z buy SOL 539 @ 101.566 fee 0.54 slip 0.27 (half spread 0.5 bps)
- 2026-10-28 03:10Z buy ADA 548 @ 0.206398 fee 0.55 slip 0.27 (half spread 1.4 bps)
- 2026-10-28 03:10Z buy AVAX 519 @ 9.011 fee 0.52 slip 0.26 (half spread 0.6 bps)
- 2026-10-28 03:10Z buy DOT 612 @ 1.00045 fee 0.61 slip 0.31 (half spread 0.5 bps)
- 2026-10-28 03:10Z buy LTC 505 @ 57.4137 fee 0.51 slip 0.25 (half spread 0.9 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,304.72 (started 10,000 at 2026-09-16 23:20Z), net +3.05% since start
- 24h +0.04%, 7d -4.31%, 30d -6.03%, max drawdown -7.32%
- fills 45 total, 8 in the last 7d
- costs 130.61 (fees 86.64 + slippage 43.97); gross pnl 435.33; cost coverage 3.33
- cash 7,723.00; positions: XRP 1940.8
- last run 2026-10-28 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 101.5 not above 120h high 104.9
- 2026-10-28 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2065 not above 120h high 0.2179
- 2026-10-28 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 9.024 not above 120h high 9.314
- 2026-10-28 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.67 not above 120h high 12.23
- 2026-10-28 03:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 1.334 still above 72h low 1.276; realised vol 41% -> weight 0.25
- 2026-10-28 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07935 not above 120h high 0.08035
- 2026-10-28 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.003 not above 120h high 1.197
- 2026-10-28 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 57.45 not above 120h high 59.69
- 2026-10-28 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.102e+04 not above 120h high 8.19e+04
- 2026-10-28 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2357 not above 120h high 2412
- 2026-10-28 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 101.8 not above 120h high 104.9
- 2026-10-28 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2069 not above 120h high 0.2179
- 2026-10-28 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 9.016 not above 120h high 9.314
- 2026-10-28 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 11.73 not above 120h high 12.22
- 2026-10-28 04:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 1.335 still above 72h low 1.276; realised vol 41% -> weight 0.25
- 2026-10-28 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07968 not above 120h high 0.08035
- 2026-10-28 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.004 not above 120h high 1.197
- 2026-10-28 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 57.46 not above 120h high 59.69

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
- XRP: 5 fills (3 buy / 2 sell), traded 9,039, gross pnl -121.82, -270 bps per round trip, avg half spread 0.2 bps, open 1940.8

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
- last run 2026-10-28 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 03:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-28 03:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2166 (need +10.0%)
- 2026-10-28 03:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-28 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.86 (need +10.0%)
- 2026-10-28 03:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.286 (need +10.0%)
- 2026-10-28 03:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07815 (need +10.0%)
- 2026-10-28 03:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-28 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)
- 2026-10-28 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-28 04:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2338 (need +10.0%)
- 2026-10-28 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 101.3 (need +10.0%)
- 2026-10-28 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2015 not a higher low vs prior low 0.2166 (need +10.0%)
- 2026-10-28 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.704 not a higher low vs prior low 9.496 (need +10.0%)
- 2026-10-28 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.86 (need +10.0%)
- 2026-10-28 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.259 not a higher low vs prior low 1.286 (need +10.0%)
- 2026-10-28 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07815 (need +10.0%)
- 2026-10-28 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9818 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-10-28 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 57.36 (need +10.0%)

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

- equity 9,662.30 (started 10,000 at 2026-10-13 17:26Z), net -3.38% since start
- 24h +2.16%, 7d -4.58%, 30d -3.38%, max drawdown -9.87%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -308.48; cost coverage -10.56
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-28 04:10Z; halted today: False

last decisions (newest last):

- 2026-10-28 03:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.16 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 03:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -1.56 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-10-28 03:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.48 vs 720h mean (entry -2.0, exit -0.25); vol 54% -> weigh...
- 2026-10-28 03:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.17 not below -2.0
- 2026-10-28 03:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -0.34 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-28 03:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.029 below threshold 0.05 | stay long: ratio to BTC z -0.80 vs 720h mean (entry -2.0, exit -0.25); vol 43% -> weigh...
- 2026-10-28 03:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.32 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-10-28 03:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.18 not below -2.0
- 2026-10-28 04:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-28 04:10Z ETH hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.18 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 04:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.14 vs 720h mean (entry -2.0, exit -0.25); vol 39% -> weigh...
- 2026-10-28 04:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -1.56 vs 720h mean (entry -2.0, exit -0.25); vol 53% -> weigh...
- 2026-10-28 04:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.53 vs 720h mean (entry -2.0, exit -0.25); vol 54% -> weigh...
- 2026-10-28 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.11 not below -2.0
- 2026-10-28 04:10Z XRP hold target 0.14 (held 0.15) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -0.37 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-28 04:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.029 below threshold 0.05 | stay long: ratio to BTC z -0.77 vs 720h mean (entry -2.0, exit -0.25); vol 42% -> weigh...
- 2026-10-28 04:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.33 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-10-28 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.22 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -83.51, -1112 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -37.14, -522 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -75.77, -464 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl +30.67, +230 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -88.47, -500 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -50.65, -287 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -3.60, -20 bps per round trip, avg half spread 0.6 bps, open 1066.7

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

- BTC: live 1729 candles, 2026-08-17 03:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1729 candles, 2026-08-17 03:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- SOL: live 1729 candles, 2026-08-17 03:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1729 candles, 2026-08-17 03:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- AVAX: live 1729 candles, 2026-08-17 03:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LINK: live 1729 candles, 2026-08-17 03:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- XRP: live 1701 candles, 2026-08-18 07:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.1 bps
- DOGE: live 1701 candles, 2026-08-18 07:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 1701 candles, 2026-08-18 07:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
- LTC: live 1701 candles, 2026-08-18 07:00Z to 2026-10-28 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.2 bps
