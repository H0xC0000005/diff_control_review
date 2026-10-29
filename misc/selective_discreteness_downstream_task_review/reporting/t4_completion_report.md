# T4 completion report

Date: 2026-09-10  
Status: T4 work complete; awaiting user approval; T5 not opened

## Outcome

All 31 records retained or conditionally retained at T3 were assessed against the approved extraction codebook. The final extraction set contains 30 records: 20 primary and 10 contextual. T0026 was rejected at the T4 value check because fixed, seeded scenario banks already provide the initially required paired stochastic treatment and a separate common-random-numbers method would add little decision value.

The final set contains 21 strong-quality and 9 adequate-quality records. There are no unresolved decision-critical access failures. The human-readable evidence, paper synopses, interpretations, and approval questions are in `../extraction/t4_evidence_audit.md`; structured coding is in `../extraction/task_evidence_matrix.csv`.

## Supplied-paper handling

T0007, *Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics*, was supplied by the user as a 14-page PDF. It was extracted locally with page markers using `pypdf` in the `differential_sim` conda environment.

- PDF SHA-256: `7c5062837923dda08a714cd232ff9fa4b9bbd7e9226d89c1b5cb04bdb070e822`
- Extracted-text SHA-256: `9388322ff100351a8fec6b0e98490ee30fe29e32e531f85a54307e90af182bea`
- Extracted text: 1,371 lines, 10,115 words, 63,012 bytes

The paper is the nearest located task predecessor: it combines an LTM network layer, continuous effective green fractions, aggregate turn queues, and a local allocation layer. It does not supply exact movement order, realized lane-access reachability, executable phase intervals, end-to-end simulator AD, or richer-evaluator gradient-transfer evidence.

## Files changed or produced in this continuation

- `archive/user_supplied/T0007_Wei_et_al_2025.txt`
- `archive/manifest.csv`
- `extraction/task_evidence_matrix.csv`
- `extraction/t4_evidence_audit.md`
- `full_text/institutional_access_request_T4.md`
- `reporting/t4_access_pause.md`
- `reporting/t4_completion_report.md`
- `README.md`
- `discussion/protocol_approval_record.md`
- `review_protocol_plan.md`

No project source, test, configuration, milestone, roadmap, or context file was modified.

## Commands and checks

- Installed `pypdf` in the existing `differential_sim` conda environment because command-line PDF text tools were unavailable.
- Extracted T0007 page by page with explicit page markers.
- Ran CSV parsing, record-count, status-count, quality-count, and unique-ID checks.
- Reconciled all T4 matrix IDs against the T3 retained/conditional set.
- Computed SHA-256 checksums and text line/word/byte counts.

Validation result: 31 unique assessed records; 20 primary, 10 contextual, and 1 T4 exclusion; final quality counts 21 strong and 9 adequate. The counts agree with the evidence audit.

## Assumptions and limitations

- Abstract synopses in the gate are paraphrases, not quotations.
- Previously archived full texts from the model-lineage review were referenced in place rather than duplicated.
- T0031 is retained only for a narrow claim supported by repository/abstract-level evidence; it controls no task-selection decision.
- Quality labels assess fitness for the specific extracted role, not an overall judgment of each publication.

## Current phase and next allowed action

T3 is closed. T4 work is complete but not closed until the user approves or corrects the five items in the T4 approval request. The next allowed action after approval is to close T4 and open T5 candidate-task synthesis. No T5 work has started.
