# quantloop summary — generated 2026-09-26 02:21Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 9.9 of 60, 50.1 days until the verdict
  so far: champion +23.79% (DD -6.75%, 66 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +9.08% (usual 0.54, this window 0.75) vs challenger1 -7.13% (usual 0.37, this window 0.16); the rule compares on skill, daily edge t -1.7 over 10 days
  market over the window: BTC +10.75%, equal weight basket of 10 pairs +27.35%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 4.7 of 60, 55.3 days until the verdict
  so far: champion +7.74% (DD -6.75%, 28 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +4.33% (usual 0.54, this window 0.80) vs challenger2 -1.80% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -1.3 over 5 days
  market over the window: BTC +0.38%, equal weight basket of 10 pairs +6.31%, basket max drawdown -7%, basket realised vol 63% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 1.0 of 60, 59.0 days until the verdict
  so far: champion +4.32% (DD -1.31%, 8 fills) vs challenger3 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +2.24% (usual 0.55, this window 0.99) vs challenger3 -0.20% (usual 0.05, this window 0.00); the rule compares on skill
  market over the window: BTC -0.17%, equal weight basket of 10 pairs +3.80%, basket max drawdown -1%, basket realised vol 50% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 0.2 of 60, 59.8 days until the verdict
  so far: champion +1.26% (DD -0.29%, 0 fills) vs challenger4 +1.10% (DD -0.16%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +1.02% (usual 0.55, this window 0.98) vs challenger4 +0.89% (usual 0.48, this window 1.00); the rule compares on skill
  market over the window: BTC +0.00%, equal weight basket of 10 pairs +0.44%, basket max drawdown -0%, basket realised vol 40% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 12,379.30 (started 10,000 at 2026-09-16 03:55Z), net +23.79% since start
- 24h +4.32%, 7d +13.35%, 30d +23.79%, max drawdown -6.75%
- fills 66 total, 52 in the last 7d
- costs 149.69 (fees 98.82 + slippage 50.87); gross pnl 2,528.98; cost coverage 16.90
- cash 264.09; positions: ADA 9547.33, DOT 2037.76, LINK 173.711, LTC 34.4177, SOL 17.9866
- last run 2026-09-26 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-26 01:20Z SOL hold target 0.20 (held 0.18) — hold: weight change +0.023 below threshold 0.05 | stay long: 72h return +2.28% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-26 01:20Z ADA hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +1.06% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.78% not above entry band +1.0%
- 2026-09-26 01:20Z LINK hold target 0.20 (held 0.20) — hold: weight change +0.004 below threshold 0.05 | stay long: 72h return +7.96% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.39% not above entry band +1.0%
- 2026-09-26 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.23% not above entry band +1.0%
- 2026-09-26 01:20Z DOT hold target 0.20 (held 0.21) — hold: weight change -0.005 below threshold 0.05 | stay long: 72h return +0.90% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-26 01:20Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +15.39% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-26 02:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.66% not above entry band +1.0% and price below 24h EMA
- 2026-09-26 02:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.25% not above entry band +1.0%
- 2026-09-26 02:21Z SOL hold target 0.20 (held 0.18) — hold: weight change +0.023 below threshold 0.05 | stay long: 72h return +3.17% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-26 02:21Z ADA hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +3.39% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 02:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.31% not above entry band +1.0%
- 2026-09-26 02:21Z LINK hold target 0.20 (held 0.20) — hold: weight change +0.004 below threshold 0.05 | stay long: 72h return +7.52% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-26 02:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.69% not above entry band +1.0%
- 2026-09-26 02:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.44% not above entry band +1.0%
- 2026-09-26 02:21Z DOT hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.84% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-26 02:21Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +16.33% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 7 fills (3 buy / 4 sell), traded 11,442, gross pnl +245.79, +430 bps per round trip, avg half spread 2.4 bps, open 9547.33
- AVAX: 8 fills (3 buy / 5 sell), traded 13,938, gross pnl +760.09, +1091 bps per round trip, avg half spread 1.3 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 8 fills (5 buy / 3 sell), traded 11,507, gross pnl +29.68, +52 bps per round trip, avg half spread 2.1 bps
- DOT: 8 fills (5 buy / 3 sell), traded 8,253, gross pnl +258.11, +625 bps per round trip, avg half spread 3.5 bps, open 2037.76
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 6 fills (3 buy / 3 sell), traded 9,478, gross pnl +200.89, +424 bps per round trip, avg half spread 2.3 bps, open 173.711
- LTC: 7 fills (3 buy / 4 sell), traded 11,216, gross pnl +655.03, +1168 bps per round trip, avg half spread 2.2 bps, open 34.4177
- SOL: 5 fills (3 buy / 2 sell), traded 7,474, gross pnl +96.18, +257 bps per round trip, avg half spread 0.4 bps, open 17.9866
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-25 11:22Z sell ADA 643 @ 0.255978 fee 0.64 slip 0.32 (half spread 2.2 bps)
- 2026-09-25 11:22Z sell LINK 711 @ 14.0686 fee 0.71 slip 0.36 (half spread 1.9 bps)
- 2026-09-25 11:22Z sell LTC 827 @ 71.0045 fee 0.83 slip 0.41 (half spread 1.4 bps)
- 2026-09-25 11:22Z buy SOL 2,176 @ 120.975 fee 2.18 slip 1.09 (half spread 0.4 bps)
- 2026-09-25 12:27Z sell XRP 722 @ 1.60683 fee 0.72 slip 0.36 (half spread 0.2 bps)
- 2026-09-25 12:27Z buy DOT 721 @ 1.18544 fee 0.72 slip 0.39 (half spread 3.4 bps)
- 2026-09-25 20:20Z sell XRP 1,979 @ 1.569 fee 1.98 slip 0.99 (half spread 0.2 bps)
- 2026-09-25 20:20Z buy DOT 1,712 @ 1.19734 fee 1.71 slip 0.99 (half spread 3.8 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-26 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-26 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.41 not below -2.0
- 2026-09-26 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.36 not below -2.0
- 2026-09-26 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.67 not below -2.0
- 2026-09-26 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.98 not below -2.0
- 2026-09-26 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.19 not below -2.0
- 2026-09-26 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.14 not below -2.0
- 2026-09-26 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.42 not below -2.0
- 2026-09-26 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.98 not below -2.0
- 2026-09-26 02:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.63 not below -2.0
- 2026-09-26 02:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.63 not below -2.0
- 2026-09-26 02:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.48 not below -2.0
- 2026-09-26 02:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.57 not below -2.0
- 2026-09-26 02:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.80 not below -2.0
- 2026-09-26 02:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.83 not below -2.0
- 2026-09-26 02:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.30 not below -2.0
- 2026-09-26 02:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.20 not below -2.0
- 2026-09-26 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.59 not below -2.0
- 2026-09-26 02:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.00 not below -2.0

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
- 24h +0.00%, 7d +0.41%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 18 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-26 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-26 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-26 02:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- 24h +0.00%, 7d +5.41%, 30d +15.12%, max drawdown -6.43%
- fills 49 total, 35 in the last 7d
- costs 101.31 (fees 66.66 + slippage 34.64); gross pnl 1,613.66; cost coverage 15.93
- cash 11,512.35; positions: none
- last run 2026-09-26 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-26 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 96.43 not a higher low vs prior low 96.49 (need +10.0%)
- 2026-09-26 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.191 not a higher low vs prior low 0.1942 (need +10.0%)
- 2026-09-26 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.197 not a higher low vs prior low 7.224 (need +10.0%)
- 2026-09-26 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.66 not a higher low vs prior low 10.88 (need +10.0%)
- 2026-09-26 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.265 not a higher low vs prior low 1.278 (need +10.0%)
- 2026-09-26 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.07958 (need +10.0%)
- 2026-09-26 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.939 not a higher low vs prior low 0.9222 (need +10.0%)
- 2026-09-26 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.28 not a higher low vs prior low 50.95 (need +10.0%)
- 2026-09-26 02:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.544e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-26 02:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2388 not a higher low vs prior low 2389 (need +10.0%)
- 2026-09-26 02:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 96.43 not a higher low vs prior low 96.49 (need +10.0%)
- 2026-09-26 02:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.191 not a higher low vs prior low 0.1942 (need +10.0%)
- 2026-09-26 02:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.197 not a higher low vs prior low 7.224 (need +10.0%)
- 2026-09-26 02:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.66 not a higher low vs prior low 10.88 (need +10.0%)
- 2026-09-26 02:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.265 not a higher low vs prior low 1.278 (need +10.0%)
- 2026-09-26 02:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.07958 (need +10.0%)
- 2026-09-26 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.939 not a higher low vs prior low 0.9278 (need +10.0%)
- 2026-09-26 02:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.28 not a higher low vs prior low 50.95 (need +10.0%)

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

- equity 10,366.52 (started 10,000 at 2026-09-25 04:23Z), net +3.67% since start
- 24h +3.74%, 7d +3.74%, 30d +3.74%, max drawdown -1.44%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 408.09; cost coverage 9.82
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-26 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-26 01:20Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +20.77% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +21.96% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z AVAX hold target 0.09 (held 0.09) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +43.53% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +22.16% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +11.27% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +13.77% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +39.25% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 01:20Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +45.11% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z BTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +6.56% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 02:21Z ETH hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +7.77% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-26 02:21Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +20.29% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +23.98% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z AVAX hold target 0.09 (held 0.09) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +46.20% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +20.44% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +11.82% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +13.69% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +39.87% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-26 02:21Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +45.35% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +100.83, +503 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +33.28, +734 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +1.63, +31 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl +4.61, +89 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +31.82, +208 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +2.53, +49 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +107.19, +529 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +38.45, +193 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +18.03, +150 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +69.74, +229 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 959 candles, 2026-08-17 03:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 959 candles, 2026-08-17 03:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 959 candles, 2026-08-17 03:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 959 candles, 2026-08-17 03:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- AVAX: live 959 candles, 2026-08-17 03:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 959 candles, 2026-08-17 03:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 931 candles, 2026-08-18 07:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 931 candles, 2026-08-18 07:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.9 bps
- DOT: live 931 candles, 2026-08-18 07:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 931 candles, 2026-08-18 07:00Z to 2026-09-26 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
