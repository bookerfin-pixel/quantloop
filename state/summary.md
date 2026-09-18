# quantloop summary — generated 2026-09-18 17:19Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 2.5 of 60, 57.5 days until the verdict
  so far: champion +6.10% (DD -1.16%, 14 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +6.48%, equal weight basket of 10 pairs +10.81%, basket realised vol 47% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,610.05 (started 10,000 at 2026-09-16 03:55Z), net +6.10% since start
- 24h +4.82%, 7d +6.10%, 30d +6.10%, max drawdown -1.16%
- fills 14 total, 14 in the last 7d
- costs 35.98 (fees 23.87 + slippage 12.10); gross pnl 646.03; cost coverage 17.96
- cash -0.00; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, DOT 1306.72, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-18 17:19Z; halted today: False

last decisions (newest last):

- 2026-09-18 16:20Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.035 below threshold 0.05 | stay long: 72h return +11.92% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 16:20Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.86% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 16:20Z AVAX hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +9.14% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +7.71% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-09-18 16:20Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.05% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z DOT hold target 0.11 (held 0.14) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +15.21% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 16:20Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.81% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-09-18 17:19Z BTC none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +5.88% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-18 17:19Z ETH none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.24% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-18 17:19Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.036 below threshold 0.05 | stay long: 72h return +12.74% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 17:19Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.18% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 17:19Z AVAX hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.75% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.93% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0%
- 2026-09-18 17:19Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.50% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z DOT hold target 0.11 (held 0.14) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +15.75% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 17:19Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +8.50% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +21.09, +125 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +134.93, +309 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +54.71, +749 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +225.83, +1202 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +50.35, +684 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +71.57, +396 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +87.56, +1186 bps per round trip, avg half spread 0.5 bps, open 13.9531

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
- 24h +0.52%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-18 17:19Z; halted today: False

last decisions (newest last):

- 2026-09-18 16:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +4.27 not below -2.0
- 2026-09-18 16:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.66 not below -2.0
- 2026-09-18 16:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.39 not below -2.0
- 2026-09-18 16:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.45 not below -2.0
- 2026-09-18 16:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.52 not below -2.0
- 2026-09-18 16:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.17 not below -2.0
- 2026-09-18 16:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.06 not below -2.0
- 2026-09-18 16:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.21 not below -2.0
- 2026-09-18 17:19Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.34 not below -2.0
- 2026-09-18 17:19Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.52 not below -2.0
- 2026-09-18 17:19Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +4.31 not below -2.0
- 2026-09-18 17:19Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.50 not below -2.0
- 2026-09-18 17:19Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.26 not below -2.0
- 2026-09-18 17:19Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.51 not below -2.0
- 2026-09-18 17:19Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.44 not below -2.0
- 2026-09-18 17:19Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.30 not below -2.0
- 2026-09-18 17:19Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.12 not below -2.0
- 2026-09-18 17:19Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.43 not below -2.0

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

- equity 10,610.05 (started 10,000 at 2026-09-16 23:20Z), net +6.10% since start
- 24h +4.82%, 7d +6.10%, 30d +6.10%, max drawdown -1.16%
- fills 14 total, 14 in the last 7d
- costs 35.98 (fees 23.87 + slippage 12.10); gross pnl 646.03; cost coverage 17.96
- cash -0.00; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, DOT 1306.72, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-18 17:19Z; halted today: False

last decisions (newest last):

- 2026-09-18 16:20Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.035 below threshold 0.05 | stay long: 72h return +11.92% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 16:20Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.86% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 16:20Z AVAX hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +9.14% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +7.71% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-09-18 16:20Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.05% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z DOT hold target 0.11 (held 0.14) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +15.21% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 16:20Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.81% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-09-18 17:19Z BTC none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +5.88% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-18 17:19Z ETH none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.24% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-18 17:19Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.036 below threshold 0.05 | stay long: 72h return +12.74% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 17:19Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.18% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 17:19Z AVAX hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.75% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.93% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0%
- 2026-09-18 17:19Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.50% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z DOT hold target 0.11 (held 0.14) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +15.75% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 17:19Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +8.50% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +21.09, +125 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +134.93, +309 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +54.71, +749 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +225.83, +1202 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +50.35, +684 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +71.57, +396 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +87.56, +1186 bps per round trip, avg half spread 0.5 bps, open 13.9531

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

- equity 10,610.05 (started 10,000 at 2026-09-16 23:20Z), net +6.10% since start
- 24h +4.82%, 7d +6.10%, 30d +6.10%, max drawdown -1.16%
- fills 14 total, 14 in the last 7d
- costs 35.98 (fees 23.87 + slippage 12.10); gross pnl 646.03; cost coverage 17.96
- cash -0.00; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, DOT 1306.72, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-18 17:19Z; halted today: False

last decisions (newest last):

- 2026-09-18 16:20Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.035 below threshold 0.05 | stay long: 72h return +11.92% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 16:20Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.86% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 16:20Z AVAX hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +9.14% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +7.71% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-09-18 16:20Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.05% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 16:20Z DOT hold target 0.11 (held 0.14) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +15.21% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 16:20Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.81% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-09-18 17:19Z BTC none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +5.88% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-18 17:19Z ETH none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.24% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-18 17:19Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.036 below threshold 0.05 | stay long: 72h return +12.74% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 17:19Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.18% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 17:19Z AVAX hold target 0.11 (held 0.14) — hold: weight change -0.031 below threshold 0.05 | stay long: 72h return +8.75% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.93% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0%
- 2026-09-18 17:19Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +7.50% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 17:19Z DOT hold target 0.11 (held 0.14) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +15.75% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 17:19Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +8.50% vs exit band -1.0% and price above 24h EMA; realised vol 4...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +21.09, +125 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +134.93, +309 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +54.71, +749 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +225.83, +1202 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +50.35, +684 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +71.57, +396 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +87.56, +1186 bps per round trip, avg half spread 0.5 bps, open 13.9531

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

- BTC: live 782 candles, 2026-08-17 03:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 782 candles, 2026-08-17 03:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 782 candles, 2026-08-17 03:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- ADA: live 782 candles, 2026-08-17 03:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.4 bps
- AVAX: live 782 candles, 2026-08-17 03:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 782 candles, 2026-08-17 03:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 754 candles, 2026-08-18 07:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 754 candles, 2026-08-18 07:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 754 candles, 2026-08-18 07:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- LTC: live 754 candles, 2026-08-18 07:00Z to 2026-09-18 16:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.7 bps
