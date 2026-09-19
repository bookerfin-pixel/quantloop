# quantloop summary — generated 2026-09-19 19:18Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 3.6 of 60, 56.4 days until the verdict
  so far: champion +10.16% (DD -2.31%, 19 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +7.26%, equal weight basket of 10 pairs +15.07%, basket realised vol 46% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,015.63 (started 10,000 at 2026-09-16 03:55Z), net +10.16% since start
- 24h +2.32%, 7d +10.16%, 30d +10.16%, max drawdown -2.31%
- fills 19 total, 19 in the last 7d
- costs 42.37 (fees 27.99 + slippage 14.38); gross pnl 1,058.00; cost coverage 24.97
- cash 0.00; positions: ADA 6882.97, AVAX 119.949, BTC 0.0148035, DOGE 17308.9, ETH 0.0928176, LINK 125.494, LTC 27.0231, SOL 13.9531, XRP 422.407
- last run 2026-09-19 19:18Z; halted today: False

last decisions (newest last):

- 2026-09-19 18:22Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +14.78% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +19.10% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +33.26% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +17.03% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z XRP hold target 0.10 (held 0.05) — hold: weight change +0.045 below threshold 0.05 | stay long: 72h return +12.73% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +14.05% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z DOT none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +16.10% vs entry band +1.0% and price above 24h EMA; realised vol 81% ...
- 2026-09-19 18:22Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +13.61% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z BTC hold target 0.10 (held 0.11) — hold: weight change -0.009 below threshold 0.05 | stay long: 72h return +7.75% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-09-19 19:18Z ETH none target 0.10 (held 0.02) — no fill possible (no cash or no position) | stay long: 72h return +10.13% vs exit band -1.0% and price above 24h EMA; realised vol 43% ->...
- 2026-09-19 19:18Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +13.71% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 19:18Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +19.67% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +34.59% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +16.01% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z XRP hold target 0.10 (held 0.05) — hold: weight change +0.045 below threshold 0.05 | stay long: 72h return +11.95% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +12.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z DOT none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +15.29% vs entry band +1.0% and price above 24h EMA; realised vol 81% ...
- 2026-09-19 19:18Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +13.52% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +93.48, +556 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 5 fills (2 buy / 3 sell), traded 9,337, gross pnl +399.12, +855 bps per round trip, avg half spread 1.1 bps, open 119.949
- BTC: 1 fills (1 buy / 0 sell), traded 1,207, gross pnl -1.39, -23 bps per round trip, avg half spread 0.0 bps, open 0.0148035
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +89.35, +1223 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 1 fills (1 buy / 0 sell), traded 246, gross pnl -1.74, -141 bps per round trip, avg half spread 0.0 bps, open 0.0928176
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +96.32, +1308 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +108.72, +602 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +71.02, +962 bps per round trip, avg half spread 0.5 bps, open 13.9531
- XRP: 1 fills (1 buy / 0 sell), traded 604, gross pnl -1.69, -56 bps per round trip, avg half spread 0.0 bps, open 422.407

last fills:

- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-09-19 08:22Z sell DOT 1,456 @ 1.11408 fee 1.46 slip 0.94 (half spread 4.5 bps)
- 2026-09-19 09:21Z buy BTC 1,207 @ 81506.2 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-09-19 09:21Z buy ETH 246 @ 2653.58 fee 0.25 slip 0.12 (half spread 0.0 bps)
- 2026-09-19 12:26Z sell AVAX 606 @ 9.09595 fee 0.61 slip 0.30 (half spread 1.6 bps)
- 2026-09-19 12:26Z buy XRP 604 @ 1.43078 fee 0.60 slip 0.30 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-19 19:18Z; halted today: False

last decisions (newest last):

- 2026-09-19 18:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.21 not below -2.0
- 2026-09-19 18:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.49 not below -2.0
- 2026-09-19 18:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +4.46 not below -2.0
- 2026-09-19 18:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.40 not below -2.0
- 2026-09-19 18:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.50 not below -2.0
- 2026-09-19 18:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.49 not below -2.0
- 2026-09-19 18:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.33 not below -2.0
- 2026-09-19 18:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.19 not below -2.0
- 2026-09-19 19:18Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.45 not below -2.0
- 2026-09-19 19:18Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.18 not below -2.0
- 2026-09-19 19:18Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.12 not below -2.0
- 2026-09-19 19:18Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.48 not below -2.0
- 2026-09-19 19:18Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +4.52 not below -2.0
- 2026-09-19 19:18Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.38 not below -2.0
- 2026-09-19 19:18Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.56 not below -2.0
- 2026-09-19 19:18Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.42 not below -2.0
- 2026-09-19 19:18Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.32 not below -2.0
- 2026-09-19 19:18Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.13 not below -2.0

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

- equity 11,015.63 (started 10,000 at 2026-09-16 23:20Z), net +10.16% since start
- 24h +2.32%, 7d +10.16%, 30d +10.16%, max drawdown -2.31%
- fills 19 total, 19 in the last 7d
- costs 42.37 (fees 27.99 + slippage 14.38); gross pnl 1,058.00; cost coverage 24.97
- cash 0.00; positions: ADA 6882.97, AVAX 119.949, BTC 0.0148035, DOGE 17308.9, ETH 0.0928176, LINK 125.494, LTC 27.0231, SOL 13.9531, XRP 422.407
- last run 2026-09-19 19:18Z; halted today: False

last decisions (newest last):

- 2026-09-19 18:22Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +14.78% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +19.10% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +33.26% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +17.03% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z XRP hold target 0.10 (held 0.05) — hold: weight change +0.045 below threshold 0.05 | stay long: 72h return +12.73% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +14.05% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z DOT none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +16.10% vs entry band +1.0% and price above 24h EMA; realised vol 81% ...
- 2026-09-19 18:22Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +13.61% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z BTC hold target 0.10 (held 0.11) — hold: weight change -0.009 below threshold 0.05 | stay long: 72h return +7.75% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-09-19 19:18Z ETH none target 0.10 (held 0.02) — no fill possible (no cash or no position) | stay long: 72h return +10.13% vs exit band -1.0% and price above 24h EMA; realised vol 43% ->...
- 2026-09-19 19:18Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +13.71% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 19:18Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +19.67% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +34.59% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +16.01% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z XRP hold target 0.10 (held 0.05) — hold: weight change +0.045 below threshold 0.05 | stay long: 72h return +11.95% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +12.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z DOT none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +15.29% vs entry band +1.0% and price above 24h EMA; realised vol 81% ...
- 2026-09-19 19:18Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +13.52% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +93.48, +556 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 5 fills (2 buy / 3 sell), traded 9,337, gross pnl +399.12, +855 bps per round trip, avg half spread 1.1 bps, open 119.949
- BTC: 1 fills (1 buy / 0 sell), traded 1,207, gross pnl -1.39, -23 bps per round trip, avg half spread 0.0 bps, open 0.0148035
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +89.35, +1223 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 1 fills (1 buy / 0 sell), traded 246, gross pnl -1.74, -141 bps per round trip, avg half spread 0.0 bps, open 0.0928176
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +96.32, +1308 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +108.72, +602 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +71.02, +962 bps per round trip, avg half spread 0.5 bps, open 13.9531
- XRP: 1 fills (1 buy / 0 sell), traded 604, gross pnl -1.69, -56 bps per round trip, avg half spread 0.0 bps, open 422.407

last fills:

- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-09-19 08:22Z sell DOT 1,456 @ 1.11408 fee 1.46 slip 0.94 (half spread 4.5 bps)
- 2026-09-19 09:21Z buy BTC 1,207 @ 81506.2 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-09-19 09:21Z buy ETH 246 @ 2653.58 fee 0.25 slip 0.12 (half spread 0.0 bps)
- 2026-09-19 12:26Z sell AVAX 606 @ 9.09595 fee 0.61 slip 0.30 (half spread 1.6 bps)
- 2026-09-19 12:26Z buy XRP 604 @ 1.43078 fee 0.60 slip 0.30 (half spread 0.0 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,015.63 (started 10,000 at 2026-09-16 23:20Z), net +10.16% since start
- 24h +2.32%, 7d +10.16%, 30d +10.16%, max drawdown -2.31%
- fills 19 total, 19 in the last 7d
- costs 42.37 (fees 27.99 + slippage 14.38); gross pnl 1,058.00; cost coverage 24.97
- cash 0.00; positions: ADA 6882.97, AVAX 119.949, BTC 0.0148035, DOGE 17308.9, ETH 0.0928176, LINK 125.494, LTC 27.0231, SOL 13.9531, XRP 422.407
- last run 2026-09-19 19:18Z; halted today: False

last decisions (newest last):

- 2026-09-19 18:22Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +14.78% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +19.10% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +33.26% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +17.03% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z XRP hold target 0.10 (held 0.05) — hold: weight change +0.045 below threshold 0.05 | stay long: 72h return +12.73% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +14.05% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 18:22Z DOT none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +16.10% vs entry band +1.0% and price above 24h EMA; realised vol 81% ...
- 2026-09-19 18:22Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +13.61% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z BTC hold target 0.10 (held 0.11) — hold: weight change -0.009 below threshold 0.05 | stay long: 72h return +7.75% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-09-19 19:18Z ETH none target 0.10 (held 0.02) — no fill possible (no cash or no position) | stay long: 72h return +10.13% vs exit band -1.0% and price above 24h EMA; realised vol 43% ->...
- 2026-09-19 19:18Z SOL hold target 0.10 (held 0.14) — hold: weight change -0.040 below threshold 0.05 | stay long: 72h return +13.71% vs exit band -1.0% and price within 2.0% of 24h EMA; real...
- 2026-09-19 19:18Z ADA hold target 0.10 (held 0.14) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +19.67% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +34.59% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z LINK hold target 0.10 (held 0.14) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +16.01% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z XRP hold target 0.10 (held 0.05) — hold: weight change +0.045 below threshold 0.05 | stay long: 72h return +11.95% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z DOGE hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +12.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-19 19:18Z DOT none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +15.29% vs entry band +1.0% and price above 24h EMA; realised vol 81% ...
- 2026-09-19 19:18Z LTC hold target 0.10 (held 0.14) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +13.52% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 3,361, gross pnl +93.48, +556 bps per round trip, avg half spread 1.2 bps, open 6882.97
- AVAX: 5 fills (2 buy / 3 sell), traded 9,337, gross pnl +399.12, +855 bps per round trip, avg half spread 1.1 bps, open 119.949
- BTC: 1 fills (1 buy / 0 sell), traded 1,207, gross pnl -1.39, -23 bps per round trip, avg half spread 0.0 bps, open 0.0148035
- DOGE: 2 fills (2 buy / 0 sell), traded 1,461, gross pnl +89.35, +1223 bps per round trip, avg half spread 0.9 bps, open 17308.9
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 1 fills (1 buy / 0 sell), traded 246, gross pnl -1.74, -141 bps per round trip, avg half spread 0.0 bps, open 0.0928176
- LINK: 1 fills (1 buy / 0 sell), traded 1,473, gross pnl +96.32, +1308 bps per round trip, avg half spread 1.4 bps, open 125.494
- LTC: 2 fills (1 buy / 1 sell), traded 3,614, gross pnl +108.72, +602 bps per round trip, avg half spread 3.2 bps, open 27.0231
- SOL: 1 fills (1 buy / 0 sell), traded 1,476, gross pnl +71.02, +962 bps per round trip, avg half spread 0.5 bps, open 13.9531
- XRP: 1 fills (1 buy / 0 sell), traded 604, gross pnl -1.69, -56 bps per round trip, avg half spread 0.0 bps, open 422.407

last fills:

- 2026-09-18 04:22Z sell LTC 1,083 @ 54.4591 fee 1.08 slip 0.61 (half spread 3.7 bps)
- 2026-09-18 05:20Z buy SOL 1,476 @ 105.808 fee 1.48 slip 0.74 (half spread 0.5 bps)
- 2026-09-18 05:20Z buy DOGE 854 @ 0.0844636 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-09-19 08:22Z sell DOT 1,456 @ 1.11408 fee 1.46 slip 0.94 (half spread 4.5 bps)
- 2026-09-19 09:21Z buy BTC 1,207 @ 81506.2 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-09-19 09:21Z buy ETH 246 @ 2653.58 fee 0.25 slip 0.12 (half spread 0.0 bps)
- 2026-09-19 12:26Z sell AVAX 606 @ 9.09595 fee 0.61 slip 0.30 (half spread 1.6 bps)
- 2026-09-19 12:26Z buy XRP 604 @ 1.43078 fee 0.60 slip 0.30 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 808 candles, 2026-08-17 03:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 808 candles, 2026-08-17 03:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 808 candles, 2026-08-17 03:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 808 candles, 2026-08-17 03:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- AVAX: live 808 candles, 2026-08-17 03:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 808 candles, 2026-08-17 03:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 780 candles, 2026-08-18 07:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 780 candles, 2026-08-18 07:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 780 candles, 2026-08-18 07:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 780 candles, 2026-08-18 07:00Z to 2026-09-19 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
