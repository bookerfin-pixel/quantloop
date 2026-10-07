"""Gate 2: a change to a challenger config or the strategy code must come with
exactly one new, complete ledger entry whose id matches the changed slot's
config, and a PR may fill only one slot. Run from the PR checkout:

    python <base>/gate/check_ledger.py --base origin/main --head HEAD

The point is not bureaucracy. A hypothesis that cannot be written down with an
expected effect and a kill rule before the test is not a hypothesis, it is a
tweak, and tweaks are how the last bot fitted itself to noise.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

import yaml

CHALLENGER_GLOB = "configs/challenger*.yaml"
STRATEGY_PATH = "bot/strategy.py"
REQUIRED_FIELDS = ["Date", "Hypothesis", "Change", "Why it should work",
                   "Expected gross bps per round trip", "Kill criteria", "Backtest", "Bench", "Status"]
FIELDS = REQUIRED_FIELDS + ["Differs from running tests"]       # every field the format names (LEDGER_FORMAT.md)
ENTRY_RE = re.compile(r"^## (H\d+)\b", re.M)


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def entries(text: str) -> dict[str, str]:
    out = {}
    text = text.split("\n## Results")[0]
    matches = list(ENTRY_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[m.group(1)] = text[m.start():end]
    return out


def said(body: str, field: str) -> str | None:
    """What an entry says under a field: the rest of the field's own line and
    the lines straight under it, up to the next field the format names, a
    heading or a blank line. None when the entry has no such field. A field
    left blank is not filled by the field under it (with `\\s*` after the
    colon it was, so an entry could leave any field empty; found 2026-10-07,
    when Bench was added), and figures written under a field's name still
    count as that field's, whether they are indented or set out as a list
    of `- ` lines (each mend for the first let one of those through as
    empty; found in review the same day)."""
    stop = "|".join(re.escape(f) for f in FIELDS)
    m = re.search(rf"^- {re.escape(field)}:[ \t]*(.*(?:\n(?!- (?:{stop}):|#|[ \t]*$).*)*)", body, re.M)
    return None if not m else m.group(1).strip()


def bench_line(text: str) -> bool:
    """Is this what a Bench field should hold: the bench's own last line, or
    `not taken:` and a reason no reading could be taken? `n/a` is neither.
    The line may be wrapped by hand, and a few words of reason are enough:
    asking for twenty characters turned away `not taken: timed out`, and the
    agent cannot read why the gate said no (found in review, 2026-10-07)."""
    text = " ".join(text.split())
    own = "twins" in text and "in sample" in text.lower()
    why_not = re.match(r"`?not taken\b:?`?\W*(.*)", text, re.I | re.S)
    return own or bool(why_not and len(why_not.group(1).strip()) >= 3)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--head", default="HEAD")
    args = ap.parse_args(argv)
    merge_base = git("merge-base", args.base, args.head).strip()
    changed = [p for p in git("diff", "--name-only", merge_base, args.head).splitlines() if p]
    challenger_files = [p for p in changed if fnmatch.fnmatch(p, CHALLENGER_GLOB)]
    strategy_touched = STRATEGY_PATH in changed
    if not challenger_files and not strategy_touched:
        print("no strategy or challenger change; ledger check not required")
        return 0

    problems = []
    if len(challenger_files) > 1:
        problems.append(f"one hypothesis per pull request: {len(challenger_files)} challenger configs changed "
                        f"({', '.join(challenger_files)})")
    base_text = git("show", f"{merge_base}:LEDGER.md") if "LEDGER.md" in git("ls-tree", "--name-only", merge_base) else ""
    head_text = Path("LEDGER.md").read_text() if Path("LEDGER.md").exists() else ""
    new_ids = [h for h in entries(head_text) if h not in entries(base_text)]
    if len(new_ids) != 1:
        problems.append(f"expected exactly one new '## H<n>' ledger entry, found {len(new_ids)}: {new_ids}")
    if challenger_files and new_ids:
        cfg = yaml.safe_load(Path(challenger_files[0]).read_text()) or {}
        hyp = str(cfg.get("hypothesis"))
        if hyp != new_ids[0]:
            problems.append(f"{challenger_files[0]} hypothesis is {hyp!r} but the new ledger entry is {new_ids[0]!r}")
    if strategy_touched and not challenger_files:
        problems.append("bot/strategy.py changed without a challenger config change; a strategy change must be "
                        "tested through a slot, so also point one challenger config at it")
    if new_ids:
        body = entries(head_text)[new_ids[0]]
        for field in REQUIRED_FIELDS:
            text = said(body, field)
            if text is None or len(text) < 3:
                problems.append(f"ledger entry {new_ids[0]} is missing a filled '- {field}:' line")
        bench = said(body, "Bench")
        if bench is not None and len(bench) >= 3 and not bench_line(bench):
            problems.append(f"ledger entry {new_ids[0]}: the '- Bench:' line must carry the line the bench printed "
                            f"(the one that begins `Bench:` and ends `In sample.`), or begin `not taken:` and say in a "
                            f"few words why the reading could not be taken")
        st = re.search(r"^- Status:[ \t]*(\w+)", body, re.M)
        if st and st.group(1) != "testing":
            problems.append(f"new ledger entry must have 'Status: testing', found {st.group(1)!r}")
        bps = re.search(r"^- Expected gross bps per round trip:[ \t]*([0-9.]+)", body, re.M)
        if not bps:
            problems.append("'Expected gross bps per round trip' must start with a number")
        elif float(bps.group(1)) < 60:
            problems.append(f"expected gross bps per round trip is {bps.group(1)}; the round trip cost is ~30 bps, "
                            "so anything under 60 has no margin for being wrong. Change the hypothesis, not the number.")
    if problems:
        print("GATE FAILED: ledger")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"ledger check passed: new entry {new_ids[0]} matches {challenger_files[0] if challenger_files else 'the strategy change'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
