"""PROTECTED. When the gate fails, the agent learns why. Each check's output is kept as it runs and the check still
fails when it fails; the last lines go out as the gate's `why`; and the closing comment quotes them without letting
any of them into a script, since they include whatever the proposal's own code printed. (Until 2026-11-20 the
comment held only a link to a log the agent cannot open, and H7 was closed on 2026-11-17 for a misplaced ledger
entry that its author never learned of.)"""
import os
import re
import stat
import subprocess
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WORKFLOWS = REPO / ".github" / "workflows"


def load(name: str) -> dict:
    return yaml.safe_load((WORKFLOWS / name).read_text(encoding="utf-8"))


def gate_steps() -> list[dict]:
    return load("gate.yml")["jobs"]["gate"]["steps"]


def run(script: str, env: dict, cwd: Path, pipefail: bool) -> subprocess.CompletedProcess:
    """A step's script as GitHub runs it: `shell: bash` is bash -eo pipefail, no shell at all is bash -e."""
    path = cwd / "step.sh"
    path.write_text(script, encoding="utf-8")
    flags = ["-eo", "pipefail"] if pipefail else ["-e"]
    return subprocess.run(["bash", "--noprofile", "--norc", *flags, str(path)], cwd=cwd, capture_output=True, text=True,
                          env={"PATH": os.environ["PATH"], **env})


def test_every_check_keeps_its_output_and_the_gate_hands_on_its_last_lines():
    gate = load("gate.yml")
    on = gate.get("on", gate.get(True))                  # yaml reads a bare `on` as true
    assert on["workflow_call"]["outputs"]["why"]["value"] == "${{ jobs.gate.outputs.why }}"
    job = gate["jobs"]["gate"]
    assert job["outputs"] == {"why": "${{ steps.why.outputs.why }}"}
    checks = [s for s in job["steps"] if re.match(r"\d\. ", s.get("name", ""))]
    assert [s["name"][:2] for s in checks] == ["1.", "2.", "3.", "4."]
    for s in checks:
        assert s["shell"] == "bash" and s["run"].startswith("set -o pipefail\n") and s["working-directory"] == "pr"
        assert re.search(r'2>&1 \| tee -a "\$RUNNER_TEMP/gate\.log"\n$', s["run"]), s["name"]
    assert job["steps"][-1]["id"] == "why" and job["steps"][-1]["if"] == "failure()"


def test_a_failing_check_still_fails_the_gate_and_its_words_are_kept(tmp_path):
    ledger = next(s for s in gate_steps() if s.get("name", "").startswith("2. "))
    command = "python ../base/gate/check_ledger.py --base origin/main --head HEAD"
    assert command in ledger["run"]
    env = {"RUNNER_TEMP": str(tmp_path)}
    failing = ledger["run"].replace(command, "( printf 'GATE FAILED: ledger\\n  - expected exactly one new entry, found 0\\n'; exit 1 )")
    done = run(failing, env, tmp_path, pipefail=True)
    assert done.returncode != 0 and "GATE FAILED: ledger" in done.stdout              # tee does not swallow the failure
    log = (tmp_path / "gate.log").read_text()
    assert log.startswith("== 2. Ledger entry ==\n") and "found 0" in log
    passing = ledger["run"].replace(command, "echo 'ledger check passed'")
    assert run(passing, env, tmp_path, pipefail=True).returncode == 0


def outputs(path: Path) -> dict[str, str]:
    """GitHub's reading of a step's output file, for the name<<delimiter form."""
    out, lines = {}, path.read_text().split("\n")
    i = 0
    while i < len(lines):
        m = re.fullmatch(r"([A-Za-z_]+)<<(.+)", lines[i])
        if m:
            end = lines.index(m.group(2), i + 1)
            out[m.group(1)] = "\n".join(lines[i + 1:end])
            i = end
        i += 1
    return out


