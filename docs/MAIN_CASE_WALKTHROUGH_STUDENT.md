# Case investigation guide — main 15-question Medium Sherlock

**Case:** NB-IR-026 | Northbridge Systems Ltd., a fictional company

The student must reconstruct a suspicious roster utility's journey from mail delivery and browser download to unexpected child process, dropped helper, scheduled-task entry, possible data staging and recurring HTTPS. Follow timestamps and correlating IDs across distinct source files.

## Boundaries that matter
- Suspicious behavior is not synonymous with proven malicious code. The actual PE bytes and runtime memory were **not captured**.
- The `STATIC-931` report is a **training-only invented text fixture** with base64 UTF-8 JSON; it is not reverse engineering of a recovered binary.
- No TLS session contents or external receiving-system records exist. Do not assert proven exfiltration.
- The approved workstation update is a competing benign explanation for *some* events, not for an unrelated unapproved task.
- Northbridge Systems is imaginary and unrelated to the author's real infrastructure.

## Required output
Answer all [15 questions](INVESTIGATION_QUESTIONS.md) with field values, source filenames and record IDs. Include a timeline with 6 or more events and at least four source types; identify indicators as source-constrained observables, not universal attribution of a malware family.

### Ready-to-run Kali/Ubuntu commands
```bash
python3 tools/verify_case.py
python3 tools/triage_case.py --timeline
python3 tools/triage_case.py --source process --limit 30
python3 tools/triage_case.py --correlation CASE-RUN-1
python3 tools/triage_case.py --decode-config
```

No Internet required. On Windows, substitute `py -3`. No code is downloaded or executed except the read-only standard-library analyst helpers.
