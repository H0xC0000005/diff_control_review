# Reporting directory guide

Reports are grouped by the sprint that owns their scientific or procedural
meaning. Filenames retain the `sNN_RR_` prefix so their identity and reading role
remain visible outside this directory.

| Directory | Contents |
|---|---|
| [`s01/`](s01) | Initial freeway-task findings, accepted gate and dialogue. |
| [`s02/`](s02) | Predecessor review, feedback responses, dialogue and work record. |
| [`s03/`](s03) | Route B evidence review, access request, work record and closure. |
| [`s04/`](s04) | Diagnostic-methodology findings, living dialogue, work record and closure. |
| [`s05/`](s05) | Analytical certificate explanation, findings, work record and closure. |
| [`s06/`](s06) | Reference bridge, colleague handout and closure. |
| [`s07/`](s07) | Reachable-preparation findings, work record and closure. |
| [`s08/`](s08) | Exact-prefix planning findings, work record and closure. |
| [`s09/`](s09) | Historical readiness audit and methodology-only scope correction. |
| [`s10/`](s10) | Sufficiency findings, final colleague report, work record and review closure. |
| [`s11/`](s11) | Temporary-closure recovery admission findings and work record. |
| [`s12/`](s12) | Analytical advice–merge–service findings, clarification dialogue and work record. |
| [`s13/`](s13) | Targeted M2 certificate findings, study-sufficiency audit, contract dialogue, work record and closure. |
| [`shared/`](shared) | Package-level navigation and maintenance records. |

Use the package [reading guide](../00_review_sequence.md) for scientific order and
the [document registry](../review_document_registry.csv) for canonical paths.
Paired source/rendered artifacts remain together in the owning sprint directory.
A dialogue file remains under its originating sprint even when later decisions
are appended to it.

The temporary-closure successor has an approved root-level
[`s11_00_...` plan](../s11_00_temporary_closure_recovery_admission_review.md).
Its findings and work records are grouped in `s11/` using the approved
`s11_RR_...` scheme.

The analytical successor has an approved root-level
[`s12_00_...` plan](../s12_00_analytical_advice_merge_service_admission_review.md).
Its bounded review is closed with G4-A/AMR-A; findings, dialogue, work record and
closure are grouped in `s12/`.

The targeted M2 successor has an approved root-level
[`s13_00_...` plan](../s13_00_m2_analytical_contract_certificate_review.md).
Its methodology-only derivation closed with M2C-A; findings, study-sufficiency
audit, dialogue, work record and closure are grouped in `s13/`.
