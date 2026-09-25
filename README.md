# quantloop

A paper trading bot that is allowed to improve itself, inside rules it cannot
change. Crypto spot, ten liquid USD pairs, hourly decisions, real market data
and live spreads, modelled Binance fees. No exchange keys, no live orders, by
construction.

## The loop

1. **Every hour** (`bot.yml`): pull Kraken candles and live quotes, run the
   champion config, every challenger slot config and (after a
   promotion) the shadow against their own paper accounts, log every
   decision with its reason and the observed spread, commit the state to
   this repo. Fills pay the larger of a 5 bps floor and the real half
   spread plus 2 bps impact, on top of a 10 bps Binance taker fee.
2. **Every day at 08:00 Brisbane** (`agent.yml`): Claude Code reads the
   state, the ledger, the findings and the backlog, and either proposes one
   hypothesis into a free slot (a change to `configs/challenger<k>.yaml` and
   maybe `bot/strategy.py`, with a ledger entry) or, if every slot is busy,
   reviews the logs and writes a note. Its commit becomes a pull request.
3. **The gate** (`gate.yml`, run from `main` so the PR cannot alter it):
   no protected file touched, no order placement or credential code added,
   a complete ledger entry, tests green, and a backtest of the changed slot
   over the last year with the live cost model that clears regime
   independent sanity bounds (no fees treadmill, enough trades to judge,
   drawdown no worse than the larger of 30% and three quarters of the
   market's own). In sample profit is reported, never required; alpha is
   judged prospectively. Pass: merged automatically. Fail: closed
   automatically with the reason, which the agent reads next time.
4. **The test**: the next hourly run sees the new slot config and starts a
   60 day prospective test, champion and challenger on the same live data.
   After the window `bot/promote.py` rules by fixed rules in
   `configs/risk.yaml`: promoted (the slot's config becomes the champion)
   or killed. A challenger down more than 15% is killed early. Verdict
   appended to `LEDGER.md` with the realised gross bps per round trip next
   to the number the hypothesis predicted and what the market did over the
   window, slot reset and free. After a promotion the deposed config keeps
   running as a shadow for one more window; if it beats the new champion
   the promotion is reverted, which is the guard against a lucky 60 days.
   Three tests run at once, about eighteen verdicts a year.
5. **The synthesis**: `FINDINGS.md` is the distilled version of the ledger,
   kept by the agent: what is confirmed, what one verdict suggests, what was
   killed and why, how well the cost arithmetic predicted reality, and what
   is still open. That file is the product; the champion is a by product.

The agent chooses what to try. The rules, costs, limits and the exam are
in files the agent cannot touch (`PROTECTED.txt`). Fin edits those by hand.

## Why it is shaped like this

Fin's first bot (2025, real money) died of two things: a short horizon
strategy whose gross edge was smaller than Binance's fees, and machinery
built before there was any evidence to calibrate it. So here the cost model
is the first class citizen (one function serves the paper account and the
backtest), every hypothesis must state its expected gross bps per round trip
against the ~30 bps cost, no verdict is reached without a minimum number of
fills, and the champion's equity curve is never reset. Backtests are treated
as plausibility checks; only the prospective window counts.

## Layout

    bot/            data, strategy (agent editable), paper account, risk, run, backtest, promote, shadow, report
    configs/        risk.yaml (protected), champion.yaml (protected), challenger1..3.yaml (agent edits, one per PR)
    gate/           the three checks the PR must pass
    tests/          gate/ is protected; the rest the agent may extend
    state/          accounts, decisions, trades, equity curves, live candle cache, two year history, summary.md
    LEDGER.md       every hypothesis and its verdict, never edited backwards
    FINDINGS.md     the distilled state of knowledge, kept current by the agent
    hypotheses/     the backlog the agent draws from
    notes/          daily observations when the slot is busy
    CLAUDE.md       the agent's operating manual
    PROTECTED.txt   what the agent may not change

## Running it yourself

    pip install -r requirements.txt
    python -m pytest tests -q
    QUANTLOOP_FAKE_DATA=1 python -m bot.run          # synthetic data, no network
    python -m bot.backtest --config configs/challenger1.yaml
    python -m bot.slot
    python -m bot.report && cat state/summary.md

## Setup (once)

- Repo secret `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`, Pro/Max)
  or `ANTHROPIC_API_KEY`. Without one the agent job fails at its first step.
- Optional repo variables: `AGENT_MODEL` (model alias for the agent),
  `AGENT_MAX_BUDGET_USD` (per run cap; only meaningful with an API key).
- Actions must be enabled. `bot.yml` and `agent.yml` can also be run by hand
  from the Actions tab.

## Changing the rules

Edit the protected file on `main` directly (or in a PR you merge yourself;
the gate runs read only on human PRs and will report the protected paths, that
is expected). To pause the whole thing, disable the two workflows in the
Actions tab. To pause only the agent, disable `agent.yml`; the paper accounts
keep running.

## Going live

There is deliberately no path from this repo to a live order. The agent is
forbidden from writing one and the gate greps for it. If the ledger ever
shows a champion with months of prospective evidence, the live version is a
separate decision and a separate piece of code, written and reviewed by a
person, with its own risk limits.

## Costs

Public repo: Actions minutes are free. The hourly bot job takes about a
minute; the agent job a few minutes plus the model's usage against Fin's
subscription (or the API key).
