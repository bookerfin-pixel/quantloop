# quantloop summary — generated 2026-09-25 17:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 9.5 of 60, 50.5 days until the verdict
  so far: champion +21.06% (DD -6.75%, 64 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +7.92% (usual 0.54, this window 0.74) vs challenger1 -6.05% (usual 0.37, this window 0.16); the rule compares on skill, daily edge t -1.5 over 10 days
  market over the window: BTC +10.31%, equal weight basket of 10 pairs +24.43%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 4.4 of 60, 55.6 days until the verdict
  so far: champion +5.36% (DD -6.75%, 26 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +3.23% (usual 0.54, this window 0.79) vs challenger2 -1.13% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -1.1 over 5 days
  market over the window: BTC -0.02%, equal weight basket of 10 pairs +3.95%, basket max drawdown -7%, basket realised vol 64% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 0.6 of 60, 59.4 days until the verdict
  so far: champion +2.02% (DD -1.31%, 6 fills) vs challenger3 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +1.19% (usual 0.55, this window 1.00) vs challenger3 -0.08% (usual 0.05, this window 0.00); the rule compares on skill
  market over the window: BTC -0.57%, equal weight basket of 10 pairs +1.51%, basket max drawdown -1%, basket realised vol 50% annualised
- challenger4: idle (free for a hypothesis)
- free slots: challenger4
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 12,106.31 (started 10,000 at 2026-09-16 03:55Z), net +21.06% since start
- 24h +1.55%, 7d +13.48%, 30d +21.06%, max drawdown -6.75%
- fills 64 total, 50 in the last 7d
- costs 144.02 (fees 95.13 + slippage 48.89); gross pnl 2,250.33; cost coverage 15.63
- cash -0.00; positions: ADA 9547.33, DOT 608.208, LINK 173.711, LTC 34.4177, SOL 17.9866, XRP 1261.6
- last run 2026-09-25 17:21Z; halted today: False

last decisions (newest last):

- 2026-09-25 16:24Z SOL hold target 0.17 (held 0.18) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +2.33% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-25 16:24Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +0.76% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.76% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 16:24Z LINK hold target 0.17 (held 0.20) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +6.00% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 16:24Z XRP hold target 0.17 (held 0.16) — hold: weight change +0.003 below threshold 0.05 | stay long: 72h return +0.26% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-09-25 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.55% not above entry band +1.0%
- 2026-09-25 16:24Z DOT none target 0.17 (held 0.06) — no fill possible (no cash or no position) | stay long: 72h return +0.40% vs exit band -1.0% and price above 24h EMA; realised vol 100% ->...
- 2026-09-25 16:24Z LTC hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +14.35% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-25 17:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 17:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 17:21Z SOL hold target 0.17 (held 0.18) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +2.89% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-25 17:21Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +1.79% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.56% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 17:21Z LINK hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +5.73% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 17:21Z XRP hold target 0.17 (held 0.16) — hold: weight change +0.003 below threshold 0.05 | stay long: 72h return -0.15% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-09-25 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.37% not above entry band +1.0%
- 2026-09-25 17:21Z DOT none target 0.17 (held 0.06) — no fill possible (no cash or no position) | stay long: 72h return +0.08% vs exit band -1.0% and price above 24h EMA; realised vol 100% ->...
- 2026-09-25 17:21Z LTC hold target 0.17 (held 0.20) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +11.74% vs exit band -1.0% and price within 2.0% of 24h EMA; real...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 7 fills (3 buy / 4 sell), traded 11,442, gross pnl +179.20, +313 bps per round trip, avg half spread 2.4 bps, open 9547.33
- AVAX: 8 fills (3 buy / 5 sell), traded 13,938, gross pnl +760.09, +1091 bps per round trip, avg half spread 1.3 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 8 fills (5 buy / 3 sell), traded 11,507, gross pnl +29.68, +52 bps per round trip, avg half spread 2.1 bps
- DOT: 7 fills (4 buy / 3 sell), traded 6,542, gross pnl +201.75, +617 bps per round trip, avg half spread 3.5 bps, open 608.208
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 6 fills (3 buy / 3 sell), traded 9,478, gross pnl +184.42, +389 bps per round trip, avg half spread 2.3 bps, open 173.711
- LTC: 7 fills (3 buy / 4 sell), traded 11,216, gross pnl +534.74, +954 bps per round trip, avg half spread 2.2 bps, open 34.4177
- SOL: 5 fills (3 buy / 2 sell), traded 7,474, gross pnl +80.89, +216 bps per round trip, avg half spread 0.4 bps, open 17.9866
- XRP: 8 fills (4 buy / 4 sell), traded 12,657, gross pnl +171.04, +270 bps per round trip, avg half spread 0.7 bps, open 1261.6

last fills:

- 2026-09-24 23:20Z sell XRP 2,584 @ 1.53306 fee 2.58 slip 1.29 (half spread 0.7 bps)
- 2026-09-25 01:20Z buy XRP 2,646 @ 1.54644 fee 2.65 slip 1.32 (half spread 0.8 bps)
- 2026-09-25 11:22Z sell ADA 643 @ 0.255978 fee 0.64 slip 0.32 (half spread 2.2 bps)
- 2026-09-25 11:22Z sell LINK 711 @ 14.0686 fee 0.71 slip 0.36 (half spread 1.9 bps)
- 2026-09-25 11:22Z sell LTC 827 @ 71.0045 fee 0.83 slip 0.41 (half spread 1.4 bps)
- 2026-09-25 11:22Z buy SOL 2,176 @ 120.975 fee 2.18 slip 1.09 (half spread 0.4 bps)
- 2026-09-25 12:27Z sell XRP 722 @ 1.60683 fee 0.72 slip 0.36 (half spread 0.2 bps)
- 2026-09-25 12:27Z buy DOT 721 @ 1.18544 fee 0.72 slip 0.39 (half spread 3.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-25 17:21Z; halted today: False

last decisions (newest last):

- 2026-09-25 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.32 not below -2.0
- 2026-09-25 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-09-25 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.57 not below -2.0
- 2026-09-25 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.88 not below -2.0
- 2026-09-25 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.40 not below -2.0
- 2026-09-25 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.07 not below -2.0
- 2026-09-25 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.95 not below -2.0
- 2026-09-25 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.81 not below -2.0
- 2026-09-25 17:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.60 not below -2.0
- 2026-09-25 17:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.61 not below -2.0
- 2026-09-25 17:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.41 not below -2.0
- 2026-09-25 17:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.28 not below -2.0
- 2026-09-25 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.56 not below -2.0
- 2026-09-25 17:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.78 not below -2.0
- 2026-09-25 17:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-09-25 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.02 not below -2.0
- 2026-09-25 17:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.87 not below -2.0
- 2026-09-25 17:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.63 not below -2.0

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
- 24h +0.00%, 7d +2.78%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 18 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-25 17:21Z; halted today: False

last decisions (newest last):

- 2026-09-25 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 17:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- 24h +0.00%, 7d +7.91%, 30d +15.12%, max drawdown -6.43%
- fills 49 total, 35 in the last 7d
- costs 101.31 (fees 66.66 + slippage 34.64); gross pnl 1,613.66; cost coverage 15.93
- cash 11,512.35; positions: none
- last run 2026-09-25 17:21Z; halted today: False

last decisions (newest last):

- 2026-09-25 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 96.43 not a higher low vs prior low 98.64 (need +10.0%)
- 2026-09-25 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.191 not a higher low vs prior low 0.2001 (need +10.0%)
- 2026-09-25 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.197 not a higher low vs prior low 7.287 (need +10.0%)
- 2026-09-25 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.66 not a higher low vs prior low 11.17 (need +10.0%)
- 2026-09-25 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.265 not a higher low vs prior low 1.329 (need +10.0%)
- 2026-09-25 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.08122 (need +10.0%)
- 2026-09-25 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.939 not a higher low vs prior low 0.9082 (need +10.0%)
- 2026-09-25 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.28 not a higher low vs prior low 51.55 (need +10.0%)
- 2026-09-25 17:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.542e+04 not a higher low vs prior low 7.589e+04 (need +10.0%)
- 2026-09-25 17:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2388 not a higher low vs prior low 2406 (need +10.0%)
- 2026-09-25 17:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 96.43 not a higher low vs prior low 98.64 (need +10.0%)
- 2026-09-25 17:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.191 not a higher low vs prior low 0.2001 (need +10.0%)
- 2026-09-25 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.197 not a higher low vs prior low 7.287 (need +10.0%)
- 2026-09-25 17:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.66 not a higher low vs prior low 11.17 (need +10.0%)
- 2026-09-25 17:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.265 not a higher low vs prior low 1.329 (need +10.0%)
- 2026-09-25 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.08122 (need +10.0%)
- 2026-09-25 17:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.939 not a higher low vs prior low 0.9082 (need +10.0%)
- 2026-09-25 17:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.28 not a higher low vs prior low 51.55 (need +10.0%)

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

## challenger4: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,174.75 (started 10,000 at 2026-09-25 04:23Z), net +1.75% since start
- 24h +1.82%, 7d +1.82%, 30d +1.82%, max drawdown -1.44%
- fills 11 total, 11 in the last 7d
- costs 23.15 (fees 15.41 + slippage 7.74); gross pnl 197.90; cost coverage 8.55
- cash -0.00; positions: ADA 6709.39, DOT 836.243, LINK 146.265, LTC 24.3435, SOL 14.2249, XRP 1299.71
- last run 2026-09-25 17:21Z; halted today: False

last decisions (newest last):

- 2026-09-25 16:24Z SOL hold target 0.17 (held 0.17) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.33% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-25 16:24Z ADA hold target 0.17 (held 0.17) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.76% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.76% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 16:24Z LINK hold target 0.17 (held 0.20) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +6.00% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 16:24Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +0.26% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-09-25 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.55% not above entry band +1.0%
- 2026-09-25 16:24Z DOT none target 0.17 (held 0.10) — no fill possible (no cash or no position) | stay long: 72h return +0.40% vs exit band -1.0% and price above 24h EMA; realised vol 100% ->...
- 2026-09-25 16:24Z LTC hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +14.35% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-25 17:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 17:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 17:21Z SOL hold target 0.17 (held 0.17) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +2.89% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-25 17:21Z ADA hold target 0.17 (held 0.17) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.79% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.56% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 17:21Z LINK hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +5.73% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 17:21Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return -0.15% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-09-25 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.37% not above entry band +1.0%
- 2026-09-25 17:21Z DOT none target 0.17 (held 0.10) — no fill possible (no cash or no position) | stay long: 72h return +0.08% vs exit band -1.0% and price above 24h EMA; realised vol 100% ->...
- 2026-09-25 17:21Z LTC hold target 0.17 (held 0.17) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +11.74% vs exit band -1.0% and price within 2.0% of 24h EMA; real...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,337, gross pnl +70.84, +425 bps per round trip, avg half spread 0.9 bps, open 6709.39
- DOT: 1 fills (1 buy / 0 sell), traded 991, gross pnl -4.68, -94 bps per round trip, avg half spread 3.4 bps, open 836.243
- LINK: 2 fills (1 buy / 1 sell), traded 3,076, gross pnl +103.35, +672 bps per round trip, avg half spread 2.1 bps, open 146.265
- LTC: 2 fills (1 buy / 1 sell), traded 3,266, gross pnl -38.42, -235 bps per round trip, avg half spread 1.4 bps, open 24.3435
- SOL: 2 fills (2 buy / 0 sell), traded 1,716, gross pnl +6.16, +72 bps per round trip, avg half spread 0.4 bps, open 14.2249
- XRP: 2 fills (1 buy / 1 sell), traded 3,024, gross pnl +60.65, +401 bps per round trip, avg half spread 0.7 bps, open 1299.71

last fills:

- 2026-09-25 06:27Z buy ADA 2,490 @ 0.247923 fee 2.49 slip 1.24 (half spread 1.2 bps)
- 2026-09-25 11:22Z sell LINK 576 @ 14.0686 fee 0.58 slip 0.29 (half spread 1.9 bps)
- 2026-09-25 11:22Z sell XRP 523 @ 1.58324 fee 0.52 slip 0.26 (half spread 1.1 bps)
- 2026-09-25 11:22Z buy SOL 1,097 @ 120.975 fee 1.10 slip 0.55 (half spread 0.4 bps)
- 2026-09-25 12:27Z sell ADA 847 @ 0.254263 fee 0.85 slip 0.42 (half spread 0.7 bps)
- 2026-09-25 12:27Z sell LTC 766 @ 70.0799 fee 0.77 slip 0.38 (half spread 0.7 bps)
- 2026-09-25 12:27Z buy SOL 619 @ 120.055 fee 0.62 slip 0.31 (half spread 0.4 bps)
- 2026-09-25 12:27Z buy DOT 991 @ 1.18544 fee 0.99 slip 0.53 (half spread 3.4 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 950 candles, 2026-08-17 03:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 950 candles, 2026-08-17 03:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 950 candles, 2026-08-17 03:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 950 candles, 2026-08-17 03:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- AVAX: live 950 candles, 2026-08-17 03:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 950 candles, 2026-08-17 03:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 922 candles, 2026-08-18 07:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 922 candles, 2026-08-18 07:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.0 bps
- DOT: live 922 candles, 2026-08-18 07:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 922 candles, 2026-08-18 07:00Z to 2026-09-25 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
