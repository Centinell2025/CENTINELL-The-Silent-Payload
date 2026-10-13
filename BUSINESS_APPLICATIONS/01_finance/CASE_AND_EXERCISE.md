# Unapproved Payment Reconciliation Tool
**Business environment:** Finance and accounts payable  
**Estimated investigation time:** 45–60 min  
**Domain:** Malware Analysis / DFIR / Blue Team  
**Level:** applied Medium practice (supplemental exercise)

## Situation
An accounts-payable employee is prompted to install a supposed reconciliation utility before a quarterly supplier review. A legitimate calendar synchronization tool runs nearby in time. The analyst must separate routine activity from a potentially malicious software chain.

**Investigation scope:** Office Windows workstation; no financial account numbers or customer transactions.

This scenario is a **synthetic composite inspired by real-world enterprise practices**, not an incident attributed to a particular company. All evidence is invented and uses no IP addresses.

## Evidence provided
See [events.csv](events.csv) (14 intentionally fabricated observations). This normalized evidence view combines distinct source families, so students must treat the `source` field as part of provenance and not as proof of complete visibility.

**Investigation starting point:** reconstruct the activity and determine what is supported, what is inferred, and what is unproven.

## Exercises — answer with record IDs and UTC timestamps
1. Identify the suspicious delivery record and explain which authentication result increases concern.
2. Which process lineage connects the downloaded archive with the hidden scripting event?
3. What file and task action suggest persistence? Cite at least two record IDs.
4. Which outbound request may be related, and what cannot be determined from encrypted proxy metadata?
5. Name the authorized updater and the change record that distinguish it from the suspect chain.
6. Write a four-step containment and evidence-preservation recommendation.

## Apply the analysis
- **Evidence acquisition:** establish the relevant user, host, file paths and time window before drawing conclusions.
- **Malware triage:** identify dropped files and abnormal process relationships; no executable samples are provided.
- **Persistence:** distinguish service, scheduled-task, registry, or module-load evidence from claims of malicious intent.
- **Business impact:** state the sector-specific risk without alleging proven harm.
- **Incident response:** propose only authorized, evidence-preserving containment.

## MITRE ATT&CK research prompt
Consider T1204.002 (User Execution), T1059.001 (PowerShell), T1053.005 (Scheduled Task), and T1071.001 (Web Protocols); justify each or leave unconfirmed.

## Learner submission template
Use [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md). Submit findings with exact `record_id` references from [events.csv](events.csv).

**Important:** This public training exercise deliberately contains no solution key and no executable malware.
