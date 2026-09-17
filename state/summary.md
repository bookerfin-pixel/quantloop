# quantloop summary — generated 2026-09-17 14:24Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.4 of 60, 58.6 days until the verdict
  so far: champion +0.46% (DD -0.19%, 2 fills) vs challenger1 +2.62% (DD -1.00%, 6 fills)
  market over the window: BTC +0.93%, equal weight basket of 10 pairs +3.03%, basket realised vol 42% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,045.77 (started 10,000 at 2026-09-16 03:55Z), net +0.46% since start
- 24h +0.46%, 7d +0.46%, 30d +0.46%, max drawdown -0.19%
- fills 2 total, 2 in the last 7d
- costs 7.60 (fees 5.01 + slippage 2.60); gross pnl 53.37; cost coverage 7.02
- cash 4,989.23; positions: AVAX 333.1, DOT 2418.21
- last run 2026-09-17 14:24Z; halted today: False

last decisions (newest last):

- 2026-09-17 13:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.69% not above entry band +1.0%
- 2026-09-17 13:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.82% not above entry band +1.0%
- 2026-09-17 13:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.05% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 13:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-09-17 13:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.48% not above entry band +1.0%
- 2026-09-17 13:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.99% not above entry band +1.0%
- 2026-09-17 13:23Z DOT buy target 0.25 (held 0.00) — enter long: 72h return +2.15% vs entry band +1.0% and price above 24h EMA; realised vol 84% -> weight 0.25
- 2026-09-17 13:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.40% not above entry band +1.0%
- 2026-09-17 14:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.95% not above entry band +1.0%
- 2026-09-17 14:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-09-17 14:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.74% not above entry band +1.0%
- 2026-09-17 14:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.79% not above entry band +1.0%
- 2026-09-17 14:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +1.68% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 14:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.77% not above entry band +1.0%
- 2026-09-17 14:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.59% not above entry band +1.0%
- 2026-09-17 14:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.85% not above entry band +1.0%
- 2026-09-17 14:24Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.55% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 14:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.68% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +44.30, +354 bps per round trip, open 333.1
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +9.07, +72 bps per round trip, avg half spread 3.4 bps, open 2418.21

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,250.44 (started 10,000 at 2026-09-16 03:55Z), net +2.50% since start
- 24h +3.37%, 7d +2.50%, 30d +2.50%, max drawdown -1.00%
- fills 6 total, 6 in the last 7d
- costs 22.68 (fees 15.12 + slippage 7.56); gross pnl 273.12; cost coverage 12.04
- cash 5,129.36; positions: ADA 12763.5, BTC 0.0328342
- last run 2026-09-17 14:24Z; halted today: False

last decisions (newest last):

- 2026-09-17 13:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.25 not below -2.0
- 2026-09-17 13:23Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -0.94 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-09-17 13:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.06 not below -2.0
- 2026-09-17 13:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.66 not below -2.0
- 2026-09-17 13:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.41 not below -2.0
- 2026-09-17 13:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.10 not below -2.0
- 2026-09-17 13:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.34 not below -2.0
- 2026-09-17 13:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.43 not below -2.0
- 2026-09-17 14:24Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: z -0.84 vs 240h mean (entry -2.0, exit -0.5); vol 32% -> weight 0.25
- 2026-09-17 14:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.44 not below -2.0
- 2026-09-17 14:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.25 not below -2.0
- 2026-09-17 14:24Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.94 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-09-17 14:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.04 not below -2.0
- 2026-09-17 14:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.66 not below -2.0
- 2026-09-17 14:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.44 not below -2.0
- 2026-09-17 14:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.06 not below -2.0
- 2026-09-17 14:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.27 not below -2.0
- 2026-09-17 14:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0

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

