# Resumed Step 3: qualification work and final review gate

Date: 2026-10-14. Scope: methodology review, source inspection, algebra and
documentation only. The user explicitly authorised closing the current gate
with the model → SUMO S-P → SUMO S-L ladder and resuming Step 3.

The ladder decision S3-M1 is closed. The bounded analytical/source review
and comparison-protocol assembly have now reached VSL-S3-G1. One physical
choice remains: S3-M2 selects a point priority boundary or finite native
junction for S-P. J-P point is provisionally recommended; neither candidate
is approved. **Step 3 is not user-closed; Step 4 is unopened.**

[Main traffic findings, direct question answers and expanded gate](vsl_step3_reference_qualification_and_final_gate.md)

## Completed review and assumptions

Reused the accepted H1/T1 analytical information/action/sensitivity results,
S13 literature and strongest-rival screen. Inspected official SUMO
documentation and public source. The new headway note derives a conditional
stationary correspondence to H1's capacity curve and an effective-server
identifiability limit; it neither changes the primary law nor calibrates it.

Qualified a source-supported request/native-service separation, with explicit
handoff lifecycle obligations. Consolidated causal finite-cohort replay,
common permitted advice, full-time completion, parameter provenance,
development/held-out separation, derivative versus policy evidence, strong
compact/search rivals and future native-admission criteria. No concrete
aggregate prior/controller, microscopic driver parameter or physical
numerical dimension was selected through a local convention.

The main report distinguishes direct source support from the review's
deductions. It compares the two remaining physical boundary representations
against the same residual-driver example, with explicit Pros/Cons and G3/G4
dependencies. The stage status and living inventory are synchronised.

One ordinary reference vehicle remains one vehicle equivalent in predictor
input. Uniform coarse profiles, native history differences, ideal-versus-
actual speed, native priority-versus-zero-A-delay and finite-versus-point
service remain declared approximation boundaries. The positive analytical
work-factor range is still not traffic-qualified; small-work/common-fastest
and negative-transfer outcomes remain admissible.

## Files changed

New durable artifacts:

- `reporting/research_readiness/vsl_step3_reference_qualification_and_final_gate.md`:
  conceptual findings, direct S3-Q1–Q4 results and S3-M2 candidates.
- `synthesis/research_readiness/vsl_step3_stationary_headway_correspondence.tex`
  and `.pdf`: two-page mathematical support.
- `reporting/research_readiness/vsl_step3_resumed_review_work_report.md`:
  this record.
- `reporting/research_readiness/vsl_step3_resumed_review_validation.json`:
  current document, unchanged-contract, PDF and exact-algebra checks.
- `reporting/research_readiness/vsl_step3_stationary_headway_build.log`:
  final successful LaTeX build log.

Updated review records:

- `synthesis/research_readiness/vsl_step3_first_verification_protocol_draft.md`:
  consolidated acceptance layers, future admission diagnostics, strong rivals,
  outcome/observer limits and execution/freeze boundary.
- `extraction/research_readiness/vsl_step3_reference_and_evidence_audit.md`:
  actual viewed documentation/source references and support/adaptation limits.
- `synthesis/research_readiness/vsl_feedback1_core_model_candidates.md`:
  live Type 2 S3-M2 inventory and dependent Type 1 split.
- `reporting/research_readiness/vsl_step3_comparison_review_plan.md`,
  `vsl_review_progress.md`, `vsl_step3_validation_ladder_decision.md`,
  `vsl_step3_findings_and_gate.md`, `vsl_step3_sumo_bridge_and_terminal_gate.md`
  and `vsl_step3_sumo_work_report.md`: resumption, gate and historical-status
  clarification.
- `reporting/research_readiness/vsl_successor_opening_dialogue.md`:
  interpreted authorisation, findings, remaining choice and checks.
- `README.md`, `vsl_successor_00_opening_plan.md`,
  `synthesis/research_readiness/vsl_successor_methods_outline.md` and
  `extraction/research_readiness/vsl_successor_baselines_and_evidence_gaps.md`:
  current gate notices and direct report entry.

The accepted H1/T1 source/PDF, all production simulator code, tests/configs,
dependency/environment files, prior scientific results and user feedback
are untouched. Preexisting root edits to AGENTS.md, PLANS.md and memo.txt
are left unchanged. The review package is Git-ignored; its artifacts are
saved on disk and their current identities are in the validation JSON.

## Commands and verification

Used read-only `sed`, `cat`, `rg` and `git status --short` for inspection.
Official-source `web__run` search/open/find supplied the documentation/source
audit. No new published paper was substantively read. Documentary edits used
`apply_patch`; a patch failed an exact context check and changed no files
before its corrected application.

The installed LaTeX engine is pdfTeX 1.40.25, TeX Live 2023/Debian. The first
build requested unavailable `lmodern.sty`. Removed that optional dependency
and used existing Computer Modern fonts; no package was installed. Replaced
bitmap bullet glyphs with numbered entries so the final PDF uses outline
fonts. The successful build has two pages and no overflow warning.

From the review-package directory:

```text
mkdir -p /tmp/vsl_step3_headway_build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/vsl_step3_headway_build synthesis/research_readiness/vsl_step3_stationary_headway_correspondence.tex
cp /tmp/vsl_step3_headway_build/vsl_step3_stationary_headway_correspondence.pdf synthesis/research_readiness/vsl_step3_stationary_headway_correspondence.pdf
cp /tmp/vsl_step3_headway_build/vsl_step3_stationary_headway_correspondence.log reporting/research_readiness/vsl_step3_stationary_headway_build.log
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_step3_resumed_review_checks.py
```

The scratch check covers Markdown target/anchor existence, current decision
status, the accepted primary source/PDF hashes, exact integer-compatible
population arithmetic, exact stationary formula correspondence and PDF
structure/text/font/build-log checks. These are documentation and algebra
checks, not traffic experiments or numerical gradient validation. No visual
raster inspection is claimed.

**Results:** all checks passed across 16 Markdown files, 340 local links
and 27 heading anchors, with 45 exact stationary-formula arithmetic cases.
Both accepted H1/T1 artifact hashes are unchanged. The new PDF has two
pages, 132020 bytes, strict parse/text checks passed, outline Type 1 fonts
and no overflow warning. The first PDF-text assertion encountered normal
line-end hyphenation; the checker now normalises that extraction detail
before checking the same required content. No scientific criterion changed.

[Detailed verification results and artifact hashes](vsl_step3_resumed_review_validation.json)

[Final LaTeX build log](vsl_step3_stationary_headway_build.log)

## Scientific limits and next allowed action

Stationary capacity shape does not admit dynamic preparation/forced-work
parameters or prove the desired speed tradeoff in traffic. External-request
conformance, initialisation, geometry, native service and full clearance need
future version-pinned execution evidence. An aggregate controller needs its
own predeclared inference/uncertainty rule; H1's complete-history collision
does not certify one in SUMO. No gradient or advice has been externally tested.

The next allowed action is selecting J-P or J-F, then documentary consistency
and approval/freeze of Step 3. No additional roadmap stage was opened. The
separate execution proposal comes later; its tolerances/settings cannot
change closed scientific meaning. Stop at this gate. Step 4, simulator
development, installations, traffic runs, urban changes and the closed
ramp line remain unopened.
