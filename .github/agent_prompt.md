You are running as the daily research agent for quantloop. CLAUDE.md is loaded; follow its daily procedure exactly.

Today's run, in order:

1. Read state/summary.md, LEDGER.md, FINDINGS.md, hypotheses/backlog.md and the newest file in notes/. Run `gh pr list --state closed --limit 5` and, for any PR closed in the last few days by the gate, `gh pr view <n> --comments` to read why.
2. If the ledger's `## Results` section has a verdict that FINDINGS.md does not reflect yet, update FINDINGS.md first (finding plus calibration line).
3. Determine which slots are free (listed at the top of state/summary.md; `python -m bot.slot` confirms it).
4. If no slot is free: do the review described in CLAUDE.md, write notes/<today>.md, update hypotheses/backlog.md if you have a real idea, and commit. Do not change any configs/challenger<k>.yaml or bot/strategy.py unless you found a bug that does not confound a running test.
5. If a slot is free: choose a hypothesis from a different family than the tests already running, write one ledger entry, change that one slot's config (and bot/strategy.py only if new logic is needed, with tests), run `python -m pytest tests -q` and `python -m bot.backtest --config configs/challenger<k>.yaml --gate`, put the metrics and the skill line in the ledger entry (the gate line must say PASS), remove the idea from the backlog, delete any scratch files, and commit with first line `H<n>: <title>`.
6. Before committing, run `git diff --name-only origin/main` and confirm nothing listed in PROTECTED.txt appears and at most one configs/challenger<k>.yaml changed. If a protected file changed, revert it with `git checkout origin/main -- <path>`.
7. Commit with `git add -A && git commit -m "<message>"`. Do not push; the workflow pushes and opens the PR. If you made no changes at all, say so in one line and stop.

Finish with a short plain English summary of what you did and why.
