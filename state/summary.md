# quantloop summary — generated 2026-09-17 07:24Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.1 of 60, 58.9 days until the verdict
  so far: champion +0.10% (DD -0.15%, 1 fills) vs challenger1 +1.77% (DD -1.00%, 4 fills)
  market over the window: BTC +0.65%, equal weight basket of 10 pairs +2.06%, basket realised vol 45% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,009.91 (started 10,000 at 2026-09-16 03:55Z), net +0.10% since start
- 24h +0.10%, 7d +0.10%, 30d +0.10%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 13.66; cost coverage 3.64
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 07:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 07:07Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-17 07:07Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.43% not above entry band +1.0%
- 2026-09-17 07:07Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.49% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 07:07Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0%
- 2026-09-17 07:07Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.19% not above entry band +1.0%
- 2026-09-17 07:07Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.03% not above entry band +1.0%
- 2026-09-17 07:07Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-17 07:07Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0%
- 2026-09-17 07:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0%
- 2026-09-17 07:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.96% not above entry band +1.0%
- 2026-09-17 07:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-17 07:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.43% not above entry band +1.0%
- 2026-09-17 07:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.49% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 07:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0%
- 2026-09-17 07:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.19% not above entry band +1.0%
- 2026-09-17 07:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.03% not above entry band +1.0%
- 2026-09-17 07:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-17 07:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +13.66, +109 bps per round trip, open 333.1

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,165.51 (started 10,000 at 2026-09-16 03:55Z), net +1.66% since start
- 24h +2.48%, 7d +1.66%, 30d +1.66%, max drawdown -1.00%
- fills 4 total, 4 in the last 7d
- costs 14.98 (fees 9.99 + slippage 4.99); gross pnl 180.50; cost coverage 12.05
- cash 0.70; positions: ADA 12763.5, BTC 0.0328342, ETH 1.04017, SOL 25.7086
- last run 2026-09-17 07:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 07:07Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.76 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 07:07Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.37 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 07:07Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.33 not below -2.0
- 2026-09-17 07:07Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.90 not below -2.0
- 2026-09-17 07:07Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.59 not below -2.0
- 2026-09-17 07:07Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.23 not below -2.0
- 2026-09-17 07:07Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.59 not below -2.0
- 2026-09-17 07:07Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.76 not below -2.0
- 2026-09-17 07:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.10 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-17 07:23Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -0.96 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-17 07:23Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.76 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 07:23Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.37 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 07:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.33 not below -2.0
- 2026-09-17 07:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.90 not below -2.0
- 2026-09-17 07:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.59 not below -2.0
- 2026-09-17 07:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.23 not below -2.0
- 2026-09-17 07:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.59 not below -2.0
- 2026-09-17 07:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.76 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 12763.5
- BTC: 1 fills (1 buy / 0 sell), traded 2,489, gross pnl -2,488.07, -19990 bps per round trip, open 0.0328342
- ETH: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 1.04017
- SOL: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 25.7086

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,009.91 (started 10,000 at 2026-09-16 23:20Z), net +0.10% since start
- 24h +0.10%, 7d +0.10%, 30d +0.10%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 13.66; cost coverage 3.64
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 07:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 07:07Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-17 07:07Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.43% not above entry band +1.0%
- 2026-09-17 07:07Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.49% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 07:07Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0%
- 2026-09-17 07:07Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.19% not above entry band +1.0%
- 2026-09-17 07:07Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.03% not above entry band +1.0%
- 2026-09-17 07:07Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-17 07:07Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0%
- 2026-09-17 07:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0%
- 2026-09-17 07:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.96% not above entry band +1.0%
- 2026-09-17 07:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-17 07:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.43% not above entry band +1.0%
- 2026-09-17 07:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.49% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 07:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0%
- 2026-09-17 07:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.19% not above entry band +1.0%
- 2026-09-17 07:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.03% not above entry band +1.0%
- 2026-09-17 07:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-17 07:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +13.66, +109 bps per round trip, open 333.1

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,009.91 (started 10,000 at 2026-09-16 23:20Z), net +0.10% since start
- 24h +0.10%, 7d +0.10%, 30d +0.10%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 13.66; cost coverage 3.64
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 07:23Z; halted today: False

last decisions (newest last):

- 2026-09-17 07:07Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-17 07:07Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.43% not above entry band +1.0%
- 2026-09-17 07:07Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.49% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 07:07Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0%
- 2026-09-17 07:07Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.19% not above entry band +1.0%
- 2026-09-17 07:07Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.03% not above entry band +1.0%
- 2026-09-17 07:07Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-17 07:07Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0%
- 2026-09-17 07:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0%
- 2026-09-17 07:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.96% not above entry band +1.0%
- 2026-09-17 07:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-17 07:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.43% not above entry band +1.0%
- 2026-09-17 07:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.49% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 07:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.30% not above entry band +1.0%
- 2026-09-17 07:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.19% not above entry band +1.0%
- 2026-09-17 07:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.03% not above entry band +1.0%
- 2026-09-17 07:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-17 07:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.14% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +13.66, +109 bps per round trip, open 333.1

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 748 candles, 2026-08-17 03:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 748 candles, 2026-08-17 03:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- SOL: live 748 candles, 2026-08-17 03:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.0 bps
- ADA: live 748 candles, 2026-08-17 03:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 3.8 bps
- AVAX: live 748 candles, 2026-08-17 03:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LINK: live 748 candles, 2026-08-17 03:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 3.1 bps
- XRP: live 720 candles, 2026-08-18 07:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- DOGE: live 720 candles, 2026-08-18 07:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.0 bps
- DOT: live 720 candles, 2026-08-18 07:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 3.0 bps
- LTC: live 720 candles, 2026-08-18 07:00Z to 2026-09-17 06:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.9 bps
