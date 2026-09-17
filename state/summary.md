# quantloop summary — generated 2026-09-17 09:23Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.2 of 60, 58.8 days until the verdict
  so far: champion +0.16% (DD -0.15%, 1 fills) vs challenger1 +2.05% (DD -1.00%, 5 fills)
  market over the window: BTC +0.78%, equal weight basket of 10 pairs +2.67%, basket realised vol 44% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,016.24 (started 10,000 at 2026-09-16 03:55Z), net +0.16% since start
- 24h +0.16%, 7d +0.16%, 30d +0.16%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 19.99; cost coverage 5.33
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 09:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 08:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-09-17 08:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.61% not above entry band +1.0%
- 2026-09-17 08:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.48% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 08:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.05% not above entry band +1.0%
- 2026-09-17 08:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.41% not above entry band +1.0%
- 2026-09-17 08:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.81% not above entry band +1.0%
- 2026-09-17 08:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.95% not above entry band +1.0%
- 2026-09-17 08:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.32% not above entry band +1.0%
- 2026-09-17 09:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-17 09:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.97% not above entry band +1.0%
- 2026-09-17 09:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.16% not above entry band +1.0%
- 2026-09-17 09:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.99% not above entry band +1.0%
- 2026-09-17 09:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.70% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 09:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.36% not above entry band +1.0%
- 2026-09-17 09:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.91% not above entry band +1.0%
- 2026-09-17 09:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.10% not above entry band +1.0%
- 2026-09-17 09:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.17% not above entry band +1.0%
- 2026-09-17 09:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.78% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +19.99, +160 bps per round trip, open 333.1

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,193.83 (started 10,000 at 2026-09-16 03:55Z), net +1.94% since start
- 24h +2.33%, 7d +1.94%, 30d +1.94%, max drawdown -1.00%
- fills 5 total, 5 in the last 7d
- costs 18.86 (fees 12.57 + slippage 6.29); gross pnl 212.69; cost coverage 11.28
- cash 2,583.50; positions: ADA 12763.5, BTC 0.0328342, ETH 1.04017
- last run 2026-09-17 09:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 08:24Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.62 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 08:24Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.23 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 08:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.29 not below -2.0
- 2026-09-17 08:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.85 not below -2.0
- 2026-09-17 08:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.55 not below -2.0
- 2026-09-17 08:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.16 not below -2.0
- 2026-09-17 08:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.62 not below -2.0
- 2026-09-17 08:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.51 not below -2.0
- 2026-09-17 09:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -0.99 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-17 09:23Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -0.86 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-17 09:23Z SOL sell target 0.00 (held 0.25) — flat: z -0.47 not below -0.5
- 2026-09-17 09:23Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.10 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 09:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.07 not below -2.0
- 2026-09-17 09:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.77 not below -2.0
- 2026-09-17 09:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.49 not below -2.0
- 2026-09-17 09:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.04 not below -2.0
- 2026-09-17 09:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.51 not below -2.0
- 2026-09-17 09:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.39 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 12763.5
- BTC: 1 fills (1 buy / 0 sell), traded 2,489, gross pnl -2,488.07, -19990 bps per round trip, open 0.0328342
- ETH: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 1.04017
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,016.24 (started 10,000 at 2026-09-16 23:20Z), net +0.16% since start
- 24h +0.16%, 7d +0.16%, 30d +0.16%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 19.99; cost coverage 5.33
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 09:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 08:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-09-17 08:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.61% not above entry band +1.0%
- 2026-09-17 08:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.48% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 08:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.05% not above entry band +1.0%
- 2026-09-17 08:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.41% not above entry band +1.0%
- 2026-09-17 08:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.81% not above entry band +1.0%
- 2026-09-17 08:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.95% not above entry band +1.0%
- 2026-09-17 08:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.32% not above entry band +1.0%
- 2026-09-17 09:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-17 09:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.97% not above entry band +1.0%
- 2026-09-17 09:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.16% not above entry band +1.0%
- 2026-09-17 09:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.99% not above entry band +1.0%
- 2026-09-17 09:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.70% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 09:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.36% not above entry band +1.0%
- 2026-09-17 09:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.91% not above entry band +1.0%
- 2026-09-17 09:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.10% not above entry band +1.0%
- 2026-09-17 09:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.17% not above entry band +1.0%
- 2026-09-17 09:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.78% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +19.99, +160 bps per round trip, open 333.1

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,016.24 (started 10,000 at 2026-09-16 23:20Z), net +0.16% since start
- 24h +0.16%, 7d +0.16%, 30d +0.16%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 19.99; cost coverage 5.33
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 09:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 08:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-09-17 08:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.61% not above entry band +1.0%
- 2026-09-17 08:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.48% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 08:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.05% not above entry band +1.0%
- 2026-09-17 08:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.41% not above entry band +1.0%
- 2026-09-17 08:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.81% not above entry band +1.0%
- 2026-09-17 08:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.95% not above entry band +1.0%
- 2026-09-17 08:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.32% not above entry band +1.0%
- 2026-09-17 09:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-17 09:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.97% not above entry band +1.0%
- 2026-09-17 09:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.16% not above entry band +1.0%
- 2026-09-17 09:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.99% not above entry band +1.0%
- 2026-09-17 09:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.70% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 09:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.36% not above entry band +1.0%
- 2026-09-17 09:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.91% not above entry band +1.0%
- 2026-09-17 09:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.10% not above entry band +1.0%
- 2026-09-17 09:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.17% not above entry band +1.0%
- 2026-09-17 09:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.78% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +19.99, +160 bps per round trip, open 333.1

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 750 candles, 2026-08-17 03:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 750 candles, 2026-08-17 03:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- SOL: live 750 candles, 2026-08-17 03:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.9 bps
- ADA: live 750 candles, 2026-08-17 03:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 3.3 bps
- AVAX: live 750 candles, 2026-08-17 03:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 750 candles, 2026-08-17 03:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 722 candles, 2026-08-18 07:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOGE: live 722 candles, 2026-08-18 07:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.0 bps
- DOT: live 722 candles, 2026-08-18 07:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 3.0 bps
- LTC: live 722 candles, 2026-08-18 07:00Z to 2026-09-17 08:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
