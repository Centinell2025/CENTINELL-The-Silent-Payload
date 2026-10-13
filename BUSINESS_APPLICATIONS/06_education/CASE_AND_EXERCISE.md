# Scholarship Portal Converter and a Hidden Login Script

**Northbridge Systems Ltd. — simulated Education administration division**  
**Difficulty:** Medium, optional applied lab (approximately 50–80 minutes)  
**Publisher:** Beacon of the Eagle LLC — Centinell Suite Defense

## Incident handoff
A student-services officer is told to convert an enrollment report before a routine review. A legitimate campus calendar synchronization runs during the same hour. All records concern fictional administrative data, not students.

## Scope, evidence and safety
The supplied [events.csv](events.csv) is a normalized synthetic event table (16 rows) with original source **categories**, not original Windows EVTX, Sysmon or network captures. All identities and hosts belong to a fictional Northbridge division. All domains end in reserved `.test`; no numerical IP addresses, malware samples, live hosts or private customer details are included. Do not run, reconstruct or deploy any named executable.

### Business question
Decide what the observed records actually establish, which hypotheses remain unproven, what extra artifacts are needed and how a security analyst should prevent disruption to normal operations.

## Investigative questions — cite event IDs and exact UTC times

1. Trace the email, browser retrieval and first execution using at least three record IDs and UTC times.
2. Identify the parent-child process and the locally written artifact; explain why this raises suspicion without a malicious binary.
3. Find the scheduled persistence mechanism and differentiate its timing from the approved calendar updater.
4. Correlate the simulated DNS and proxy observations with process ancestry. What cannot be inferred from TLS metadata?
5. Is there evidence that real student records were taken? State the strongest supported and unsupported propositions.
6. Propose containment and validation steps preserving data and access continuity for student services.

## Working method (Kali/Ubuntu/Windows)
From the repository root:

```bash
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py BUSINESS_APPLICATIONS/06_education/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all
```

Build a timeline first. Compare source families and correlation IDs, identify unrelated approved business events, then prepare a two-column observation-versus-inference table. When there is no actual executable or content payload in the artifacts, you **must not** assert malware-family attribution, decrypted HTTPS payload contents or confirmed data theft.

## Deliverable
Complete [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md) with the event chain, a benign alternative, whether persistence is observed or only plausible, business impact *if* the scenario were real, evidence acquisition recommendations and proportionate containment. See [ASSESSMENT_RUBRIC.md](../ASSESSMENT_RUBRIC.md) for assessment. These six questions are ungraded practice, separate from the main HTB Sherlock.

**Author:** Beacon of the Eagle LLC / Centinell Suite Defense. Synthetic defensive training only.
