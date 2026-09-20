# quantloop summary — generated 2026-09-20 03:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 3.9 of 60, 56.1 days until the verdict
  so far: champion +7.67% (DD -3.07%, 26 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +5.79%, equal weight basket of 10 pairs +11.18%, basket realised vol 52% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,766.52 (started 10,000 at 2026-09-16 03:55Z), net +7.67% since start
- 24h -1.27%, 7d +7.67%, 30d +7.67%, max drawdown -3.07%
- fills 26 total, 26 in the last 7d
- costs 56.62 (fees 37.31 + slippage 19.31); gross pnl 823.14; cost coverage 14.54
- cash 3,945.76; positions: AVAX 279.519, BTC 0.0148035, ETH 0.0928176, LTC 46.9242
- last run 2026-09-20 03:22Z; halted today: False

last decisions (newest last):

- 2026-09-20 02:21Z SOL hold target 0.11 (held 0.14) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +11.05% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-20 02:21Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +15.75% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 02:21Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +29.21% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 02:21Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.030 below threshold 0.05 | stay long: 72h return +10.81% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-20 02:21Z XRP none target 0.11 (held 0.05) — no fill possible (no cash or no position) | stay long: 72h return +7.73% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 02:21Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.027 below threshold 0.05 | stay long: 72h return +7.67% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 02:21Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +11.19% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 03:22Z BTC none target 0.25 (held 0.11) — no fill possible (no cash or no position) | stay long: 72h return +5.24% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 03:22Z ETH none target 0.25 (held 0.02) — no fill possible (no cash or no position) | stay long: 72h return +6.04% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 03:22Z SOL sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z ADA sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z AVAX buy target 0.25 (held 0.11) — stay long: 72h return +26.52% vs exit band -1.0% and price above 24h EMA; realised vol 95% -> weight 0.25
- 2026-09-20 03:22Z LINK sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z XRP sell target 0.00 (held 0.05) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z DOGE sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 03:22Z LTC buy target 0.25 (held 0.14) — stay long: 72h return +8.98% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 55% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +391.14, +719 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 1 fills (1 buy / 0 sell), traded 1,207, gross pnl -14.58, -242 bps per round trip, avg half spread 0.0 bps, open 0.0148035
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 1 fills (1 buy / 0 sell), traded 246, gross pnl -5.86, -476 bps per round trip, avg half spread 0.0 bps, open 0.0928176
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +105.35, +443 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-19 12:26Z buy XRP 604 @ 1.43078 fee 0.60 slip 0.30 (half spread 0.0 bps)
- 2026-09-20 03:22Z sell SOL 1,517 @ 108.721 fee 1.52 slip 0.76 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-20 03:22Z; halted today: False

last decisions (newest last):

- 2026-09-20 02:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.72 not below -2.0
- 2026-09-20 02:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.97 not below -2.0
- 2026-09-20 02:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.34 not below -2.0
- 2026-09-20 02:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.68 not below -2.0
- 2026-09-20 02:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.88 not below -2.0
- 2026-09-20 02:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-09-20 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.08 not below -2.0
- 2026-09-20 02:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.07 not below -2.0
- 2026-09-20 03:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.55 not below -2.0
- 2026-09-20 03:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.06 not below -2.0
- 2026-09-20 03:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.16 not below -2.0
- 2026-09-20 03:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.17 not below -2.0
- 2026-09-20 03:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.94 not below -2.0
- 2026-09-20 03:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.96 not below -2.0
- 2026-09-20 03:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.24 not below -2.0
- 2026-09-20 03:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.59 not below -2.0
- 2026-09-20 03:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0
- 2026-09-20 03:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.47 not below -2.0

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

- equity 10,766.52 (started 10,000 at 2026-09-16 23:20Z), net +7.67% since start
- 24h -1.27%, 7d +7.67%, 30d +7.67%, max drawdown -3.07%
- fills 26 total, 26 in the last 7d
- costs 56.62 (fees 37.31 + slippage 19.31); gross pnl 823.14; cost coverage 14.54
- cash 3,945.76; positions: AVAX 279.519, BTC 0.0148035, ETH 0.0928176, LTC 46.9242
- last run 2026-09-20 03:22Z; halted today: False

last decisions (newest last):

- 2026-09-20 02:21Z SOL hold target 0.11 (held 0.14) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +11.05% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-20 02:21Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +15.75% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 02:21Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +29.21% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 02:21Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.030 below threshold 0.05 | stay long: 72h return +10.81% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-20 02:21Z XRP none target 0.11 (held 0.05) — no fill possible (no cash or no position) | stay long: 72h return +7.73% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 02:21Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.027 below threshold 0.05 | stay long: 72h return +7.67% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 02:21Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +11.19% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 03:22Z BTC none target 0.25 (held 0.11) — no fill possible (no cash or no position) | stay long: 72h return +5.24% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 03:22Z ETH none target 0.25 (held 0.02) — no fill possible (no cash or no position) | stay long: 72h return +6.04% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 03:22Z SOL sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z ADA sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z AVAX buy target 0.25 (held 0.11) — stay long: 72h return +26.52% vs exit band -1.0% and price above 24h EMA; realised vol 95% -> weight 0.25
- 2026-09-20 03:22Z LINK sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z XRP sell target 0.00 (held 0.05) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z DOGE sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 03:22Z LTC buy target 0.25 (held 0.14) — stay long: 72h return +8.98% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 55% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +391.14, +719 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 1 fills (1 buy / 0 sell), traded 1,207, gross pnl -14.58, -242 bps per round trip, avg half spread 0.0 bps, open 0.0148035
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 1 fills (1 buy / 0 sell), traded 246, gross pnl -5.86, -476 bps per round trip, avg half spread 0.0 bps, open 0.0928176
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +105.35, +443 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-19 12:26Z buy XRP 604 @ 1.43078 fee 0.60 slip 0.30 (half spread 0.0 bps)
- 2026-09-20 03:22Z sell SOL 1,517 @ 108.721 fee 1.52 slip 0.76 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,766.52 (started 10,000 at 2026-09-16 23:20Z), net +7.67% since start
- 24h -1.27%, 7d +7.67%, 30d +7.67%, max drawdown -3.07%
- fills 26 total, 26 in the last 7d
- costs 56.62 (fees 37.31 + slippage 19.31); gross pnl 823.14; cost coverage 14.54
- cash 3,945.76; positions: AVAX 279.519, BTC 0.0148035, ETH 0.0928176, LTC 46.9242
- last run 2026-09-20 03:22Z; halted today: False

last decisions (newest last):

- 2026-09-20 02:21Z SOL hold target 0.11 (held 0.14) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +11.05% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-20 02:21Z ADA hold target 0.11 (held 0.14) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +15.75% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 02:21Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +29.21% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 02:21Z LINK hold target 0.11 (held 0.14) — hold: weight change -0.030 below threshold 0.05 | stay long: 72h return +10.81% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-20 02:21Z XRP none target 0.11 (held 0.05) — no fill possible (no cash or no position) | stay long: 72h return +7.73% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 02:21Z DOGE hold target 0.11 (held 0.14) — hold: weight change -0.027 below threshold 0.05 | stay long: 72h return +7.67% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 02:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 02:21Z LTC hold target 0.11 (held 0.14) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +11.19% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 03:22Z BTC none target 0.25 (held 0.11) — no fill possible (no cash or no position) | stay long: 72h return +5.24% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 03:22Z ETH none target 0.25 (held 0.02) — no fill possible (no cash or no position) | stay long: 72h return +6.04% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-20 03:22Z SOL sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z ADA sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z AVAX buy target 0.25 (held 0.11) — stay long: 72h return +26.52% vs exit band -1.0% and price above 24h EMA; realised vol 95% -> weight 0.25
- 2026-09-20 03:22Z LINK sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z XRP sell target 0.00 (held 0.05) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z DOGE sell target 0.00 (held 0.14) — exit: price more than 2.0% below 24h EMA
- 2026-09-20 03:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 03:22Z LTC buy target 0.25 (held 0.14) — stay long: 72h return +8.98% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 55% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +391.14, +719 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 1 fills (1 buy / 0 sell), traded 1,207, gross pnl -14.58, -242 bps per round trip, avg half spread 0.0 bps, open 0.0148035
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 1 fills (1 buy / 0 sell), traded 246, gross pnl -5.86, -476 bps per round trip, avg half spread 0.0 bps, open 0.0928176
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +105.35, +443 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-19 12:26Z buy XRP 604 @ 1.43078 fee 0.60 slip 0.30 (half spread 0.0 bps)
- 2026-09-20 03:22Z sell SOL 1,517 @ 108.721 fee 1.52 slip 0.76 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 816 candles, 2026-08-17 03:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 816 candles, 2026-08-17 03:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 816 candles, 2026-08-17 03:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 816 candles, 2026-08-17 03:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- AVAX: live 816 candles, 2026-08-17 03:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.5 bps
- LINK: live 816 candles, 2026-08-17 03:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 788 candles, 2026-08-18 07:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 788 candles, 2026-08-18 07:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- DOT: live 788 candles, 2026-08-18 07:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 788 candles, 2026-08-18 07:00Z to 2026-09-20 02:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
