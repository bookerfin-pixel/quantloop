"""Gate 1: a pull request may not touch protected paths or add live trading or
credential code. Run from the PR checkout:

    python <base>/gate/check_protected.py --base origin/main --head HEAD [--protected <base>/PROTECTED.txt]

Exit 0 when clean, 1 with a list of violations otherwise.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

# Any of these appearing in an ADDED line of a .py/.yaml/.yml/.toml/.json/.sh file
# fails the gate. They are the fingerprints of live order placement and secrets.
FORBIDDEN = [
    r"create_order", r"createOrder", r"AddOrder", r"new_order", r"place_order", r"submit_order",
    r"/api/v3/order", r"/0/private/", r"API-Sign", r"X-MBX-APIKEY",
    r"api_key\s*=", r"apiKey\s*=", r"api_secret", r"secret_key", r"SECRET_KEY",
    r"withdraw", r"private_key", r"ccxt\.[a-z]+\(\{",
]
CODE_EXT = (".py", ".yaml", ".yml", ".toml", ".json", ".sh", ".cfg", ".ini")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def load_patterns(path: Path) -> list[str]:
    pats = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            pats.append(line)
    return pats


def matches(path: str, pattern: str) -> bool:
    if pattern.endswith("/**"):
        root = pattern[:-3]
        return path == root or path.startswith(root + "/")
    return fnmatch.fnmatch(path, pattern) or path == pattern


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--head", default="HEAD")
    ap.add_argument("--protected", default=None, help="PROTECTED.txt to enforce (defaults to the base branch copy)")
    args = ap.parse_args(argv)

    merge_base = git("merge-base", args.base, args.head).strip()
    changed = [p for p in git("diff", "--name-only", merge_base, args.head).splitlines() if p]
    if args.protected:
        patterns = load_patterns(Path(args.protected))
    else:
        patterns = [ln.strip() for ln in git("show", f"{merge_base}:PROTECTED.txt").splitlines()
                    if ln.strip() and not ln.strip().startswith("#")]

    violations: list[str] = []
    for path in changed:
        for pat in patterns:
            if matches(path, pat):
                violations.append(f"protected path changed: {path} (matches '{pat}')")
                break

    diff = git("diff", "--unified=0", merge_base, args.head)
    current_file = None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            current_file = line[4:].removeprefix("b/")
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        if current_file and current_file.endswith(CODE_EXT):
            for pat in FORBIDDEN:
                if re.search(pat, line):
                    violations.append(f"forbidden token /{pat}/ added in {current_file}: {line[1:].strip()[:80]}")
                    break

    print(f"changed files ({len(changed)}):")
    for p in changed:
        print(f"  {p}")
    if violations:
        print("\nGATE FAILED: protected paths or forbidden code")
        for v in violations:
            print(f"  - {v}")
        return 1
    print("\nprotected check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
