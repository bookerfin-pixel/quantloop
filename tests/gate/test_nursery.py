"""PROTECTED. The nursery (bot/nursery.py): that it takes every idea under configs/nursery and says which it
cannot, that an idea is seen from the day it first appears and again only when it changes, that the days since
are read as a test's are (whole days, the basket held from that day, skill at the usual exposure of the hours
before, the early kill), and that it ranks without promoting and stays apart from the hourly loop."""
import json
import re
from pathlib import Path

import numpy as np
import pytest

from bot import config, nursery, promote

REPO = Path(__file__).resolve().parents[2]
DAY0 = 1_790_000_000 // 86400 * 86400                 # a UTC midnight
RULES = config.load_yaml(REPO / "configs" / "risk.yaml")["challenger"]


@pytest.fixture
def root(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "CONFIGS", tmp_path / "configs")
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    (tmp_path / "configs" / "nursery").mkdir(parents=True)
    return tmp_path


def write(root: Path, name: str, text: str) -> None:
    (root / "configs" / "nursery" / name).write_text(text, encoding="utf-8")


GOOD = "hypothesis: {h}\nstrategy: ts_momentum\nparams:\n  lookback_hours: {lb}\n"


def test_every_config_under_configs_nursery_is_an_idea_and_one_that_cannot_be_taken_is_said(root):
    write(root, "H7.yaml", GOOD.format(h="H7", lb=720))
    write(root, "H8.yaml", "hypothesis: H8\nstrategy: ts_momentum\n")                     # no params
    write(root, "H9.yaml", GOOD.format(h="H10", lb=720))                                  # not its file's name
    write(root, "H11.yaml", "hypothesis: H11\nstrategy: no_such_strategy\nparams: {}\n")
    write(root, "H12.yaml", "hypothesis: [\n")                                            # not yaml at all
    found, problems = nursery.ideas()
    assert [name for name, _ in found] == ["H7"]
    assert len(problems) == 4 and all(p.startswith("FAILED: configs/nursery/") for p in problems)
    assert any("H9.yaml" in p and "not its file's name" in p for p in problems)
    assert any("H8.yaml" in p and "'params'" in p for p in problems)


def test_an_idea_is_seen_from_the_day_it_first_appears_and_again_only_when_it_changes(root):
    write(root, "H7.yaml", GOOD.format(h="H7", lb=720))
    found, _ = nursery.ideas()
    seen = nursery.stamp({}, found, "2026-11-15")
    assert seen["H7"]["seen"] == "2026-11-15" and re.fullmatch(r"[0-9a-f]{16}", seen["H7"]["signature"])
    assert nursery.stamp(seen, found, "2026-11-20")["H7"]["seen"] == "2026-11-15"          # unchanged: the same day
    write(root, "H7.yaml", GOOD.format(h="H7", lb=360))
    changed, _ = nursery.ideas()
    again = nursery.stamp(seen, changed, "2026-11-20")
    assert again["H7"]["seen"] == "2026-11-20" and again["H7"]["signature"] != seen["H7"]["signature"]
    assert nursery.stamp(again, [], "2026-11-21") == again                                 # gone from file: its line stays
    # a date written in the config itself counts for nothing
    write(root, "H7.yaml", GOOD.format(h="H7", lb=360) + "seen: 2020-01-01\n")
    dated, _ = nursery.ideas()
    assert nursery.stamp({}, dated, "2026-11-22")["H7"]["seen"] == "2026-11-22"


def series(days=10, pairs=2, seed=1, held=0.5, crash_day=None):
    """A replay as bench.series leaves it: `days` whole UTC days of hours from DAY0 and one hour of the next."""
    rng = np.random.default_rng(seed)
    n = days * 24 + 1
    r = rng.normal(0.0, 0.002, (n, pairs))
    if crash_day is not None:
        r[crash_day * 24 + 5, 0] = -0.5                    # pair 0 halves in one hour; the basket holds both pairs
    w = np.zeros((n, pairs))
    w[:, 0] = held
    c = np.zeros(n)
    c[[3, 30, 100]] = 0.001
    return {"ts": DAY0 + 3600 * np.arange(n), "starts": np.arange(0, n, 24), "held": w, "w": w, "r": r,
            "hourly": (w * r).sum(axis=1), "c": c, "valid": np.ones((n, pairs), dtype=bool),
            "fills": np.arange(days + 1) % 3}


