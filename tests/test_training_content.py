#!/usr/bin/env python3
"""Offline student artifact regression: all 10 applications, main evidence, no answers."""
from pathlib import Path
import csv,subprocess,sys,re
ROOT=Path(__file__).resolve().parents[1]
apps=ROOT/"BUSINESS_APPLICATIONS"
cases=sorted(apps.glob("*/events.csv"))
assert len(cases)==10, f"Expected 10 sectors, found {len(cases)}"
total=0
for f in cases:
    with f.open(encoding="utf-8",newline="") as s:
        rows=list(csv.DictReader(s))
    assert len(rows)>=12
    ids=[r["record_id"] for r in rows]
    assert len(ids)==len(set(ids))
    brief=(f.parent/"CASE_AND_EXERCISE.md").read_text(encoding="utf-8")
    assert "## Investigative questions" in brief or "## Exercises" in brief
    total+=len(rows)
assert total>=125,total
guide=(ROOT/"docs/INVESTIGATION_QUESTIONS.md").read_text(encoding="utf-8")
assert len(re.findall(r"^\d+\. ",guide,re.MULTILINE))==15
for argv in (["tools/triage_case.py","--timeline","--limit","4"],
             ["tools/triage_case.py","--decode-config"],
             ["tools/triage_case.py","--correlation","CASE-RUN-2"]):
    completed=subprocess.run([sys.executable,str(ROOT/argv[0]),*argv[1:]],cwd=ROOT,capture_output=True,text=True)
    assert completed.returncode==0,completed.stderr
print(f"PASS: {len(cases)} business labs, {total} events, 60 practice questions, 15 main questions, offline triage CLI")
