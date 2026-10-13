# Business Applications & Exercises
## Aplicaciones empresariales y ejercicios

**CENTINELL — The Silent Payload | Applied Malware Analysis (Medium)**

These **ten fictionalized, anonymized training exercises** imitate common workflows and defensive investigation challenges found in real businesses. They are **not case studies of particular companies**, not copied incident reports and not derived from private customer data. Names, hosts, senders, telemetry and domain names have been invented. **No IP addresses** or runnable malware are supplied.

Estos diez ejercicios representan escenarios empresariales habituales **sin revelar nombres de empresas, direcciones IP ni información real**. Todos los incidentes y registros son simulados.

| Training scenario | Business environment | Key skill | Estimated time |
|---|---|---|---|
| [Unapproved Payment Reconciliation Tool](01_finance/CASE_AND_EXERCISE.md) | Finance and accounts payable | Attachment and origin correlation + Process tree reconstruction | 45–60 min |
| [Appointment Utility That Changed a Service](02_healthcare/CASE_AND_EXERCISE.md) | Healthcare administration | Service creation analysis + User/process correlation | 45–60 min |
| [Planning-Station Utility and an Unexpected DLL](03_manufacturing/CASE_AND_EXERCISE.md) | Manufacturing business operations | DLL-load telemetry interpretation + Office IT vs OT boundary | 50–70 min |
| [Shipping Label Helper and Data Staging](04_logistics/CASE_AND_EXERCISE.md) | Distribution and logistics | Registry Run-key triage + Local staging investigation | 45–65 min |
| [Client Report Add-In with Abnormal Child Processes](05_professional_services/CASE_AND_EXERCISE.md) | Professional services / consulting | Process-chain reconstruction + Task-based persistence | 45–60 min |

| [Scholarship Portal Converter and a Hidden Login Script](06_education/CASE_AND_EXERCISE.md) | Education administration | User Execution / Task Scheduler / simulated browser hijack | 50–80 min |
| [Grid Planning Spreadsheet Add-in and DLL Search Order](07_energy/CASE_AND_EXERCISE.md) | Energy planning office IT | DLL observation / scheduled task / IT-OT scoping | 50–80 min |
| [Reservation Export Helper and Auto-Start Service](08_hospitality/CASE_AND_EXERCISE.md) | Hospitality back-office | Service persistence / credential-boundary analysis | 50–80 min |
| [Inventory Price Sheet and WMI Subscription](09_retail/CASE_AND_EXERCISE.md) | Retail inventory support | WMI persistence / business impact uncertainty | 50–80 min |
| [Media Render Queue and Masquerading Login Item](10_media/CASE_AND_EXERCISE.md) | Media production operations | Startup persistence / masquerade / provenance | 50–80 min |

### Instructions
For each scenario open `CASE_AND_EXERCISE.md` and `events.csv`. Answer with precise event IDs and UTC timestamps; label **observation**, **inference**, and **unproven claim** separately. Investigations are offline only.

Suggested Kali commands:
```bash
head -n 5 BUSINESS_APPLICATIONS/01_finance/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py BUSINESS_APPLICATIONS/01_finance/events.csv
python3 BUSINESS_APPLICATIONS/tools/inspect_events.py --validate-all
```
All ten exercises are introductory-to-intermediate applied practice. They supplement — and do not replace — the **main Medium Sherlock investigation**. They are not independent paid HTB submissions.

### Training principles
1. **Realistic operating patterns, fictional records:** do not claim any scenario happened at a real named enterprise.
2. **No disclosure:** all hostnames and emails are test data; domains end in `.test`; no numeric IP addresses.
3. **Defensive scope:** no code execution, exploit development, credential collection, or malware binaries.
4. **Evidence-first reasoning:** every answer must cite exact row IDs and distinguish telemetry from intent.
5. **No instructor solutions in this public repo:** the instructor key remains offline.

**Publisher:** Beacon of the Eagle LLC / Centinell Suite Defense.
