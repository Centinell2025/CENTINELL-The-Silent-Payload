# Assessment Rubric — Applied Malware Analysis

Score each sector exercise out of **100 points**:
- **Evidence attribution (25):** correct source records and joins; consistent UTC timeline.
- **Malware behavior assessment (25):** accurately differentiates process/file/persistence observation from malware classification; no unsupported claims.
- **Benign activity discrimination (15):** explains why at least one nearby event is not part of the suspicious chain.
- **Business context and impact (15):** explains plausible operational consequences without inventing actual data loss or system compromise.
- **Containment & integrity (15):** non-destructive, authorized response, provenance and artifact preservation.
- **Reporting quality (5):** clear, reproducible wording and references.

**Passing target:** 75/100; **expert-quality goal:** >=90/100. These are internal learning thresholds, **not HTB grading criteria**.

Never award full marks for statements like “data was exfiltrated” when the only support is encrypted proxy byte counts. Require packet capture, decrypted application logs, receiving-system audit trails, or comparable direct evidence before a definitive conclusion.

**Exercise mode:** optional independent drills, not the mandatory HTB Sherlock question set. Instructor keys and private write-up must not be committed to this public student repository.
