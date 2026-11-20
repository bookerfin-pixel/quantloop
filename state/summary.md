# quantloop summary — generated 2026-11-20 20:04Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-11-13 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 1 pair day (the cap is 4 fills in one pair in one UTC day)
- champion, XRP, 2026-11-19: 4 fills (buy 05:10, sell 09:10, buy 20:10, sell 22:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: idle, holds cash (free for a hypothesis)
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 45.9 of 60, 14.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -32.70% (max drawdown -32.99%, 297 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.59% (usual 0.55, this window 0.32) vs challenger3 -0.09% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +1.07 over 46 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10% that this is a real edge (every idea starts at 10%; the daily skill t is +0.17 over 46 days)
  fills: 10 in 45.9 days, 8 of them in the hour it began; at this pace about 13 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -31.94%, equal weight basket of 10 pairs -42.10%, basket max drawdown -43%, basket realised vol 60% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 35.9 of 120, 84.1 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -24.37% (max drawdown -27.40%, 67 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -5.78% (usual 0.53, this window 0.87); the rule compares on skill, daily edge t -0.58 over 36 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -36.35% so far
  trades: its 24 finished trades made -24.40% of its starting equity after costs (3 won, 21 lost, 19 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.58 over 36 days)
  market over the window: BTC -28.96%, equal weight basket of 10 pairs -35.21%, basket max drawdown -36%, basket realised vol 60% annualised
- free slots: challenger1, challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 7,477.55 (started 10,000 at 2026-09-16 03:55Z), net -25.22% since start
- 24h -1.21%, 7d -4.98%, 30d -23.23%, max drawdown -40.21%
- fills 486 total, 43 in the last 7d
- costs 1,034.93 (fees 684.88 + slippage 350.05); gross pnl -1,487.52; cost coverage -1.44
- cash 7,477.55; positions: none
- last run 2026-11-20 20:04Z; halted today: False

last decisions (newest last):

- 2026-11-20 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.01% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.43% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.64% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.33% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.49% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.15% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.22% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.17% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.16% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -10.23% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.38% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.61% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.48% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.19% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.34% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.98% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.76% not above entry band +1.0% and price below 24h EMA
- 2026-11-20 20:04Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -10.26% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 42 fills (19 buy / 23 sell), traded 53,054, gross pnl -203.84, -77 bps per round trip, avg half spread 2.2 bps
- AVAX: 58 fills (27 buy / 31 sell), traded 96,907, gross pnl -48.77, -10 bps per round trip, avg half spread 1.6 bps
- BTC: 43 fills (24 buy / 19 sell), traded 60,178, gross pnl -158.33, -53 bps per round trip, avg half spread 0.1 bps
- DOGE: 47 fills (24 buy / 23 sell), traded 57,628, gross pnl -380.75, -132 bps per round trip, avg half spread 1.0 bps
- DOT: 51 fills (24 buy / 27 sell), traded 73,139, gross pnl -190.79, -52 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 53 fills (27 buy / 26 sell), traded 86,429, gross pnl -486.84, -113 bps per round trip, avg half spread 2.1 bps
- LTC: 47 fills (22 buy / 25 sell), traded 62,740, gross pnl +364.38, +116 bps per round trip, avg half spread 1.6 bps
- SOL: 46 fills (24 buy / 22 sell), traded 65,540, gross pnl -163.50, -50 bps per round trip, avg half spread 0.5 bps
- XRP: 55 fills (27 buy / 28 sell), traded 71,088, gross pnl -82.79, -23 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-11-19 16:10Z buy DOGE 387 @ 0.0587299 fee 0.39 slip 0.19 (half spread 1.7 bps)
- 2026-11-19 17:10Z sell DOGE 1,888 @ 0.0580804 fee 1.89 slip 0.94 (half spread 1.9 bps)
- 2026-11-19 20:10Z buy XRP 381 @ 0.962266 fee 0.38 slip 0.19 (half spread 0.3 bps)
- 2026-11-19 21:10Z sell ADA 1,519 @ 0.151107 fee 1.52 slip 0.76 (half spread 2.2 bps)
- 2026-11-19 22:10Z sell SOL 1,505 @ 72.4488 fee 1.51 slip 0.75 (half spread 0.7 bps)
- 2026-11-19 22:10Z sell XRP 1,878 @ 0.954562 fee 1.88 slip 0.94 (half spread 0.7 bps)
- 2026-11-20 07:10Z buy XRP 1,882 @ 0.967784 fee 1.88 slip 0.94 (half spread 0.4 bps)
- 2026-11-20 12:10Z sell XRP 1,836 @ 0.944033 fee 1.84 slip 0.92 (half spread 0.5 bps)

## challenger1: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-14 05:10Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-20 20:04Z; halted today: False

last decisions (newest last):

- 2026-11-20 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-20 20:04Z; halted today: False

last decisions (newest last):

- 2026-11-20 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-20 20:04Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-20 20:04Z; halted today: False

last decisions (newest last):

- 2026-11-20 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 67.82 not a higher low vs prior low 81.86 (need +10.0%)
- 2026-11-20 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1398 not a higher low vs prior low 0.1722 (need +10.0%)
- 2026-11-20 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.479 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-20 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.323 not a higher low vs prior low 10.19 (need +10.0%)
- 2026-11-20 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8979 not a higher low vs prior low 1.041 (need +10.0%)
- 2026-11-20 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05376 not a higher low vs prior low 0.06702 (need +10.0%)
- 2026-11-20 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6581 not a higher low vs prior low 0.8336 (need +10.0%)
- 2026-11-20 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 39.89 not a higher low vs prior low 49.8 (need +10.0%)
- 2026-11-20 20:04Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 5.834e+04 not a higher low vs prior low 7.281e+04 (need +10.0%)
- 2026-11-20 20:04Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1615 not a higher low vs prior low 2017 (need +10.0%)
- 2026-11-20 20:04Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 67.82 not a higher low vs prior low 81.86 (need +10.0%)
- 2026-11-20 20:04Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1398 not a higher low vs prior low 0.1722 (need +10.0%)
- 2026-11-20 20:04Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 6.479 not a higher low vs prior low 7.826 (need +10.0%)
- 2026-11-20 20:04Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.323 not a higher low vs prior low 10.19 (need +10.0%)
- 2026-11-20 20:04Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8979 not a higher low vs prior low 1.041 (need +10.0%)
- 2026-11-20 20:04Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.05376 not a higher low vs prior low 0.06702 (need +10.0%)
- 2026-11-20 20:04Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.6581 not a higher low vs prior low 0.8336 (need +10.0%)
- 2026-11-20 20:04Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 39.89 not a higher low vs prior low 49.8 (need +10.0%)

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

- equity 7,560.45 (started 10,000 at 2026-10-13 17:26Z), net -24.40% since start
- 24h -5.97%, 7d -10.21%, 30d -26.95%, max drawdown -27.40%
- fills 67 total, 14 in the last 7d
- costs 152.68 (fees 99.00 + slippage 53.68); gross pnl -2,286.86; cost coverage -14.98
- cash 7,560.45; positions: none
- last run 2026-11-20 20:04Z; halted today: True

last decisions (newest last):

- 2026-11-20 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-11-20 20:04Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -292.12, -807 bps per round trip, avg half spread 3.8 bps
- AVAX: 5 fills (3 buy / 2 sell), traded 7,243, gross pnl -155.50, -429 bps per round trip, avg half spread 3.3 bps
- DOGE: 9 fills (4 buy / 5 sell), traded 13,665, gross pnl -505.62, -740 bps per round trip, avg half spread 1.4 bps
- DOT: 6 fills (3 buy / 3 sell), traded 8,161, gross pnl -60.50, -148 bps per round trip, avg half spread 4.4 bps
- ETH: 10 fills (5 buy / 5 sell), traded 12,792, gross pnl -518.93, -811 bps per round trip, avg half spread 0.7 bps
- LINK: 5 fills (3 buy / 2 sell), traded 8,173, gross pnl +207.92, +509 bps per round trip, avg half spread 2.0 bps
- LTC: 5 fills (2 buy / 3 sell), traded 8,367, gross pnl -67.04, -160 bps per round trip, avg half spread 1.5 bps
- SOL: 12 fills (5 buy / 7 sell), traded 18,884, gross pnl -572.56, -606 bps per round trip, avg half spread 0.9 bps
- XRP: 10 fills (4 buy / 6 sell), traded 14,469, gross pnl -322.52, -446 bps per round trip, avg half spread 1.0 bps

last fills:

- 2026-11-15 00:10Z buy XRP 1,945 @ 0.919565 fee 1.94 slip 0.97 (half spread 1.0 bps)
- 2026-11-15 00:10Z buy DOGE 1,937 @ 0.0572885 fee 1.94 slip 0.97 (half spread 1.7 bps)
- 2026-11-18 08:10Z sell XRP 2,114 @ 0.99941 fee 2.11 slip 1.06 (half spread 0.4 bps)
- 2026-11-20 04:10Z buy LTC 1,988 @ 41.5608 fee 1.99 slip 0.99 (half spread 2.4 bps)
- 2026-11-20 16:10Z sell ETH 1,810 @ 1645.36 fee 1.81 slip 0.91 (half spread 0.7 bps)
- 2026-11-20 16:10Z sell SOL 1,903 @ 68.7706 fee 1.90 slip 0.95 (half spread 0.7 bps)
- 2026-11-20 16:10Z sell DOGE 1,821 @ 0.0538537 fee 1.82 slip 0.91 (half spread 0.1 bps)
- 2026-11-20 16:10Z sell LTC 1,912 @ 39.985 fee 1.91 slip 0.96 (half spread 1.2 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 2297 candles, 2026-08-17 03:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- ETH: live 2297 candles, 2026-08-17 03:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.3 bps
- SOL: live 2297 candles, 2026-08-17 03:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.8 bps
- ADA: live 2297 candles, 2026-08-17 03:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 2297 candles, 2026-08-17 03:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LINK: live 2297 candles, 2026-08-17 03:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- XRP: live 2269 candles, 2026-08-18 07:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 2269 candles, 2026-08-18 07:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 2269 candles, 2026-08-18 07:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LTC: live 2269 candles, 2026-08-18 07:00Z to 2026-11-20 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
