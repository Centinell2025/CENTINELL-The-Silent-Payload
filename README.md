# CENTINELL — The Silent Payload
### Hack The Box Sherlock | Medium | Malware Analysis & DFIR

**Created by Beacon of the Eagle LLC / Centinell Suite Defense**

An analyst at the fictional **Northbridge Systems Ltd.** receives an endpoint escalation: a roster-review utility launches an unexpected child process, writes a second executable, and establishes recurring network activity. The learner must reconstruct the intrusion from independent forensic artifacts, separate authorized activity from attacker behavior, and identify the simulated malware family's capabilities.

**Investigation type:** offline, evidence-based malware triage. **Difficulty target:** Medium (4–8 hours). **Expected tools:** Kali Linux, `file`, `strings`, `grep`, `jq`, `python3`, YARA (optional), timeline analysis.

## Case assets
- [Case brief](docs/CASE_BRIEF.md)
- [Student instructions](docs/STUDENT_GUIDE.md)
- [15 Investigation questions](docs/INVESTIGATION_QUESTIONS.md)
- [Scope and safety](docs/SAFETY_AND_SCOPE.md)
- [MITRE analysis worksheet](docs/ATTACK_WORKSHEET.md)

## Applied business examples and practical exercises
**NEW:** [BUSINESS_APPLICATIONS — Aplicaciones empresariales y ejercicios](BUSINESS_APPLICATIONS/README.md)

Ten evidence-backed fictionalized scenarios using realistic enterprise patterns but **no real company names, IPs or customer information**:
1. Finance and accounts payable
2. Healthcare administration
3. Manufacturing office operations
4. Distribution and logistics
5. Professional services
6. Education administration
7. Energy planning (office IT only)
8. Hospitality back-office
9. Retail inventory support
10. Media operations

Includes **60 practice questions**, anonymized CSV event logs, Kali-compatible offline analysis helper, assessment rubric and analyst report template. These are supplemental training exercises, not separate submitted HTB Sherlocks.

## Main Sherlock investigation
The **main case evidence files are now published** in [evidence/](evidence/README.md), with an inert static-analysis report, offline tools, cryptographic manifest and student ZIP. The instructor's confidential walkthrough and independent blind-solves remain outstanding. Do not call this HTB-approved or ready for payment.

## Student training download
- [Evidence and file map](evidence/README.md)
- [15-question main case](docs/MAIN_CASE_WALKTHROUGH_STUDENT.md)
- [Student ZIP — full case and 10 business labs](downloads/CENTINELL-The-Silent-Payload-STUDENT.zip)

Use `python3 tools/verify_case.py` to check the manifest, `python3 tools/triage_case.py --timeline` to analyze events, and `python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all` to validate sector lab records. All analysis works offline.

## Important
All names, identities, domains, devices and events are **fabricated for training**. No real IP addresses, live malware binaries, secrets, private Centinell technology or customer information are published. Do not treat narrative claims as proved: cite exact artifacts and timestamps.

**Student-safe repository:** instructor answer keys and walkthroughs are not stored here. HTB submission artifacts will be assembled after independent verification.

© 2026 Beacon of the Eagle LLC. Original simulated training case. All rights reserved; evaluation and training use by permission.
