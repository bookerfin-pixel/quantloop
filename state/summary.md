# quantloop summary — generated 2026-09-17 20:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.6 of 60, 58.4 days until the verdict
  so far: champion +1.31% (DD -0.52%, 2 fills) vs challenger1 +2.41% (DD -1.00%, 6 fills)
  market over the window: BTC +0.82%, equal weight basket of 10 pairs +3.54%, basket realised vol 41% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,130.67 (started 10,000 at 2026-09-16 03:55Z), net +1.31% since start
- 24h +1.31%, 7d +1.31%, 30d +1.31%, max drawdown -0.52%
- fills 2 total, 2 in the last 7d
- costs 7.60 (fees 5.01 + slippage 2.60); gross pnl 138.27; cost coverage 18.19
- cash 4,989.23; positions: AVAX 333.1, DOT 2418.21
- last run 2026-09-17 20:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.75% not above entry band +1.0%
- 2026-09-17 19:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.86% not above entry band +1.0%
- 2026-09-17 19:20Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.18% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.37% not above entry band +1.0%
- 2026-09-17 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -12.37% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.27% not above entry band +1.0%
- 2026-09-17 19:20Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.005 below threshold 0.05 | stay long: 72h return +4.50% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.37% not above entry band +1.0%
- 2026-09-17 20:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.13% not above entry band +1.0%
- 2026-09-17 20:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.63% not above entry band +1.0%
- 2026-09-17 20:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.28% not above entry band +1.0%
- 2026-09-17 20:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.12% not above entry band +1.0%
- 2026-09-17 20:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.20% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 20:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.74% not above entry band +1.0%
- 2026-09-17 20:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.57% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 20:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.64% not above entry band +1.0%
- 2026-09-17 20:22Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +4.56% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 20:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.04% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +37.31, +298 bps per round trip, open 333.1
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +100.96, +806 bps per round trip, avg half spread 3.4 bps, open 2418.21

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,229.22 (started 10,000 at 2026-09-16 03:55Z), net +2.29% since start
- 24h +1.73%, 7d +2.29%, 30d +2.29%, max drawdown -1.00%
- fills 6 total, 6 in the last 7d
- costs 22.68 (fees 15.12 + slippage 7.56); gross pnl 251.90; cost coverage 11.11
- cash 5,129.36; positions: ADA 12763.5, BTC 0.0328342
- last run 2026-09-17 20:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.16 not below -2.0
- 2026-09-17 19:20Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -0.83 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-09-17 19:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.05 not below -2.0
- 2026-09-17 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.57 not below -2.0
- 2026-09-17 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.54 not below -2.0
- 2026-09-17 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.99 not below -2.0
- 2026-09-17 19:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-09-17 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.11 not below -2.0
- 2026-09-17 20:22Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: z -0.89 vs 240h mean (entry -2.0, exit -0.5); vol 32% -> weight 0.25
- 2026-09-17 20:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.72 not below -2.0
- 2026-09-17 20:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.09 not below -2.0
- 2026-09-17 20:22Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.79 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-09-17 20:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.02 not below -2.0
- 2026-09-17 20:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.57 not below -2.0
- 2026-09-17 20:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.52 not below -2.0
- 2026-09-17 20:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.91 not below -2.0
- 2026-09-17 20:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.11 not below -2.0
- 2026-09-17 20:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.49 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 12763.5
- BTC: 1 fills (1 buy / 0 sell), traded 2,489, gross pnl -2,488.07, -19990 bps per round trip, open 0.0328342
- ETH: 2 fills (1 buy / 1 sell), traded 5,048, gross pnl +50.93, +202 bps per round trip, avg half spread 0.4 bps
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)
- 2026-09-17 13:23Z sell ETH 2,548 @ 2449.98 fee 2.55 slip 1.27 (half spread 0.4 bps)

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,130.67 (started 10,000 at 2026-09-16 23:20Z), net +1.31% since start
- 24h +1.31%, 7d +1.31%, 30d +1.31%, max drawdown -0.52%
- fills 2 total, 2 in the last 7d
- costs 7.60 (fees 5.01 + slippage 2.60); gross pnl 138.27; cost coverage 18.19
- cash 4,989.23; positions: AVAX 333.1, DOT 2418.21
- last run 2026-09-17 20:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.75% not above entry band +1.0%
- 2026-09-17 19:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.86% not above entry band +1.0%
- 2026-09-17 19:20Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.18% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.37% not above entry band +1.0%
- 2026-09-17 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -12.37% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.27% not above entry band +1.0%
- 2026-09-17 19:20Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.005 below threshold 0.05 | stay long: 72h return +4.50% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.37% not above entry band +1.0%
- 2026-09-17 20:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.13% not above entry band +1.0%
- 2026-09-17 20:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.63% not above entry band +1.0%
- 2026-09-17 20:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.28% not above entry band +1.0%
- 2026-09-17 20:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.12% not above entry band +1.0%
- 2026-09-17 20:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.20% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 20:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.74% not above entry band +1.0%
- 2026-09-17 20:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.57% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 20:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.64% not above entry band +1.0%
- 2026-09-17 20:22Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +4.56% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 20:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.04% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +37.31, +298 bps per round trip, open 333.1
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +100.96, +806 bps per round trip, avg half spread 3.4 bps, open 2418.21

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,130.67 (started 10,000 at 2026-09-16 23:20Z), net +1.31% since start
- 24h +1.31%, 7d +1.31%, 30d +1.31%, max drawdown -0.52%
- fills 2 total, 2 in the last 7d
- costs 7.60 (fees 5.01 + slippage 2.60); gross pnl 138.27; cost coverage 18.19
- cash 4,989.23; positions: AVAX 333.1, DOT 2418.21
- last run 2026-09-17 20:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 19:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.75% not above entry band +1.0%
- 2026-09-17 19:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.86% not above entry band +1.0%
- 2026-09-17 19:20Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.18% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 19:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.37% not above entry band +1.0%
- 2026-09-17 19:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -12.37% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 19:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.27% not above entry band +1.0%
- 2026-09-17 19:20Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.005 below threshold 0.05 | stay long: 72h return +4.50% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 19:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.37% not above entry band +1.0%
- 2026-09-17 20:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.13% not above entry band +1.0%
- 2026-09-17 20:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.63% not above entry band +1.0%
- 2026-09-17 20:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.28% not above entry band +1.0%
- 2026-09-17 20:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.12% not above entry band +1.0%
- 2026-09-17 20:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.20% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 20:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.74% not above entry band +1.0%
- 2026-09-17 20:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.57% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 20:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.64% not above entry band +1.0%
- 2026-09-17 20:22Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +4.56% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 20:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.04% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +37.31, +298 bps per round trip, open 333.1
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +100.96, +806 bps per round trip, avg half spread 3.4 bps, open 2418.21

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 761 candles, 2026-08-17 03:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 761 candles, 2026-08-17 03:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 761 candles, 2026-08-17 03:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 761 candles, 2026-08-17 03:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 3.0 bps
- AVAX: live 761 candles, 2026-08-17 03:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 761 candles, 2026-08-17 03:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- XRP: live 733 candles, 2026-08-18 07:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.3 bps
- DOGE: live 733 candles, 2026-08-18 07:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 733 candles, 2026-08-18 07:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- LTC: live 733 candles, 2026-08-18 07:00Z to 2026-09-17 19:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.3 bps
