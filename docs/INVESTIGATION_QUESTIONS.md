# Investigation Questions — Medium
Answer each with exact artifact names, record IDs, and UTC times where applicable. Some questions require joining multiple tables. **Do not guess** when evidence permits only a narrower claim.

1. Which message (Message-ID and subject) preceded the suspicious file activity, and who was the recipient?
2. What archive was delivered and how do the email and file-origin evidence connect it to the endpoint?
3. What is the first observed launch time of the suspicious extracted executable, and which process launched it?
4. Reconstruct the suspicious process chain, including process GUIDs, from initial execution to the staged agent.
5. Which file was written to a persistence-related path? Give the observed destination and artifact tying it to the process chain.
6. Identify the persistence mechanism, task path, executable target, trigger and account. Which independent records corroborate it?
7. Which static-inspection traits make the staged agent suspicious, and what **cannot** be concluded from the static report alone?
8. Decode the inert configuration field in the static report. What campaign identifier, domain, URI path and interval does it declare?
9. Which DNS and proxy events align with that declared endpoint? Give the time of the first matching **observed** request.
10. Which local archive was staged, and which two data-source paths were recorded immediately before it?
11. How do proxy byte counts and staging records support a *possible transfer*, and what limitation prevents proving the specific contents uploaded?
12. Identify one legitimate software-update event that might be mistaken for part of this intrusion. Explain how you distinguished it.
13. Construct a defensible 6+ event timeline, correlating at least four different evidence sources.
14. Select three appropriate MITRE ATT&CK techniques and give artifact-level justification for each.
15. Propose an evidence-based containment sequence that preserves investigative integrity and limits further activity.

**HTB portal:** short-answer, unique-answer forms and accepted variations should be finalized after independent solve-test. This document intentionally excludes answer values.
