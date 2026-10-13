# NB-IR-026 — Main Sherlock Student Evidence

**Beacon of the Eagle LLC / Centinell Suite Defense** — author and publisher. The investigated organization **Northbridge Systems Ltd.** is fictional.

This is a self-contained, simulated, **offline** incident package for the 15 principal questions in `docs/INVESTIGATION_QUESTIONS.md`. Every artifact is pedagogical, not acquired from a real victim. No IP addresses, running malware, passwords or personal data are included.

## Artifacts

| Path | Modeled source | Evidence limitation |
|---|---|---|
| `01_mail/messages.csv` | MTA/mail gateway | No original MIME messages |
| `02_file/file_origin.csv` | Browser/file audit | Path observations, no extracted executable |
| `03_endpoint/process_events.csv` | Endpoint process telemetry | Simulated process GUIDs, no actual PE |
| `04_persistence/tasks.csv` | Task Scheduler | Task target/trigger claims, not malware-code proof |
| `05_network/dns_events.csv` | Resolver telemetry | No IP addresses or packet trace |
| `05_network/proxy_events.csv` | HTTPS proxy | No decrypted payload content, no receiving audit |
| `06_control/change_control.csv` | Change approval | Legitimate comparator |
| `07_alerts/edr_alerts.csv` | EDR alert summaries | Alert is not independent proof |
| `08_static/static_report.txt` | **Inert fictional simulated static-analysis report** | No binary was inspected; hashes unavailable |
| `MANIFEST.sha256` | Computed checksum list | Integrity of training files, not real-world authenticity |

## First steps
```bash
python3 tools/verify_case.py
python3 tools/triage_case.py --timeline
python3 tools/triage_case.py --correlation CASE-RUN-2
sha256sum -c evidence/MANIFEST.sha256
```

Answers require **event IDs and UTC times**. Distinguish observed file staging and proxy metadata from a confirmed upload of particular contents. The encoded configuration is an inert, base64 JSON string in the static report; decoding it must never be confused with executing malware.
