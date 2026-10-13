#!/usr/bin/env python3
"""Deterministic, spoiler-safe schema and relationship tests for optional deep dive."""
import csv,re,sys,subprocess
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"evidence/09_deep_dive"
SRC=("auth_context.csv","file_provenance.csv","task_audit.csv","egress_context.csv","analyst_hypotheses.csv")
ALL_IDS=set()
files={}
for filename in SRC:
    p=BASE/filename
    with p.open(newline="",encoding="utf-8") as f:
        rdr=csv.DictReader(f)
        rows=list(rdr)
    assert 10<=len(rows)<=150,filename
    assert len(set((row.get("event_id") or row.get("note_id")) for row in rows))==len(rows)
    for row in rows:
        assert datetime.fromisoformat(row["timestamp_utc"].replace("Z","+00:00")).utcoffset().total_seconds()==0
        assert not re.search(r"(?<![\\d.])(?:\\d{1,3}\\.){3}\\d{1,3}(?![\\d.])"," ".join(row.values()))
        key=row.get("event_id") or row.get("note_id")
        assert key and key not in ALL_IDS,key
        ALL_IDS.add(key)
    files[filename]=rows
assert sum(len(x) for x in files.values())>=75
with (ROOT/"evidence/03_endpoint/process_events.csv").open(newline="",encoding="utf-8") as f:
    original=list(csv.DictReader(f))
proc_ids={r["event_id"] for r in original}
with (ROOT/"evidence/05_network/proxy_events.csv").open(newline="",encoding="utf-8") as f:
    prox=list(csv.DictReader(f))
proxy_ids={r["event_id"] for r in prox}
assert sum(r["source_event"] in proc_ids for r in files["file_provenance.csv"])>=4
assert sum(r["proxy_event_id"] in proxy_ids for r in files["egress_context.csv"])>=3
assert len({r["session_id"] for r in files["auth_context.csv"]})>=3
assert len({r["task_path"] for r in files["task_audit.csv"]})>=3
assert any(r["assessment_status"]=="unsupported" for r in files["analyst_hypotheses.csv"])
assert any(r["assessment_status"]=="supported_model" for r in files["analyst_hypotheses.csv"])
runner=ROOT/"tools/deep_correlate.py"
for args in [["--summary"],["--timeline","--limit","5"],["--record","PROC-302"],["--record","PROXY-802"]]:
    out=subprocess.run([sys.executable,str(runner),*args],capture_output=True,text=True,cwd=ROOT)
    assert out.returncode==0,out.stderr
    assert out.stdout.strip(),args
print("PASS: 5 optional DFIR source files, cross-source references, competing hypotheses and read-only CLI")
