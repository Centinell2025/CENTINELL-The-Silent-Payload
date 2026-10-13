# Case Brief — NB-IR-026
**Organization:** Northbridge Systems Ltd. (entirely fictional)  
**Case date:** 22 September 2026 (all timestamps UTC)  
**Endpoint:** NB-WS-044  
**Assigned user:** NORTHBRIDGE\\mrivera  
**Escalation:** suspicious utility launched from a downloaded archive; unusual scheduled task and outbound HTTPS requests followed.

The employee reports receiving an email about quarterly roster corrections and extracting a utility named `RosterViewer.exe`. Security analysts recovered sanitized process, file, task, network, email, and static-inspection records. Authorized business and software-updater activity occurs in the same window. The investigation must prove which events belong to the incident.

## Objectives
1. Establish the delivery path and the user action.
2. Identify process ancestry and the point of malicious execution.
3. Recover and interpret suspicious capabilities from **inert static-inspection artifacts**.
4. Determine whether persistence was created, by what mechanism and under which identity.
5. Correlate file staging with egress events, without claiming facts unsupported by packet content.
6. Recommend detection and containment supported by the evidence.

## Evidence standard
Each response must reference specific **file, record ID, and UTC timestamp**. Correlate across two or more independent evidence types where possible. Distinguish observation, inference, and uncertainty.

**Boundary:** no real production system is involved. The case is completely synthetic.
