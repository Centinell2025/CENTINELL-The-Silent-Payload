# Shipping Label Helper and Data Staging
**Business environment:** Distribution and logistics  
**Estimated investigation time:** 45–65 min  
**Domain:** Malware Analysis / DFIR / Blue Team  
**Level:** applied Medium practice (supplemental exercise)

## Situation
A dispatch clerk downloads a shipping-label utility from an unsolicited notification. The executable creates a helper file and accesses synthetic dispatch manifests. Analysts must separate data staging from proven external disclosure.

**Investigation scope:** Back-office Windows terminal; manifest filenames are fictional, no vehicle location feeds or real addresses.

This scenario is a **synthetic composite inspired by real-world enterprise practices**, not an incident attributed to a particular company. All evidence is invented and uses no IP addresses.

## Evidence provided
See [events.csv](events.csv) (13 intentionally fabricated observations). This normalized evidence view combines distinct source families, so students must treat the `source` field as part of provenance and not as proof of complete visibility.

**Investigation starting point:** reconstruct the activity and determine what is supported, what is inferred, and what is unproven.

## Exercises — answer with record IDs and UTC timestamps
1. Identify the initial lure, archive and interactive launch.
2. What persistence mechanism is used and what is its exact registry path?
3. Which two data-source files preceded creation of a local archive?
4. Which outbound event is suspicious, and why does it NOT prove the contents of any upload?
5. Identify legitimate printing-related activity and the evidence it was approved.
6. Recommend immediate triage priorities, preserving the staged archive for further review.

## Apply the analysis
- **Evidence acquisition:** establish the relevant user, host, file paths and time window before drawing conclusions.
- **Malware triage:** identify dropped files and abnormal process relationships; no executable samples are provided.
- **Persistence:** distinguish service, scheduled-task, registry, or module-load evidence from claims of malicious intent.
- **Business impact:** state the sector-specific risk without alleging proven harm.
- **Incident response:** propose only authorized, evidence-preserving containment.

## MITRE ATT&CK research prompt
Evaluate T1204.002, T1547.001 (Registry Run Keys), T1074.001 (Local Data Staging), T1071.001.

## Learner submission template
Use [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). Submit findings with exact `record_id` references from [events.csv](events.csv).

**Important:** This public training exercise deliberately contains no solution key and no executable malware.