- equity 10,045.77 (started 10,000 at 2026-09-16 23:20Z), net +0.46% since start
- 24h +0.46%, 7d +0.46%, 30d +0.46%, max drawdown -0.19%
- fills 2 total, 2 in the last 7d
- costs 7.60 (fees 5.01 + slippage 2.60); gross pnl 53.37; cost coverage 7.02
- cash 4,989.23; positions: AVAX 333.1, DOT 2418.21
- last run 2026-09-17 14:24Z; halted today: False

last decisions (newest last):

- 2026-09-17 13:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.69% not above entry band +1.0%
- 2026-09-17 13:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.82% not above entry band +1.0%
- 2026-09-17 13:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.05% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 13:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-09-17 13:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.48% not above entry band +1.0%
- 2026-09-17 13:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.99% not above entry band +1.0%
- 2026-09-17 13:23Z DOT buy target 0.25 (held 0.00) — enter long: 72h return +2.15% vs entry band +1.0% and price above 24h EMA; realised vol 84% -> weight 0.25
- 2026-09-17 13:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.40% not above entry band +1.0%
- 2026-09-17 14:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.95% not above entry band +1.0%
- 2026-09-17 14:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-09-17 14:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.74% not above entry band +1.0%
- 2026-09-17 14:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.79% not above entry band +1.0%
- 2026-09-17 14:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +1.68% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 14:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.77% not above entry band +1.0%
- 2026-09-17 14:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.59% not above entry band +1.0%
- 2026-09-17 14:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.85% not above entry band +1.0%
- 2026-09-17 14:24Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.55% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 14:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.68% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +44.30, +354 bps per round trip, open 333.1
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +9.07, +72 bps per round trip, avg half spread 3.4 bps, open 2418.21

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,045.77 (started 10,000 at 2026-09-16 23:20Z), net +0.46% since start
- 24h +0.46%, 7d +0.46%, 30d +0.46%, max drawdown -0.19%
- fills 2 total, 2 in the last 7d
- costs 7.60 (fees 5.01 + slippage 2.60); gross pnl 53.37; cost coverage 7.02
- cash 4,989.23; positions: AVAX 333.1, DOT 2418.21
- last run 2026-09-17 14:24Z; halted today: False

last decisions (newest last):

- 2026-09-17 13:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.69% not above entry band +1.0%
- 2026-09-17 13:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.82% not above entry band +1.0%
- 2026-09-17 13:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.05% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 13:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.37% not above entry band +1.0%
- 2026-09-17 13:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.48% not above entry band +1.0%
- 2026-09-17 13:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.99% not above entry band +1.0%
- 2026-09-17 13:23Z DOT buy target 0.25 (held 0.00) — enter long: 72h return +2.15% vs entry band +1.0% and price above 24h EMA; realised vol 84% -> weight 0.25
- 2026-09-17 13:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.40% not above entry band +1.0%
- 2026-09-17 14:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.95% not above entry band +1.0%
- 2026-09-17 14:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-09-17 14:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.74% not above entry band +1.0%
- 2026-09-17 14:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.79% not above entry band +1.0%
- 2026-09-17 14:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +1.68% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 14:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.77% not above entry band +1.0%
- 2026-09-17 14:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.59% not above entry band +1.0%
- 2026-09-17 14:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.85% not above entry band +1.0%
- 2026-09-17 14:24Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.55% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 14:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.68% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +44.30, +354 bps per round trip, open 333.1
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +9.07, +72 bps per round trip, avg half spread 3.4 bps, open 2418.21

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 755 candles, 2026-08-17 03:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 755 candles, 2026-08-17 03:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 755 candles, 2026-08-17 03:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- ADA: live 755 candles, 2026-08-17 03:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 3.3 bps
- AVAX: live 755 candles, 2026-08-17 03:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.5 bps
- LINK: live 755 candles, 2026-08-17 03:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 727 candles, 2026-08-18 07:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 727 candles, 2026-08-18 07:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.7 bps
- DOT: live 727 candles, 2026-08-18 07:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.4 bps
- LTC: live 727 candles, 2026-08-18 07:00Z to 2026-09-17 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.4 bps
