# RM9 accepted-kernel continuation work report

Date: 2026-10-02. Status: **UG2.A accepted; continuation completed to UG3;
residual resource part of G2 explicitly reopened. RM9 remains open.**

## Authorized task and completed result

The user accepted the PDF handout, confirmed stashing the extension ideas and
instructed review continuation to the next user gate. Recorded UG2.A adoption
without a repeated approval request and retained X1–X3 as Deferred hypotheses.
No git stash or alteration of unrelated working changes was performed.

Continued the bounded static mathematical review. Proved conditional mass/storage
bounds, per-cell total-plus-one-lane state equivalence, a free-flow lateral-to-
forward debit in the accepted residual coupling, its persistence as timestep
shrinks at fixed state/length, and a conditional independent-speed reconstruction
including the unknown transfer direction. Made a separate-resource alternative
concrete and proved its conditional storage/conservation bounds before stopping.

The original accepted equation/PDF artifact is preserved. New evidence makes the
implicit service cost explicit and reopens only G2's residual rate-resource
clause at UG3. A retains a declared conditional common-service resource; B
(recommended) proposes separate transverse occupancy and forward capacity.
Neither a new law nor a weakened observer was adopted. No feasible exact-history/
useful-action pair, full derivative verification or independent one-step gradient
usefulness has been established. This is not RM9 closure or a new stage opening.

## Assumptions and material limitations

- Acceptance adopts the candidate for review; it does not prove physical
  calibration, necessity of hidden lanes or externally useful derivatives.
- UG1 priorities remain Default and common across comparisons; numerical values
  are not chosen to induce action reversal. X1–X3 stay deferred by user approval.
- The debit proof is for strict uncapped sending and enough residual downstream
  receiving on an ordinary interface. It uses neither equal lane speeds nor a
  special ramp cost; it does not prove total-time loss for an entire trajectory.
- The original conservation proof passes under step and paired-flow/ramp/boundary
  conditions. Conservation and physical service-resource justification differ.
- The strong-observer theorem assumes positive lanes and a co-supported independent
  passage-speed map with known unequal lane speeds. The actual observer is not
  frozen; no universal field/congested-state sufficiency is claimed.
- One extra lane coordinate is sufficient given each cell's total in the two-lane
  reference. It is not one scalar for an entire multi-cell zone or proof of
  individual vehicle/discrete-order necessity.
- The proposed separate-resource operator is a new interpretation, not a clerical
  deletion of redundant bounds or calibrated literature adoption. Common forward
  merge receiving remains shared; transverse and longitudinal rate resources
  are declared different, while traffic mass and finite storage are conserved.
- Exact geometry, ramp propagation/boundaries, observation support/initialization,
  remaining action relevance, event derivatives and richer-reference usefulness
  remain unresolved. No extension supplies an automatic positive result.

## Files created

- `discussion/rm9_handout_acceptance_and_ug2_closure.md`
- `reporting/rm9_40_accepted_kernel_findings_and_resource_gate.md`
- `extraction/rm9_accepted_kernel_claims.md`
- `synthesis/rm9/rm9_accepted_kernel_semantics_audit.tex`
- `synthesis/rm9/rm9_accepted_kernel_semantics_audit.pdf`
- `reporting/rm9_96_accepted_kernel_audit_work_report.md`

## Existing documents updated

- `discussion/rm9_review_dialogue.md`
- `synthesis/rm9/rm9_deferred_lane_interaction_extensions.md` (confirmed deferral)
- `rm9_00_compact_local_merge_formulation_review.md`
- `synthesis/rm9/rm9_formulation_contract_inventory.md`
- `reporting/rm9_current_handoff.md`
- `reporting/rm9_30_allocator_contract_and_control_chain.md` (history/disposition)
- `extraction/rm9_joint_flow_readiness_audit.md` (subsequent disposition)
- `synthesis/rm7_post_selection_design_inventory.md` (active status only)
- `README.md`
- `../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md` (navigation only)
- `../differentiable_freeway_bottleneck_task_review/synthesis/s10/s10_post_closure_next_step_plan.md` (navigation only)

Root AGENTS.md and PLANS.md already had user modifications and were not edited.
No production source/tests/configs, environment/dependency, approved implementation
plan, feedback inbox or archived source PDF changed. The original accepted
handout PDF and TeX remain untouched. Review files are in the existing ignored
misc tree, so git status alone does not enumerate this documentation work.

## Sources, commands and validation method

Rechecked primary FB0030 final PDF's coupling and detector-speed sections and
RM0018's node section through direct web open calls. Existing IDs/versions and
archives retained. These establish provenance boundaries, not the new theorems.
No new search query, source ID or full-text download; old query/screening CSVs
remain intact. The new six claim IDs C17–C22 are scoped in the extraction record.

Read-only shell inspection used rg, cat, sed, head, command -v and git status.
Temporary standard-library scripts recorded decisions and synchronized reports:

```
python /tmp/rm9_acceptance.py
python /tmp/rm9_kernel_results.py
python /tmp/rm9_kernel_sync.py
python /tmp/rm9_kernel_work_report.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_kernel_audit_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_accepted_kernel_semantics_audit.tex
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/rm9_kernel_validate.py
```

The new TeX was written through a shell heredoc; a first build caught a missing
backslash at an equation-environment closing delimiter. Corrected transcription
and rebuilt, with no change to mathematics. Installed pdfTeX 1.40.25 / TeX Live
2023 and latexmk 4.83 used without installation. Build auxiliaries stay in /tmp;
PDF and editable TeX are together in the branch. Validation uses Python 3.11.9 /
pypdf 6.15.0. No available raster preview was used; no visual-inspection claim.

Mathematics was checked by direct derivation and hand arithmetic. No numerical
traffic simulation, finite-difference/autograd test, optimizer, SUMO, production
unit test or environment-modifying operation ran. Document verification covers
links, source/claim IDs, CSV integrity, active/historical status, preserved old
PDF checksum and new PDF page/text/log checks. An initial PDF text check expected a literal phrase not used in the handout;
corrected that document-harness marker to the actual forward-budget explanation.
No formula or scientific criterion was changed. Final results follow below.

## Current status and next allowed action

UG2.A acceptance and X1–X3 deferral recorded. Continued analysis reached UG3;
G2 residual resource meaning is reopened, while lane count, bounded propensity,
Default node allocation, action and accounting remain. G1 is unfinished and
G3/G4 core certificates unestablished. Discuss UG3 before changing any accepted
law or continuing its dependent certificate. No implementation, numerical
experiment, RM10, multi-ramp review or deferred VSL successor opened.

## Final verification result

Passed with zero errors: 15 changed Markdown documents, 88 local links,
11 existing query records, 7 existing source/lead records, six scoped new claims,
and a 5-page mathematical PDF. Final LaTeX log has no overflow/underfull boxes,
undefined references or compilation errors. The accepted prior PDF checksum is
unchanged. Scope: six new artifacts and eleven existing document updates.
No production or numerical scientific tests ran.

New PDF SHA-256: `b0e4b08e849539716c778b9d0b37eab4c7dad2cec87e6a3b14dc2216b7b3a05d`.

Accepted prior PDF SHA-256: `5c572965ff85079191741437f36e96baf5ec88fc1a0b1e91fd02db8dc77cf613`.
