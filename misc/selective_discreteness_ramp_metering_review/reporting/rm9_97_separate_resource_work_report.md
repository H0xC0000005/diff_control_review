# RM9 separate-resource continuation work report

Date: 2026-10-02. Status: **UG3.B approved; bounded continuation completed to
observation-contract gate UG4; RM9 remains open.**

## Completed work and approval scope

The user explicitly selects Candidate B and asks continuation to the next gate.
Recorded UG3.B adoption and amended only G2's residual rate-resource coupling.
Lateral occupancy exchange and forward flow now have separate rate resources;
post-lateral forward sending/receiving are recomputed. Other UG2 clauses, UG1
Default allocation, strong history/action/accounting and X1–X3 deferral remain.

Rechecked conditional mass/storage bounds, local free-flow rates, post-lateral
reconstruction and conditional reconstruction from prior-step fluxes. An exact
rational example shows lateral-map noninjectivity within accepted bounds, without
equal lane speeds; equal post-states cannot distinguish actions occurring only
after that common map. No extra timestep/propensity condition was introduced.
Wrote strict-branch sensitivity and complete-time/departure identities.

Continued to G1's unresolved independent speed/support specification. UG4.A
(recommended) proposes an explicit idealized FD/passage observation hypothesis;
UG4.B proposes a bounded physical measurement/source review first. Neither is
approved or used to claim a full-history certificate. The resource choice did
not adopt a speed map. No numerical traffic/gradient experiment was performed.

## Scientific limits and assumptions

- Proofs are local/conditional on existing step and paired-transfer bounds.
  Exact ramp propagation, boundary geometry and complete observation support
  still need transcription; no whole-task calibration is claimed.
- The revised law is a reviewer adaptation, not the full published lane model.
  Removing the forced debit does not show every real maneuver is costless.
- Free-flow inversion identifies post-lateral state on its specified ordinary
  unimpeded branch. It does not automatically identify the pre-state or congested
  traffic; the independent speed channel is retained.
- Conditional history reconstruction requires identified actual per-lane fluxes
  and an audited ramp balance. No unknown post-meter traffic is silently removed.
- Noninjectivity of a control-independent stage is not a useful hidden-state
  result when the differing pre-states have identical post-states and all
  remaining state/forcing agree. No private forcing/prehistory is introduced.
- UG4's speed hypothesis adds a measurement idealization, not new acceleration
  dynamics. Its transient/physical passage interpretation is unvalidated.
- G3 exact strong-history/action and G4 numerical correctness/independent
  usefulness remain unestablished. Local different flow or internal derivative
  alone cannot prove complete-time benefit. Negative/sufficient results remain
  admissible; no new penalty is added to force a favorable result.

## New artifacts

- discussion/rm9_resource_b_approval_and_continuation.md
- reporting/rm9_50_separate_resource_findings_and_observer_gate.md
- extraction/rm9_separate_resource_claims.md
- synthesis/rm9/rm9_separate_resource_and_observer_audit.tex
- synthesis/rm9/rm9_separate_resource_and_observer_audit.pdf
- reporting/rm9_97_separate_resource_work_report.md

## Existing documents updated

- reporting/rm9_current_handoff.md
- synthesis/rm9/rm9_formulation_contract_inventory.md
- README.md
- rm9_00_compact_local_merge_formulation_review.md
- reporting/rm9_40_accepted_kernel_findings_and_resource_gate.md
- reporting/rm9_41_resource_literature_clarification.md
- extraction/rm9_accepted_kernel_claims.md
- extraction/rm9_joint_flow_readiness_audit.md
- synthesis/rm7_post_selection_design_inventory.md
- synthesis/rm9/rm9_deferred_lane_interaction_extensions.md
- discussion/rm9_review_dialogue.md
- ../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md (navigation only)
- ../differentiable_freeway_bottleneck_task_review/synthesis/s10/s10_post_closure_next_step_plan.md (navigation only)

Original handout/audit PDFs and TeX remain historical and unchanged. Root
AGENTS.md/PLANS.md retain pre-existing user modifications; no production
source/config/test, feedback inbox, source archive, CSV or environment change.

## Sources and commands

Reused FB0030 and RM0018 versions/IDs, directly opening primary PDFs to recheck
printed 1768–1769 measurement discussion and Section 3.1 node allocation.
No new query, source screening row or download. These are antecedents and
provenance checks, not proofs of new reviewer claims C23–C28.

Read-only inspection used rg/cat/sed/command -v/git status. New artifacts were
written using structured patches; the two living records were rewritten through
a Python heredoc. Other records were synchronized with a guarded script:

    python /tmp/rm9_b_sync.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_b_observer_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex
    cp /tmp/rm9_b_observer_latex/rm9_separate_resource_and_observer_audit.pdf misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.pdf
    /home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/rm9_b_validate.py

Local latexmk 4.83 and pdfTeX 1.40.25 / TeX Live 2023 compiled the new handout
without installation. Auxiliaries remain in /tmp. An initial attempted read
used a nonexistent RM8 filename; inspected the actual files returned by rg.
Two document synchronization patches failed format/context checks before
mutation; corrected the document-write method and exact anchors. Scientific
equations, gates and acceptance criteria were not changed to fix these issues.

Verification checks relative links, active/historical status, six stable new
claim IDs, CSV integrity/counts, preserved PDF hashes, exact rational hand
examples, PDF page/text output and the final LaTeX log. Python/pypdf inspect
document structure; no raster/visual-inspection claim. Hand arithmetic checks
are scalar identity verification, not traffic simulation or numerical gradients.
No production or scientific numerical tests ran.

## Status and next allowed action

UG3 closed with B approved. G2's resource clause amended, G1 at UG4, G3/G4
certificates unfinished. Discuss/adopt the observation route before dependent
history/action construction. No successor, deferred extension/VSL stage,
implementation, SUMO or experiment is opened. Final verification follows.

## Final verification

Passed with zero errors: 17 new/updated Markdown records, 114 local links,
11 existing query records, seven existing source/lead records, six stable new
claim IDs, exact rational hand arithmetic and a five-page PDF. The final LaTeX
log has no overflow/underfull boxes, undefined references or compilation errors.
Both historical PDF checksums remain unchanged. The final primary-source links
were added to the new PDF and its affected build/document checks rerun.

New PDF SHA-256:
f52fd2805fd6155d999a54e33bf2f6e3afc43edaaed5cae6da669b44a7e266bd.

Scope: six new artifacts and 13 existing review-document updates. Root git
status still shows only the pre-existing AGENTS.md and PLANS.md changes because
misc review artifacts are ignored. No production/scientific numerical tests ran.