def test_a_reading_is_the_whole_days_since_the_day_first_seen_read_as_a_test_is():
    s = series()
    out = nursery.reading(s, DAY0 + 4 * 86400, RULES)
    assert out["days"] == 6                                     # days 4 to 9: day 10 has one hour so far
    h0, h1 = 4 * 24, 10 * 24
    net = np.prod((1 + s["hourly"][h0:h1]) * (1 - s["c"][h0:h1])) - 1
    basket = np.prod(1 + s["r"][h0:h1], axis=0).mean() - 1
    assert out["net"] == pytest.approx(net) and out["basket"] == pytest.approx(basket)
    assert out["usual"] == pytest.approx(0.5) and out["skill"] == pytest.approx(net - 0.5 * basket)
    assert out["fills"] == int(s["fills"][4:10].sum()) and out["early_kill_day"] is None
    assert out["skill_t"] is not None and out["confidence"] == promote.confidence(out["skill_t"], 6, RULES)
    assert -1 < out["max_drawdown"] <= 0 and out["costs"] == pytest.approx(0.001 * np.prod(1 + (s["hourly"] - s["c"] * (1 + s["hourly"]))[h0:100]), rel=1e-9)


def test_the_early_kill_is_the_hour_it_had_lost_more_than_the_limit_and_more_than_the_market():
    out = nursery.reading(series(crash_day=6, held=0.4), DAY0 + 4 * 86400, RULES)
    # held at 0.4, a halving loses it 20%, past 15%, while the basket of both pairs lost about 25%: no kill
    assert out["early_kill_day"] is None
    out = nursery.reading(series(crash_day=6, held=0.9), DAY0 + 4 * 86400, RULES)
    # held at 0.9 the same hour loses it 45%, more than the basket's 25%: ended in that hour, 2 days and 6
    # hours after the day first seen
    assert out["early_kill_day"] == pytest.approx((2 * 24 + 6) / 24)
    assert nursery.reading(series(), DAY0 + 10 * 86400, RULES)["days"] == 0              # nothing whole yet
    assert nursery.reading(series(), DAY0 + 4 * 86400 + 1800, RULES)["days"] == 0        # not the start of a day


def test_the_leader_is_the_most_confident_idea_with_sixty_days_in_no_slot_and_not_ended_by_the_early_kill():
    rows = [{"idea": "A", "days": 90, "confidence": 0.30, "slot": "challenger1", "early_kill_day": None},
            {"idea": "B", "days": 90, "confidence": 0.25, "slot": None, "early_kill_day": 40.0},
            {"idea": "C", "days": 59, "confidence": 0.40, "slot": None, "early_kill_day": None},
            {"idea": "D", "days": 61, "confidence": 0.12, "slot": None, "early_kill_day": None},
            {"idea": "E", "days": 120, "confidence": 0.15, "slot": None, "early_kill_day": None},
            {"idea": "F", "days": 0, "slot": None}]
    assert nursery.leader(rows) == "E"
    assert nursery.leader(rows[:4]) == "D" and nursery.leader(rows[:3]) is None
    text = nursery.table(rows, ["FAILED: X could not be replayed (boom)"], "2026-11-15")
    assert "Next in line for a free slot: E" in text and "## Not read" in text and "- FAILED: X could not be replayed" in text
    assert text.index("| C |") < text.index("| A |") < text.index("| B |")               # by confidence, highest first
    assert "Nothing is promoted from here" in text


def test_it_is_protected_and_apart_from_the_hourly_loop():
    from gate import check_protected
    patterns = check_protected.load_patterns(REPO / "PROTECTED.txt")
    for path in ("bot/nursery.py", "tests/gate/test_nursery.py", ".github/workflows/nursery.yml", "state/nursery/seen.json"):
        assert any(check_protected.matches(path, p) for p in patterns), path
    assert not any(check_protected.matches("configs/nursery/H7.yaml", p) for p in patterns)   # the agent adds ideas
    src = (REPO / "bot" / "nursery.py").read_text(encoding="utf-8")
    for pat in check_protected.FORBIDDEN:
        assert not re.search(pat, src), pat
    for module in ("__init__", "run", "promote", "report", "slot", "config", "data", "paper", "risk", "shadow",
                   "backtest", "strategy"):
        assert "nursery" not in (REPO / "bot" / f"{module}.py").read_text(encoding="utf-8"), module
    from tests.gate import hourly_driver
    assert "nursery" in hourly_driver.WATCHED            # a strategy that opened state/nursery would be seen doing it


def test_the_job_commits_under_the_benchs_word_so_the_daily_check_does_not_take_it_for_the_agent():
    job = (REPO / ".github" / "workflows" / "nursery.yml").read_text(encoding="utf-8")
    assert "python -m bot.nursery --save" in job and 'git commit -q -m "bench: nursery $(date -u +%Y-%m-%d)"' in job
    assert "group: nursery" in job and "cancel-in-progress: false" in job


