"""
Zero-API-cost crosscheck: re-applies gavel.py's own regex/substring oracle_rules locally against
every raw [Output] already captured in the logs, then compares against the judge verdicts already
recorded in batch_judge_results.csv. Replaces the old judge_crosscheck.py analysis (whose own
outputs are no longer on disk) with a version covering all 540 (transcript, rule) pairs across all
3 repeats, judged by the current judge (Claude Haiku 4.5 / Gemini for Claude's own cells) instead
of the original Gemini 3.1 Flash-Lite judge.
"""
import csv
import glob
import os
import re
import sys

sys.path.insert(0, os.path.abspath("."))
from gavel import load_rules, strip_reasoning_trace  # noqa: E402
from batch_judge import parse_log, FNAME_RE  # noqa: E402

FULL_RUNS = "research/full_runs"
VARIANCE_RUNS = "research/variance_runs"
RULES_DIR = "rules"
JUDGE_CSV = "research/batch_judge_results.csv"
OUT_CSV = "research/regex_vs_judge_results.csv"
OUT_MD = "research/regex_vs_judge_summary.md"


def regex_verdict(output, rule):
    stripped = strip_reasoning_trace(output)
    for r in rule.get("oracle_rules", []):
        pattern = str(r.get("pattern", "")).lower()
        if r.get("type", "negative_match") == "negative_match" and pattern in stripped.lower():
            return "FAIL"
    return "PASS"


def main():
    rules = load_rules(RULES_DIR)
    all_rules = {r["id"]: r for r in rules.get("silicon", []) + rules.get("statute", [])}

    # judge_verdicts[(model, persona, repeat, rule_id)] = "PASS"/"FAIL"
    judge_verdicts = {}
    with open(JUDGE_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (row["model"], row["persona"], int(row["repeat"]), row["rule_id"])
            judge_verdicts[key] = row["judge_verdict"]

    log_files = []
    for path in sorted(glob.glob(os.path.join(FULL_RUNS, "log_*.txt"))):
        m = FNAME_RE.match(os.path.basename(path))
        if m:
            model, persona, _ = m.groups()
            log_files.append((path, model, persona, 1))
    for path in sorted(glob.glob(os.path.join(VARIANCE_RUNS, "log_*_r*.txt"))):
        m = FNAME_RE.match(os.path.basename(path))
        if m:
            model, persona, rep = m.groups()
            log_files.append((path, model, persona, int(rep)))

    rows = []
    for path, model, persona, repeat in log_files:
        _, cells = parse_log(path)
        for rule_id, output in cells:
            rule = all_rules.get(rule_id)
            if not rule:
                continue
            rv = regex_verdict(output, rule)
            jv = judge_verdicts.get((model, persona, repeat, rule_id), "MISSING")
            rows.append({
                "model": model, "persona": persona, "repeat": repeat, "rule_id": rule_id,
                "regex_verdict": rv, "judge_verdict": jv, "agree": rv == jv,
            })

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["model", "persona", "repeat", "rule_id", "regex_verdict", "judge_verdict", "agree"])
        w.writeheader()
        w.writerows(rows)

    total = len(rows)
    agree = sum(1 for r in rows if r["agree"])
    disagreements = [r for r in rows if not r["agree"]]

    by_rule = {}
    for r in disagreements:
        by_rule.setdefault(r["rule_id"], []).append(r)

    lines = []
    lines.append("# Regex vs. Judge Crosscheck — All 3 Repeats, Current Judge (Claude Haiku 4.5 / Gemini)\n")
    lines.append(f"**Agreement: {agree}/{total} ({round(agree/total*100)}%)**. "
                  f"{len(disagreements)} disagreements found across {len(by_rule)} distinct rules.\n")
    lines.append("| Rule | Disagreements | Regex said FAIL, judge said PASS | Regex said PASS, judge said FAIL |")
    lines.append("| :--- | :---: | :---: | :---: |")
    for rule_id in sorted(by_rule.keys()):
        items = by_rule[rule_id]
        regex_fail_judge_pass = sum(1 for r in items if r["regex_verdict"] == "FAIL" and r["judge_verdict"] == "PASS")
        regex_pass_judge_fail = sum(1 for r in items if r["regex_verdict"] == "PASS" and r["judge_verdict"] == "FAIL")
        lines.append(f"| {rule_id} | {len(items)} | {regex_fail_judge_pass} | {regex_pass_judge_fail} |")

    lines.append("\n## Full disagreement list\n")
    lines.append("| Model | Persona | Repeat | Rule | Regex | Judge |")
    lines.append("| :--- | :--- | :---: | :--- | :---: | :---: |")
    for r in disagreements:
        lines.append(f"| {r['model']} | {r['persona']} | {r['repeat']} | {r['rule_id']} | {r['regex_verdict']} | {r['judge_verdict']} |")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Agreement: {agree}/{total} ({round(agree/total*100)}%)")
    print(f"Wrote {OUT_CSV} and {OUT_MD}")
    for rule_id in sorted(by_rule.keys()):
        print(f"  {rule_id}: {len(by_rule[rule_id])} disagreements")


if __name__ == "__main__":
    main()
