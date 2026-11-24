# quantloop summary — generated 2026-11-24 02:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-17 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 1 pair day (the cap is 4 fills in one pair in one UTC day)
- champion, XRP, 2026-11-19: 4 fills (buy 05:10, sell 09:10, buy 20:10, sell 22:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: idle, holds cash (free for a hypothesis)
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 49.2 of 60, 10.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -33.61% (max drawdown -34.26%, 309 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.25% (usual 0.55, this window 0.31) vs challenger3 -0.18% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.49 over 49 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is +0.04 over 49 days)
  fills: 10 in 49.2 days, 8 of them in the hour it began; at this pace about 12 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -29.00%, equal weight basket of 10 pairs -38.90%, basket max drawdown -45%, basket realised vol 63% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 39.1 of 120, 80.9 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -21.12% (max drawdown -28.22%, 70 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -4.43% (usual 0.53, this window 0.85); the rule compares on skill, daily edge t -0.38 over 39 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -38.92% so far
  trades: its 24 finished trades made -24.40% of its starting equity after costs (3 won, 21 lost, 19 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.38 over 39 days)
  market over the window: BTC -25.89%, equal weight basket of 10 pairs -31.62%, basket max drawdown -39%, basket realised vol 64% annualised
- free slots: challenger1, challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,376.93 (started 10,000 at 2026-09-16 03:55Z), net -26.23% since start
- 24h -1.35%, 7d -5.45%, 30d -18.95%, max drawdown -41.34%
- fills 498 total, 54 in the last 7d
- costs 1,053.35 (fees 697.09 + slippage 356.26); gross pnl -1,569.72; cost coverage -1.49
- cash -0.00; positions: ADA 5032.35, AVAX 108.924, BTC 0.0120703, DOGE 13070, DOT 1081.77, ETH 0.425069, LINK 82.3349, LTC 17.8497, SOL 10.094, XRP 776.174
- last run 2026-11-24 02:10Z; halted today: False

last decisions (newest last):

- 2026-11-24 01:10Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +4.75% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 01:10Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +4.24% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 01:10Z AVAX hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +4.41% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-11-24 01:10Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +5.76% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 01:10Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +3.74% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 01:10Z DOGE hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +4.05% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 01:10Z DOT hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +2.48% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 01:10Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.17% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 02:10Z BTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +3.56% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 02:10Z ETH hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +4.96% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 02:10Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +4.46% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 02:10Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +4.27% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 02:10Z AVAX hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +4.81% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-11-24 02:10Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +5.91% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 02:10Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +4.13% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 02:10Z DOGE hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +4.02% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-24 02:10Z DOT hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.76% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-24 02:10Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.19% vs exit band -1.0% and price above 24h EMA; realised vol 8...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 43 fills (20 buy / 23 sell), traded 53,818, gross pnl -214.82, -80 bps per round trip, avg half spread 2.1 bps, open 5032.35
- AVAX: 59 fills (28 buy / 31 sell), traded 97,671, gross pnl -69.79, -14 bps per round trip, avg half spread 1.6 bps, open 108.924
- BTC: 44 fills (25 buy / 19 sell), traded 60,941, gross pnl -186.58, -61 bps per round trip, avg half spread 0.1 bps, open 0.0120703
- DOGE: 48 fills (25 buy / 23 sell), traded 58,391, gross pnl -402.32, -138 bps per round trip, avg half spread 1.0 bps, open 13070
- DOT: 52 fills (25 buy / 27 sell), traded 73,902, gross pnl -219.67, -59 bps per round trip, avg half spread 2.3 bps, open 1081.77
- ETH: 45 fills (22 buy / 23 sell), traded 58,937, gross pnl -175.40, -60 bps per round trip, avg half spread 0.2 bps, open 0.425069
- LINK: 55 fills (28 buy / 27 sell), traded 89,485, gross pnl -421.40, -94 bps per round trip, avg half spread 2.0 bps, open 82.3349
- LTC: 48 fills (23 buy / 25 sell), traded 63,495, gross pnl +351.26, +111 bps per round trip, avg half spread 1.6 bps, open 17.8497
- SOL: 48 fills (25 buy / 23 sell), traded 68,601, gross pnl -120.04, -35 bps per round trip, avg half spread 0.5 bps, open 10.094
- XRP: 56 fills (28 buy / 28 sell), traded 71,852, gross pnl -110.94, -31 bps per round trip, avg half spread 0.5 bps, open 776.174

last fills:

- 2026-11-23 14:10Z buy BTC 763 @ 63250.4 fee 0.76 slip 0.38 (half spread 0.0 bps)
- 2026-11-23 14:10Z buy ETH 763 @ 1796.06 fee 0.76 slip 0.38 (half spread 1.7 bps)
- 2026-11-23 14:10Z buy ADA 763 @ 0.151708 fee 0.76 slip 0.38 (half spread 1.7 bps)
- 2026-11-23 14:10Z buy AVAX 763 @ 7.009 fee 0.76 slip 0.38 (half spread 2.1 bps)
- 2026-11-23 14:10Z buy XRP 763 @ 0.983607 fee 0.76 slip 0.38 (half spread 2.5 bps)
- 2026-11-23 14:10Z buy DOGE 763 @ 0.0584126 fee 0.76 slip 0.38 (half spread 0.5 bps)
- 2026-11-23 14:10Z buy DOT 763 @ 0.705741 fee 0.76 slip 0.48 (half spread 4.3 bps)
- 2026-11-23 14:10Z buy LTC 755 @ 42.2961 fee 0.75 slip 0.38 (half spread 1.2 bps)

## challenger1: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-14 05:10Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-24 02:10Z; halted today: False

last decisions (newest last):

- 2026-11-24 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-24 02:10Z; halted today: False

last decisions (newest last):

- 2026-11-24 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-24 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-24 02:10Z; halted today: False

last decisions (newest last):

- 2026-11-24 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 65.36 not a higher low vs prior low 77.57 (need +10.0%)
- 2026-11-24 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1347 not a higher low vs prior low 0.1669 (need +10.0%)
- 2026-11-24 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.093 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-24 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.043 not a higher low vs prior low 9.678 (need +10.0%)
- 2026-11-24 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8707 not a higher low vs prior low 1.005 (need +10.0%)
- 2026-11-24 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05142 not a higher low vs prior low 0.06322 (need +10.0%)
- 2026-11-24 01:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6244 not a higher low vs prior low 0.8025 (need +10.0%)
- 2026-11-24 01:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 38.05 not a higher low vs prior low 47.79 (need +10.0%)
- 2026-11-24 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 5.57e+04 not a higher low vs prior low 6.808e+04 (need +10.0%)
- 2026-11-24 02:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1559 not a higher low vs prior low 1910 (need +10.0%)
- 2026-11-24 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 65.36 not a higher low vs prior low 77.57 (need +10.0%)
- 2026-11-24 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1347 not a higher low vs prior low 0.1669 (need +10.0%)
- 2026-11-24 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.093 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-24 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.043 not a higher low vs prior low 9.678 (need +10.0%)
- 2026-11-24 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8707 not a higher low vs prior low 1.005 (need +10.0%)
- 2026-11-24 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05142 not a higher low vs prior low 0.06322 (need +10.0%)
- 2026-11-24 02:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6244 not a higher low vs prior low 0.8025 (need +10.0%)
- 2026-11-24 02:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 38.05 not a higher low vs prior low 47.79 (need +10.0%)

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

- equity 7,885.17 (started 10,000 at 2026-10-13 17:26Z), net -21.15% since start
- 24h +1.85%, 7d -1.73%, 30d -18.36%, max drawdown -28.22%
- fills 70 total, 9 in the last 7d
- costs 161.23 (fees 104.69 + slippage 56.53); gross pnl -1,953.60; cost coverage -12.12
- cash 1,856.64; positions: DOT 2971.63, ETH 1.16622, LTC 48.766
- last run 2026-11-24 02:10Z; halted today: False

last decisions (newest last):

- 2026-11-24 01:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.10 not below -2.0
- 2026-11-24 01:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.06 not below -2.0
- 2026-11-24 01:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.08 not below -2.0
- 2026-11-24 01:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +1.73 not below -2.0
- 2026-11-24 01:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.15 not below -2.0
- 2026-11-24 01:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.78 not below -2.0
- 2026-11-24 01:10Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.005 below threshold 0.05 | stay long: ratio to BTC z -1.42 vs 720h mean (entry -2.0, exit -0.25); vol 90% -> weigh...
- 2026-11-24 01:10Z LTC hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: ratio to BTC z -1.09 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...
- 2026-11-24 02:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-24 02:10Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.17 vs 720h mean (entry -2.0, exit -0.25); vol 89% -> weigh...
- 2026-11-24 02:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.14 not below -2.0
- 2026-11-24 02:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.18 not below -2.0
- 2026-11-24 02:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.12 not below -2.0
- 2026-11-24 02:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +2.08 not below -2.0
- 2026-11-24 02:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.05 not below -2.0
- 2026-11-24 02:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.55 not below -2.0
- 2026-11-24 02:10Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: ratio to BTC z -1.32 vs 720h mean (entry -2.0, exit -0.25); vol 90% -> weigh...
- 2026-11-24 02:10Z LTC hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: ratio to BTC z -0.92 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 9 fills (4 buy / 5 sell), traded 13,665, gross pnl -505.62, -740 bps per round trip, avg half spread 1.4 bps
- DOT: 7 fills (4 buy / 3 sell), traded 10,079, gross pnl +38.90, +77 bps per round trip, avg half spread 4.1 bps, open 2971.63
- ETH: 11 fills (6 buy / 5 sell), traded 14,682, gross pnl -421.86, -575 bps per round trip, avg half spread 0.7 bps, open 1.16622
- LINK: 5 fills (3 buy / 2 sell), traded 8,173, gross pnl +207.92, +509 bps per round trip, avg half spread 2.0 bps
- LTC: 6 fills (3 buy / 3 sell), traded 10,257, gross pnl +69.75, +136 bps per round trip, avg half spread 1.5 bps, open 48.766
- SOL: 12 fills (5 buy / 7 sell), traded 18,884, gross pnl -572.56, -606 bps per round trip, avg half spread 0.9 bps
- XRP: 10 fills (4 buy / 6 sell), traded 14,469, gross pnl -322.52, -446 bps per round trip, avg half spread 1.0 bps

last fills:

- 2026-11-20 04:10Z buy LTC 1,988 @ 41.5608 fee 1.99 slip 0.99 (half spread 2.4 bps)
- 2026-11-20 16:10Z sell ETH 1,810 @ 1645.36 fee 1.81 slip 0.91 (half spread 0.7 bps)
- 2026-11-20 16:10Z sell SOL 1,903 @ 68.7706 fee 1.90 slip 0.95 (half spread 0.7 bps)
- 2026-11-20 16:10Z sell DOGE 1,821 @ 0.0538537 fee 1.82 slip 0.91 (half spread 0.1 bps)
- 2026-11-20 16:10Z sell LTC 1,912 @ 39.985 fee 1.91 slip 0.96 (half spread 1.2 bps)
- 2026-11-21 01:10Z buy ETH 1,890 @ 1620.71 fee 1.89 slip 0.94 (half spread 0.0 bps)
- 2026-11-21 08:10Z buy LTC 1,890 @ 38.7544 fee 1.89 slip 0.94 (half spread 1.3 bps)
- 2026-11-21 22:10Z buy DOT 1,918 @ 0.645473 fee 1.92 slip 0.96 (half spread 2.3 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 2375 candles, 2026-08-17 03:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- ETH: live 2375 candles, 2026-08-17 03:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.2 bps
- SOL: live 2375 candles, 2026-08-17 03:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- ADA: live 2375 candles, 2026-08-17 03:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 2375 candles, 2026-08-17 03:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- LINK: live 2375 candles, 2026-08-17 03:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 2347 candles, 2026-08-18 07:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.4 bps
- DOGE: live 2347 candles, 2026-08-18 07:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 2347 candles, 2026-08-18 07:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- LTC: live 2347 candles, 2026-08-18 07:00Z to 2026-11-24 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
