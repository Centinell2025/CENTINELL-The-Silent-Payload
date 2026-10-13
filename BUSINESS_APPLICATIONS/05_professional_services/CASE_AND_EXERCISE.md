# Client Report Add-In with Abnormal Child Processes
**Business environment:** Professional services / consulting  
**Estimated investigation time:** 45–60 min  
**Domain:** Malware Analysis / DFIR / Blue Team  
**Level:** applied Medium practice (supplemental exercise)

## Situation
An analyst receives a supposed report-formatting add-in shortly before a client review. A browser retrieval is followed by an unexpected command interpreter and persistent launcher. Nearby document conversion events may be legitimate.

**Investigation scope:** General-purpose office IT; no real client name, case work product, contracts, or confidential consulting material.

This scenario is a **synthetic composite inspired by real-world enterprise practices**, not an incident attributed to a particular company. All evidence is invented and uses no IP addresses.

## Evidence provided
See [events.csv](events.csv) (12 intentionally fabricated observations). This normalized evidence view combines distinct source families, so students must treat the `source` field as part of provenance and not as proof of complete visibility.

**Investigation starting point:** reconstruct the activity and determine what is supported, what is inferred, and what is unproven.

## Exercises — answer with record IDs and UTC timestamps
1. Which delivery evidence connects the message and the extracted setup tool?
2. Provide the suspicious process parent-child relation with both record IDs.
3. Which persistence artifact was registered and how would it trigger?
4. Which later network events align with the suspicious chain, and what observation limits remain?
5. Identify the legitimate document conversion and its change-control reference.
6. Describe how analysts could obtain additional evidence without opening genuine client documents.

## Apply the analysis
- **Evidence acquisition:** establish the relevant user, host, file paths and time window before drawing conclusions.
- **Malware triage:** identify dropped files and abnormal process relationships; no executable samples are provided.
- **Persistence:** distinguish service, scheduled-task, registry, or module-load evidence from claims of malicious intent.
- **Business impact:** state the sector-specific risk without alleging proven harm.
- **Incident response:** propose only authorized, evidence-preserving containment.

## MITRE ATT&CK research prompt
Consider T1204.002, T1059.003 (Windows Command Shell), T1053.005 and T1071.001.

## Learner submission template
Use [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). Submit findings with exact `record_id` references from [events.csv](events.csv).

**Important:** This public training exercise deliberately contains no solution key and no executable malware.
