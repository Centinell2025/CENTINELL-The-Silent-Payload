#!/usr/bin/env python3
"""Offline Northbridge simulated case browser. Prints observations, not conclusions."""
from __future__ import annotations
import argparse,base64,csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/"evidence"
SOURCES=[
"01_mail/messages.csv","02_file/file_origin.csv","03_endpoint/process_events.csv",
"04_persistence/tasks.csv","05_network/dns_events.csv","05_network/proxy_events.csv",
"06_control/change_control.csv","07_alerts/edr_alerts.csv"]
def rows():
    for path in SOURCES:
        with (CASE/path).open(encoding="utf-8",newline="") as f:
            for row in csv.DictReader(f):
                yield path,row
def decode():
    data=(CASE/"08_static/static_report.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        if line.startswith("value: "):
            value=line.split("value: ",1)[1]
            b=base64.b64decode(value,validate=True)
            obj=json.loads(b.decode("utf-8"))
            if set(obj)!={"campaign","domain","path","interval_seconds"}:
                raise ValueError("Unexpected inert training configuration keys")
            print(json.dumps(obj,indent=2,ensure_ascii=False))
            print("This is a text-only fictional configuration, NOT recovered malware instructions.")
            return
    raise ValueError("Missing inert base64 configuration")
def main():
    p=argparse.ArgumentParser(description=__doc__)
    group=p.add_mutually_exclusive_group(required=True)
    group.add_argument("--timeline",action="store_true")
    group.add_argument("--source",help="Filter source filename; e.g. process")
    group.add_argument("--correlation",help="Filter correlation ID; e.g. CASE-RUN-2")
    group.add_argument("--decode-config",action="store_true")
    p.add_argument("--limit",type=int,default=60)
    a=p.parse_args()
    if a.limit<1:raise ValueError("--limit must be positive")
    if a.decode_config:return decode()
    found=[]
    for path,row in rows():
        if a.source and a.source.casefold() not in path.casefold():continue
        if a.correlation and row.get("correlation_id")!=a.correlation:continue
        ts=row["timestamp_utc"]
        rid=row.get("event_id") or row.get("ticket_id")
        label=row.get("activity") or row.get("action") or row.get("approval_status")
        artifact=row.get("path") or row.get("image") or row.get("task_path") or row.get("url_host") or row.get("query") or row.get("attachment") or row.get("authorized_software") or row.get("signal")
        found.append((ts,path,rid,label,artifact))
    found.sort()
    for ts,path,rid,label,artifact in found[:a.limit]:
        print(f"{ts} | {path} | {rid} | {label} | {artifact}")
    print(f"Displayed {min(len(found),a.limit)} of {len(found)} simulated records (not verified real incident evidence).")
if __name__=="__main__":
    try:sys.exit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print("ERROR:",exc,file=sys.stderr);sys.exit(2)
