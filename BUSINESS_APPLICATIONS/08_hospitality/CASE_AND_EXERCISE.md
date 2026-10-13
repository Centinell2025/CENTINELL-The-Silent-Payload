# Reservation Export Helper and Auto-Start Service

**Northbridge Systems Ltd. — simulated Hospitality back-office division**  
**Difficulty:** Medium, optional applied lab (approximately 50–80 minutes)  
**Publisher:** Beacon of the Eagle LLC — Centinell Suite Defense

## Incident handoff
A hotel back-office clerk receives an unexpected booking reconciliation helper. The provided records exclude payment cards, guest names, and production reservation systems; a routine breakfast-scheduling utility serves as the decoy.

## Scope, evidence and safety
The supplied [events.csv](events.csv) is a normalized synthetic event table (16 rows) with original source **categories**, not original Windows EVTX, Sysmon or network captures. All identities and hosts belong to a fictional Northbridge division. All domains end in reserved `.test`; no numerical IP addresses, malware samples, live hosts or private customer details are included. Do not run, reconstruct or deploy any named executable.

### Business question
Decide what the observed records actually establish, which hypotheses remain unproven, what extra artifacts are needed and how a security analyst should prevent disruption to normal operations.

## Investigative questions — cite event IDs and exact UTC times

1. Connect the mail attachment to the user-launched executable and its immediate child process.
2. Which generated file and service installation form the observed persistence candidate? Give IDs and times.
3. Compare the service's account context with the initial user session; is credential theft proven?
4. Which outbound hostname appears and what independent DNS/proxy fields support the link?
5. Separate the legitimate breakfast software updater from the unapproved service chain.
6. Recommend evidence-preserving containment that avoids disruption to actual reservations and payments.

## Working method (Kali/Ubuntu/Windows)
From the repository root:

```bash
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py BUSINESS_APPLICATIONS/08_hospitality/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all
```

Build a timeline first. Compare source families and correlation IDs, identify unrelated approved business events, then prepare a two-column observation-versus-inference table. When there is no actual executable or content payload in the artifacts, you **must not** assert malware-family attribution, decrypted HTTPS payload contents or confirmed data theft.

## Deliverable
Complete [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md) with the event chain, a benign alternative, whether persistence is observed or only plausible, business impact *if* the scenario were real, evidence acquisition recommendations and proportionate containment. See [ASSESSMENT_RUBRIC.md](../ASSESSMENT_RUBRIC.md) for assessment. These six questions are ungraded practice, separate from the main HTB Sherlock.

**Author:** Beacon of the Eagle LLC / Centinell Suite Defense. Synthetic defensive training only.
