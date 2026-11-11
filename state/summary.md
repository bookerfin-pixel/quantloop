# quantloop summary — generated 2026-11-11 15:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168 (2 of them replayed after a missed run)
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-04 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 56.4 of 60, 3.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.77% (max drawdown -36.89%, 441 fills) vs challenger1 -8.85% (max drawdown -15.05%, 153 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -16.86% (usual 0.54, this window 0.47) vs challenger1 -6.15% (usual 0.37, this window 0.54); the rule compares on skill, daily edge t +0.71 over 56 days
  trades: its 46 finished trades made -4.34% of its starting equity after costs (29 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.71 over 56 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.10%, equal weight basket of 10 pairs -7.26%, basket max drawdown -29%, basket realised vol 57% annualised
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 36.7 of 60, 23.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -28.69% (max drawdown -29.26%, 252 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -13.95% (usual 0.55, this window 0.34) vs challenger3 -0.52% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.41 over 37 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.40 over 37 days)
  fills: 10 in 36.7 days, 8 of them in the hour it began; at this pace about 14 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -14.48%, equal weight basket of 10 pairs -26.86%, basket max drawdown -29%, basket realised vol 56% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 26.7 of 120, 93.3 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -12.84% (max drawdown -17.91%, 42 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -3.24% (usual 0.53, this window 0.87); the rule compares on skill, daily edge t -0.39 over 27 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -21.33% so far
  trades: its 13 finished trades made -8.65% of its starting equity after costs (2 won, 11 lost, 11 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.39 over 27 days)
  market over the window: BTC -10.73%, equal weight basket of 10 pairs -18.18%, basket max drawdown -21%, basket realised vol 54% annualised
- free slots: challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,923.31 (started 10,000 at 2026-09-16 03:55Z), net -20.77% since start
- 24h +0.35%, 7d -8.06%, 30d -24.40%, max drawdown -36.89%
- fills 441 total, 31 in the last 7d
- costs 957.52 (fees 633.28 + slippage 324.24); gross pnl -1,119.17; cost coverage -1.17
- cash 5,920.00; positions: AVAX 234.937
- last run 2026-11-11 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-11 14:09Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.16% not above entry band +1.0%
- 2026-11-11 14:09Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.16% not above entry band +1.0%
- 2026-11-11 14:09Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +4.85% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-11-11 14:09Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.19% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 14:09Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.53% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 14:09Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.06% not above entry band +1.0%
- 2026-11-11 14:09Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.01% not above entry band +1.0%
- 2026-11-11 14:09Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.89% not above entry band +1.0%
- 2026-11-11 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.23% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 15:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.13% not above entry band +1.0%
- 2026-11-11 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.05% not above entry band +1.0%
- 2026-11-11 15:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +3.98% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-11 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.71% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.88% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.48% not above entry band +1.0% and price below 24h EMA
- 2026-11-11 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.79% not above entry band +1.0%
- 2026-11-11 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.18% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 36 fills (16 buy / 20 sell), traded 45,961, gross pnl -172.72, -75 bps per round trip, avg half spread 2.2 bps
- AVAX: 55 fills (26 buy / 29 sell), traded 91,086, gross pnl +63.62, +14 bps per round trip, avg half spread 1.6 bps, open 234.937
- BTC: 43 fills (24 buy / 19 sell), traded 60,178, gross pnl -158.33, -53 bps per round trip, avg half spread 0.1 bps
- DOGE: 39 fills (19 buy / 20 sell), traded 49,043, gross pnl -313.08, -128 bps per round trip, avg half spread 1.0 bps
- DOT: 47 fills (22 buy / 25 sell), traded 69,133, gross pnl -174.48, -50 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 49 fills (25 buy / 24 sell), traded 81,140, gross pnl -448.58, -111 bps per round trip, avg half spread 2.1 bps
- LTC: 45 fills (21 buy / 24 sell), traded 60,527, gross pnl +373.93, +124 bps per round trip, avg half spread 1.6 bps
- SOL: 40 fills (21 buy / 19 sell), traded 60,786, gross pnl -147.60, -49 bps per round trip, avg half spread 0.5 bps
- XRP: 43 fills (21 buy / 22 sell), traded 57,249, gross pnl -5.63, -2 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-11-05 15:10Z sell LTC 889 @ 53.1884 fee 0.89 slip 0.44 (half spread 2.8 bps)
- 2026-11-05 15:10Z buy BTC 1,100 @ 77074.5 fee 1.10 slip 0.55 (half spread 0.0 bps)
- 2026-11-05 15:10Z buy XRP 1,100 @ 1.26162 fee 1.10 slip 0.55 (half spread 2.3 bps)
- 2026-11-05 16:10Z sell BTC 1,975 @ 75762.1 fee 1.97 slip 0.99 (half spread 0.0 bps)
- 2026-11-05 16:10Z sell XRP 1,985 @ 1.24647 fee 1.98 slip 0.99 (half spread 0.0 bps)
- 2026-11-09 13:10Z buy AVAX 1,990 @ 8.57571 fee 1.99 slip 1.44 (half spread 5.3 bps)
- 2026-11-10 11:10Z sell AVAX 1,929 @ 8.31184 fee 1.93 slip 0.97 (half spread 1.2 bps)
- 2026-11-11 00:10Z buy AVAX 1,974 @ 8.4022 fee 1.97 slip 0.99 (half spread 1.2 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,105.07 (started 10,000 at 2026-09-16 03:55Z), net -8.95% since start
- 24h +1.17%, 7d -4.90%, 30d -7.21%, max drawdown -15.05%
- fills 153 total, 23 in the last 7d
- costs 289.55 (fees 189.98 + slippage 99.56); gross pnl -605.39; cost coverage -2.09
- cash 987.18; positions: ADA 5226.63, BTC 0.0122833, DOGE 13255.7, DOT 1063.05, ETH 0.430747, LINK 88.4303, LTC 18.2152, SOL 10.5703, XRP 813.358
- last run 2026-11-11 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-11 14:09Z SOL hold target 0.11 (held 0.10) — hold: weight change +0.013 below threshold 0.05 | stay long: z -1.49 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-11-11 14:09Z ADA hold target 0.11 (held 0.10) — hold: weight change +0.010 below threshold 0.05 | stay long: z -1.02 vs 240h mean (entry -2.0, exit -0.5); vol 76% -> weight 0.25
- 2026-11-11 14:09Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.57 not below -2.0
- 2026-11-11 14:09Z LINK hold target 0.11 (held 0.10) — hold: weight change +0.011 below threshold 0.05 | stay long: z -1.45 vs 240h mean (entry -2.0, exit -0.5); vol 75% -> weight 0.25
- 2026-11-11 14:09Z XRP hold target 0.11 (held 0.09) — hold: weight change +0.017 below threshold 0.05 | stay long: z -1.61 vs 240h mean (entry -2.0, exit -0.5); vol 66% -> weight 0.25
- 2026-11-11 14:09Z DOGE hold target 0.11 (held 0.10) — hold: weight change +0.012 below threshold 0.05 | stay long: z -1.52 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-11-11 14:09Z DOT hold target 0.11 (held 0.10) — hold: weight change +0.010 below threshold 0.05 | stay long: z -1.12 vs 240h mean (entry -2.0, exit -0.5); vol 77% -> weight 0.25
- 2026-11-11 14:09Z LTC hold target 0.11 (held 0.10) — hold: weight change +0.009 below threshold 0.05 | stay long: z -0.96 vs 240h mean (entry -2.0, exit -0.5); vol 66% -> weight 0.25
- 2026-11-11 15:10Z BTC hold target 0.11 (held 0.10) — hold: weight change +0.012 below threshold 0.05 | stay long: z -1.53 vs 240h mean (entry -2.0, exit -0.5); vol 43% -> weight 0.25
- 2026-11-11 15:10Z ETH hold target 0.11 (held 0.10) — hold: weight change +0.014 below threshold 0.05 | stay long: z -1.76 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25
- 2026-11-11 15:10Z SOL hold target 0.11 (held 0.10) — hold: weight change +0.014 below threshold 0.05 | stay long: z -1.62 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-11-11 15:10Z ADA hold target 0.11 (held 0.10) — hold: weight change +0.010 below threshold 0.05 | stay long: z -1.10 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-11-11 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.45 not below -2.0
- 2026-11-11 15:10Z LINK hold target 0.11 (held 0.10) — hold: weight change +0.011 below threshold 0.05 | stay long: z -1.54 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-11-11 15:10Z XRP hold target 0.11 (held 0.09) — hold: weight change +0.017 below threshold 0.05 | stay long: z -1.64 vs 240h mean (entry -2.0, exit -0.5); vol 63% -> weight 0.25
- 2026-11-11 15:10Z DOGE hold target 0.11 (held 0.10) — hold: weight change +0.012 below threshold 0.05 | stay long: z -1.56 vs 240h mean (entry -2.0, exit -0.5); vol 62% -> weight 0.25
- 2026-11-11 15:10Z DOT hold target 0.11 (held 0.10) — hold: weight change +0.010 below threshold 0.05 | stay long: z -1.16 vs 240h mean (entry -2.0, exit -0.5); vol 75% -> weight 0.25
- 2026-11-11 15:10Z LTC hold target 0.11 (held 0.10) — hold: weight change +0.009 below threshold 0.05 | stay long: z -1.07 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 14 fills (7 buy / 7 sell), traded 17,768, gross pnl -83.49, -94 bps per round trip, avg half spread 2.2 bps, open 5226.63
- AVAX: 17 fills (9 buy / 8 sell), traded 20,029, gross pnl +155.71, +155 bps per round trip, avg half spread 1.8 bps
- BTC: 11 fills (7 buy / 4 sell), traded 14,145, gross pnl +66.59, +94 bps per round trip, avg half spread 0.1 bps, open 0.0122833
- DOGE: 17 fills (9 buy / 8 sell), traded 23,156, gross pnl -164.89, -142 bps per round trip, avg half spread 0.9 bps, open 13255.7
- DOT: 12 fills (6 buy / 6 sell), traded 14,947, gross pnl -458.33, -613 bps per round trip, avg half spread 3.2 bps, open 1063.05
- ETH: 16 fills (8 buy / 8 sell), traded 22,188, gross pnl +95.32, +86 bps per round trip, avg half spread 0.4 bps, open 0.430747
- LINK: 19 fills (11 buy / 8 sell), traded 21,160, gross pnl +162.90, +154 bps per round trip, avg half spread 2.1 bps, open 88.4303
- LTC: 17 fills (9 buy / 8 sell), traded 20,048, gross pnl +29.82, +30 bps per round trip, avg half spread 1.4 bps, open 18.2152
- SOL: 17 fills (11 buy / 6 sell), traded 22,622, gross pnl -140.93, -125 bps per round trip, avg half spread 0.6 bps, open 10.5703
- XRP: 13 fills (7 buy / 6 sell), traded 13,921, gross pnl -268.09, -385 bps per round trip, avg half spread 0.8 bps, open 813.358

last fills:

- 2026-11-08 22:10Z sell DOGE 612 @ 0.0688335 fee 0.61 slip 0.33 (half spread 3.3 bps)
- 2026-11-08 22:10Z sell DOT 596 @ 0.857728 fee 0.60 slip 0.57 (half spread 7.6 bps)
- 2026-11-08 22:10Z sell LTC 609 @ 50.0949 fee 0.61 slip 0.30 (half spread 2.0 bps)
- 2026-11-08 22:10Z buy BTC 913 @ 74349.1 fee 0.91 slip 0.46 (half spread 0.0 bps)
- 2026-11-08 22:10Z buy ETH 913 @ 2120.15 fee 0.91 slip 0.46 (half spread 1.4 bps)
- 2026-11-08 22:10Z buy SOL 913 @ 86.3982 fee 0.91 slip 0.46 (half spread 1.7 bps)
- 2026-11-08 22:10Z buy XRP 906 @ 1.11384 fee 0.91 slip 0.45 (half spread 2.0 bps)
- 2026-11-09 13:10Z sell AVAX 988 @ 8.56329 fee 0.99 slip 0.72 (half spread 5.3 bps)

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-11 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-11 14:09Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 14:09Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-11 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-11 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-11 14:09Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 81.86 not a higher low vs prior low 93.78 (need +10.0%)
- 2026-11-11 14:09Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1722 not a higher low vs prior low 0.1868 (need +10.0%)
- 2026-11-11 14:09Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.826 not a higher low vs prior low 8.186 (need +10.0%)
- 2026-11-11 14:09Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.19 not a higher low vs prior low 10.49 (need +10.0%)
- 2026-11-11 14:09Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.041 not a higher low vs prior low 1.207 (need +10.0%)
- 2026-11-11 14:09Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.06702 not a higher low vs prior low 0.07388 (need +10.0%)
- 2026-11-11 14:09Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8329 not a higher low vs prior low 0.8971 (need +10.0%)
- 2026-11-11 14:09Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 49.8 not a higher low vs prior low 54.24 (need +10.0%)
- 2026-11-11 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.281e+04 not a higher low vs prior low 7.65e+04 (need +10.0%)
- 2026-11-11 15:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2017 not a higher low vs prior low 2191 (need +10.0%)
- 2026-11-11 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 81.86 not a higher low vs prior low 93.78 (need +10.0%)
- 2026-11-11 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1722 not a higher low vs prior low 0.1868 (need +10.0%)
- 2026-11-11 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.826 not a higher low vs prior low 8.186 (need +10.0%)
- 2026-11-11 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.19 not a higher low vs prior low 10.49 (need +10.0%)
- 2026-11-11 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.041 not a higher low vs prior low 1.207 (need +10.0%)
- 2026-11-11 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.06702 not a higher low vs prior low 0.07388 (need +10.0%)
- 2026-11-11 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8329 not a higher low vs prior low 0.8971 (need +10.0%)
- 2026-11-11 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 49.8 not a higher low vs prior low 54.24 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 4 fills (2 buy / 2 sell), traded 7,389, gross pnl -111.53, -302 bps per round trip, avg half spread 0.7 bps
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)
- 2026-10-06 15:25Z buy AVAX 2,503 @ 11.5663 fee 2.50 slip 1.25 (half spread 0.4 bps)
- 2026-10-07 22:22Z sell AVAX 2,381 @ 11.0025 fee 2.38 slip 1.19 (half spread 0.9 bps)

## challenger4: relative_reversion (H6)

params: {"entry_z": 2.0, "exit_z": 0.25, "max_weight": 0.25, "ratio_hours": 720, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,712.61 (started 10,000 at 2026-10-13 17:26Z), net -12.87% since start
- 24h +1.32%, 7d -12.32%, 30d -12.87%, max drawdown -17.91%
- fills 42 total, 12 in the last 7d
- costs 97.82 (fees 62.42 + slippage 35.40); gross pnl -1,189.58; cost coverage -12.16
- cash -0.00; positions: DOGE 25813.1, ETH 0.466071, LTC 35.5795, SOL 25.4938, XRP 1943.04
- last run 2026-11-11 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-11 14:09Z SOL hold target 0.20 (held 0.25) — hold: weight change -0.046 below threshold 0.05 | stay long: ratio to BTC z -2.03 vs 720h mean (entry -2.0, exit -0.25); vol 65% -> weigh...
- 2026-11-11 14:09Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.11 not below -2.0
- 2026-11-11 14:09Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.49 not below -2.0
- 2026-11-11 14:09Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.25 not below -2.0
- 2026-11-11 14:09Z XRP hold target 0.20 (held 0.23) — hold: weight change -0.035 below threshold 0.05 | stay long: ratio to BTC z -3.07 vs 720h mean (entry -2.0, exit -0.25); vol 66% -> weigh...
- 2026-11-11 14:09Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -2.03 vs 720h mean (entry -2.0, exit -0.25); vol 65% -> weigh...
- 2026-11-11 14:09Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.20 not below -2.0
- 2026-11-11 14:09Z LTC hold target 0.20 (held 0.21) — hold: weight change -0.009 below threshold 0.05 | stay long: ratio to BTC z -0.98 vs 720h mean (entry -2.0, exit -0.25); vol 66% -> weigh...
- 2026-11-11 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-11 15:10Z ETH none target 0.20 (held 0.11) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-11-11 15:10Z SOL hold target 0.20 (held 0.24) — hold: weight change -0.045 below threshold 0.05 | stay long: ratio to BTC z -2.11 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-11-11 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.12 not below -2.0
- 2026-11-11 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.49 not below -2.0
- 2026-11-11 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.27 not below -2.0
- 2026-11-11 15:10Z XRP hold target 0.20 (held 0.24) — hold: weight change -0.036 below threshold 0.05 | stay long: ratio to BTC z -3.06 vs 720h mean (entry -2.0, exit -0.25); vol 63% -> weigh...
- 2026-11-11 15:10Z DOGE hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.99 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-11-11 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.19 not below -2.0
- 2026-11-11 15:10Z LTC hold target 0.20 (held 0.21) — hold: weight change -0.008 below threshold 0.05 | stay long: ratio to BTC z -1.02 vs 720h mean (entry -2.0, exit -0.25); vol 64% -> weigh...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 5 fills (2 buy / 3 sell), traded 7,535, gross pnl -167.98, -446 bps per round trip, avg half spread 1.9 bps, open 25813.1
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 5 fills (2 buy / 3 sell), traded 5,853, gross pnl -183.63, -628 bps per round trip, avg half spread 0.9 bps, open 0.466071
- LINK: 2 fills (1 buy / 1 sell), traded 4,797, gross pnl +245.83, +1025 bps per round trip, avg half spread 2.6 bps
- LTC: 2 fills (1 buy / 1 sell), traded 2,682, gross pnl +30.74, +229 bps per round trip, avg half spread 1.5 bps, open 35.5795
- SOL: 7 fills (3 buy / 4 sell), traded 11,735, gross pnl -285.50, -487 bps per round trip, avg half spread 0.9 bps, open 25.4938
- XRP: 5 fills (2 buy / 3 sell), traded 7,173, gross pnl -320.90, -895 bps per round trip, avg half spread 1.4 bps, open 1943.04

last fills:

- 2026-11-05 23:10Z sell DOT 2,257 @ 0.89712 fee 2.26 slip 1.96 (half spread 6.7 bps)
- 2026-11-06 00:10Z buy SOL 2,284 @ 89.5798 fee 2.28 slip 1.14 (half spread 0.6 bps)
- 2026-11-06 21:10Z buy XRP 2,285 @ 1.17624 fee 2.29 slip 1.14 (half spread 0.0 bps)
- 2026-11-08 22:10Z buy DOGE 2,231 @ 0.0689068 fee 2.23 slip 1.19 (half spread 3.3 bps)
- 2026-11-08 22:10Z buy LTC 2,231 @ 50.1451 fee 2.23 slip 1.12 (half spread 2.0 bps)
- 2026-11-08 23:10Z sell DOGE 457 @ 0.0695648 fee 0.46 slip 0.23 (half spread 2.0 bps)
- 2026-11-08 23:10Z sell LTC 450 @ 50.4698 fee 0.45 slip 0.23 (half spread 1.0 bps)
- 2026-11-08 23:10Z buy ETH 999 @ 2143.75 fee 1.00 slip 0.50 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 2076 candles, 2026-08-17 03:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 2076 candles, 2026-08-17 03:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 2076 candles, 2026-08-17 03:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 2076 candles, 2026-08-17 03:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- AVAX: live 2076 candles, 2026-08-17 03:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LINK: live 2076 candles, 2026-08-17 03:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 2048 candles, 2026-08-18 07:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.3 bps
- DOGE: live 2048 candles, 2026-08-18 07:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 2048 candles, 2026-08-18 07:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.6 bps
- LTC: live 2048 candles, 2026-08-18 07:00Z to 2026-11-11 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
