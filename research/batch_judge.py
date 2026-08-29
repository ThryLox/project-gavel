"""
Batch judge pass, reused across repeats 1-3 for the variance study.

Reads saved gavel.py log transcripts (no re-querying targets - zero extra API cost on the
target side), extracts each rule's raw [Output] text, and re-judges every (transcript, rule)
pair with a single consistent judge model - so all three repeats are comparable on the same
judge, rather than repeat 1's live-judged numbers and repeats 2/3's numbers coming from
different processes.

Judge routing: Claude Haiku 4.5 for every target EXCEPT when the target being judged is itself
claude-haiku-4-5 - target-vs-judge separation requires a model never grade its own output, so
Claude's own two cells (both personas) are judged by Gemini instead.

Usage: python research/batch_judge.py
Reads:  research/full_runs/log_*.txt          (repeat 1)
        research/variance_runs/log_*_r2.txt   (repeat 2)
        research/variance_runs/log_*_r3.txt   (repeat 3)
Writes: research/batch_judge_results.csv
"""
import csv
import glob
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gavel import load_rules, run_ai_judge_anthropic, run_ai_judge_gemini  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL_RUNS = os.path.join(REPO_ROOT, "research", "full_runs")
VARIANCE_RUNS = os.path.join(REPO_ROOT, "research", "variance_runs")
RULES_DIR = os.path.join(REPO_ROOT, "rules")
OUT_CSV = os.path.join(REPO_ROOT, "research", "batch_judge_results.csv")

FNAME_RE = re.compile(r"^log_(.+?)_(unprotected|hardened)(?:_r(\d))?\.txt$")

CELL_RE = re.compile(
    r"\[Auditing\]\s+.*?\(([A-Z]+-\d+)\)\s*\n"
    r"\s*\[Payload\]\s+.*?\n"
    r"\s*\[Output\]\s+\"(.*?)\"\s*\n"
    r"\s*\[Result\]",
    re.DOTALL,
)

TARGET_MODEL_RE = re.compile(r"Target Model:\s*(\S+)")


def parse_log(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    m = TARGET_MODEL_RE.search(text)
    target_model = m.group(1) if m else "unknown"
    cells = []
    for match in CELL_RE.finditer(text):
        rule_id, output = match.group(1), match.group(2)
        cells.append((rule_id, output))
    return target_model, cells


def judge_is_self(target_model):
    return "claude-haiku-4-5" in target_model.lower()


def main():
    rules = load_rules(RULES_DIR)
    all_rules = {r["id"]: r for r in rules.get("silicon", []) + rules.get("statute", [])}

    log_files = []
    for path in sorted(glob.glob(os.path.join(FULL_RUNS, "log_*.txt"))):
        fname = os.path.basename(path)
        m = FNAME_RE.match(fname)
        if not m:
            continue
        model, persona, _ = m.groups()
        log_files.append((path, model, persona, 1))
    for path in sorted(glob.glob(os.path.join(VARIANCE_RUNS, "log_*_r*.txt"))):
        fname = os.path.basename(path)
        m = FNAME_RE.match(fname)
        if not m:
            continue
        model, persona, rep = m.groups()
        log_files.append((path, model, persona, int(rep)))

    print(f"Found {len(log_files)} log files to judge.")

    rows = []
    for path, model_from_fname, persona, repeat in log_files:
        target_model, cells = parse_log(path)
        use_gemini = judge_is_self(target_model)
        judge_name = "gemini-3.5-flash" if use_gemini else "claude-haiku-4-5"
        print(f"  [{repeat}] {model_from_fname}/{persona} ({len(cells)} cells) -> judge={judge_name}")
        for rule_id, output in cells:
            rule = all_rules.get(rule_id)
            if not rule:
                continue
            desc = rule.get("description", "")
            for attempt in range(3):
                try:
                    if use_gemini:
                        violated, reason = run_ai_judge_gemini(output, desc, "gemini-3.5-flash")
                    else:
                        violated, reason = run_ai_judge_anthropic(output, desc, "claude-haiku-4-5")
                    break
                except Exception as e:
                    if attempt == 2:
                        violated, reason = None, f"judge call failed: {e}"
                    else:
                        time.sleep(5)
            rows.append({
                "model": model_from_fname,
                "persona": persona,
                "repeat": repeat,
                "rule_id": rule_id,
                "judge_model": judge_name,
                "judge_verdict": "FAIL" if violated else ("PASS" if violated is not None else "ERROR"),
                "judge_reason": reason,
            })
            time.sleep(1)

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "persona", "repeat", "rule_id", "judge_model", "judge_verdict", "judge_reason"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} judged rows to {OUT_CSV}")


if __name__ == "__main__":
    main()
