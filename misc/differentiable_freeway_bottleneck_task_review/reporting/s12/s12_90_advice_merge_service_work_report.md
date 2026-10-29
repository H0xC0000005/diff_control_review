# S12.90 — Advice–merge–service review work report

Date: 2026-09-30. Status: **Closed; G4-A approved and AMR-A accepted.**

## Work completed

- Recorded approval of G1-A, G2-A and G3-A and the user's deferral of G4.
- Reconstructed the S05 fixed-service obstruction and reused S06/S10/S11 source
  and scope boundaries before new discovery.
- Screened lane-change void/relaxation, conservative mandatory transfer with
  finite receiving, controlled lane balancing, perceived-density capacity drop
  and aggregate capacity-drop/hysteresis families.
- Audited conservation, common-VSL reachability, S05 escape, aggregate limit,
  observer separation, complete-accounting implications and derivative regime.
- Identified one bounded family that provisionally passes working G4-A and
  stopped at the required user gate.

## Files created

- `extraction/s12_advice_merge_service_source_audit.md`
- `synthesis/s12/s12_mechanism_admission_matrix.md`
- `search/s12_advice_merge_service_query_log.csv`
- `search/s12_advice_merge_service_access_log.csv`
- `reporting/s12/s12_20_advice_merge_service_findings_and_gate.md`
- `reporting/s12/s12_90_advice_merge_service_work_report.md`
- `reporting/s12/s12_80_advice_merge_service_dialogue.md`
- `reporting/s12/s12_99_advice_merge_service_sprint_closure.md`

## Files updated

- `s12_00_analytical_advice_merge_service_admission_review.md`
- package navigation, reporting/synthesis guides, successor status and document
  registry.
- S12 findings and mechanism matrix were expanded after the user requested the
  sufficient admission rationale and research-question status explicitly.
- The S12 dialogue now records the task-formulation and methodology differences
  between the S05 restricted analytical construction and S12/M2.
- The user-approved G4-A/AMR-A closure and targeted S13 planning handoff were
  recorded; the root-level S13 proposal was opened at S13-PG1.

## Commands and tools

- Repository inspection with `rg`, `find`, `sed` and `cat`.
- Bounded primary-source web search and rendered full-text/abstract inspection,
  recorded in the S12 search/access logs.
- Package-local Markdown-link, CSV and registry validation; focused trailing-
  whitespace checks for all S12/updated navigation files; `git diff --check`.
  All S12 checks passed. A package-wide whitespace scan also reported eight
  pre-existing trailing-space lines in S01/S02 and one archived draft; these
  unrelated historical files were left unchanged.

No simulator, SUMO, implementation, calibration, optimization, numerical traffic
experiment, gradient calculation or environment-changing command was run.

## Acceptance results

| Planned item | Result |
|---|---|
| Permanent lane-drop/common-VSL compatibility | Passed for the selected class, with response-law qualification. |
| Conservative finite receiving/service mechanism | Passed. |
| Coefficient-independent S05 structural escape | Passed: binding receiving plus positive mandatory transfer removes fixed service. |
| Strong-history observer separation | Coherent admission argument; exact near-drop witness remains open. |
| Aggregate countercandidate | Passed; aggregate capacity drop remains viable and limits the claim. |
| Complete action-ranking result | Not established; intentionally reserved for full derivation. |
| Derivative boundary | Classified as piecewise differentiable with active-set boundaries; no gradient claim. |
| G4-A verdict | AMR-A accepted; one family admitted for separate analytical planning. |

## Assumptions and unresolved risks

The review assumes only that a later model may combine compatible source-backed
elements; it does not assume that the combined chain produces a useful action
split. Common-VSL response is supported across related lane-drop/merge settings,
but no inspected source supplies the exact joined law. The strong-observer
separation is structural and conditional, not yet a reachable full-history
certificate. The search is bounded and does not prove literature-wide absence or
uniqueness of the admitted family.

## Closure and handoff

The user selected G4-A, accepted AMR-A and closed S12. A targeted S13 has been
inserted before ramp-metering review. S13 may now propose its analytical model-
contract/certificate plan, but no equations, derivation, implementation or
experiment may begin before S13-PG1 approval.
