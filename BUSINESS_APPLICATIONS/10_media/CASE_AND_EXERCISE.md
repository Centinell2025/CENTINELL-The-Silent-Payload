# Media Render Queue and Masquerading Login Item

**Northbridge Systems Ltd. — simulated Media production operations division**  
**Difficulty:** Medium, optional applied lab (approximately 50–80 minutes)  
**Publisher:** Beacon of the Eagle LLC — Centinell Suite Defense

## Incident handoff
A video-operations coordinator receives a render-queue booster. A background task writes a lookalike startup item while a genuine approved codec update happens nearby. No licensed media, artists, or real content is provided.

## Scope, evidence and safety
The supplied [events.csv](events.csv) is a normalized synthetic event table (16 rows) with original source **categories**, not original Windows EVTX, Sysmon or network captures. All identities and hosts belong to a fictional Northbridge division. All domains end in reserved `.test`; no numerical IP addresses, malware samples, live hosts or private customer details are included. Do not run, reconstruct or deploy any named executable.

### Business question
Decide what the observed records actually establish, which hypotheses remain unproven, what extra artifacts are needed and how a security analyst should prevent disruption to normal operations.

## Investigative questions — cite event IDs and exact UTC times

1. Connect the downloaded render helper with the first observed child process and retained file.
2. Compare legitimate codec-update authorization with the suspicious lookalike file and identify exact records.
3. Which Startup-folder artifact implies possible persistence and what proof of its execution is missing?
4. Correlate DNS and outbound proxy observations to the suspicious command chain.
5. Is the alleged copying of production media demonstrated by these artifacts? Explain the evidentiary limit.
6. Propose a non-disruptive investigation that preserves active render workloads and suspected persistence.

## Working method (Kali/Ubuntu/Windows)
From the repository root:

```bash
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py BUSINESS_APPLICATIONS/10_media/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all
```

Build a timeline first. Compare source families and correlation IDs, identify unrelated approved business events, then prepare a two-column observation-versus-inference table. When there is no actual executable or content payload in the artifacts, you **must not** assert malware-family attribution, decrypted HTTPS payload contents or confirmed data theft.

## Deliverable
Complete [REPORT_TEMPLATE.md](../REPORT_TEMPLATE.md) with the event chain, a benign alternative, whether persistence is observed or only plausible, business impact *if* the scenario were real, evidence acquisition recommendations and proportionate containment. See [ASSESSMENT_RUBRIC.md](../ASSESSMENT_RUBRIC.md) for assessment. These six questions are ungraded practice, separate from the main HTB Sherlock.

**Author:** Beacon of the Eagle LLC / Centinell Suite Defense. Synthetic defensive training only.
