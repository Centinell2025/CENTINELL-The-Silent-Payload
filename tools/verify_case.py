#!/usr/bin/env python3
"""Validate synthetic case integrity and cross-source provenance; never disclose answer key."""
from __future__ import annotations
from pathlib import Path
from datetime import datetime
import csv,hashlib,re
ROOT=Path(__file__).resolve().parents[1];EV=ROOT/"evidence"
MAIN=[
"01_mail/messages.csv","02_file/file_origin.csv","03_endpoint/process_events.csv",
"04_persistence/tasks.csv","05_network/dns_events.csv","05_network/proxy_events.csv",
"06_control/change_control.csv","07_alerts/edr_alerts.csv"]
def read(relative):
    with (EV/relative).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
def check():
    manifest=EV/"MANIFEST.sha256"
    lines=manifest.read_text(encoding="utf-8").splitlines()
    hashes={}
    for line in lines:
        if not line.strip() or line.startswith("#"):continue
        digest,sep,path=line.partition("  ")
        assert sep and re.fullmatch("[0-9a-f]{64}",digest) and path not in hashes
        f=ROOT/path
        assert f.is_file() and f.resolve().is_relative_to(EV.resolve())
        assert hashlib.sha256(f.read_bytes()).hexdigest()==digest, f"Bad digest: {path}"
        hashes[path]=digest
    expected={"evidence/"+p for p in MAIN}|{"evidence/08_static/static_report.txt","evidence/README.md"}
    actual={"evidence/"+p.relative_to(EV).as_posix() for p in EV.rglob("*") if p.is_file() and p.name!="MANIFEST.sha256"}
    assert set(hashes)==actual and expected<=set(hashes), "Manifest does not cover all case exhibits"
    all_ids=set();by_source={}
    for source in MAIN:
        rows=read(source); assert rows, source;by_source[source]=rows
        for row in rows:
            key=row.get("event_id") or row.get("ticket_id")
            assert key and key not in all_ids,key
            all_ids.add(key)
            ts=datetime.fromisoformat(row["timestamp_utc"].replace("Z","+00:00"))
            assert row["timestamp_utc"].endswith("Z") and ts.utcoffset().total_seconds()==0
            assert not re.search(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"," ".join(str(v) for v in row.values()))
    emails=by_source["01_mail/messages.csv"]
    origins=by_source["02_file/file_origin.csv"]
    process=by_source["03_endpoint/process_events.csv"]
    tasks=by_source["04_persistence/tasks.csv"]
    dns=by_source["05_network/dns_events.csv"]
    prox=by_source["05_network/proxy_events.csv"]
    changes=by_source["06_control/change_control.csv"]
    assert any(e["message_id"]==o["correlation_id"] and e["attachment"] in o["path"]
               for e in emails for o in origins if o["activity"]=="browser_download")
    assert any(e["process_guid"]==p["parent_guid"] and e["correlation_id"]==p["correlation_id"]
               for e in process for p in process)
    assert any(p["task_path"].endswith("SyncHealth") and p["action"]=="registered" for p in tasks)
    assert any(d["query"]==p["url_host"] and d["correlation_id"]==p["correlation_id"] for d in dns for p in prox)
    assert any(t["approval_status"]=="approved" for t in changes)
    report=(EV/"08_static/static_report.txt").read_text(encoding="utf-8")
    assert "NO executable" not in report or "no PE" in report
    assert "value: " in report and "NOT AVAILABLE" in report
    assert len(hashes)>=10
    print(f"PASS: {len(hashes)} evidence SHA-256 checks and cross-source integrity; no malware binary, no numeric IP")
if __name__=="__main__":check()
