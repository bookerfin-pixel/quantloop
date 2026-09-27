# quantloop summary — generated 2026-09-27 19:20Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 11.6 of 60, 48.4 days until the verdict
  so far: champion +23.87% (DD -6.75%, 78 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +9.06% (usual 0.54, this window 0.78) vs challenger1 -7.20% (usual 0.37, this window 0.13); the rule compares on skill, daily edge t -1.7 over 12 days
  market over the window: BTC +11.71%, equal weight basket of 10 pairs +27.54%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 6.5 of 60, 53.5 days until the verdict
  so far: champion +7.81% (DD -6.75%, 40 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +4.36% (usual 0.54, this window 0.85) vs challenger2 -1.83% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -1.3 over 7 days
  market over the window: BTC +1.25%, equal weight basket of 10 pairs +6.39%, basket max drawdown -7%, basket realised vol 59% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 2.7 of 60, 57.3 days until the verdict
  so far: champion +4.38% (DD -2.14%, 20 fills) vs challenger3 +0.43% (DD -0.32%, 1 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +2.23% (usual 0.55, this window 0.98) vs challenger3 +0.22% (usual 0.05, this window 0.02); the rule compares on skill, daily edge t -0.6 over 3 days
  market over the window: BTC +0.69%, equal weight basket of 10 pairs +3.95%, basket max drawdown -2%, basket realised vol 47% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 1.9 of 60, 58.1 days until the verdict
  so far: champion +1.33% (DD -2.14%, 12 fills) vs challenger4 +1.05% (DD -1.73%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +1.01% (usual 0.55, this window 0.97) vs challenger4 +0.77% (usual 0.48, this window 1.00); the rule compares on skill
  market over the window: BTC +0.87%, equal weight basket of 10 pairs +0.59%, basket max drawdown -2%, basket realised vol 45% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 12,387.45 (started 10,000 at 2026-09-16 03:55Z), net +23.87% since start
- 24h +1.40%, 7d +9.09%, 30d +23.87%, max drawdown -6.75%
- fills 78 total, 40 in the last 7d
- costs 172.28 (fees 113.86 + slippage 58.42); gross pnl 2,559.73; cost coverage 14.86
- cash 1,757.80; positions: ADA 7032.63, AVAX 147.431, DOGE 18175.9, DOT 1429.85, LINK 126.164, SOL 14.9336
- last run 2026-09-27 19:20Z; halted today: False

last decisions (newest last):

- 2026-09-27 18:24Z SOL hold target 0.17 (held 0.15) — hold: weight change +0.019 below threshold 0.05 | stay long: 72h return +4.58% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-27 18:24Z ADA hold target 0.17 (held 0.15) — hold: weight change +0.021 below threshold 0.05 | stay long: 72h return +3.37% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-27 18:24Z AVAX hold target 0.17 (held 0.13) — hold: weight change +0.036 below threshold 0.05 | stay long: 72h return +6.74% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-27 18:24Z LINK hold target 0.17 (held 0.14) — hold: weight change +0.022 below threshold 0.05 | stay long: 72h return +9.31% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-27 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.20% not above entry band +1.0% and price below 24h EMA
- 2026-09-27 18:24Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: 72h return +1.15% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-27 18:24Z DOT hold target 0.17 (held 0.15) — hold: weight change +0.021 below threshold 0.05 | stay long: 72h return +7.25% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-09-27 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.61% not above entry band +1.0% and price below 24h EMA
- 2026-09-27 19:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.40% not above entry band +1.0%
- 2026-09-27 19:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.31% not above entry band +1.0%
- 2026-09-27 19:20Z SOL hold target 0.17 (held 0.15) — hold: weight change +0.018 below threshold 0.05 | stay long: 72h return +5.01% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-27 19:20Z ADA hold target 0.17 (held 0.15) — hold: weight change +0.021 below threshold 0.05 | stay long: 72h return +3.68% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-09-27 19:20Z AVAX hold target 0.17 (held 0.13) — hold: weight change +0.035 below threshold 0.05 | stay long: 72h return +5.80% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-27 19:20Z LINK hold target 0.17 (held 0.14) — hold: weight change +0.023 below threshold 0.05 | stay long: 72h return +5.23% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-27 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.12% not above entry band +1.0%
- 2026-09-27 19:20Z DOGE hold target 0.17 (held 0.14) — hold: weight change +0.024 below threshold 0.05 | stay long: 72h return +1.09% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-27 19:20Z DOT hold target 0.17 (held 0.15) — hold: weight change +0.021 below threshold 0.05 | stay long: 72h return +7.55% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-09-27 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.17% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (4 buy / 5 sell), traded 15,700, gross pnl +198.96, +253 bps per round trip, avg half spread 2.5 bps, open 7032.63
- AVAX: 9 fills (4 buy / 5 sell), traded 15,572, gross pnl +752.94, +967 bps per round trip, avg half spread 1.2 bps, open 147.431
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 9 fills (6 buy / 3 sell), traded 13,297, gross pnl +13.47, +20 bps per round trip, avg half spread 1.9 bps, open 18175.9
- DOT: 9 fills (5 buy / 4 sell), traded 9,022, gross pnl +345.18, +765 bps per round trip, avg half spread 3.4 bps, open 1429.85
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 9 fills (4 buy / 5 sell), traded 11,413, gross pnl +247.22, +433 bps per round trip, avg half spread 2.3 bps, open 126.164
- LTC: 9 fills (3 buy / 6 sell), traded 13,674, gross pnl +599.56, +877 bps per round trip, avg half spread 2.1 bps
- SOL: 7 fills (4 buy / 3 sell), traded 9,669, gross pnl +119.21, +247 bps per round trip, avg half spread 0.5 bps, open 14.9336
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-26 11:20Z buy ADA 1,806 @ 0.256778 fee 1.81 slip 0.90 (half spread 2.7 bps)
- 2026-09-26 15:21Z sell SOL 1,283 @ 121.104 fee 1.28 slip 0.64 (half spread 0.4 bps)
- 2026-09-26 15:21Z sell LINK 680 @ 14.3363 fee 0.68 slip 0.37 (half spread 3.4 bps)
- 2026-09-26 15:21Z sell DOT 769 @ 1.26502 fee 0.77 slip 0.38 (half spread 2.8 bps)
- 2026-09-26 15:21Z sell LTC 699 @ 72.8586 fee 0.70 slip 0.35 (half spread 2.1 bps)
- 2026-09-26 15:21Z buy AVAX 1,634 @ 11.0855 fee 1.63 slip 0.82 (half spread 0.9 bps)
- 2026-09-26 15:21Z buy DOGE 1,790 @ 0.0984591 fee 1.79 slip 0.89 (half spread 0.3 bps)
- 2026-09-27 15:21Z sell LTC 1,760 @ 70.8745 fee 1.76 slip 0.88 (half spread 1.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-27 19:20Z; halted today: False

last decisions (newest last):

- 2026-09-27 18:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.30 not below -2.0
- 2026-09-27 18:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.00 not below -2.0
- 2026-09-27 18:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.74 not below -2.0
- 2026-09-27 18:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.48 not below -2.0
- 2026-09-27 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.51 not below -2.0
- 2026-09-27 18:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.64 not below -2.0
- 2026-09-27 18:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.75 not below -2.0
- 2026-09-27 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.20 not below -2.0
- 2026-09-27 19:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.63 not below -2.0
- 2026-09-27 19:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.44 not below -2.0
- 2026-09-27 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.52 not below -2.0
- 2026-09-27 19:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.18 not below -2.0
- 2026-09-27 19:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.78 not below -2.0
- 2026-09-27 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.53 not below -2.0
- 2026-09-27 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.68 not below -2.0
- 2026-09-27 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.77 not below -2.0
- 2026-09-27 19:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.98 not below -2.0
- 2026-09-27 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.22 not below -2.0

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
- last run 2026-09-27 19:20Z; halted today: False

last decisions (newest last):

- 2026-09-27 18:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2698 not above 120h high 2779
- 2026-09-27 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-27 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 11,562.11 (started 10,000 at 2026-09-16 23:20Z), net +15.62% since start
- 24h +0.43%, 7d +1.82%, 30d +15.62%, max drawdown -6.74%
- fills 50 total, 12 in the last 7d
- costs 105.62 (fees 69.54 + slippage 36.08); gross pnl 1,667.73; cost coverage 15.79
- cash 8,631.39; positions: DOT 2325.6
- last run 2026-09-27 19:20Z; halted today: False

last decisions (newest last):

- 2026-09-27 18:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 100.8 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-27 18:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2006 not a higher low vs prior low 0.191 (need +10.0%)
- 2026-09-27 18:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.581 not a higher low vs prior low 7.197 (need +10.0%)
- 2026-09-27 18:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.31 not a higher low vs prior low 10.66 (need +10.0%)
- 2026-09-27 18:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.291 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-27 18:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08136 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-27 18:24Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: price 1.248 still above the 48h low 1.177; realised vol 97% -> weight 0.25
- 2026-09-27 18:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 53.41 not a higher low vs prior low 50.28 (need +10.0%)
- 2026-09-27 19:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.635e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-27 19:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2444 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-27 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 100.8 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-27 19:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2006 not a higher low vs prior low 0.191 (need +10.0%)
- 2026-09-27 19:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.581 not a higher low vs prior low 7.197 (need +10.0%)
- 2026-09-27 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.31 not a higher low vs prior low 10.66 (need +10.0%)
- 2026-09-27 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.291 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-27 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08136 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-27 19:20Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: price 1.26 still above the 48h low 1.187; realised vol 97% -> weight 0.25
- 2026-09-27 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 53.41 not a higher low vs prior low 50.28 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 7,783, gross pnl +116.26, +299 bps per round trip, avg half spread 2.4 bps
- AVAX: 8 fills (3 buy / 5 sell), traded 13,906, gross pnl +728.79, +1048 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 6 fills (3 buy / 3 sell), traded 8,299, gross pnl +261.70, +631 bps per round trip, avg half spread 3.1 bps, open 2325.6
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 4 fills (2 buy / 2 sell), traded 5,855, gross pnl +90.07, +308 bps per round trip, avg half spread 2.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 7,523, gross pnl +177.57, +472 bps per round trip, avg half spread 2.3 bps
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-23 14:23Z sell BTC 1,463 @ 84040.5 fee 1.46 slip 0.73 (half spread 2.3 bps)
- 2026-09-23 14:23Z sell SOL 1,170 @ 113.378 fee 1.17 slip 0.59 (half spread 0.4 bps)
- 2026-09-23 14:23Z sell ADA 1,481 @ 0.237347 fee 1.48 slip 0.74 (half spread 2.9 bps)
- 2026-09-23 14:23Z sell AVAX 1,293 @ 10.3313 fee 1.29 slip 0.65 (half spread 2.4 bps)
- 2026-09-23 14:23Z sell XRP 1,531 @ 1.51841 fee 1.53 slip 0.77 (half spread 1.9 bps)
- 2026-09-23 14:23Z sell DOGE 1,415 @ 0.0938014 fee 1.42 slip 1.32 (half spread 7.3 bps)
- 2026-09-23 14:23Z sell LTC 1,466 @ 60.04 fee 1.47 slip 0.73 (half spread 1.7 bps)
- 2026-09-27 14:20Z buy DOT 2,878 @ 1.23757 fee 2.88 slip 1.44 (half spread 0.4 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,361.06 (started 10,000 at 2026-09-25 04:23Z), net +3.61% since start
- 24h +1.30%, 7d +3.69%, 30d +3.69%, max drawdown -1.73%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 402.63; cost coverage 9.69
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-27 19:20Z; halted today: False

last decisions (newest last):

- 2026-09-27 18:24Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +16.61% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 18:24Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +25.22% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 18:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.009 below threshold 0.05 | stay long: 720h return +50.79% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 18:24Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +22.90% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 18:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +9.77% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-27 18:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +14.07% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 18:24Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +46.97% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 18:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +45.01% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +9.37% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-27 19:20Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +11.09% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +19.53% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +27.85% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +52.49% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +24.65% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +12.04% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +15.94% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +49.51% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-27 19:20Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +45.86% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +79.93, +398 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +41.79, +921 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +11.12, +214 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -10.57, -205 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +67.43, +441 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +3.71, +71 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +119.93, +592 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +12.40, +62 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +30.49, +253 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +46.42, +152 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1000 candles, 2026-08-17 03:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1000 candles, 2026-08-17 03:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1000 candles, 2026-08-17 03:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1000 candles, 2026-08-17 03:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- AVAX: live 1000 candles, 2026-08-17 03:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.2 bps
- LINK: live 1000 candles, 2026-08-17 03:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 972 candles, 2026-08-18 07:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 972 candles, 2026-08-18 07:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.8 bps
- DOT: live 972 candles, 2026-08-18 07:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 972 candles, 2026-08-18 07:00Z to 2026-09-27 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
