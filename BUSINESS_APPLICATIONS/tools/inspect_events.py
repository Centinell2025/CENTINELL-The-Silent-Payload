#!/usr/bin/env python3
"""Read or validate anonymized CENTINELL practice telemetry. Standard library only."""
import csv
import pathlib
import re
import sys
from datetime import datetime

BASE = pathlib.Path(__file__).resolve().parents[1]
COLUMNS = ["record_id", "timestamp_utc", "source", "host", "principal",
           "activity", "artifact", "correlation_id", "observation"]
IPV4 = re.compile(r"(?<![\\d.])(?:\\d{1,3}\\.){3}\\d{1,3}(?![\\d.])")


def validate(path):
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"Unexpected columns: {path}: {reader.fieldnames}")
        seen = set()
        rows = list(reader)
    if len(rows) < 10:
        raise ValueError(f"Insufficient practice events: {path}")
    for row in rows:
        rid = row["record_id"]
        if not rid or rid in seen:
            raise ValueError(f"Duplicate or empty record_id in {path}: {rid}")
        seen.add(rid)
        date = datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))
        if not row["timestamp_utc"].endswith("Z") or date.utcoffset().total_seconds() != 0:
            raise ValueError(f"Timestamp must be UTC: {rid}")
        # Numeric IPs are intentionally prohibited, including in free-text notes.
        if IPV4.search(" ".join(row.values())):
            raise ValueError(f"IP-like address found in {rid}; redact it")
    return rows


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--validate-all":
        paths = sorted(BASE.glob("*/events.csv"))
        if not paths:
            raise ValueError("No practice event files found")
        for path in paths:
            rows = validate(path)
            print(f"PASS {path.relative_to(BASE)}: {len(rows)} rows")
        print(f"Validated {len(paths)} exercises")
        return 0

    if len(sys.argv) != 2:
        print("Usage: python3 inspect_events.py CSV_PATH | --validate-all", file=sys.stderr)
        return 2
    path = pathlib.Path(sys.argv[1])
    rows = validate(path)
    for row in sorted(rows, key=lambda x: x["timestamp_utc"]):
        print(f'{row["timestamp_utc"]} | {row["record_id"]:<8} | '
              f'{row["source"]:<8} | {row["activity"]:<12} | '
              f'{row["artifact"]} | {row["correlation_id"]}')
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
