# Ledger

Every hypothesis this system has tested, with its verdict. The agent adds a
`## H<n>` entry before a test starts (format in LEDGER_FORMAT.md) and
bot/promote.py appends the verdict under `## Results`. Nothing is deleted. A
killed idea is evidence, and the next agent run reads it before proposing.

## Prior evidence

Not tests run here, but the reasons this system is shaped the way it is. They
come from Fin's first bot (2025, real money, Binance spot, seven pairs).

### P1: short horizon mean reversion could not pay Binance fees
- It was built for 20 to 22 bps moves. Realised gross edge on short horizon
  mean reversion came in at single digit bps per trade against roughly 22 bps
  of round trip cost. The direction was often right; the size of the move was
  not. Costs killed it, not the signal.
- Carried here as: the cost coverage gate, the trades per day cap, and the
  "Expected gross bps per round trip" line every hypothesis must fill in.

### P2: machinery built before validation starved itself
- Kelly sizing needed 40+ closed trades, the transaction cost model needed
  fill samples, the ML model needed 500+ labelled observations. The risk gates
  skipped nearly every candidate trade, so none of that ever calibrated.
- Carried here as: a small bot, one change at a time, a minimum fill count
  before any verdict, and no component that needs data the system is not
  yet producing.

## H0: baseline, slow time series momentum, long or flat
- Date: 2026-09-16
- Hypothesis: a 72 hour momentum signal with an EMA filter and entry/exit bands on six majors catches multi day trends often enough that a 30 bps round trip is small next to the average move captured.
- Change: seed configuration (configs/champion.yaml), strategy `ts_momentum`.
- Why it should work: trend persistence over days is the most replicated effect in crypto returns, and the bands hold turnover near 0.3 fills per pair per day so the strategy is not on a costs treadmill.
- Expected gross bps per round trip: 150
- Kill criteria: none. This is the champion; it is only replaced by a challenger that beats it in a prospective test.
- Backtest: first 23 days of real Kraken data (2026-08-24 to 2026-09-16, a choppy, falling window): total return -6.1%, max drawdown -10.8%, 110 fills (0.80 per pair per day, max 5 in one pair in one day), gross pnl -300, costs 311, cost coverage -0.96. On this window the baseline would fail its own gate on churn and cost coverage. It is the floor the first challenger has to beat, not evidence of edge.
- Status: champion

## H1: long horizon mean reversion, deep dips only, six majors
- Date: 2026-09-16
- Hypothesis: on a 10 day window, a price that is 2 standard deviations below its own trailing mean has moved further, faster, than the recent character of that pair's returns explains, and it tends to claw back most of the gap before either resuming its prior trend or rolling over. The pullback itself, not a change in trend, is the tradeable event.
- Change: configs/challenger.yaml only, no strategy code change. Uses the existing `mean_reversion` strategy (bot/strategy.py) across all six pairs (BTC, ETH, SOL, ADA, AVAX, LINK), not the two the backlog note suggested: window_hours 240 (was 96), entry_z 2.0 (was implicitly tuned for a short horizon), exit_z 0.5, vol_lookback_hours 168, target_vol_annual 0.30, max_weight 0.25. Six pairs instead of two because at entry_z 2.0 two pairs alone would not clear risk.yaml's challenger.min_trades (20 fills in 21 days) and an under-traded test cannot get a verdict from bot/promote.py at all (it kills automatically for insufficient fills, not for being wrong).
- Why it should work: P1 (see Prior evidence) killed short horizon mean reversion because the realised edge was single digit bps against ~22 bps of Binance cost — the direction was often right but the move was too small. This is the same family at ten times the horizon: entering at z below -2.0 and exiting at z above -0.5 chases a gap of 1.5 standard deviations of the 10 day return distribution. At a typical major's realised annualised vol of 40-80%, a 10 day (240h) standard deviation of price is roughly 7-11%, so 1.5 of those standard deviations is on the order of 1000+ bps of potential reversion between entry and exit band, far larger than the ~30 bps round trip cost. It will not capture the whole gap every time; the backtest below realised about 200 bps gross per round trip on this window, which still clears the 30 bps cost by more than six times.
- Expected gross bps per round trip: 200, from the backtest: cost coverage 6.58 x the ~30 bps round trip cost model = 197 bps, rounded to 200. The vol-band arithmetic above (~1000+ bps of band gap) is the ceiling, not the estimate; 200 bps is what was actually realised on this window.
- Kill criteria: this is a small sample by construction (rare, large deviations). If the prospective window produces materially fewer than 22 fills (its backtest count over a 20 day window on the same six pairs), the idea should be judged not-yet-tested rather than wrong, regardless of what promote.py's standard fill-count kill says. If it trades enough and still does not beat the champion, the mechanism did not generalise past the exact window it was picked on, which is the real risk here: this window contains few genuinely deep dips to fit to, so the parameters could be overfit to a handful of trades.
- Backtest: `python -m bot.backtest --config configs/challenger.yaml` on 19.9 days of real Kraken data (2026-08-27 to 2026-09-16): total return +3.89%, max drawdown -2.80%, sharpe 4.39, 22 fills (0.184 per pair per day, max 2 in one pair in one day), gross pnl 458.80, costs 69.69 (fees 46.46 + slippage 23.23), cost coverage 6.58. This is the same window H0 lost money on; it is a small, favourable sample for a strategy that only trades a few times, and the prospective test is what actually counts, not this number.
- Status: testing
