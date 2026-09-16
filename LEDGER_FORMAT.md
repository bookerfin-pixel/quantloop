# Ledger entry format

PROTECTED. gate/check_ledger.py enforces this. Copy the block, fill every
line, keep the field names exactly.

```
## H<n>: <short title>
- Date: YYYY-MM-DD
- Hypothesis: one or two sentences stating a mechanism in the market, not a parameter value. "Trends that survive a pullback continue" is a hypothesis. "lookback 96 instead of 72" is not.
- Change: exactly what changed in configs/challenger.yaml and/or bot/strategy.py.
- Why it should work: the reason, in plain English, with the cost arithmetic. Say what size of move the signal is chasing and how that compares to the ~30 bps round trip.
- Expected gross bps per round trip: <number first>, then how you got it. Below 60 the gate rejects the entry, because 30 bps of cost leaves no room for being wrong.
- Kill criteria: what result in the prospective window would prove the hypothesis wrong. promote.py applies the standard rule regardless; this line is for the next reader to judge whether the standard rule was even the right question.
- Backtest: the metrics line from `python -m bot.backtest --config configs/challenger.yaml`, in particular n_trades, trades_per_pair_per_day_max, cost_coverage, max_drawdown. Backtests here are plausibility, not evidence; say so if the number looks too good.
- Status: testing
```

`<n>` is one more than the highest existing H number. `hypothesis: H<n>` in
configs/challenger.yaml must match.

Verdicts are appended by bot/promote.py under `## Results` and the Status
line is flipped to `promoted` or `killed`. Do not edit those by hand.
