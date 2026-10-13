# Grid Planning Spreadsheet Add-in and DLL Search Order

**Northbridge Systems Ltd. — simulated Energy planning office IT division**  
**Difficulty:** Medium, optional applied lab (approximately 50–80 minutes)  
**Publisher:** Beacon of the Eagle LLC — Centinell Suite Defense

## Incident handoff
A planning analyst works on a fictional monthly load forecast. A downloaded plugin causes an unexplained library load on an office workstation. There is no operational technology, ICS device, grid control or live industrial asset in this exercise.

## Scope, evidence and safety
The supplied [events.csv](events.csv) is a normalized synthetic event table (16 rows) with original source **categories**, not original Windows EVTX, Sysmon or network captures. All identities and hosts belong to a fictional Northbridge division. All domains end in reserved `.test`; no numerical IP addresses, malware samples, live hosts or private customer details are included. Do not run, reconstruct or deploy any named executable.

### Business question
Decide what the observed records actually establish, which hypotheses remain unproven, what extra artifacts are needed and how a security analyst should prevent disruption to normal operations.

## Investigative questions — cite event IDs and exact UTC times

1. Which events prove the plugin originated from an unauthenticated message rather than a signed internal deployment?
2. Build the parent process and module-load timeline; does the evidence prove actual DLL sideloading?
3. Which file, task or service event suggests attempted persistence and when did it occur?
4. Contrast one approved forecasting agent action with the suspect chain using change approval and host context.
5. Correlate DNS and proxy telemetry and state why it cannot prove an OT compromise or actual dataset exfiltration.
6. List three IT containment actions and two reasons not to interfere with production control systems.

## Working method (Kali/Ubuntu/Windows)
From the repository root:

```bash
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py BUSINESS_APPLICATIONS/07_energy/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all
```

Build a timeline first. Compare source families and correlation IDs, identify unrelated approved business events, then prepare a two-column observation-versus-inference table. When there is no actual executable or content payload in the artifacts, you **must not** assert malware-family attribution, decrypted HTTPS payload contents or confirmed data theft.

## Deliverable
Complete [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md) with the event chain, a benign alternative, whether persistence is observed or only plausible, business impact *if* the scenario were real, evidence acquisition recommendations and proportionate containment. See [ASSESSMENT_RUBRIC.md](../ASSESSMENT_RUBRIC.md) for assessment. These six questions are ungraded practice, separate from the main HTB Sherlock.

**Author:** Beacon of the Eagle LLC / Centinell Suite Defense. Synthetic defensive training only.
