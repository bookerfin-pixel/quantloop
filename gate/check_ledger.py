"""Gate 2: a change to a challenger config or the strategy code must come with
exactly one new, complete ledger entry whose id matches the changed slot's
config, and a PR may fill only one slot. And FINDINGS.md stays under
FINDINGS_CAP characters: a PR that leaves it over that and longer than it was
fails, whatever else it changes. One exception to the first (2026-11-15): an
idea put on paper in the nursery (configs/nursery/) may bring a strategy of
its own with no slot and no ledger entry, as long as the code of every
strategy the champion or a slot runs is the same as before, to the last node
of its syntax: a running test's code never changes mid window. Run from the
PR checkout:

    python <base>/gate/check_ledger.py --base origin/main --head HEAD

The point is not bureaucracy. A hypothesis that cannot be written down with an
expected effect and a kill rule before the test is not a hypothesis, it is a
tweak, and tweaks are how the last bot fitted itself to noise.
"""
from __future__ import annotations

import argparse
import ast
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

import yaml

CHALLENGER_GLOB = "configs/challenger*.yaml"
NURSERY_GLOB = "configs/nursery/*.yaml"
IN_USE = ["configs/champion.yaml", CHALLENGER_GLOB]       # the configs whose strategies run in an account
STRATEGY_PATH = "bot/strategy.py"
REQUIRED_FIELDS = ["Date", "Hypothesis", "Change", "Why it should work",
                   "Expected gross bps per round trip", "Kill criteria", "Backtest", "Bench", "Status"]
FIELDS = REQUIRED_FIELDS + ["Differs from running tests"]       # every field the format names (LEDGER_FORMAT.md)
ENTRY_RE = re.compile(r"^## (H\d+)\b", re.M)
FINDINGS = "FINDINGS.md"
FINDINGS_CAP = 30_000       # characters. The agent reads the whole file every day; past this it condenses before it adds
                            # (CLAUDE.md, the bookkeeping step). An idea from phil, another agent's repo, whose memory
                            # file grew without end. FINDINGS.md was 77,865 characters on 2026-11-03, 55,401 of them
                            # measurements of the machinery, which moved to MACHINERY.md and left about 16,300


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


def strategy_codes(text: str) -> dict[str, str]:
    """Each strategy registered in a bot/strategy.py text, as the code it runs: the syntax of its own function,
    of every function or class of the module it reaches by name, and of every module level statement that
    defines a name it reaches (a constant, an import), so that a change to anything it runs shows and a change
    to another strategy, to the module's docstring or to a comment does not (as bench.strategy_code reads it)."""
    tree = ast.parse(text)
    named, defines = {}, {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            named[node.name] = node
            continue
        targets = []
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            targets = [(a.asname or a.name).split(".")[0] for a in node.names]
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            for target in (node.targets if isinstance(node, ast.Assign) else [node.target]):
                targets += [n.id for n in ast.walk(target) if isinstance(n, ast.Name)]
        for name in targets:
            defines.setdefault(name, []).append(node)
    out = {}
    for node in list(named.values()):
        for d in getattr(node, "decorator_list", []):
            func = getattr(d, "func", None)
            if not (isinstance(d, ast.Call) and getattr(func, "id", getattr(func, "attr", None)) == "register"
                    and d.args and isinstance(d.args[0], ast.Constant)):
                continue
            reach, todo = set(), [node.name]
            while todo:
                name = todo.pop()
                if name in reach:
                    continue
                reach.add(name)
                for part in ([named[name]] if name in named else []) + defines.get(name, []):
                    todo += [n.id for n in ast.walk(part) if isinstance(n, ast.Name)]
            parts = [named[n] for n in sorted(reach) if n in named]
            parts += [s for s in tree.body if any(s in defines.get(n, []) for n in reach)]
            out[str(d.args[0].value)] = "".join(ast.dump(s) for s in parts)
    return out


def strategies_in_use(merge_base: str) -> set[str]:
    """The strategies the champion and every slot run, as their configs stood at the merge base."""
    out = set()
    for path in git("ls-tree", "-r", "--name-only", merge_base, "configs").splitlines():
        if any(fnmatch.fnmatch(path, pattern) for pattern in IN_USE):
            try:
                cfg = yaml.safe_load(git("show", f"{merge_base}:{path}")) or {}
            except Exception:  # noqa: BLE001 - a config that cannot be read names no strategy
                continue
            if isinstance(cfg, dict) and isinstance(cfg.get("strategy"), str):
                out.add(cfg["strategy"])
    return out


def nursery_problem(merge_base: str) -> str | None:
    """For a pull request that changes bot/strategy.py along with an idea in the nursery and no slot: the
    sentence when it changes the code of a strategy the champion or a slot runs, or None when it does not."""
    try:
        base = strategy_codes(git("show", f"{merge_base}:{STRATEGY_PATH}"))
        head = strategy_codes(Path(STRATEGY_PATH).read_text())
    except SyntaxError as e:
        return f"{STRATEGY_PATH} cannot be read as Python ({e})"
    moved = sorted(s for s in strategies_in_use(merge_base) if s in base and base[s] != head.get(s))
    if not moved:
        return None
    return (f"{STRATEGY_PATH} changes the code of {', '.join(moved)}, which the champion or a slot runs: a nursery "
            f"idea may bring a strategy of its own, never change one a running test uses mid window")


def findings_problem(merge_base: str) -> str | None:
    """FINDINGS.md over FINDINGS_CAP characters and longer than it was at the
    merge base. A pull request that leaves it as it was, or makes it shorter,
    passes whatever its size, so a file already over the cap is condensed
    over as many runs as it takes and blocks nothing else meanwhile."""
    head = Path(FINDINGS).read_text() if Path(FINDINGS).exists() else ""
    base = git("show", f"{merge_base}:{FINDINGS}") if FINDINGS in git("ls-tree", "--name-only", merge_base) else ""
    if len(head) <= FINDINGS_CAP or len(head) <= len(base):
        return None
    return (f"{FINDINGS} is {len(head):,} characters, over the cap of {FINDINGS_CAP:,}, and this pull request makes it "
            f"longer (it was {len(base):,}). Condense it first, as CLAUDE.md's bookkeeping step says, then add")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--head", default="HEAD")
    args = ap.parse_args(argv)
    merge_base = git("merge-base", args.base, args.head).strip()
    changed = [p for p in git("diff", "--name-only", merge_base, args.head).splitlines() if p]
    challenger_files = [p for p in changed if fnmatch.fnmatch(p, CHALLENGER_GLOB)]
    nursery_files = [p for p in changed if fnmatch.fnmatch(p, NURSERY_GLOB)]
    strategy_touched = STRATEGY_PATH in changed
    too_long = findings_problem(merge_base)
    if strategy_touched and not challenger_files and nursery_files:
        problems = [p for p in (too_long, nursery_problem(merge_base)) if p]
        if problems:
            print("GATE FAILED: ledger")
            for p in problems:
                print(f"  - {p}")
            return 1
        print(f"a nursery idea ({', '.join(nursery_files)}) with a strategy of its own; no strategy a test runs "
              f"changed; ledger check not required")
        return 0
    if not challenger_files and not strategy_touched:
        if too_long:
            print(f"GATE FAILED: ledger\n  - {too_long}")
            return 1
        print("no strategy or challenger change; ledger check not required")
        return 0

    problems = [too_long] if too_long else []
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
