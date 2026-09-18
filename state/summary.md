# quantloop summary — generated 2026-09-18 04:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 2.0 of 60, 58.0 days until the verdict
  so far: champion +3.02% (DD -0.60%, 12 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +1.84%, equal weight basket of 10 pairs +7.15%, basket realised vol 43% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,301.91 (started 10,000 at 2026-09-16 03:55Z), net +3.02% since start
- 24h +3.03%, 7d +3.02%, 30d +3.02%, max drawdown -0.60%
- fills 12 total, 12 in the last 7d
- costs 32.48 (fees 21.54 + slippage 10.94); gross pnl 334.39; cost coverage 10.29
- cash 2,332.44; positions: ADA 6882.97, AVAX 186.526, DOGE 7200.88, DOT 1306.72, LINK 125.494, LTC 27.0231
- last run 2026-09-18 04:22Z; halted today: False

last decisions (newest last):

- 2026-09-18 03:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.67% not above entry band +1.0%
- 2026-09-18 03:21Z ADA buy target 0.25 (held 0.00) — enter long: 72h return +2.93% vs entry band +1.0% and price above 24h EMA; realised vol 74% -> weight 0.25
- 2026-09-18 03:21Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.93% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 03:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.25% not above entry band +1.0%
- 2026-09-18 03:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0%
- 2026-09-18 03:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.26% not above entry band +1.0%
- 2026-09-18 03:21Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +12.63% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 03:21Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +2.57% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 04:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.46% not above entry band +1.0%
- 2026-09-18 04:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.85% not above entry band +1.0%
- 2026-09-18 04:22Z SOL none target 0.14 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +2.96% vs entry band +1.0% and price above 24h EMA; realised vol 55% -...
- 2026-09-18 04:22Z ADA sell target 0.14 (held 0.23) — stay long: 72h return +5.38% vs exit band -1.0% and price above 24h EMA; realised vol 75% -> weight 0.25
- 2026-09-18 04:22Z AVAX sell target 0.14 (held 0.25) — stay long: 72h return +5.35% vs exit band -1.0% and price above 24h EMA; realised vol 65% -> weight 0.25
- 2026-09-18 04:22Z LINK buy target 0.14 (held 0.00) — enter long: 72h return +2.22% vs entry band +1.0% and price above 24h EMA; realised vol 63% -> weight 0.25
- 2026-09-18 04:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.35% not above entry band +1.0%
- 2026-09-18 04:22Z DOGE buy target 0.14 (held 0.00) — enter long: 72h return +1.38% vs entry band +1.0% and price above 24h EMA; realised vol 55% -> weight 0.25
- 2026-09-18 04:22Z DOT sell target 0.14 (held 0.26) — stay long: 72h return +12.99% vs exit band -1.0% and price above 24h EMA; realised vol 85% -> weight 0.25
- 2026-09-18 04:22Z LTC sell target 0.14 (held 0.25) — stay long: 72h return +3.27% vs exit band -1.0% and price above 24h EMA; realised vol 52% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl -13.72, -82 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +101.54, +233 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 1 fills (1 buy / 0 sell), traded 607, gross pnl +0.00, +0 bps per round trip, avg half spread 1.4 bps, open 7200.88
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +220.54, +1174 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +0.00, +0 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +26.03, +144 bps per round trip, avg half spread 3.2 bps, open 27.0231

last fills:

- 2026-09-18 02:23Z buy AVAX 2,553 @ 7.68984 fee 2.55 slip 1.28 (half spread 1.3 bps)
- 2026-09-18 03:21Z buy ADA 2,424 @ 0.21528 fee 2.42 slip 1.21 (half spread 2.4 bps)
- 2026-09-18 04:22Z sell ADA 936 @ 0.213847 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +2.24%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-18 04:22Z; halted today: False

last decisions (newest last):

- 2026-09-18 03:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.86 not below -2.0
- 2026-09-18 03:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.82 not below -2.0
- 2026-09-18 03:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.65 not below -2.0
- 2026-09-18 03:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.06 not below -2.0
- 2026-09-18 03:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.20 not below -2.0
- 2026-09-18 03:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.51 not below -2.0
- 2026-09-18 03:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.96 not below -2.0
- 2026-09-18 03:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.97 not below -2.0
- 2026-09-18 04:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.04 not below -2.0
- 2026-09-18 04:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.02 not below -2.0
- 2026-09-18 04:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.79 not below -2.0
- 2026-09-18 04:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.14 not below -2.0
- 2026-09-18 04:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.58 not below -2.0
- 2026-09-18 04:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.41 not below -2.0
- 2026-09-18 04:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.77 not below -2.0
- 2026-09-18 04:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.05 not below -2.0
- 2026-09-18 04:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.95 not below -2.0
- 2026-09-18 04:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.23 not below -2.0

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

- equity 10,301.91 (started 10,000 at 2026-09-16 23:20Z), net +3.02% since start
- 24h +3.03%, 7d +3.02%, 30d +3.02%, max drawdown -0.60%
- fills 12 total, 12 in the last 7d
- costs 32.48 (fees 21.54 + slippage 10.94); gross pnl 334.39; cost coverage 10.29
- cash 2,332.44; positions: ADA 6882.97, AVAX 186.526, DOGE 7200.88, DOT 1306.72, LINK 125.494, LTC 27.0231
- last run 2026-09-18 04:22Z; halted today: False

last decisions (newest last):

- 2026-09-18 03:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.67% not above entry band +1.0%
- 2026-09-18 03:21Z ADA buy target 0.25 (held 0.00) — enter long: 72h return +2.93% vs entry band +1.0% and price above 24h EMA; realised vol 74% -> weight 0.25
- 2026-09-18 03:21Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.93% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 03:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.25% not above entry band +1.0%
- 2026-09-18 03:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0%
- 2026-09-18 03:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.26% not above entry band +1.0%
- 2026-09-18 03:21Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +12.63% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 03:21Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +2.57% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 04:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.46% not above entry band +1.0%
- 2026-09-18 04:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.85% not above entry band +1.0%
- 2026-09-18 04:22Z SOL none target 0.14 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +2.96% vs entry band +1.0% and price above 24h EMA; realised vol 55% -...
- 2026-09-18 04:22Z ADA sell target 0.14 (held 0.23) — stay long: 72h return +5.38% vs exit band -1.0% and price above 24h EMA; realised vol 75% -> weight 0.25
- 2026-09-18 04:22Z AVAX sell target 0.14 (held 0.25) — stay long: 72h return +5.35% vs exit band -1.0% and price above 24h EMA; realised vol 65% -> weight 0.25
- 2026-09-18 04:22Z LINK buy target 0.14 (held 0.00) — enter long: 72h return +2.22% vs entry band +1.0% and price above 24h EMA; realised vol 63% -> weight 0.25
- 2026-09-18 04:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.35% not above entry band +1.0%
- 2026-09-18 04:22Z DOGE buy target 0.14 (held 0.00) — enter long: 72h return +1.38% vs entry band +1.0% and price above 24h EMA; realised vol 55% -> weight 0.25
- 2026-09-18 04:22Z DOT sell target 0.14 (held 0.26) — stay long: 72h return +12.99% vs exit band -1.0% and price above 24h EMA; realised vol 85% -> weight 0.25
- 2026-09-18 04:22Z LTC sell target 0.14 (held 0.25) — stay long: 72h return +3.27% vs exit band -1.0% and price above 24h EMA; realised vol 52% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl -13.72, -82 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +101.54, +233 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 1 fills (1 buy / 0 sell), traded 607, gross pnl +0.00, +0 bps per round trip, avg half spread 1.4 bps, open 7200.88
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +220.54, +1174 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +0.00, +0 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +26.03, +144 bps per round trip, avg half spread 3.2 bps, open 27.0231

last fills:

- 2026-09-18 02:23Z buy AVAX 2,553 @ 7.68984 fee 2.55 slip 1.28 (half spread 1.3 bps)
- 2026-09-18 03:21Z buy ADA 2,424 @ 0.21528 fee 2.42 slip 1.21 (half spread 2.4 bps)
- 2026-09-18 04:22Z sell ADA 936 @ 0.213847 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,301.91 (started 10,000 at 2026-09-16 23:20Z), net +3.02% since start
- 24h +3.03%, 7d +3.02%, 30d +3.02%, max drawdown -0.60%
- fills 12 total, 12 in the last 7d
- costs 32.48 (fees 21.54 + slippage 10.94); gross pnl 334.39; cost coverage 10.29
- cash 2,332.44; positions: ADA 6882.97, AVAX 186.526, DOGE 7200.88, DOT 1306.72, LINK 125.494, LTC 27.0231
- last run 2026-09-18 04:22Z; halted today: False

last decisions (newest last):

- 2026-09-18 03:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.67% not above entry band +1.0%
- 2026-09-18 03:21Z ADA buy target 0.25 (held 0.00) — enter long: 72h return +2.93% vs entry band +1.0% and price above 24h EMA; realised vol 74% -> weight 0.25
- 2026-09-18 03:21Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.93% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-18 03:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.25% not above entry band +1.0%
- 2026-09-18 03:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0%
- 2026-09-18 03:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.26% not above entry band +1.0%
- 2026-09-18 03:21Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +12.63% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 03:21Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +2.57% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 04:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.46% not above entry band +1.0%
- 2026-09-18 04:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.85% not above entry band +1.0%
- 2026-09-18 04:22Z SOL none target 0.14 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +2.96% vs entry band +1.0% and price above 24h EMA; realised vol 55% -...
- 2026-09-18 04:22Z ADA sell target 0.14 (held 0.23) — stay long: 72h return +5.38% vs exit band -1.0% and price above 24h EMA; realised vol 75% -> weight 0.25
- 2026-09-18 04:22Z AVAX sell target 0.14 (held 0.25) — stay long: 72h return +5.35% vs exit band -1.0% and price above 24h EMA; realised vol 65% -> weight 0.25
- 2026-09-18 04:22Z LINK buy target 0.14 (held 0.00) — enter long: 72h return +2.22% vs entry band +1.0% and price above 24h EMA; realised vol 63% -> weight 0.25
- 2026-09-18 04:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.35% not above entry band +1.0%
- 2026-09-18 04:22Z DOGE buy target 0.14 (held 0.00) — enter long: 72h return +1.38% vs entry band +1.0% and price above 24h EMA; realised vol 55% -> weight 0.25
- 2026-09-18 04:22Z DOT sell target 0.14 (held 0.26) — stay long: 72h return +12.99% vs exit band -1.0% and price above 24h EMA; realised vol 85% -> weight 0.25
- 2026-09-18 04:22Z LTC sell target 0.14 (held 0.25) — stay long: 72h return +3.27% vs exit band -1.0% and price above 24h EMA; realised vol 52% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl -13.72, -82 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 4 fills (2 buy / 2 sell), traded 8,731, gross pnl +101.54, +233 bps per round trip, avg half spread 0.9 bps, open 186.526
- DOGE: 1 fills (1 buy / 0 sell), traded 607, gross pnl +0.00, +0 bps per round trip, avg half spread 1.4 bps, open 7200.88
- DOT: 2 fills (1 buy / 1 sell), traded 3,758, gross pnl +220.54, +1174 bps per round trip, avg half spread 2.8 bps, open 1306.72
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +0.00, +0 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +26.03, +144 bps per round trip, avg half spread 3.2 bps, open 27.0231

last fills:

- 2026-09-18 02:23Z buy AVAX 2,553 @ 7.68984 fee 2.55 slip 1.28 (half spread 1.3 bps)
- 2026-09-18 03:21Z buy ADA 2,424 @ 0.21528 fee 2.42 slip 1.21 (half spread 2.4 bps)
- 2026-09-18 04:22Z sell ADA 936 @ 0.213847 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-09-18 04:22Z sell AVAX 1,148 @ 7.89055 fee 1.15 slip 0.57 (half spread 0.6 bps)
- 2026-09-18 04:22Z buy LINK 1,473 @ 11.7384 fee 1.47 slip 0.74 (half spread 1.4 bps)
- 2026-09-18 04:22Z buy DOGE 607 @ 0.0843329 fee 0.61 slip 0.30 (half spread 1.4 bps)
- 2026-09-18 04:22Z sell DOT 1,252 @ 1.12629 fee 1.25 slip 0.63 (half spread 2.2 bps)
- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 769 candles, 2026-08-17 03:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 769 candles, 2026-08-17 03:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 769 candles, 2026-08-17 03:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- ADA: live 769 candles, 2026-08-17 03:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.5 bps
- AVAX: live 769 candles, 2026-08-17 03:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 769 candles, 2026-08-17 03:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- XRP: live 741 candles, 2026-08-18 07:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 741 candles, 2026-08-18 07:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 741 candles, 2026-08-18 07:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 741 candles, 2026-08-18 07:00Z to 2026-09-18 03:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
