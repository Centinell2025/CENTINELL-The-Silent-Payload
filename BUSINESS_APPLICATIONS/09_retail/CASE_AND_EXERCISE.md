# Inventory Price Sheet and WMI Subscription

**Northbridge Systems Ltd. — simulated Retail inventory support division**  
**Difficulty:** Medium, optional applied lab (approximately 50–80 minutes)  
**Publisher:** Beacon of the Eagle LLC — Centinell Suite Defense

## Incident handoff
A merchandise analyst tests a price-sheet importer that was not approved for deployment. WMI-related records show a durable subscription; no checkout devices, payment data, or customer information is included.

## Scope, evidence and safety
The supplied [events.csv](events.csv) is a normalized synthetic event table (17 rows) with original source **categories**, not original Windows EVTX, Sysmon or network captures. All identities and hosts belong to a fictional Northbridge division. All domains end in reserved `.test`; no numerical IP addresses, malware samples, live hosts or private customer details are included. Do not run, reconstruct or deploy any named executable.

### Business question
Decide what the observed records actually establish, which hypotheses remain unproven, what extra artifacts are needed and how a security analyst should prevent disruption to normal operations.

## Investigative questions — cite event IDs and exact UTC times

1. Trace the price importer to the initial user-execution and child-process events.
2. Identify the WMI permanent-event subscription artifacts and explain what they show without code execution.
3. Differentiate a registry configuration record from evidence that a scheduled payload ran.
4. Connect local file staging with network events, and state why exfiltration contents remain unknown.
5. Show how approved stock-check activity differs in source, host, and change scope.
6. Provide a response plan that keeps actual point-of-sale terminals out of scope.

## Working method (Kali/Ubuntu/Windows)
From the repository root:

```bash
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py BUSINESS_APPLICATIONS/09_retail/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all
```

Build a timeline first. Compare source families and correlation IDs, identify unrelated approved business events, then prepare a two-column observation-versus-inference table. When there is no actual executable or content payload in the artifacts, you **must not** assert malware-family attribution, decrypted HTTPS payload contents or confirmed data theft.

## Deliverable
Complete [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md) with the event chain, a benign alternative, whether persistence is observed or only plausible, business impact *if* the scenario were real, evidence acquisition recommendations and proportionate containment. See [ASSESSMENT_RUBRIC.md](../ASSESSMENT_RUBRIC.md) for assessment. These six questions are ungraded practice, separate from the main HTB Sherlock.

**Author:** Beacon of the Eagle LLC / Centinell Suite Defense. Synthetic defensive training only.
