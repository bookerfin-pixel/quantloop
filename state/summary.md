# quantloop summary — generated 2026-09-28 12:30Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 12.3 of 60, 47.7 days until the verdict
  so far: champion +18.79% (DD -6.75%, 92 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +6.03% (usual 0.54, this window 0.77) vs challenger1 -5.79% (usual 0.37, this window 0.13); the rule compares on skill, daily edge t -1.2 over 13 days
  market over the window: BTC +9.43%, equal weight basket of 10 pairs +23.72%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 7.2 of 60, 52.8 days until the verdict
  so far: champion +3.39% (DD -6.75%, 54 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +1.61% (usual 0.54, this window 0.82) vs challenger2 -0.94% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -0.4 over 8 days
  market over the window: BTC -0.82%, equal weight basket of 10 pairs +3.29%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 3.4 of 60, 56.6 days until the verdict
  so far: champion +0.10% (DD -5.02%, 34 fills) vs challenger3 +1.52% (DD -1.89%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -0.36% (usual 0.55, this window 0.90) vs challenger3 +1.47% (usual 0.05, this window 0.11); the rule compares on skill, daily edge t +0.3 over 4 days
  market over the window: BTC -1.36%, equal weight basket of 10 pairs +0.85%, basket max drawdown -5%, basket realised vol 49% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 2.6 of 60, 57.4 days until the verdict
  so far: champion -2.83% (DD -5.02%, 26 fills) vs challenger4 -0.33% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.52% (usual 0.55, this window 0.87) vs challenger4 +0.82% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +0.8 over 3 days
  market over the window: BTC -1.19%, equal weight basket of 10 pairs -2.40%, basket max drawdown -5%, basket realised vol 48% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,879.13 (started 10,000 at 2026-09-16 03:55Z), net +18.79% since start
- 24h -3.43%, 7d -0.63%, 30d +18.79%, max drawdown -6.75%
- fills 92 total, 54 in the last 7d
- costs 206.33 (fees 136.30 + slippage 70.03); gross pnl 2,085.46; cost coverage 10.11
- cash 8,909.71; positions: LTC 41.1276
- last run 2026-09-28 12:29Z; halted today: False

last decisions (newest last):

- 2026-09-28 11:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.63% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 11:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.88% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 11:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.99% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 11:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.22% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 11:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.35% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 11:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.02% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 11:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-28 11:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.65% not above entry band +1.0%
- 2026-09-28 12:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.79% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.79% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.76% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.73% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.88% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.14% not above entry band +1.0%
- 2026-09-28 12:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.38% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.94% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.06% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 12:29Z LTC buy target 0.25 (held 0.00) — enter long: 72h return +1.31% vs entry band +1.0% and price above 24h EMA; realised vol 109% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (5 buy / 6 sell), traded 18,727, gross pnl +101.44, +108 bps per round trip, avg half spread 2.4 bps
- AVAX: 11 fills (5 buy / 6 sell), traded 18,801, gross pnl +665.50, +708 bps per round trip, avg half spread 1.1 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 15,017, gross pnl -37.42, -50 bps per round trip, avg half spread 1.7 bps
- DOT: 12 fills (7 buy / 5 sell), traded 13,246, gross pnl +261.75, +395 bps per round trip, avg half spread 3.1 bps
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 12 fills (6 buy / 6 sell), traded 15,650, gross pnl +177.90, +227 bps per round trip, avg half spread 2.6 bps
- LTC: 10 fills (4 buy / 6 sell), traded 16,645, gross pnl +599.56, +720 bps per round trip, avg half spread 2.0 bps, open 41.1276
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-28 06:31Z sell ADA 2,368 @ 0.245465 fee 2.37 slip 1.18 (half spread 1.9 bps)
- 2026-09-28 06:31Z sell AVAX 2,383 @ 10.5512 fee 2.38 slip 1.19 (half spread 0.5 bps)
- 2026-09-28 07:26Z sell SOL 2,397 @ 118.176 fee 2.40 slip 1.20 (half spread 0.4 bps)
- 2026-09-28 07:26Z buy LINK 597 @ 13.6988 fee 0.60 slip 0.34 (half spread 3.7 bps)
- 2026-09-28 07:26Z buy DOT 595 @ 1.21426 fee 0.60 slip 0.30 (half spread 0.4 bps)
- 2026-09-28 08:27Z sell LINK 2,973 @ 13.6792 fee 2.97 slip 1.78 (half spread 4.0 bps)
- 2026-09-28 08:27Z sell DOT 2,970 @ 1.21149 fee 2.97 slip 1.49 (half spread 2.5 bps)
- 2026-09-28 12:29Z buy LTC 2,971 @ 72.2361 fee 2.97 slip 1.48 (half spread 1.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-28 12:29Z; halted today: False

last decisions (newest last):

- 2026-09-28 11:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.48 not below -2.0
- 2026-09-28 11:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.21 not below -2.0
- 2026-09-28 11:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.10 not below -2.0
- 2026-09-28 11:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.12 not below -2.0
- 2026-09-28 11:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.10 not below -2.0
- 2026-09-28 11:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.24 not below -2.0
- 2026-09-28 11:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.48 not below -2.0
- 2026-09-28 11:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.10 not below -2.0
- 2026-09-28 12:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-09-28 12:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.22 not below -2.0
- 2026-09-28 12:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.53 not below -2.0
- 2026-09-28 12:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.24 not below -2.0
- 2026-09-28 12:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.08 not below -2.0
- 2026-09-28 12:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-09-28 12:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.05 not below -2.0
- 2026-09-28 12:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.20 not below -2.0
- 2026-09-28 12:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.50 not below -2.0
- 2026-09-28 12:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.09 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- ETH: 2 fills (1 buy / 1 sell), traded 5,048, gross pnl +50.93, +202 bps per round trip, avg half spread 0.4 bps
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)
- 2026-09-17 13:23Z sell ETH 2,548 @ 2449.98 fee 2.55 slip 1.27 (half spread 0.4 bps)
- 2026-09-18 01:20Z sell ADA 2,628 @ 0.205888 fee 2.63 slip 1.31 (half spread 2.2 bps)
- 2026-09-18 03:21Z sell BTC 2,538 @ 77289.3 fee 2.54 slip 1.27 (half spread 0.0 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,965.71 (started 10,000 at 2026-09-16 23:20Z), net +9.66% since start
- 24h +0.00%, 7d +0.00%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 0 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-28 12:29Z; halted today: False

last decisions (newest last):

- 2026-09-28 11:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 11:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.306e+04 not above 120h high 8.578e+04
- 2026-09-28 12:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2668 not above 120h high 2727
- 2026-09-28 12:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 12:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 3 fills (2 buy / 1 sell), traded 5,380, gross pnl -12.20, -45 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 3 fills (2 buy / 1 sell), traded 5,361, gross pnl -9.44, -35 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)

## challenger3: swing_reversal (H3)

params: {"exit_hours": 48, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,687.29 (started 10,000 at 2026-09-16 23:20Z), net +16.87% since start
- 24h +1.52%, 7d -2.23%, 30d +16.87%, max drawdown -7.66%
- fills 67 total, 29 in the last 7d
- costs 179.65 (fees 117.99 + slippage 61.67); gross pnl 1,866.94; cost coverage 10.39
- cash -0.00; positions: ADA 11635.5, AVAX 271.951, DOT 2357.66, LINK 203.945
- last run 2026-09-28 12:29Z; halted today: False

last decisions (newest last):

- 2026-09-28 11:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 105.6 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-28 11:23Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 0.2452 still above the 48h low 0.2424; realised vol 78% -> weight 0.25
- 2026-09-28 11:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 10.5 still above the 48h low 10.35; realised vol 93% -> weight 0.25
- 2026-09-28 11:23Z LINK buy target 0.25 (held 0.00) — enter long: higher low 11.81 vs prior low 10.66 (+10.8%) then broke above the reaction high 11.88 at 13.92; realised vol 83% -> weight 0.25
- 2026-09-28 11:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.323 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-28 11:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-28 11:23Z DOT buy target 0.25 (held 0.00) — enter long: higher low 1.075 vs prior low 0.939 (+14.5%) then broke above the reaction high 1.162 at 1.195; realised vol 94% -> weight 0.25
- 2026-09-28 11:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.14 not a higher low vs prior low 50.28 (need +10.0%)
- 2026-09-28 12:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.798e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-28 12:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2500 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-28 12:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 105.6 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-28 12:29Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.2457 still above the 48h low 0.2424; realised vol 78% -> weight 0.25
- 2026-09-28 12:29Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 10.49 still above the 48h low 10.35; realised vol 93% -> weight 0.25
- 2026-09-28 12:29Z LINK hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: price 14.06 still above the 48h low 13.57; realised vol 83% -> weight 0.25
- 2026-09-28 12:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.323 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-28 12:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-28 12:29Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 1.196 still above the 48h low 1.188; realised vol 94% -> weight 0.25
- 2026-09-28 12:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.14 not a higher low vs prior low 50.28 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 12 fills (6 buy / 6 sell), traded 27,788, gross pnl +184.63, +133 bps per round trip, avg half spread 2.3 bps, open 11635.5
- AVAX: 9 fills (4 buy / 5 sell), traded 16,757, gross pnl +755.99, +902 bps per round trip, avg half spread 1.4 bps, open 271.951
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 10 fills (5 buy / 5 sell), traded 19,617, gross pnl +190.23, +194 bps per round trip, avg half spread 3.2 bps, open 2357.66
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 9 fills (5 buy / 4 sell), traded 20,124, gross pnl +265.19, +264 bps per round trip, avg half spread 2.8 bps, open 203.945
- LTC: 5 fills (2 buy / 3 sell), traded 7,523, gross pnl +177.57, +472 bps per round trip, avg half spread 2.3 bps
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-28 08:27Z buy AVAX 2,851 @ 10.4837 fee 2.85 slip 1.42 (half spread 1.4 bps)
- 2026-09-28 09:27Z buy ADA 2,844 @ 0.244404 fee 2.84 slip 1.42 (half spread 2.4 bps)
- 2026-09-28 09:27Z buy LINK 2,844 @ 13.646 fee 2.84 slip 1.47 (half spread 3.2 bps)
- 2026-09-28 09:27Z buy DOT 2,841 @ 1.19914 fee 2.84 slip 1.52 (half spread 3.3 bps)
- 2026-09-28 10:25Z sell LINK 2,870 @ 13.7708 fee 2.87 slip 1.44 (half spread 3.0 bps)
- 2026-09-28 10:25Z sell DOT 2,828 @ 1.19376 fee 2.83 slip 1.51 (half spread 3.3 bps)
- 2026-09-28 11:23Z buy LINK 2,856 @ 14.0056 fee 2.86 slip 1.43 (half spread 2.8 bps)
- 2026-09-28 11:23Z buy DOT 2,830 @ 1.20054 fee 2.83 slip 1.86 (half spread 4.6 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,220.01 (started 10,000 at 2026-09-25 04:23Z), net +2.20% since start
- 24h -0.77%, 7d +2.28%, 30d +2.28%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 261.58; cost coverage 6.29
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-28 12:29Z; halted today: False

last decisions (newest last):

- 2026-09-28 11:23Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +14.47% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 11:23Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +22.55% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-28 11:23Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.010 below threshold 0.05 | stay long: 720h return +44.42% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 11:23Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +22.87% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 11:23Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.49% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 11:23Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +10.02% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-28 11:23Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +42.23% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 11:23Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +46.10% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 12:29Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +7.05% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 12:29Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +9.53% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 12:29Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +14.65% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 12:29Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +22.97% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-28 12:29Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.011 below threshold 0.05 | stay long: 720h return +44.48% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 12:29Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.008 below threshold 0.05 | stay long: 720h return +24.34% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 12:29Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +7.94% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 12:29Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +10.28% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-28 12:29Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +42.36% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 12:29Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +46.35% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +59.13, +295 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +2.84, +63 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -7.22, -139 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -45.40, -881 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +33.46, +219 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -3.09, -59 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +165.66, +817 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +25.86, +130 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -2.97, -25 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +33.30, +109 bps per round trip, avg half spread 0.7 bps, open 665.342

last fills:

- 2026-09-25 22:21Z sell LINK 979 @ 13.7945 fee 0.98 slip 0.49 (half spread 2.4 bps)
- 2026-09-25 22:21Z sell DOT 1,014 @ 1.19895 fee 1.01 slip 0.51 (half spread 0.4 bps)
- 2026-09-25 22:21Z sell LTC 719 @ 72.2139 fee 0.72 slip 0.36 (half spread 2.8 bps)
- 2026-09-25 22:21Z buy BTC 1,040 @ 83966.2 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-09-25 22:21Z buy ETH 1,040 @ 2688.17 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-09-25 22:21Z buy AVAX 907 @ 10.5508 fee 0.91 slip 0.45 (half spread 0.5 bps)
- 2026-09-25 22:21Z buy XRP 1,040 @ 1.5631 fee 1.04 slip 0.52 (half spread 1.0 bps)
- 2026-09-25 22:21Z buy DOGE 1,031 @ 0.0985782 fee 1.03 slip 0.52 (half spread 0.1 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1017 candles, 2026-08-17 03:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1017 candles, 2026-08-17 03:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1017 candles, 2026-08-17 03:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1017 candles, 2026-08-17 03:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- AVAX: live 1017 candles, 2026-08-17 03:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1017 candles, 2026-08-17 03:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 989 candles, 2026-08-18 07:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOGE: live 989 candles, 2026-08-18 07:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- DOT: live 989 candles, 2026-08-18 07:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 989 candles, 2026-08-18 07:00Z to 2026-09-28 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
