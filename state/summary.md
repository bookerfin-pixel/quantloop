# quantloop summary — generated 2026-09-19 08:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 3.1 of 60, 56.9 days until the verdict
  so far: champion +7.90% (DD -2.31%, 15 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +6.80%, equal weight basket of 10 pairs +11.76%, basket realised vol 47% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,790.06 (started 10,000 at 2026-09-16 03:55Z), net +7.90% since start
- 24h +3.81%, 7d +7.90%, 30d +7.90%, max drawdown -2.31%
- fills 15 total, 15 in the last 7d
- costs 38.38 (fees 25.33 + slippage 13.05); gross pnl 828.44; cost coverage 21.59
- cash 1,454.33; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-19 08:22Z; halted today: False

last decisions (newest last):

- 2026-09-19 07:20Z SOL hold target 0.10 (held 0.15) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +14.87% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +13.89% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z AVAX hold target 0.10 (held 0.15) — hold: weight change -0.048 below threshold 0.05 | stay long: 72h return +15.84% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +14.40% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.57% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 07:20Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +8.61% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-19 07:20Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.035 below threshold 0.05 | stay long: 72h return +17.41% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 07:20Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +11.81% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z BTC none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.08% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-19 08:22Z ETH none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.65% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-19 08:22Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +15.14% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +14.32% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 08:22Z AVAX hold target 0.11 (held 0.15) — hold: weight change -0.038 below threshold 0.05 | stay long: 72h return +18.14% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +14.35% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z XRP none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.80% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 08:22Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +8.94% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-19 08:22Z DOT sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-19 08:22Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +11.49% vs exit band -1.0% and price within 2.0% of 24h EMA; real...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +53.16, +316 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +242.83, +556 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +51.65, +707 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +86.47, +1174 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +99.67, +552 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +89.86, +1217 bps per round trip, avg half spread 0.5 bps, open 13.9531

last fills:

- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-09-19 08:22Z sell DOT 1,456 @ 1.11408 fee 1.46 slip 0.94 (half spread 4.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-19 08:22Z; halted today: False

last decisions (newest last):

- 2026-09-19 07:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.75 not below -2.0
- 2026-09-19 07:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.90 not below -2.0
- 2026-09-19 07:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.17 not below -2.0
- 2026-09-19 07:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.11 not below -2.0
- 2026-09-19 07:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.37 not below -2.0
- 2026-09-19 07:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.21 not below -2.0
- 2026-09-19 07:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.01 not below -2.0
- 2026-09-19 07:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.37 not below -2.0
- 2026-09-19 08:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.64 not below -2.0
- 2026-09-19 08:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.40 not below -2.0
- 2026-09-19 08:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.64 not below -2.0
- 2026-09-19 08:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.74 not below -2.0
- 2026-09-19 08:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.32 not below -2.0
- 2026-09-19 08:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.02 not below -2.0
- 2026-09-19 08:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.14 not below -2.0
- 2026-09-19 08:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.10 not below -2.0
- 2026-09-19 08:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.82 not below -2.0
- 2026-09-19 08:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.09 not below -2.0

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

- equity 10,790.06 (started 10,000 at 2026-09-16 23:20Z), net +7.90% since start
- 24h +3.81%, 7d +7.90%, 30d +7.90%, max drawdown -2.31%
- fills 15 total, 15 in the last 7d
- costs 38.38 (fees 25.33 + slippage 13.05); gross pnl 828.44; cost coverage 21.59
- cash 1,454.33; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-19 08:22Z; halted today: False

last decisions (newest last):

- 2026-09-19 07:20Z SOL hold target 0.10 (held 0.15) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +14.87% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +13.89% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z AVAX hold target 0.10 (held 0.15) — hold: weight change -0.048 below threshold 0.05 | stay long: 72h return +15.84% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +14.40% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.57% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 07:20Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +8.61% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-19 07:20Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.035 below threshold 0.05 | stay long: 72h return +17.41% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 07:20Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +11.81% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z BTC none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.08% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-19 08:22Z ETH none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.65% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-19 08:22Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +15.14% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +14.32% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 08:22Z AVAX hold target 0.11 (held 0.15) — hold: weight change -0.038 below threshold 0.05 | stay long: 72h return +18.14% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +14.35% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z XRP none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.80% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 08:22Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +8.94% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-19 08:22Z DOT sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-19 08:22Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +11.49% vs exit band -1.0% and price within 2.0% of 24h EMA; real...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +53.16, +316 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +242.83, +556 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +51.65, +707 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +86.47, +1174 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +99.67, +552 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +89.86, +1217 bps per round trip, avg half spread 0.5 bps, open 13.9531

last fills:

- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-09-19 08:22Z sell DOT 1,456 @ 1.11408 fee 1.46 slip 0.94 (half spread 4.5 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,790.06 (started 10,000 at 2026-09-16 23:20Z), net +7.90% since start
- 24h +3.81%, 7d +7.90%, 30d +7.90%, max drawdown -2.31%
- fills 15 total, 15 in the last 7d
- costs 38.38 (fees 25.33 + slippage 13.05); gross pnl 828.44; cost coverage 21.59
- cash 1,454.33; positions: ADA 6882.97, AVAX 186.526, DOGE 17308.9, LINK 125.494, LTC 27.0231, SOL 13.9531
- last run 2026-09-19 08:22Z; halted today: False

last decisions (newest last):

- 2026-09-19 07:20Z SOL hold target 0.10 (held 0.15) — hold: weight change -0.045 below threshold 0.05 | stay long: 72h return +14.87% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +13.89% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z AVAX hold target 0.10 (held 0.15) — hold: weight change -0.048 below threshold 0.05 | stay long: 72h return +15.84% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +14.40% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 07:20Z XRP none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.57% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 07:20Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +8.61% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-19 07:20Z DOT hold target 0.10 (held 0.14) — hold: weight change -0.035 below threshold 0.05 | stay long: 72h return +17.41% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 07:20Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.044 below threshold 0.05 | stay long: 72h return +11.81% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z BTC none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +7.08% vs entry band +1.0% and price above 24h EMA; realised vol 34% -...
- 2026-09-19 08:22Z ETH none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.65% vs entry band +1.0% and price above 24h EMA; realised vol 43% -...
- 2026-09-19 08:22Z SOL hold target 0.11 (held 0.15) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +15.14% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +14.32% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 08:22Z AVAX hold target 0.11 (held 0.15) — hold: weight change -0.038 below threshold 0.05 | stay long: 72h return +18.14% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +14.35% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 08:22Z XRP none target 0.11 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +9.80% vs entry band +1.0% and price above 24h EMA; realised vol 79% -...
- 2026-09-19 08:22Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +8.94% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-19 08:22Z DOT sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-19 08:22Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +11.49% vs exit band -1.0% and price within 2.0% of 24h EMA; real...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +53.16, +316 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +242.83, +556 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +51.65, +707 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +86.47, +1174 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +99.67, +552 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +89.86, +1217 bps per round trip, avg half spread 0.5 bps, open 13.9531

last fills:

- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-09-19 08:22Z sell DOT 1,456 @ 1.11408 fee 1.46 slip 0.94 (half spread 4.5 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 797 candles, 2026-08-17 03:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 797 candles, 2026-08-17 03:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 797 candles, 2026-08-17 03:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- ADA: live 797 candles, 2026-08-17 03:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.4 bps
- AVAX: live 797 candles, 2026-08-17 03:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 797 candles, 2026-08-17 03:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 769 candles, 2026-08-18 07:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 769 candles, 2026-08-18 07:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 769 candles, 2026-08-18 07:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 769 candles, 2026-08-18 07:00Z to 2026-09-19 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
