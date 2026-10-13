# Appointment Utility That Changed a Service
**Business environment:** Healthcare administration  
**Estimated investigation time:** 45–60 min  
**Domain:** Malware Analysis / DFIR / Blue Team  
**Level:** applied Medium practice (supplemental exercise)

## Situation
An administrator on a scheduling workstation opens a purported appointment-helper bundle. Endpoint events later show a new service and periodic requests. A separate, approved scheduling application also runs in the interval. The investigator must determine which activity is attributable to the unapproved bundle.

**Investigation scope:** Administrative desktop only; no patient identity, patient records, clinical devices, or operational medical systems.

This scenario is a **synthetic composite inspired by real-world enterprise practices**, not an incident attributed to a particular company. All evidence is invented and uses no IP addresses.

## Evidence provided
See [events.csv](events.csv) (13 intentionally fabricated observations). This normalized evidence view combines distinct source families, so students must treat the `source` field as part of provenance and not as proof of complete visibility.

**Investigation starting point:** reconstruct the activity and determine what is supported, what is inferred, and what is unproven.

## Exercises — answer with record IDs and UTC timestamps
1. Which delivered item initiated the unapproved activity, and what corroborates the path to execution?
2. Identify the parent-child process relationship and the dropped agent location.
3. Which service indicates persistence, what is its startup configuration, and which events corroborate actual start?
4. Find the first recorded check-in request and state the uncertainty associated with it.
5. Identify the approved scheduling process and the maintenance ticket supporting legitimate activity.
6. Explain how to preserve evidence without exposing sensitive personal or clinical information.

## Apply the analysis
- **Evidence acquisition:** establish the relevant user, host, file paths and time window before drawing conclusions.
- **Malware triage:** identify dropped files and abnormal process relationships; no executable samples are provided.
- **Persistence:** distinguish service, scheduled-task, registry, or module-load evidence from claims of malicious intent.
- **Business impact:** state the sector-specific risk without alleging proven harm.
- **Incident response:** propose only authorized, evidence-preserving containment.

## MITRE ATT&CK research prompt
Evaluate T1204.002, T1543.003 (Windows Service), and T1071.001; distinguish confirmed events from assumptions.

## Learner submission template
Use [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). Submit findings with exact `record_id` references from [events.csv](events.csv).

**Important:** This public training exercise deliberately contains no solution key and no executable malware.
