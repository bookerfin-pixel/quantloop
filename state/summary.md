# quantloop summary — generated 2026-11-19 21:11Z

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
- challenger3: testing H5 since 2026-10-05 22:23Z, day 44.9 of 60, 15.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -32.07% (max drawdown -32.36%, 293 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.38% (usual 0.55, this window 0.32) vs challenger3 -0.21% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.42 over 45 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.00 over 45 days)
  fills: 10 in 44.9 days, 8 of them in the hour it began; at this pace about 13 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -27.78%, equal weight basket of 10 pairs -37.69%, basket max drawdown -40%, basket realised vol 59% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 34.9 of 120, 85.1 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -19.78% (max drawdown -27.00%, 62 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -3.80% (usual 0.53, this window 0.88); the rule compares on skill, daily edge t -0.35 over 35 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -33.33% so far
  trades: its 20 finished trades made -20.57% of its starting equity after costs (3 won, 17 lost, 15 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.35 over 35 days)
  market over the window: BTC -24.62%, equal weight basket of 10 pairs -30.26%, basket max drawdown -33%, basket realised vol 58% annualised
- free slots: challenger1, challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,547.83 (started 10,000 at 2026-09-16 03:55Z), net -24.52% since start
- 24h -1.61%, 7d -4.05%, 30d -21.21%, max drawdown -39.65%
- fills 482 total, 40 in the last 7d
- costs 1,024.28 (fees 677.78 + slippage 346.50); gross pnl -1,427.89; cost coverage -1.39
- cash 4,147.62; positions: SOL 20.7751, XRP 1967.48
- last run 2026-11-19 21:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 20:10Z SOL hold target 0.25 (held 0.20) — hold: weight change +0.049 below threshold 0.05 | stay long: 72h return +2.81% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-19 20:10Z ADA hold target 0.25 (held 0.20) — hold: weight change +0.048 below threshold 0.05 | stay long: 72h return -0.81% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-19 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.38% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.87% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 20:10Z XRP buy target 0.25 (held 0.20) — stay long: 72h return +0.74% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 79% -> weight 0.25
- 2026-11-19 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.61% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.46% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.88% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.53% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.28% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z SOL hold target 0.25 (held 0.20) — hold: weight change +0.050 below threshold 0.05 | stay long: 72h return +2.34% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-19 21:10Z ADA sell target 0.00 (held 0.20) — exit: 72h return -1.01% fell below exit band -1.0%
- 2026-11-19 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.72% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.73% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.74% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-19 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.90% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.61% not above entry band +1.0% and price below 24h EMA
- 2026-11-19 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.97% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 42 fills (19 buy / 23 sell), traded 53,054, gross pnl -203.84, -77 bps per round trip, avg half spread 2.2 bps
- AVAX: 58 fills (27 buy / 31 sell), traded 96,907, gross pnl -48.77, -10 bps per round trip, avg half spread 1.6 bps
- BTC: 43 fills (24 buy / 19 sell), traded 60,178, gross pnl -158.33, -53 bps per round trip, avg half spread 0.1 bps
- DOGE: 47 fills (24 buy / 23 sell), traded 57,628, gross pnl -380.75, -132 bps per round trip, avg half spread 1.0 bps
- DOT: 51 fills (24 buy / 27 sell), traded 73,139, gross pnl -190.79, -52 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 53 fills (27 buy / 26 sell), traded 86,429, gross pnl -486.84, -113 bps per round trip, avg half spread 2.1 bps
- LTC: 47 fills (22 buy / 25 sell), traded 62,740, gross pnl +364.38, +116 bps per round trip, avg half spread 1.6 bps
- SOL: 45 fills (24 buy / 21 sell), traded 64,035, gross pnl -156.86, -49 bps per round trip, avg half spread 0.5 bps, open 20.7751
- XRP: 52 fills (26 buy / 26 sell), traded 65,493, gross pnl -29.81, -9 bps per round trip, avg half spread 0.4 bps, open 1967.48

last fills:

- 2026-11-19 09:10Z buy ADA 1,548 @ 0.154076 fee 1.55 slip 0.77 (half spread 0.0 bps)
- 2026-11-19 09:10Z buy LINK 1,548 @ 9.20943 fee 1.55 slip 0.77 (half spread 2.0 bps)
- 2026-11-19 09:10Z buy DOGE 1,543 @ 0.0595549 fee 1.54 slip 0.77 (half spread 0.0 bps)
- 2026-11-19 16:10Z sell LINK 1,515 @ 9.01317 fee 1.52 slip 0.76 (half spread 2.4 bps)
- 2026-11-19 16:10Z buy DOGE 387 @ 0.0587299 fee 0.39 slip 0.19 (half spread 1.7 bps)
- 2026-11-19 17:10Z sell DOGE 1,888 @ 0.0580804 fee 1.89 slip 0.94 (half spread 1.9 bps)
- 2026-11-19 20:10Z buy XRP 381 @ 0.962266 fee 0.38 slip 0.19 (half spread 0.3 bps)
- 2026-11-19 21:10Z sell ADA 1,519 @ 0.151107 fee 1.52 slip 0.76 (half spread 2.2 bps)

## challenger1: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-14 05:10Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-19 21:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-19 21:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-19 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-19 21:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 67.82 not a higher low vs prior low 85.47 (need +10.0%)
- 2026-11-19 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1437 not a higher low vs prior low 0.1722 (need +10.0%)
- 2026-11-19 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.828 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-19 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.677 not a higher low vs prior low 10.2 (need +10.0%)
- 2026-11-19 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8979 not a higher low vs prior low 1.08 (need +10.0%)
- 2026-11-19 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05611 not a higher low vs prior low 0.06795 (need +10.0%)
- 2026-11-19 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6911 not a higher low vs prior low 0.8508 (need +10.0%)
- 2026-11-19 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 42.57 not a higher low vs prior low 49.8 (need +10.0%)
- 2026-11-19 21:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.217e+04 not a higher low vs prior low 7.378e+04 (need +10.0%)
- 2026-11-19 21:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1729 not a higher low vs prior low 2091 (need +10.0%)
- 2026-11-19 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 67.82 not a higher low vs prior low 85.47 (need +10.0%)
- 2026-11-19 21:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1437 not a higher low vs prior low 0.1722 (need +10.0%)
- 2026-11-19 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.828 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-19 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.677 not a higher low vs prior low 10.2 (need +10.0%)
- 2026-11-19 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8979 not a higher low vs prior low 1.08 (need +10.0%)
- 2026-11-19 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05611 not a higher low vs prior low 0.06795 (need +10.0%)
- 2026-11-19 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6911 not a higher low vs prior low 0.8508 (need +10.0%)
- 2026-11-19 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 42.57 not a higher low vs prior low 49.8 (need +10.0%)

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

- equity 8,019.02 (started 10,000 at 2026-10-13 17:26Z), net -19.81% since start
- 24h -0.19%, 7d -6.00%, 30d -21.20%, max drawdown -27.00%
- fills 62 total, 16 in the last 7d
- costs 138.53 (fees 89.56 + slippage 48.97); gross pnl -1,842.45; cost coverage -13.30
- cash 2,111.45; positions: DOGE 33810.2, ETH 1.10018, SOL 27.6689
- last run 2026-11-19 21:10Z; halted today: False

last decisions (newest last):

- 2026-11-19 20:10Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -0.31 vs 720h mean (entry -2.0, exit -0.25); vol 84% -> weigh...
- 2026-11-19 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.17 not below -2.0
- 2026-11-19 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.27 not below -2.0
- 2026-11-19 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.47 not below -2.0
- 2026-11-19 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.10 not below -2.0
- 2026-11-19 20:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: ratio to BTC z -0.40 vs 720h mean (entry -2.0, exit -0.25); vol 80% -> weigh...
- 2026-11-19 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.84 not below -2.0
- 2026-11-19 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.95 not below -2.0
- 2026-11-19 21:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-19 21:10Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.009 below threshold 0.05 | stay long: ratio to BTC z -0.79 vs 720h mean (entry -2.0, exit -0.25); vol 77% -> weigh...
- 2026-11-19 21:10Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -0.35 vs 720h mean (entry -2.0, exit -0.25); vol 84% -> weigh...
- 2026-11-19 21:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.25 not below -2.0
- 2026-11-19 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.11 not below -2.0
- 2026-11-19 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.37 not below -2.0
- 2026-11-19 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.12 not below -2.0
- 2026-11-19 21:10Z DOGE hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: ratio to BTC z -0.53 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...
- 2026-11-19 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.95 not below -2.0
- 2026-11-19 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.53 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 8 fills (4 buy / 4 sell), traded 11,844, gross pnl -367.46, -620 bps per round trip, avg half spread 1.5 bps, open 33810.2
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 9 fills (5 buy / 4 sell), traded 10,982, gross pnl -396.77, -723 bps per round trip, avg half spread 0.7 bps, open 1.10018
- LINK: 5 fills (3 buy / 2 sell), traded 8,173, gross pnl +207.92, +509 bps per round trip, avg half spread 2.0 bps
- LTC: 3 fills (1 buy / 2 sell), traded 4,467, gross pnl +6.37, +29 bps per round trip, avg half spread 1.3 bps
- SOL: 11 fills (5 buy / 6 sell), traded 16,981, gross pnl -461.88, -544 bps per round trip, avg half spread 1.0 bps, open 27.6689
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

- BTC: live 2274 candles, 2026-08-17 03:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- ETH: live 2274 candles, 2026-08-17 03:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- SOL: live 2274 candles, 2026-08-17 03:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- ADA: live 2274 candles, 2026-08-17 03:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 2274 candles, 2026-08-17 03:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- LINK: live 2274 candles, 2026-08-17 03:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- XRP: live 2246 candles, 2026-08-18 07:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 2246 candles, 2026-08-18 07:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 2246 candles, 2026-08-18 07:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- LTC: live 2246 candles, 2026-08-18 07:00Z to 2026-11-19 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