def test_the_last_lines_go_out_under_a_delimiter_nothing_the_proposal_printed_can_guess(tmp_path):
    why = gate_steps()[-1]
    (tmp_path / "gate.log").write_text("\n".join(f"line {i}" for i in range(100)) + "\nGATE_SAID_0000\n" + "x" * 500 + "\nGATE FAILED: ledger\r\n")
    env = {"RUNNER_TEMP": str(tmp_path), "GITHUB_OUTPUT": str(tmp_path / "out")}
    assert run(why["run"], env, tmp_path, pipefail=True).returncode == 0
    text = (tmp_path / "out").read_text()
    assert re.match(r"why<<GATE_SAID_[0-9a-f]{32}\n", text)
    said = outputs(tmp_path / "out")["why"].split("\n")
    assert len(said) == 60 and said[0] == "line 43" and said[-1] == "GATE FAILED: ledger"       # the last 60, no \r
    assert "GATE_SAID_0000" in said and max(len(x) for x in said) == 300
    (tmp_path / "gate.log").unlink()
    (tmp_path / "out").unlink()
    run(why["run"], env, tmp_path, pipefail=True)
    assert outputs(tmp_path / "out")["why"] == "the gate stopped before its first check (checkout or install failed)"


def fake_gh(folder: Path) -> Path:
    """A `gh` that notes how it was called, answers the two reads of the fallback, and does nothing else."""
    folder.mkdir()
    gh = folder / "gh"
    gh.write_text("#!/bin/bash\n"
                  'printf "%s\\n" "$*" >> "$GH_CALLS"\n'
                  'case "$*" in\n'
                  '  *"/runs/"*"/jobs"*) echo 4242 ;;\n'
                  '  *"/jobs/4242/logs"*) printf "setup\\nGATE FAILED: tests\\n" ;;\n'
                  "esac\n")
    gh.chmod(gh.stat().st_mode | stat.S_IEXEC)
    return folder


def test_the_closing_comment_quotes_the_gate_and_keeps_its_words_out_of_the_script(tmp_path):
    reject = load("agent.yml")["jobs"]["reject"]
    step = reject["steps"][0]
    assert reject["permissions"] == {"contents": "write", "pull-requests": "write", "actions": "read"}
    assert step["env"]["WHY"] == "${{ needs.gate.outputs.why }}" and step["env"]["RESULT"] == "${{ needs.gate.result }}"
    assert "${{" not in step["run"]                      # nothing is pasted into the script before it runs
    bin_ = fake_gh(tmp_path / "bin")
    work = tmp_path / "work"
    work.mkdir()
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "GH_CALLS": str(tmp_path / "calls"), "PR": "63", "RESULT": "failure",
           "RUN_URL": "https://github.com/o/r/actions/runs/1", "GITHUB_REPOSITORY": "o/r", "GITHUB_RUN_ID": "1",
           "RUNNER_TEMP": str(tmp_path), "GITHUB_STEP_SUMMARY": str(tmp_path / "summary"),
           "WHY": "== 2. Ledger entry ==\nGATE FAILED: ledger\n$(touch pwned) `touch pwned2` ${HOME}"}
    done = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c", step["run"]], cwd=work, env=env, capture_output=True, text=True)
    assert done.returncode == 0, done.stderr
    comment = (tmp_path / "comment.md").read_text()
    assert comment.startswith("Gate failed (result: failure). Details: https://github.com/o/r/actions/runs/1 .")
    assert "GATE FAILED: ledger\n$(touch pwned) `touch pwned2` ${HOME}\n```" in comment and "gh pr diff 63" in comment
    assert not (work / "pwned").exists() and not (work / "pwned2").exists()
    calls = (tmp_path / "calls").read_text().splitlines()
    assert calls == [f"pr comment 63 --repo o/r --body-file {tmp_path}/comment.md", "pr close 63 --repo o/r --delete-branch"]
    # no lines came through: the end of the gate job's own log is read instead
    (tmp_path / "calls").unlink()
    done = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c", step["run"]], cwd=work, env={**env, "WHY": ""},
                          capture_output=True, text=True)
    assert done.returncode == 0, done.stderr
    assert "setup\nGATE FAILED: tests\n```" in (tmp_path / "comment.md").read_text()
    assert (tmp_path / "calls").read_text().splitlines()[1] == "api repos/o/r/actions/jobs/4242/logs"
