# Student Guide
This Sherlock is an **offline malware-analysis case**. You do not need to run suspicious software or connect to any host.

## Suggested Kali Linux workflow
1. Clone the repository or download GitHub's source ZIP.
2. Inspect the published `evidence/` and run `python3 tools/verify_case.py` and `sha256sum -c evidence/MANIFEST.sha256` to verify all file digests.
3. Normalize timestamps to UTC; use event IDs and correlation IDs rather than trusting only filenames.
4. Follow the email → archive → process → dropped-file → persistence → network → staged-files sequence.
5. Review the static-inspection text reports; these are inert simulations of examination results, **not malware to execute**.
6. Document your answers with exact evidence references. Answer conservatively when content cannot be proven.

## Example tools
```bash
find evidence -type f -maxdepth 3 -print
grep -Rni 'RosterViewer\|SyncHealth' evidence/
python3 tools/triage_case.py --timeline
python3 tools/triage_case.py --correlation CASE-RUN-2
python3 tools/triage_case.py --decode-config
sha256sum -c evidence/MANIFEST.sha256
```
For CSV use a spreadsheet, `csvkit`, or Python's `csv` module. Never run `RosterViewer.exe` or `nbupdate.exe`; no executable samples are supplied.

## Deliverable
A concise case report covering delivery, execution, behavior, persistence, network observations, indicators, and recommended containment, with an evidence-grounded timeline.

## Deep-Dive investigation (optional)
Use `python3 tools/deep_correlate.py --summary`, `python3 tools/deep_correlate.py --timeline --limit 25`, and `python3 tools/deep_correlate.py --record PROC-302`. Complete the [12 ungraded questions](FORENSIC_DEEP_DIVE.md) and [blank worksheet](../templates/DEEP_INVESTIGATION_REPORT.md). Notes in `analyst_hypotheses.csv` are intentionally contradictory and must **not** be treated as ground truth.
