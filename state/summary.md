# quantloop summary — generated 2026-09-19 02:21Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 2.9 of 60, 57.1 days until the verdict
  so far: champion +9.51% (DD -1.16%, 14 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +7.06%, equal weight basket of 10 pairs +13.34%, basket realised vol 46% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,950.66 (started 10,000 at 2026-09-16 03:55Z), net +9.51% since start
- 24h +7.26%, 7d +9.51%, 30d +9.51%, max drawdown -1.16%
- fills 14 total, 14 in the last 7d
- costs 35.98 (fees 23.87 + slippage 12.10); gross pnl 986.63; cost coverage 27.42
- cash -0.00; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, DOT 1306.72, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-19 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-19 01:21Z SOL hold target 0.10 (held 0.15) — hold: weight change -0.047 below threshold 0.05 | stay long: 72h return +17.12% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +16.95% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z AVAX hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +15.05% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +13.43% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.46% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 01:21Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +9.80% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-19 01:21Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.037 below threshold 0.05 | stay long: 72h return +20.76% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +14.36% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z BTC none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.73% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-19 02:21Z ETH none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.33% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-19 02:21Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +17.60% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +19.08% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z AVAX hold target 0.10 (held 0.15) — hold: weight change -0.046 below threshold 0.05 | stay long: 72h return +20.79% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +14.41% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +10.75% vs entry band +1.0% and price above 24h EMA; realised vol 79% ...
- 2026-09-19 02:21Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +10.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.037 below threshold 0.05 | stay long: 72h return +20.46% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z LTC hold target 0.10 (held 0.15) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +15.54% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +98.73, +588 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +230.52, +528 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +71.17, +974 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +246.28, +1311 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +87.08, +1182 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +142.91, +791 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +109.95, +1489 bps per round trip, avg half spread 0.5 bps, open 13.9531

last fills:

- 2026-09-18 04:22Z sell ADA 936 @ 0.213847 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.16%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-19 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-19 01:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.75 not below -2.0
- 2026-09-19 01:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.60 not below -2.0
- 2026-09-19 01:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.09 not below -2.0
- 2026-09-19 01:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.13 not below -2.0
- 2026-09-19 01:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.07 not below -2.0
- 2026-09-19 01:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.44 not below -2.0
- 2026-09-19 01:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-09-19 01:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.61 not below -2.0
- 2026-09-19 02:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.06 not below -2.0
- 2026-09-19 02:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.38 not below -2.0
- 2026-09-19 02:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.57 not below -2.0
- 2026-09-19 02:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.81 not below -2.0
- 2026-09-19 02:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +4.35 not below -2.0
- 2026-09-19 02:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.07 not below -2.0
- 2026-09-19 02:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.16 not below -2.0
- 2026-09-19 02:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.47 not below -2.0
- 2026-09-19 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.21 not below -2.0
- 2026-09-19 02:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.54 not below -2.0

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

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,950.66 (started 10,000 at 2026-09-16 23:20Z), net +9.51% since start
- 24h +7.26%, 7d +9.51%, 30d +9.51%, max drawdown -1.16%
- fills 14 total, 14 in the last 7d
- costs 35.98 (fees 23.87 + slippage 12.10); gross pnl 986.63; cost coverage 27.42
- cash -0.00; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, DOT 1306.72, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-19 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-19 01:21Z SOL hold target 0.10 (held 0.15) — hold: weight change -0.047 below threshold 0.05 | stay long: 72h return +17.12% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +16.95% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z AVAX hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +15.05% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +13.43% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.46% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 01:21Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +9.80% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-19 01:21Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.037 below threshold 0.05 | stay long: 72h return +20.76% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +14.36% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z BTC none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.73% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-19 02:21Z ETH none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.33% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-19 02:21Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +17.60% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +19.08% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z AVAX hold target 0.10 (held 0.15) — hold: weight change -0.046 below threshold 0.05 | stay long: 72h return +20.79% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +14.41% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +10.75% vs entry band +1.0% and price above 24h EMA; realised vol 79% ...
- 2026-09-19 02:21Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +10.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.037 below threshold 0.05 | stay long: 72h return +20.46% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z LTC hold target 0.10 (held 0.15) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +15.54% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +98.73, +588 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +230.52, +528 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +71.17, +974 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +246.28, +1311 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +87.08, +1182 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +142.91, +791 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +109.95, +1489 bps per round trip, avg half spread 0.5 bps, open 13.9531

last fills:

- 2026-09-18 04:22Z sell ADA 936 @ 0.213847 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,950.66 (started 10,000 at 2026-09-16 23:20Z), net +9.51% since start
- 24h +7.26%, 7d +9.51%, 30d +9.51%, max drawdown -1.16%
- fills 14 total, 14 in the last 7d
- costs 35.98 (fees 23.87 + slippage 12.10); gross pnl 986.63; cost coverage 27.42
- cash -0.00; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, DOT 1306.72, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-19 02:21Z; halted today: False

last decisions (newest last):

- 2026-09-19 01:21Z SOL hold target 0.10 (held 0.15) — hold: weight change -0.047 below threshold 0.05 | stay long: 72h return +17.12% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +16.95% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z AVAX hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +15.05% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +13.43% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.46% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 01:21Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +9.80% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-19 01:21Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.037 below threshold 0.05 | stay long: 72h return +20.76% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 01:21Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +14.36% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z BTC none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.73% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-19 02:21Z ETH none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.33% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-19 02:21Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +17.60% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +19.08% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z AVAX hold target 0.10 (held 0.15) — hold: weight change -0.046 below threshold 0.05 | stay long: 72h return +20.79% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +14.41% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +10.75% vs entry band +1.0% and price above 24h EMA; realised vol 79% ...
- 2026-09-19 02:21Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +10.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.037 below threshold 0.05 | stay long: 72h return +20.46% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 02:21Z LTC hold target 0.10 (held 0.15) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +15.54% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +98.73, +588 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +230.52, +528 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +71.17, +974 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +246.28, +1311 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +87.08, +1182 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +142.91, +791 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +109.95, +1489 bps per round trip, avg half spread 0.5 bps, open 13.9531

last fills:

- 2026-09-18 04:22Z sell ADA 936 @ 0.213847 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 791 candles, 2026-08-17 03:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 791 candles, 2026-08-17 03:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 791 candles, 2026-08-17 03:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- ADA: live 791 candles, 2026-08-17 03:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.4 bps
- AVAX: live 791 candles, 2026-08-17 03:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 791 candles, 2026-08-17 03:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 763 candles, 2026-08-18 07:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 763 candles, 2026-08-18 07:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 763 candles, 2026-08-18 07:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- LTC: live 763 candles, 2026-08-18 07:00Z to 2026-09-19 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
