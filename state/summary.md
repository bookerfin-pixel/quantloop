# quantloop summary — generated 2026-09-20 13:21Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 4.3 of 60, 55.7 days until the verdict
  so far: champion +9.82% (DD -3.54%, 28 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +6.01%, equal weight basket of 10 pairs +13.11%, basket max drawdown -4%, basket realised vol 52% annualised
- challenger2: testing H2 since 2026-09-20 13:21Z, day 0.0 of 60, 60.0 days until the verdict
  so far: champion +0.00% (DD 0.00%, 0 fills) vs challenger2 +0.00% (DD 0.00%, 4 fills)
  market over the window: no candle data for the window
- challenger3: idle (free for a hypothesis)
- free slots: challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,982.16 (started 10,000 at 2026-09-16 03:55Z), net +9.82% since start
- 24h +0.29%, 7d +9.82%, 30d +9.82%, max drawdown -3.54%
- fills 28 total, 28 in the last 7d
- costs 62.52 (fees 41.24 + slippage 21.27); gross pnl 1,044.68; cost coverage 16.71
- cash 10.51; positions: AVAX 279.519, BTC 0.0333537, ETH 1.03803, LTC 46.9242
- last run 2026-09-20 13:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.015 below threshold 0.05 | stay long: 72h return +37.88% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +8.21% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z BTC hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +4.96% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +4.95% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z AVAX hold target 0.25 (held 0.27) — hold: weight change -0.018 below threshold 0.05 | stay long: 72h return +36.28% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 13:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.007 below threshold 0.05 | stay long: 72h return +8.32% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +637.82, +1173 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 2 fills (2 buy / 0 sell), traded 2,697, gross pnl -12.19, -90 bps per round trip, avg half spread 0.0 bps, open 0.0333537
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 2 fills (2 buy / 0 sell), traded 2,687, gross pnl -9.44, -70 bps per round trip, avg half spread 0.0 bps, open 1.03803
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +81.42, +342 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-20 13:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.30 not below -2.0
- 2026-09-20 12:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.61 not below -2.0
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.12 not below -2.0
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.46 not below -2.0
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.49 not below -2.0
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.86 not below -2.0
- 2026-09-20 12:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.59 not below -2.0
- 2026-09-20 13:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.52 not below -2.0
- 2026-09-20 13:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.06 not below -2.0
- 2026-09-20 13:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.22 not below -2.0
- 2026-09-20 13:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.38 not below -2.0
- 2026-09-20 13:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.45 not below -2.0
- 2026-09-20 13:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.16 not below -2.0
- 2026-09-20 13:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.46 not below -2.0
- 2026-09-20 13:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.50 not below -2.0
- 2026-09-20 13:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.84 not below -2.0
- 2026-09-20 13:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.56 not below -2.0

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

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,965.71 (started 10,000 at 2026-09-16 23:20Z), net +9.66% since start
- 24h +0.14%, 7d +9.66%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 32 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-20 13:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.015 below threshold 0.05 | stay long: 72h return +37.88% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +8.21% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z BTC sell target 0.00 (held 0.24) — flat: only 826 candles, need 1610
- 2026-09-20 13:21Z ETH sell target 0.00 (held 0.24) — flat: only 826 candles, need 1610
- 2026-09-20 13:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 826 candles, need 1610
- 2026-09-20 13:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 826 candles, need 1610
- 2026-09-20 13:21Z AVAX sell target 0.00 (held 0.27) — flat: only 826 candles, need 1610
- 2026-09-20 13:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 826 candles, need 1610
- 2026-09-20 13:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 798 candles, need 1610
- 2026-09-20 13:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 798 candles, need 1610
- 2026-09-20 13:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 798 candles, need 1610
- 2026-09-20 13:21Z LTC sell target 0.00 (held 0.24) — flat: only 798 candles, need 1610

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 3 fills (2 buy / 1 sell), traded 5,380, gross pnl -12.20, -45 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 3 fills (2 buy / 1 sell), traded 5,361, gross pnl -9.44, -35 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,982.16 (started 10,000 at 2026-09-16 23:20Z), net +9.82% since start
- 24h +0.29%, 7d +9.82%, 30d +9.82%, max drawdown -3.54%
- fills 28 total, 28 in the last 7d
- costs 62.52 (fees 41.24 + slippage 21.27); gross pnl 1,044.68; cost coverage 16.71
- cash 10.51; positions: AVAX 279.519, BTC 0.0333537, ETH 1.03803, LTC 46.9242
- last run 2026-09-20 13:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.015 below threshold 0.05 | stay long: 72h return +37.88% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +8.21% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z BTC hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +4.96% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +4.95% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 13:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z AVAX hold target 0.25 (held 0.27) — hold: weight change -0.018 below threshold 0.05 | stay long: 72h return +36.28% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 13:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 13:21Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.007 below threshold 0.05 | stay long: 72h return +8.32% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +637.82, +1173 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 2 fills (2 buy / 0 sell), traded 2,697, gross pnl -12.19, -90 bps per round trip, avg half spread 0.0 bps, open 0.0333537
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 2 fills (2 buy / 0 sell), traded 2,687, gross pnl -9.44, -70 bps per round trip, avg half spread 0.0 bps, open 1.03803
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +81.42, +342 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 826 candles, 2026-08-17 03:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 826 candles, 2026-08-17 03:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 826 candles, 2026-08-17 03:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 826 candles, 2026-08-17 03:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- AVAX: live 826 candles, 2026-08-17 03:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.5 bps
- LINK: live 826 candles, 2026-08-17 03:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 798 candles, 2026-08-18 07:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 798 candles, 2026-08-18 07:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 798 candles, 2026-08-18 07:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 798 candles, 2026-08-18 07:00Z to 2026-09-20 12:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.7 bps
