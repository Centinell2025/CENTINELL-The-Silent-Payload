#!/usr/bin/env python3
"""Read-only synthetic forensic-source explorer. Standard-library only.

This searches records and their referent IDs. It does NOT generate a verdict,
recover binary payloads or establish real-world forensic provenance.
"""
import argparse,csv,sys
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"evidence/09_deep_dive"
FILES=(
"auth_context.csv","file_provenance.csv","task_audit.csv",
"egress_context.csv","analyst_hypotheses.csv",
)
def records():
    for filename in FILES:
        with (DIR/filename).open(newline="",encoding="utf-8") as f:
            for line,row in enumerate(csv.DictReader(f),2):
                yield filename,line,row
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    args=parser.add_mutually_exclusive_group(required=True)
    args.add_argument("--summary",action="store_true")
    args.add_argument("--timeline",action="store_true")
    args.add_argument("--source",type=str,help="Filter by filename substring")
    args.add_argument("--record",type=str,help="Match a record id or reference, case insensitive")
    parser.add_argument("--limit",type=int,default=50)
    a=parser.parse_args()
    if a.limit<1:parser.error("--limit must be positive")
    rows=list(records())
    if a.summary:
        for name in FILES:
            print(f"{name}: {sum(path==name for path,_,_ in rows)} rows")
        print("Provenance: all files are constructed simulations; not native logs.")
        return 0
    if a.source:
        rows=[x for x in rows if a.source.lower() in x[0].lower()]
    if a.record:
        rows=[x for x in rows if a.record.lower() in
              " ".join(str(v) for v in x[2].values()).lower()]
    if a.timeline:
        rows.sort(key=lambda x:(datetime.fromisoformat(x[2]["timestamp_utc"].replace("Z","+00:00")),x[0],x[1]))
    for name,line,row in rows[:a.limit]:
        key=row.get("event_id") or row.get("note_id")
        detail=row.get("observation") or row.get("limitation")
        print(f'{row["timestamp_utc"]} | {name}:{line} | {key} | {detail}')
    print(f"Displayed {min(len(rows),a.limit)} of {len(rows)} rows. Verification of claims is the investigator's task.")
    return 0
if __name__=="__main__":
    try:sys.exit(main())
    except (OSError,ValueError) as e:print("ERROR:",e,file=sys.stderr);sys.exit(2)
