# Forensic Deep-Dive — NB-IR-026

**Publisher:** Beacon of the Eagle LLC / Centinell Suite Defense  
**Fictional incident company:** Northbridge Systems Ltd.  
**Target level:** Medium main Sherlock with optional higher-effort DFIR extension. **Neither HTB acceptance nor difficulty is certified.**

## Why this extension exists
The original case traces a simulated roster tool through email, download, process execution, task persistence, file staging and proxy telemetry. The *deep-dive* adds five normalized synthetic reference families:

| Source | Analytical question | Caveat |
|---|---|---|
| `auth_context.csv` | Which session and principal can be linked? | Not a raw Windows Security EVTX; no human identity proof |
| `file_provenance.csv` | Which file/process relationships repeat across a collection chain? | Signature and PE bytes are not collected |
| `task_audit.csv` | Did a task register, trigger, run, or merely remain ready? | Modeled scheduler events, not native Windows XML |
| `egress_context.csv` | Does a network request belong to user software, normal activity, or neither? | Derived synthetic proxy and background traffic |
| `analyst_hypotheses.csv` | Which explanations are unsupported, partially supported, or contradicted? | These are *opinions*, not source-of-truth evidence |

**No numeric IPs, usable malware, live credentials or sensitive real-world records** are present. In particular, two modeled sources should **not** be described as two independently acquired forensic captures. Additional exercises are not HTB's 15 graded questions.

## Twelve expert-level investigations (ungraded)

| Task | Required deliverable |
|---|---|
| DD-01 | Distinguish a reported session token from human attribution using `auth_context.csv` and `process_events.csv` |
| DD-02 | Contrast the user's downloaded utility with the authorized updater's documented change scope, matching exact time windows |
| DD-03 | Trace the executable's claimed write using parent GUID, file provenance, and task-registration source references |
| DD-04 | Separate task registration, readiness and triggering; explain which facts do **not** prove code execution or payload behavior |
| DD-05 | Normalize a timeline in UTC while separating event time from SOC alert time and later analyst commentary |
| DD-06 | Build two competing hypotheses for the recurring network requests and test them against two modeled source families |
| DD-07 | Contrast the archive staging observation with observed HTTPS metadata and explain why payload contents cannot be proven |
| DD-08 | Identify four intentionally unsupported interpretations in `analyst_hypotheses.csv` and give specific contradictory or missing artifacts |
| DD-09 | Compare the benign health updater to the unapproved helper by account, process ancestry, task path, authorization and egress domain |
| DD-10 | Build a case-ready evidence-citation chain including original record IDs, acquisition gaps, hashes and confidence levels |
| DD-11 | Design one detection rule for suspicious service or task activity plus a second filter to reduce benign-update false positives |
| DD-12 | Write a 250–400 word executive summary with supported, plausible and unproven findings; propose containment without erasing evidence |

## Kali Linux / Ubuntu commands
```bash
python3 tools/verify_case.py
python3 tools/deep_correlate.py --summary
python3 tools/deep_correlate.py --timeline --limit 30
python3 tools/deep_correlate.py --source auth_context --limit 30
python3 tools/deep_correlate.py --record PROC-302
python3 tools/deep_correlate.py --record PROXY-802
python3 tools/triage_case.py --decode-config
```

## Submission standard
Use `templates/DEEP_INVESTIGATION_REPORT.md`. A high-quality answer states an observation, exact file and record ID, corroboration (or why none exists), a plausible alternative, a limitation, and the operational implication. For simulated sources, avoid manufactured confidence. The author-side validator checks the schema and relationships; it **does not** establish expert difficulty.

## Instructor review
This extension's 12 tasks are narrative and currently **ungraded in HTB**. An instructor must assess quality of evidence reasoning and cross-source correlations, not merely quote the event labels. No expected answers are included in public artifacts.
