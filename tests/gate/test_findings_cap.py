"""PROTECTED. FINDINGS.md stays short enough for the agent to read whole every day: the gate's ledger
check (gate/check_ledger.py) fails a pull request that leaves it over FINDINGS_CAP characters and longer
than it was. An idea from phil, another agent's repo, whose memory file grew without end; FINDINGS.md had
reached 77,865 characters by 2026-11-03, 55,401 of them measurements of the machinery, which moved to
MACHINERY.md."""
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("check_ledger", REPO / "gate" / "check_ledger.py")
check_ledger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_ledger)
CAP = check_ledger.FINDINGS_CAP


def git(cwd, *args, env):
    subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True)


def gate_on(tmp_path, before, after, also=None):
    """main with FINDINGS.md as `before` (None: no such file), a branch with it as `after` and the files in
    `also` written, and the gate's own check run on it as the gate runs it."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"HOME": str(tmp_path), "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})
    me = ("-c", "user.name=somebody", "-c", "user.email=somebody@example.com")
    repo = tmp_path / "repo"
    (repo / "notes").mkdir(parents=True)
    git(tmp_path, "init", "-q", "-b", "main", str(repo), env=env)
    (repo / "LEDGER.md").write_text("# Ledger\n\n## Results\n")
    (repo / "notes" / "README.md").write_text("notes\n")
    if before is not None:
        (repo / "FINDINGS.md").write_text(before)
    git(repo, "add", "-A", env=env)
    git(repo, *me, "commit", "-q", "-m", "base", env=env)
    git(repo, "checkout", "-q", "-b", "agent", env=env)
    (repo / "FINDINGS.md").write_text(after)
    for name, text in (also or {}).items():
        (repo / name).parent.mkdir(parents=True, exist_ok=True)
        (repo / name).write_text(text)
    git(repo, "add", "-A", env=env)
    git(repo, *me, "commit", "-q", "-m", "notes: today", env=env)
    return subprocess.run([sys.executable, str(REPO / "gate" / "check_ledger.py"), "--base", "main", "--head", "HEAD"],
                          cwd=repo, env=env, capture_output=True, text=True)


def test_findings_may_grow_up_to_the_cap_and_no_further(tmp_path):
    note = {"notes/2026-11-04.md": "# 2026-11-04\n\nnothing new\n"}
    ok = gate_on(tmp_path / "a", "x" * 1000, "x" * CAP, note)
    assert ok.returncode == 0 and "ledger check not required" in ok.stdout, ok.stdout + ok.stderr
    over = gate_on(tmp_path / "b", "x" * 1000, "x" * (CAP + 1), note)
    assert over.returncode == 1 and over.stdout.startswith("GATE FAILED: ledger"), over.stdout + over.stderr
    assert (f"FINDINGS.md is {CAP + 1:,} characters, over the cap of {CAP:,}, and this pull request makes it longer (it was 1,000). "
            f"Condense it first, as CLAUDE.md's bookkeeping step says, then add") in over.stdout
    born = gate_on(tmp_path / "c", None, "x" * (CAP + 1))                  # a file that was not there at all is longer than nothing
    assert born.returncode == 1 and "(it was 0)" in born.stdout
    # it counts characters, not bytes: a finding in other alphabets is not cut shorter for it
    assert gate_on(tmp_path / "d", "x", "é" * CAP).returncode == 0


def test_findings_over_the_cap_blocks_nothing_that_does_not_lengthen_it(tmp_path):
    """Already over the cap (a patch of Fin's could put it there): a pull request that leaves it alone or
    shortens it passes, so it can be condensed over as many runs as it takes and nothing else waits on it."""
    big = "y" * (CAP + 5000)
    same = gate_on(tmp_path / "a", big, big, {"notes/2026-11-04.md": "a note\n"})
    assert same.returncode == 0, same.stdout + same.stderr
    shorter = gate_on(tmp_path / "b", big, big[:-100])
    assert shorter.returncode == 0, shorter.stdout + shorter.stderr
    longer = gate_on(tmp_path / "c", big, big + "z")
    assert longer.returncode == 1 and f"over the cap of {CAP:,}, and this pull request makes it longer (it was {len(big):,})" in longer.stdout


def test_a_proposal_that_lengthens_findings_past_the_cap_fails_with_its_other_problems(tmp_path):
    entry = ("## H2: a new one\n\n- Date: 2026-11-04\n- Hypothesis: something.\n- Change: configs/challenger1.yaml runs it.\n"
             "- Why it should work: a reason.\n- Expected gross bps per round trip: 120\n- Kill criteria: the rule.\n"
             "- Backtest: the metrics.\n- Bench: not taken: no time\n- Status: testing\n\n")
    files = {"LEDGER.md": "# Ledger\n\n" + entry + "## Results\n", "configs/challenger1.yaml": "hypothesis: H2\nstrategy: b\nparams: {}\n"}
    good = gate_on(tmp_path / "a", "x", "x" * 10, files)
    assert good.returncode == 0 and "ledger check passed: new entry H2" in good.stdout, good.stdout + good.stderr
    bad = gate_on(tmp_path / "b", "x", "x" * (CAP + 1), files)
    assert bad.returncode == 1 and "over the cap of" in bad.stdout and "ledger check passed" not in bad.stdout


def flat(text: str) -> str:
    return " ".join(text.split())


def test_the_measurements_live_apart_and_the_manual_says_how_to_keep_findings_short():
    """What FINDINGS.md holds is the agent's to write, so its size is held by the gate's ledger check and by
    nothing here: a test that read its size would fail every pull request, notes and all, from the day it
    grew past what the test allowed, and the agent cannot mend a protected test (found in review, 2026-11-03)."""
    assert "## How the machinery shapes results" not in (REPO / "FINDINGS.md").read_text()
    assert (REPO / "MACHINERY.md").read_text().startswith("# How the machinery shapes results")
    assert "MACHINERY.md" in (REPO / "PROTECTED.txt").read_text().splitlines()
    manual, sheet = flat((REPO / "CLAUDE.md").read_text()), flat((REPO / ".github" / "agent_prompt.md").read_text())
    for text in (manual, sheet):
        assert f"{CAP:,} characters" in text and "wc -m FINDINGS.md" in text
    assert "MACHINERY.md" in manual and "never add to it" in manual
    assert "Never shorten the Calibration section, and never drop a finding" in manual


def test_the_agent_reviews_its_own_calls_once_a_week():
    manual, sheet = flat((REPO / "CLAUDE.md").read_text()), flat((REPO / ".github" / "agent_prompt.md").read_text())
    for text in (manual, sheet):
        assert "no note dated since the last Monday (UTC) has a `## Weekly review` section" in text
        assert "below any lines for Fin at its top" in text
    assert "keep (it held up), sharpen" in manual and "or revert (wrong: say why)" in manual
    assert "a finding that was wrong moves to `## Overturned` with the reason, it is not deleted" in manual
    assert "score your own forecasts" in manual and "a ledger entry is never rewritten" in manual


def test_no_slot_goes_to_an_idea_the_bench_reads_as_no_sign_of_timing():
    manual, sheet = flat((REPO / "CLAUDE.md").read_text()), flat((REPO / ".github" / "agent_prompt.md").read_text())
    assert "does not go in a slot, not even under the idle slot rule below" in manual
    assert "leave the slot in cash and say so in the note" in manual and "one whose reading could not be taken does not qualify here" in manual
    assert "An idea that reads as nothing may still run under the idle slot rule" not in manual
    # the step that spends a slot reads the idea on the bench before the tests and the long backtest
    step = next(ln for ln in (REPO / ".github" / "agent_prompt.md").read_text().splitlines() if ln.startswith("8. If a slot is free"))
    bench_at, tests_at = step.index("python -m bot.bench --config"), step.index("python -m pytest tests -q")
    assert bench_at < tests_at < step.index("python -m bot.backtest") and "leave the slot in cash and say why in the note" in sheet
    assert "as soon as the slot's config points at the idea and before the tests and the long backtest" in manual
