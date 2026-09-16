# state

Written by the hourly workflow. Do not edit by hand and never in a PR.

    champion/     account.json, decisions.csv, trades.csv, equity.csv
    challenger/   the same, plus meta.json (slot status and test start)
    candles/      one CSV per pair, hourly, grows every run
    archive/      challenger accounts from finished tests, one folder per hypothesis
    summary.md    what the agent reads first each day
