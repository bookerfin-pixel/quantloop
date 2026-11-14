# quantloop summary — generated 2026-11-14 05:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168 (2 of them replayed after a missed run)
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-07 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: idle, holds cash (free for a hypothesis)
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 39.3 of 60, 20.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -29.78% (max drawdown -30.08%, 255 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.16% (usual 0.55, this window 0.33) vs challenger3 -0.37% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.96 over 39 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.21 over 39 days)
  fills: 10 in 39.3 days, 8 of them in the hour it began; at this pace about 14 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -22.01%, equal weight basket of 10 pairs -32.10%, basket max drawdown -33%, basket realised vol 56% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 29.3 of 120, 90.7 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -19.29% (max drawdown -22.84%, 53 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -6.60% (usual 0.53, this window 0.88); the rule compares on skill, daily edge t -0.83 over 29 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -25.82% so far
  trades: its 15 finished trades made -9.09% of its starting equity after costs (2 won, 13 lost, 11 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.83 over 29 days)
  market over the window: BTC -18.59%, equal weight basket of 10 pairs -24.03%, basket max drawdown -26%, basket realised vol 54% annualised
- free slots: challenger1, challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,802.19 (started 10,000 at 2026-09-16 03:55Z), net -21.98% since start
- 24h -0.82%, 7d -2.00%, 30d -22.53%, max drawdown -37.62%
- fills 444 total, 6 in the last 7d
- costs 966.25 (fees 639.10 + slippage 327.15); gross pnl -1,231.56; cost coverage -1.27
- cash 7,802.19; positions: none
- last run 2026-11-14 05:10Z; halted today: False

last decisions (newest last):

- 2026-11-14 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.89% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.77% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.62% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.09% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.40% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.44% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.53% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.40% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.99% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.99% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.75% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.14% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.97% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.20% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.55% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.57% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.90% not above entry band +1.0% and price below 24h EMA
- 2026-11-14 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.47% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 36 fills (16 buy / 20 sell), traded 45,961, gross pnl -172.72, -75 bps per round trip, avg half spread 2.2 bps
- AVAX: 58 fills (27 buy / 31 sell), traded 96,907, gross pnl -48.77, -10 bps per round trip, avg half spread 1.6 bps
- BTC: 43 fills (24 buy / 19 sell), traded 60,178, gross pnl -158.33, -53 bps per round trip, avg half spread 0.1 bps
- DOGE: 39 fills (19 buy / 20 sell), traded 49,043, gross pnl -313.08, -128 bps per round trip, avg half spread 1.0 bps
- DOT: 47 fills (22 buy / 25 sell), traded 69,133, gross pnl -174.48, -50 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 49 fills (25 buy / 24 sell), traded 81,140, gross pnl -448.58, -111 bps per round trip, avg half spread 2.1 bps
- LTC: 45 fills (21 buy / 24 sell), traded 60,527, gross pnl +373.93, +124 bps per round trip, avg half spread 1.6 bps
- SOL: 40 fills (21 buy / 19 sell), traded 60,786, gross pnl -147.60, -49 bps per round trip, avg half spread 0.5 bps
- XRP: 43 fills (21 buy / 22 sell), traded 57,249, gross pnl -5.63, -2 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-11-05 16:10Z sell BTC 1,975 @ 75762.1 fee 1.97 slip 0.99 (half spread 0.0 bps)
- 2026-11-05 16:10Z sell XRP 1,985 @ 1.24647 fee 1.98 slip 0.99 (half spread 0.0 bps)
- 2026-11-09 13:10Z buy AVAX 1,990 @ 8.57571 fee 1.99 slip 1.44 (half spread 5.3 bps)
- 2026-11-10 11:10Z sell AVAX 1,929 @ 8.31184 fee 1.93 slip 0.97 (half spread 1.2 bps)
- 2026-11-11 00:10Z buy AVAX 1,974 @ 8.4022 fee 1.97 slip 0.99 (half spread 1.2 bps)
- 2026-11-12 14:10Z sell AVAX 1,949 @ 8.29485 fee 1.95 slip 0.97 (half spread 2.4 bps)
- 2026-11-13 11:10Z buy AVAX 1,967 @ 8.4092 fee 1.97 slip 0.98 (half spread 2.4 bps)
- 2026-11-13 23:10Z sell AVAX 1,906 @ 8.14942 fee 1.91 slip 0.95 (half spread 1.8 bps)

## challenger1: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-14 05:10Z), net +0.00% since start
- 24h n/a, 7d n/a, 30d n/a, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-14 05:10Z; halted today: False

last decisions (newest last):

- 2026-11-14 05:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-14 05:10Z; halted today: False

last decisions (newest last):

- 2026-11-14 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-14 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-14 05:10Z; halted today: False

last decisions (newest last):

- 2026-11-14 04:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 76.14 not a higher low vs prior low 90.75 (need +10.0%)
- 2026-11-14 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1652 not a higher low vs prior low 0.1849 (need +10.0%)
- 2026-11-14 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.826 not a higher low vs prior low 8.186 (need +10.0%)
- 2026-11-14 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.678 not a higher low vs prior low 10.49 (need +10.0%)
- 2026-11-14 04:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.003 not a higher low vs prior low 1.207 (need +10.0%)
- 2026-11-14 04:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.06322 not a higher low vs prior low 0.07307 (need +10.0%)
- 2026-11-14 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.7975 not a higher low vs prior low 0.8971 (need +10.0%)
- 2026-11-14 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 47.79 not a higher low vs prior low 52.57 (need +10.0%)
- 2026-11-14 05:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.668e+04 not a higher low vs prior low 7.604e+04 (need +10.0%)
- 2026-11-14 05:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1882 not a higher low vs prior low 2191 (need +10.0%)
- 2026-11-14 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 75 not a higher low vs prior low 90.75 (need +10.0%)
- 2026-11-14 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1632 not a higher low vs prior low 0.1849 (need +10.0%)
- 2026-11-14 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.826 not a higher low vs prior low 8.186 (need +10.0%)
- 2026-11-14 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 9.538 not a higher low vs prior low 10.49 (need +10.0%)
- 2026-11-14 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9896 not a higher low vs prior low 1.207 (need +10.0%)
- 2026-11-14 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.06253 not a higher low vs prior low 0.07307 (need +10.0%)
- 2026-11-14 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.7898 not a higher low vs prior low 0.8971 (need +10.0%)
- 2026-11-14 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 47.79 not a higher low vs prior low 52.57 (need +10.0%)

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

- equity 8,068.29 (started 10,000 at 2026-10-13 17:26Z), net -19.32% since start
- 24h -2.29%, 7d -11.48%, 30d -19.32%, max drawdown -22.84%
- fills 53 total, 16 in the last 7d
- costs 112.02 (fees 71.89 + slippage 40.13); gross pnl -1,819.69; cost coverage -16.24
- cash -0.00; positions: DOGE 32333.7, ETH 1.07957, SOL 26.1167, XRP 2029.53
- last run 2026-11-14 05:10Z; halted today: False

last decisions (newest last):

- 2026-11-14 04:10Z SOL hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: ratio to BTC z -2.05 vs 720h mean (entry -2.0, exit -0.25); vol 61% -> weigh...
- 2026-11-14 04:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.66 not below -2.0
- 2026-11-14 04:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +1.67 not below -2.0
- 2026-11-14 04:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.45 not below -2.0
- 2026-11-14 04:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.47 vs 720h mean (entry -2.0, exit -0.25); vol 61% -> weigh...
- 2026-11-14 04:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.17 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-11-14 04:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.89 not below -2.0
- 2026-11-14 04:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.96 not below -2.0
- 2026-11-14 05:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-14 05:10Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: ratio to BTC z -1.48 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-11-14 05:10Z SOL hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: ratio to BTC z -2.01 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-11-14 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.67 not below -2.0
- 2026-11-14 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +1.70 not below -2.0
- 2026-11-14 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.35 not below -2.0
- 2026-11-14 05:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.46 vs 720h mean (entry -2.0, exit -0.25); vol 61% -> weigh...
- 2026-11-14 05:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.10 vs 720h mean (entry -2.0, exit -0.25); vol 62% -> weigh...
- 2026-11-14 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.88 not below -2.0
- 2026-11-14 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +1.03 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 6 fills (3 buy / 3 sell), traded 7,955, gross pnl -311.17, -782 bps per round trip, avg half spread 1.6 bps, open 32333.7
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 7 fills (4 buy / 3 sell), traded 7,069, gross pnl -308.44, -873 bps per round trip, avg half spread 0.6 bps, open 1.07957
- LINK: 5 fills (3 buy / 2 sell), traded 8,173, gross pnl +207.92, +509 bps per round trip, avg half spread 2.0 bps
- LTC: 3 fills (1 buy / 2 sell), traded 4,467, gross pnl +6.37, +29 bps per round trip, avg half spread 1.3 bps
- SOL: 9 fills (4 buy / 5 sell), traded 13,128, gross pnl -474.99, -724 bps per round trip, avg half spread 0.9 bps, open 26.1167
- XRP: 7 fills (3 buy / 4 sell), traded 8,453, gross pnl -431.25, -1020 bps per round trip, avg half spread 1.0 bps, open 2029.53

last fills:

- 2026-11-12 02:10Z buy LINK 802 @ 10.1615 fee 0.80 slip 0.40 (half spread 1.4 bps)
- 2026-11-13 01:10Z sell LTC 1,785 @ 50.1799 fee 1.79 slip 0.89 (half spread 1.0 bps)
- 2026-11-13 01:10Z buy LINK 906 @ 10.1059 fee 0.91 slip 0.45 (half spread 2.0 bps)
- 2026-11-13 08:10Z sell LINK 1,668 @ 9.89698 fee 1.67 slip 0.83 (half spread 1.4 bps)
- 2026-11-13 08:10Z buy ETH 734 @ 1935.69 fee 0.73 slip 0.37 (half spread 0.0 bps)
- 2026-11-13 08:10Z buy SOL 708 @ 80.015 fee 0.71 slip 0.35 (half spread 0.6 bps)
- 2026-11-13 08:10Z buy XRP 679 @ 1.02967 fee 0.68 slip 0.34 (half spread 0.0 bps)
- 2026-11-13 08:10Z buy DOGE 420 @ 0.0644784 fee 0.42 slip 0.21 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 2138 candles, 2026-08-17 03:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 2138 candles, 2026-08-17 03:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 2138 candles, 2026-08-17 03:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.7 bps
- ADA: live 2138 candles, 2026-08-17 03:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- AVAX: live 2138 candles, 2026-08-17 03:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LINK: live 2138 candles, 2026-08-17 03:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 2110 candles, 2026-08-18 07:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.3 bps
- DOGE: live 2110 candles, 2026-08-18 07:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- DOT: live 2110 candles, 2026-08-18 07:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 2110 candles, 2026-08-18 07:00Z to 2026-11-14 04:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
