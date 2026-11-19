# quantloop summary — generated 2026-11-19 10:11Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-12 (today and the 7 UTC days before it): no buy stopped by the cap and no pair that filled 4 times or more in one UTC day, in any account read (the cap is 4 fills in one pair in one UTC day)

## Challenger slots

- challenger1: idle, holds cash (free for a hypothesis)
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 44.5 of 60, 15.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -30.50% (max drawdown -31.25%, 288 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.68% (usual 0.55, this window 0.32) vs challenger3 -0.26% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.32 over 44 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.06 over 44 days)
  fills: 10 in 44.5 days, 8 of them in the hour it began; at this pace about 13 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -25.77%, equal weight basket of 10 pairs -36.11%, basket max drawdown -40%, basket realised vol 59% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 34.5 of 120, 85.5 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -18.31% (max drawdown -27.00%, 62 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -3.27% (usual 0.53, this window 0.88); the rule compares on skill, daily edge t -0.28 over 34 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -33.33% so far
  trades: its 20 finished trades made -20.57% of its starting equity after costs (3 won, 17 lost, 15 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.28 over 34 days)
  market over the window: BTC -22.52%, equal weight basket of 10 pairs -28.49%, basket max drawdown -33%, basket realised vol 58% annualised
- free slots: challenger1, challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,722.23 (started 10,000 at 2026-09-16 03:55Z), net -22.78% since start
- 24h -0.87%, 7d -2.52%, 30d -19.39%, max drawdown -38.66%
- fills 477 total, 36 in the last 7d
- costs 1,015.74 (fees 672.09 + slippage 343.66); gross pnl -1,262.03; cost coverage -1.24
- cash 0.00; positions: ADA 10050.1, DOGE 25909.1, LINK 168.139, SOL 20.7751, XRP 1571.21
- last run 2026-11-19 10:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 09:10Z SOL sell target 0.20 (held 0.25) — stay long: 72h return +5.20% vs exit band -1.0% and price above 24h EMA; realised vol 83% -> weight 0.25
- 2026-11-19 09:10Z ADA buy target 0.20 (held 0.00) — enter long: 72h return +1.21% vs entry band +1.0% and price above 24h EMA; realised vol 82% -> weight 0.25
- 2026-11-19 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.95% not above entry band +1.0%
- 2026-11-19 09:10Z LINK buy target 0.20 (held 0.00) — enter long: 72h return +1.04% vs entry band +1.0% and price above 24h EMA; realised vol 79% -> weight 0.25
- 2026-11-19 09:10Z XRP sell target 0.20 (held 0.25) — stay long: 72h return +3.34% vs exit band -1.0% and price above 24h EMA; realised vol 78% -> weight 0.25
- 2026-11-19 09:10Z DOGE buy target 0.20 (held 0.00) — enter long: 72h return +1.63% vs entry band +1.0% and price above 24h EMA; realised vol 81% -> weight 0.25
- 2026-11-19 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.28% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.52% not above entry band +1.0%
- 2026-11-19 10:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.75% not above entry band +1.0%
- 2026-11-19 10:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.49% not above entry band +1.0%
- 2026-11-19 10:10Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +5.21% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-19 10:10Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +1.79% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-19 10:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.34% not above entry band +1.0%
- 2026-11-19 10:10Z LINK hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +1.45% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-19 10:10Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +4.52% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-19 10:10Z DOGE hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +2.11% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-19 10:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.12% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 10:10Z LTC none target 0.17 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 41 fills (19 buy / 22 sell), traded 51,536, gross pnl -175.78, -68 bps per round trip, avg half spread 2.1 bps, open 10050.1
- AVAX: 58 fills (27 buy / 31 sell), traded 96,907, gross pnl -48.77, -10 bps per round trip, avg half spread 1.6 bps
- BTC: 43 fills (24 buy / 19 sell), traded 60,178, gross pnl -158.33, -53 bps per round trip, avg half spread 0.1 bps
- DOGE: 45 fills (23 buy / 22 sell), traded 55,352, gross pnl -344.97, -125 bps per round trip, avg half spread 1.0 bps, open 25909.1
- DOT: 51 fills (24 buy / 27 sell), traded 73,139, gross pnl -190.79, -52 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 52 fills (27 buy / 25 sell), traded 84,914, gross pnl -458.03, -108 bps per round trip, avg half spread 2.1 bps, open 168.139
- LTC: 47 fills (22 buy / 25 sell), traded 62,740, gross pnl +364.38, +116 bps per round trip, avg half spread 1.6 bps
- SOL: 45 fills (24 buy / 21 sell), traded 64,035, gross pnl -121.95, -38 bps per round trip, avg half spread 0.5 bps, open 20.7751
- XRP: 51 fills (25 buy / 26 sell), traded 65,111, gross pnl +8.49, +3 bps per round trip, avg half spread 0.4 bps, open 1571.21

last fills:

- 2026-11-18 22:10Z sell DOGE 1,920 @ 0.0581921 fee 1.92 slip 0.96 (half spread 0.4 bps)
- 2026-11-18 23:10Z sell XRP 1,909 @ 0.964587 fee 1.91 slip 0.96 (half spread 0.3 bps)
- 2026-11-19 05:10Z buy XRP 1,930 @ 0.973141 fee 1.93 slip 0.96 (half spread 0.1 bps)
- 2026-11-19 09:10Z sell SOL 409 @ 74.4877 fee 0.41 slip 0.20 (half spread 0.7 bps)
- 2026-11-19 09:10Z sell XRP 406 @ 0.984902 fee 0.41 slip 0.20 (half spread 0.2 bps)
- 2026-11-19 09:10Z buy ADA 1,548 @ 0.154076 fee 1.55 slip 0.77 (half spread 0.0 bps)
- 2026-11-19 09:10Z buy LINK 1,548 @ 9.20943 fee 1.55 slip 0.77 (half spread 2.0 bps)
- 2026-11-19 09:10Z buy DOGE 1,543 @ 0.0595549 fee 1.54 slip 0.77 (half spread 0.0 bps)

## challenger1: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-14 05:10Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-19 10:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-19 10:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 10:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-19 10:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 09:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 67.82 not a higher low vs prior low 85.47 (need +10.0%)
- 2026-11-19 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1437 not a higher low vs prior low 0.1722 (need +10.0%)
- 2026-11-19 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.828 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-19 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.677 not a higher low vs prior low 10.2 (need +10.0%)
- 2026-11-19 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8979 not a higher low vs prior low 1.083 (need +10.0%)
- 2026-11-19 09:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05611 not a higher low vs prior low 0.06795 (need +10.0%)
- 2026-11-19 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6911 not a higher low vs prior low 0.8508 (need +10.0%)
- 2026-11-19 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 43.05 not a higher low vs prior low 49.8 (need +10.0%)
- 2026-11-19 10:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.217e+04 not a higher low vs prior low 7.378e+04 (need +10.0%)
- 2026-11-19 10:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1729 not a higher low vs prior low 2091 (need +10.0%)
- 2026-11-19 10:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 67.82 not a higher low vs prior low 85.47 (need +10.0%)
- 2026-11-19 10:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1437 not a higher low vs prior low 0.1722 (need +10.0%)
- 2026-11-19 10:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.828 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-19 10:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.677 not a higher low vs prior low 10.2 (need +10.0%)
- 2026-11-19 10:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8979 not a higher low vs prior low 1.083 (need +10.0%)
- 2026-11-19 10:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05611 not a higher low vs prior low 0.06795 (need +10.0%)
- 2026-11-19 10:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6911 not a higher low vs prior low 0.8508 (need +10.0%)
- 2026-11-19 10:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 43.05 not a higher low vs prior low 49.8 (need +10.0%)

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

- equity 8,165.89 (started 10,000 at 2026-10-13 17:26Z), net -18.34% since start
- 24h +0.30%, 7d -4.95%, 30d -17.23%, max drawdown -27.00%
- fills 62 total, 16 in the last 7d
- costs 138.53 (fees 89.56 + slippage 48.97); gross pnl -1,695.58; cost coverage -12.24
- cash 2,111.45; positions: DOGE 33810.2, ETH 1.10018, SOL 27.6689
- last run 2026-11-19 10:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 09:10Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -0.50 vs 720h mean (entry -2.0, exit -0.25); vol 83% -> weigh...
- 2026-11-19 09:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.55 not below -2.0
- 2026-11-19 09:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.16 not below -2.0
- 2026-11-19 09:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.23 not below -2.0
- 2026-11-19 09:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.21 not below -2.0
- 2026-11-19 09:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: ratio to BTC z -0.65 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...
- 2026-11-19 09:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.16 not below -2.0
- 2026-11-19 09:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.09 not below -2.0
- 2026-11-19 10:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-19 10:10Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.007 below threshold 0.05 | stay long: ratio to BTC z -0.91 vs 720h mean (entry -2.0, exit -0.25); vol 77% -> weigh...
- 2026-11-19 10:10Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -0.54 vs 720h mean (entry -2.0, exit -0.25); vol 83% -> weigh...
- 2026-11-19 10:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.59 not below -2.0
- 2026-11-19 10:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.18 not below -2.0
- 2026-11-19 10:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.25 not below -2.0
- 2026-11-19 10:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.20 not below -2.0
- 2026-11-19 10:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: ratio to BTC z -0.79 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...
- 2026-11-19 10:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.19 not below -2.0
- 2026-11-19 10:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.25 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 8 fills (4 buy / 4 sell), traded 11,844, gross pnl -321.04, -542 bps per round trip, avg half spread 1.5 bps, open 33810.2
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 9 fills (5 buy / 4 sell), traded 10,982, gross pnl -342.81, -624 bps per round trip, avg half spread 0.7 bps, open 1.10018
- LINK: 5 fills (3 buy / 2 sell), traded 8,173, gross pnl +207.92, +509 bps per round trip, avg half spread 2.0 bps
- LTC: 3 fills (1 buy / 2 sell), traded 4,467, gross pnl +6.37, +29 bps per round trip, avg half spread 1.3 bps
- SOL: 11 fills (5 buy / 6 sell), traded 16,981, gross pnl -415.40, -489 bps per round trip, avg half spread 1.0 bps, open 27.6689
- XRP: 10 fills (4 buy / 6 sell), traded 14,469, gross pnl -322.52, -446 bps per round trip, avg half spread 1.0 bps

last fills:

- 2026-11-14 16:10Z sell SOL 1,908 @ 73.0635 fee 1.91 slip 0.95 (half spread 1.4 bps)
- 2026-11-14 16:10Z sell XRP 1,958 @ 0.964587 fee 1.96 slip 0.98 (half spread 1.2 bps)
- 2026-11-14 16:10Z sell DOGE 1,952 @ 0.0603795 fee 1.95 slip 0.98 (half spread 1.1 bps)
- 2026-11-15 00:10Z buy ETH 1,945 @ 1767.63 fee 1.94 slip 0.97 (half spread 0.8 bps)
- 2026-11-15 00:10Z buy SOL 1,945 @ 70.2851 fee 1.94 slip 0.97 (half spread 1.4 bps)
- 2026-11-15 00:10Z buy XRP 1,945 @ 0.919565 fee 1.94 slip 0.97 (half spread 1.0 bps)
- 2026-11-15 00:10Z buy DOGE 1,937 @ 0.0572885 fee 1.94 slip 0.97 (half spread 1.7 bps)
- 2026-11-18 08:10Z sell XRP 2,114 @ 0.99941 fee 2.11 slip 1.06 (half spread 0.4 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 2263 candles, 2026-08-17 03:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- ETH: live 2263 candles, 2026-08-17 03:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- SOL: live 2263 candles, 2026-08-17 03:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- ADA: live 2263 candles, 2026-08-17 03:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- AVAX: live 2263 candles, 2026-08-17 03:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- LINK: live 2263 candles, 2026-08-17 03:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- XRP: live 2235 candles, 2026-08-18 07:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 2235 candles, 2026-08-18 07:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 2235 candles, 2026-08-18 07:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LTC: live 2235 candles, 2026-08-18 07:00Z to 2026-11-19 09:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