def test_the_ideas_on_file_can_all_be_taken():
    found, problems = nursery.ideas()
    assert problems == [] and {name for name, _ in found} >= {"H0", "H1", "H2", "H4", "H5", "H6"}
    seen = json.loads((REPO / "state" / "nursery" / "seen.json").read_text(encoding="utf-8"))
    # the ideas seeded from the ledger are all there; an idea added since joins on the nursery's next run, so a
    # pull request that adds one cannot have it in seen.json yet (it once could not pass this test at all)
    assert set(seen) >= {"H0", "H1", "H2", "H4", "H5", "H6"}
    assert all(re.fullmatch(r"\d{4}-\d{2}-\d{2}", v["seen"]) for v in seen.values())
    assert nursery.YEAR_DAYS == 365 and nursery.LEADER_DAYS == RULES["window_days"]


# --- the gate: a nursery idea may bring a strategy of its own --------------------------------

STRATEGY = '''"""strategies"""
from dataclasses import dataclass

HOURS = 24
STRATEGIES = {}


def register(name):
    def wrap(fn):
        STRATEGIES[name] = fn
        return fn
    return wrap


@dataclass
class Target:
    weight: float
    reason: str


def helper(x):
    return x * HOURS


@register("ts_momentum")
def ts_momentum(candles, params, current_weights):
    return {p: Target(helper(0.0), "flat") for p in candles}


@register("mean_reversion")
def mean_reversion(candles, params, current_weights):
    return {p: Target(0.0, "flat") for p in candles}
'''


def gate_on(tmp_path, before: dict, after: dict):
    """main with the files in `before`, a branch that writes those in `after` (None removes one), and the
    gate's ledger check run on it as the gate runs it."""
    import os
    import subprocess
    import sys
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"HOME": str(tmp_path), "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})
    me = ("-c", "user.name=somebody", "-c", "user.email=somebody@example.com")
    repo = tmp_path / "repo"

    def git(*args, cwd=repo):
        subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True)

    repo.mkdir(parents=True)
    git("init", "-q", "-b", "main", str(repo), cwd=tmp_path)

    def put(files):
        for name, text in files.items():
            path = repo / name
            if text is None:
                path.unlink()
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)

    put({"LEDGER.md": "# Ledger\n\n## Results\n", "bot/strategy.py": STRATEGY,
         "configs/champion.yaml": "hypothesis: H0\nstrategy: ts_momentum\nparams: {}\n",
         "configs/challenger1.yaml": "hypothesis: H1\nstrategy: mean_reversion\nparams: {}\n", **before})
    git("add", "-A")
    git(*me, "commit", "-q", "-m", "base")
    git("checkout", "-q", "-b", "agent")
    put(after)
    git("add", "-A")
    git(*me, "commit", "-q", "-m", "H7: nursery: an idea")
    return subprocess.run([sys.executable, str(REPO / "gate" / "check_ledger.py"), "--base", "main", "--head", "HEAD"],
                          cwd=repo, env=env, capture_output=True, text=True)


NEW_ONE = STRATEGY + '''

import math


@register("new_one")
def new_one(candles, params, current_weights):
    return {p: Target(math.floor(0.0), "flat") for p in candles}
'''
IDEA = {"configs/nursery/H7.yaml": "hypothesis: H7\nstrategy: new_one\nparams: {}\n"}


def test_a_nursery_idea_may_bring_a_strategy_of_its_own_and_never_change_one_a_test_runs(tmp_path):
    ok = gate_on(tmp_path / "a", {}, {"bot/strategy.py": NEW_ONE, **IDEA})
    assert ok.returncode == 0 and "a nursery idea (configs/nursery/H7.yaml)" in ok.stdout, ok.stdout + ok.stderr
    plain = gate_on(tmp_path / "b", {}, IDEA)                       # an idea on a strategy already there
    assert plain.returncode == 0 and "ledger check not required" in plain.stdout, plain.stdout + plain.stderr
    moved = gate_on(tmp_path / "c", {}, {"bot/strategy.py": NEW_ONE.replace("return x * HOURS", "return x * HOURS * 2"), **IDEA})
    assert moved.returncode == 1 and "changes the code of ts_momentum, which the champion or a slot runs" in moved.stdout
    const = gate_on(tmp_path / "d", {}, {"bot/strategy.py": NEW_ONE.replace("HOURS = 24", "HOURS = 25"), **IDEA})
    assert const.returncode == 1 and "ts_momentum" in const.stdout and "mean_reversion" not in const.stdout.split("changes the code of")[1]
    alone = gate_on(tmp_path / "e", {}, {"bot/strategy.py": NEW_ONE})   # no idea, no slot: as before
    assert alone.returncode == 1 and "changed without a challenger config change" in alone.stdout
    broken = gate_on(tmp_path / "f", {}, {"bot/strategy.py": NEW_ONE + "\ndef (\n", **IDEA})
    assert broken.returncode == 1 and "cannot be read as Python" in broken.stdout
    docs = gate_on(tmp_path / "g", {}, {"bot/strategy.py": NEW_ONE.replace('"""strategies"""', '"""all the strategies"""'), **IDEA})
    assert docs.returncode == 0, docs.stdout                         # the module's docstring runs nothing
