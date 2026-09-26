# quantloop summary — generated 2026-09-26 18:24Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 10.5 of 60, 49.5 days until the verdict
  so far: champion +23.59% (DD -6.75%, 77 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +8.89% (usual 0.54, this window 0.76) vs challenger1 -7.12% (usual 0.37, this window 0.15); the rule compares on skill, daily edge t -1.7 over 11 days
  market over the window: BTC +10.83%, equal weight basket of 10 pairs +27.32%, basket max drawdown -7%, basket realised vol 59% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 5.4 of 60, 54.6 days until the verdict
  so far: champion +7.56% (DD -6.75%, 39 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +4.19% (usual 0.54, this window 0.82) vs challenger2 -1.78% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -1.3 over 6 days
  market over the window: BTC +0.45%, equal weight basket of 10 pairs +6.24%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 1.6 of 60, 58.4 days until the verdict
  so far: champion +4.15% (DD -1.31%, 19 fills) vs challenger3 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +2.08% (usual 0.55, this window 0.98) vs challenger3 -0.20% (usual 0.05, this window 0.00); the rule compares on skill
  market over the window: BTC -0.10%, equal weight basket of 10 pairs +3.78%, basket max drawdown -1%, basket realised vol 47% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 0.8 of 60, 59.2 days until the verdict
  so far: champion +1.10% (DD -1.19%, 11 fills) vs challenger4 +0.70% (DD -1.19%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +0.87% (usual 0.55, this window 0.96) vs challenger4 +0.51% (usual 0.48, this window 1.00); the rule compares on skill
  market over the window: BTC +0.07%, equal weight basket of 10 pairs +0.41%, basket max drawdown -1%, basket realised vol 42% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 12,359.13 (started 10,000 at 2026-09-16 03:55Z), net +23.59% since start
- 24h +1.58%, 7d +12.20%, 30d +23.59%, max drawdown -6.75%
- fills 77 total, 58 in the last 7d
- costs 169.64 (fees 112.10 + slippage 57.54); gross pnl 2,528.76; cost coverage 14.91
- cash -0.00; positions: ADA 7032.63, AVAX 147.431, DOGE 18175.9, DOT 1429.85, LINK 126.164, LTC 24.8264, SOL 14.9336
- last run 2026-09-26 18:24Z; halted today: False

last decisions (newest last):

- 2026-09-26 17:20Z SOL hold target 0.13 (held 0.15) — hold: weight change -0.019 below threshold 0.05 | stay long: 72h return +6.30% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-26 17:20Z ADA hold target 0.13 (held 0.15) — hold: weight change -0.019 below threshold 0.05 | stay long: 72h return +8.30% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 17:20Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.014 below threshold 0.05 | stay long: 72h return +7.32% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-26 17:20Z LINK hold target 0.13 (held 0.15) — hold: weight change -0.019 below threshold 0.05 | stay long: 72h return +16.91% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-26 17:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-26 17:20Z DOGE hold target 0.13 (held 0.14) — hold: weight change -0.017 below threshold 0.05 | stay long: 72h return +6.48% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 17:20Z DOT hold target 0.13 (held 0.15) — hold: weight change -0.020 below threshold 0.05 | stay long: 72h return +17.67% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-26 17:20Z LTC hold target 0.13 (held 0.14) — hold: weight change -0.018 below threshold 0.05 | stay long: 72h return +20.51% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-26 18:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.22% not above entry band +1.0%
- 2026-09-26 18:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.85% not above entry band +1.0%
- 2026-09-26 18:24Z SOL hold target 0.14 (held 0.15) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +6.05% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-26 18:24Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +7.14% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 18:24Z AVAX hold target 0.13 (held 0.13) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +5.30% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-26 18:24Z LINK hold target 0.14 (held 0.15) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +16.79% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-26 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-26 18:24Z DOGE hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +5.75% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 18:24Z DOT hold target 0.14 (held 0.15) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +15.12% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-26 18:24Z LTC hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +18.36% vs exit band -1.0% and price within 2.0% of 24h EMA; real...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (4 buy / 5 sell), traded 15,700, gross pnl +192.40, +245 bps per round trip, avg half spread 2.5 bps, open 7032.63
- AVAX: 9 fills (4 buy / 5 sell), traded 15,572, gross pnl +725.45, +932 bps per round trip, avg half spread 1.2 bps, open 147.431
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 9 fills (6 buy / 3 sell), traded 13,297, gross pnl +13.94, +21 bps per round trip, avg half spread 1.9 bps, open 18175.9
- DOT: 9 fills (5 buy / 4 sell), traded 9,022, gross pnl +339.96, +754 bps per round trip, avg half spread 3.4 bps, open 1429.85
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 9 fills (4 buy / 5 sell), traded 11,413, gross pnl +259.89, +455 bps per round trip, avg half spread 2.3 bps, open 126.164
- LTC: 8 fills (3 buy / 5 sell), traded 11,915, gross pnl +624.88, +1049 bps per round trip, avg half spread 2.2 bps, open 24.8264
- SOL: 7 fills (4 buy / 3 sell), traded 9,669, gross pnl +89.04, +184 bps per round trip, avg half spread 0.5 bps, open 14.9336
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-26 11:20Z sell LINK 632 @ 14.2776 fee 0.63 slip 0.32 (half spread 0.2 bps)
- 2026-09-26 11:20Z buy ADA 1,806 @ 0.256778 fee 1.81 slip 0.90 (half spread 2.7 bps)
- 2026-09-26 15:21Z sell SOL 1,283 @ 121.104 fee 1.28 slip 0.64 (half spread 0.4 bps)
- 2026-09-26 15:21Z sell LINK 680 @ 14.3363 fee 0.68 slip 0.37 (half spread 3.4 bps)
- 2026-09-26 15:21Z sell DOT 769 @ 1.26502 fee 0.77 slip 0.38 (half spread 2.8 bps)
- 2026-09-26 15:21Z sell LTC 699 @ 72.8586 fee 0.70 slip 0.35 (half spread 2.1 bps)
- 2026-09-26 15:21Z buy AVAX 1,634 @ 11.0855 fee 1.63 slip 0.82 (half spread 0.9 bps)
- 2026-09-26 15:21Z buy DOGE 1,790 @ 0.0984591 fee 1.79 slip 0.89 (half spread 0.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-26 18:24Z; halted today: False

last decisions (newest last):

- 2026-09-26 17:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.33 not below -2.0
- 2026-09-26 17:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-09-26 17:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.90 not below -2.0
- 2026-09-26 17:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.07 not below -2.0
- 2026-09-26 17:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.90 not below -2.0
- 2026-09-26 17:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.02 not below -2.0
- 2026-09-26 17:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.80 not below -2.0
- 2026-09-26 17:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.72 not below -2.0
- 2026-09-26 18:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.55 not below -2.0
- 2026-09-26 18:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.52 not below -2.0
- 2026-09-26 18:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-09-26 18:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.20 not below -2.0
- 2026-09-26 18:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.76 not below -2.0
- 2026-09-26 18:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.07 not below -2.0
- 2026-09-26 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.79 not below -2.0
- 2026-09-26 18:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.91 not below -2.0
- 2026-09-26 18:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.19 not below -2.0
- 2026-09-26 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.60 not below -2.0

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
- 24h +0.00%, 7d -0.45%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 13 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-26 18:24Z; halted today: False

last decisions (newest last):

- 2026-09-26 17:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 17:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 11,512.35 (started 10,000 at 2026-09-16 23:20Z), net +15.12% since start
- 24h +0.00%, 7d +4.51%, 30d +15.12%, max drawdown -6.43%
- fills 49 total, 30 in the last 7d
- costs 101.31 (fees 66.66 + slippage 34.64); gross pnl 1,613.66; cost coverage 15.93
- cash 11,512.35; positions: none
- last run 2026-09-26 18:24Z; halted today: False

last decisions (newest last):

- 2026-09-26 17:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 97.04 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-26 17:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.192 not a higher low vs prior low 0.191 (need +10.0%)
- 2026-09-26 17:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.24 not a higher low vs prior low 7.197 (need +10.0%)
- 2026-09-26 17:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.71 not a higher low vs prior low 10.66 (need +10.0%)
- 2026-09-26 17:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.266 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-26 17:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.07889 (need +10.0%)
- 2026-09-26 17:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9729 not a higher low vs prior low 0.939 (need +10.0%)
- 2026-09-26 17:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.64 not a higher low vs prior low 50.28 (need +10.0%)
- 2026-09-26 18:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.556e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-26 18:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2388 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-26 18:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 97.04 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-26 18:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.192 not a higher low vs prior low 0.191 (need +10.0%)
- 2026-09-26 18:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.24 not a higher low vs prior low 7.197 (need +10.0%)
- 2026-09-26 18:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.71 not a higher low vs prior low 10.66 (need +10.0%)
- 2026-09-26 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.266 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-26 18:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.07889 (need +10.0%)
- 2026-09-26 18:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9729 not a higher low vs prior low 0.939 (need +10.0%)
- 2026-09-26 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.68 not a higher low vs prior low 50.28 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 7,783, gross pnl +116.26, +299 bps per round trip, avg half spread 2.4 bps
- AVAX: 8 fills (3 buy / 5 sell), traded 13,906, gross pnl +728.79, +1048 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 5 fills (2 buy / 3 sell), traded 5,421, gross pnl +207.63, +766 bps per round trip, avg half spread 3.6 bps
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 4 fills (2 buy / 2 sell), traded 5,855, gross pnl +90.07, +308 bps per round trip, avg half spread 2.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 7,523, gross pnl +177.57, +472 bps per round trip, avg half spread 2.3 bps
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-23 13:24Z sell ETH 1,463 @ 2713.17 fee 1.46 slip 0.73 (half spread 0.4 bps)
- 2026-09-23 14:23Z sell BTC 1,463 @ 84040.5 fee 1.46 slip 0.73 (half spread 2.3 bps)
- 2026-09-23 14:23Z sell SOL 1,170 @ 113.378 fee 1.17 slip 0.59 (half spread 0.4 bps)
- 2026-09-23 14:23Z sell ADA 1,481 @ 0.237347 fee 1.48 slip 0.74 (half spread 2.9 bps)
- 2026-09-23 14:23Z sell AVAX 1,293 @ 10.3313 fee 1.29 slip 0.65 (half spread 2.4 bps)
- 2026-09-23 14:23Z sell XRP 1,531 @ 1.51841 fee 1.53 slip 0.77 (half spread 1.9 bps)
- 2026-09-23 14:23Z sell DOGE 1,415 @ 0.0938014 fee 1.42 slip 1.32 (half spread 7.3 bps)
- 2026-09-23 14:23Z sell LTC 1,466 @ 60.04 fee 1.47 slip 0.73 (half spread 1.7 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,325.46 (started 10,000 at 2026-09-25 04:23Z), net +3.25% since start
- 24h +1.02%, 7d +3.33%, 30d +3.33%, max drawdown -1.44%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 367.03; cost coverage 8.83
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-26 18:24Z; halted today: False

last decisions (newest last):

- 2026-09-26 17:20Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +11.59% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 17:20Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +19.79% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 17:20Z AVAX hold target 0.09 (held 0.09) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +46.63% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 17:20Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +20.68% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 17:20Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +5.50% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 17:20Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +10.26% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 17:20Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +47.13% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 17:20Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +44.61% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 18:24Z BTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +4.55% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 18:24Z ETH hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +6.83% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 18:24Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +12.28% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 18:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +18.73% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 18:24Z AVAX hold target 0.09 (held 0.09) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +44.18% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 18:24Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +20.52% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 18:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +5.30% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 18:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +9.64% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 18:24Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +42.84% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 18:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +43.38% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +76.13, +379 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +25.75, +568 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +1.94, +37 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -10.30, -200 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +64.27, +421 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +0.25, +5 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +127.49, +629 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +21.97, +110 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +13.25, +110 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +46.27, +152 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 975 candles, 2026-08-17 03:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 975 candles, 2026-08-17 03:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 975 candles, 2026-08-17 03:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 975 candles, 2026-08-17 03:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- AVAX: live 975 candles, 2026-08-17 03:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 975 candles, 2026-08-17 03:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 947 candles, 2026-08-18 07:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOGE: live 947 candles, 2026-08-18 07:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.9 bps
- DOT: live 947 candles, 2026-08-18 07:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 947 candles, 2026-08-18 07:00Z to 2026-09-26 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
