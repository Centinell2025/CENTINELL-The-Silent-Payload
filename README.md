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

Five evidence-backed fictionalized scenarios using realistic enterprise patterns but **no real company names, IPs or customer information**:
1. Finance and accounts payable
2. Healthcare administration
3. Manufacturing office operations
4. Distribution and logistics
5. Professional services

Includes **30 practice questions**, anonymized CSV event logs, Kali-compatible offline analysis helper, assessment rubric and analyst report template. These are supplemental training exercises, not separate submitted HTB Sherlocks.

## Main Sherlock investigation
The primary Sherlock evidence set and evaluator write-up are separate release milestones. This repository currently includes the case design and the five applied exercises; the **main Sherlock evidence bundle has not yet been published or independently solved**. Do not submit to HTB as complete at this stage.

## Important
All names, identities, domains, devices and events are **fabricated for training**. No real IP addresses, live malware binaries, secrets, private Centinell technology or customer information are published. Do not treat narrative claims as proved: cite exact artifacts and timestamps.

**Student-safe repository:** instructor answer keys and walkthroughs are not stored here. HTB submission artifacts will be assembled after independent verification.

© 2026 Beacon of the Eagle LLC. Original simulated training case. All rights reserved; evaluation and training use by permission.
