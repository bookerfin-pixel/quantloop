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
