# Student Guide
This Sherlock is an **offline malware-analysis case**. You do not need to run suspicious software or connect to any host.

## Suggested Kali Linux workflow
1. Clone the repository or download GitHub's source ZIP.
2. Inspect `evidence/` and check `evidence/MANIFEST.sha256` against file contents once evidence publication is complete.
3. Normalize timestamps to UTC; use event IDs and correlation IDs rather than trusting only filenames.
4. Follow the email → archive → process → dropped-file → persistence → network → staged-files sequence.
5. Review the static-inspection text reports; these are inert simulations of examination results, **not malware to execute**.
6. Document your answers with exact evidence references. Answer conservatively when content cannot be proven.

## Example tools
```bash
find evidence -type f -maxdepth 3 -print
grep -Rni 'RosterViewer\|SyncHealth' evidence/
python3 -m csv evidence/process_events.csv  # example only; use a CSV-capable viewer/script
sha256sum -c evidence/MANIFEST.sha256
```
For CSV use a spreadsheet, `csvkit`, or Python's `csv` module. Never run `RosterViewer.exe` or `nbupdate.exe`; no executable samples are supplied.

## Deliverable
A concise case report covering delivery, execution, behavior, persistence, network observations, indicators, and recommended containment, with an evidence-grounded timeline.
