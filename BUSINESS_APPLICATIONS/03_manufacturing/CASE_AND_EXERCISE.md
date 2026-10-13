# Planning-Station Utility and an Unexpected DLL
**Business environment:** Manufacturing business operations  
**Estimated investigation time:** 50–70 min  
**Domain:** Malware Analysis / DFIR / Blue Team  
**Level:** applied Medium practice (supplemental exercise)

## Situation
A production-planning office workstation receives a counterfeit spreadsheet-analysis extension. The suspicious chain appears within the business IT zone, while an unrelated approved equipment-monitoring tool is active. Investigators must restrict conclusions to the observed office environment and avoid claims about industrial controllers.

**Investigation scope:** Office IT only; no programmable logic controllers, plant networks, production secrets, or operational control actions.

This scenario is a **synthetic composite inspired by real-world enterprise practices**, not an incident attributed to a particular company. All evidence is invented and uses no IP addresses.

## Evidence provided
See [events.csv](events.csv) (12 intentionally fabricated observations). This normalized evidence view combines distinct source families, so students must treat the `source` field as part of provenance and not as proof of complete visibility.

**Investigation starting point:** reconstruct the activity and determine what is supported, what is inferred, and what is unproven.

## Exercises — answer with record IDs and UTC timestamps
1. Identify the user-driven delivery and execution sequence from at least three sources.
2. Which record supports the presence of a DLL load, and what cannot be inferred without the binary?
3. Locate the persistence candidate and the triggering schedule.
4. Which network event correlates with the suspicious execution chain?
5. Which process is supported as approved, and why is it not sufficient to call the production control network compromised?
6. Draft two business-IT remediation priorities and one scope statement.

## Apply the analysis
- **Evidence acquisition:** establish the relevant user, host, file paths and time window before drawing conclusions.
- **Malware triage:** identify dropped files and abnormal process relationships; no executable samples are provided.
- **Persistence:** distinguish service, scheduled-task, registry, or module-load evidence from claims of malicious intent.
- **Business impact:** state the sector-specific risk without alleging proven harm.
- **Incident response:** propose only authorized, evidence-preserving containment.

## MITRE ATT&CK research prompt
Consider T1204.002, T1574 (Hijack Execution Flow — mapping requires additional proof), T1053.005 and T1071.001. Avoid asserting DLL sideloading without load-path evidence.

## Learner submission template
Use [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). Submit findings with exact `record_id` references from [events.csv](events.csv).

**Important:** This public training exercise deliberately contains no solution key and no executable malware.
