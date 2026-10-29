# Accepted direction: coupled point merging with choke-line completion

**Status: Approved; S3-M2's representation/completion choice closed,
2026-10-14.** The user accepted revised option 1 as a middle ground and
asked whether that choice closes the current gate. It does: select C-P
for the bounded terminal qualification, retaining a local completion
objective. This records the methodological choice, not approval of service
equations that have yet to be formed.

The task keeps the merging point and its completion line. Its terminal
model must allow compulsory E entry to restrict continuing A traffic,
with physical queueing and propagation on the existing terminal approach.
A priority convention can remain, but A is no longer required to be immune
to the consequences of an admitted slow E vehicle in the successor model.
Traffic completing the measured task must retain whatever causal influence
is needed to determine later departures.

## What the decision fixes

| Closed choice | Accepted meaning |
|---|---|
| **S3-M2-A: representation direction** | Qualify coupled point service/state that permits continuing-traffic delay and upstream propagation. The old zero-A-delay restriction is reopened within the narrow G3 terminal review. No exact replacement law, work factor or recovery state is selected yet. |
| **S3-M2-B: completion domain** | Count the full initial cohort from decision to crossing the choke line. Include all delay before crossing. Post-crossing vehicle-time is outside this local objective, while its causal influence on unfinished traffic must persist. |
| **Scope of the return** | Requalify compulsory service and terminal storage/receiving. Preserve H1 preparation and its handoff where the new domain supports them; consequential feedback into preparation is a stop/reopen condition. |
| **Alternative status** | C-Z's downstream recovery reach is unselected and retained as a return route. Adopting it would explicitly reopen the accepted representation/completion choice and G4; it is not an automatic fallback. |

The scope is complete cohort accounting **within the measured road**, not
all downstream recovery cost. There is no interior-optimum requirement,
new control variable, new observation privilege or presumed information
advantage. The strong aggregate/history, ending-scalar and scalar-search
rivals remain. No native junction-generation flag is approved merely by
selecting this causal representation; its mapping must conform to the chosen
service and completion meanings.

## What remains open

**The current choice gate is closed; the full Step 3 freeze gate is not.**
The exact source-supported coupled service/state law, its conservation,
well-posedness, storage/receiving, clearance and complete-time sensitivity
must be qualified. Dependent initial-information and action certificates
must be checked for the amended member instead of inherited automatically.
SUMO correspondence and the comparison protocol then need consistency review.

The original Step 2 law remains an unchanged approved predecessor/reference.
Its zero-A-delay restriction is now **reopened for the C-P successor
qualification**; the closed-source artifacts are not silently rewritten.
Replacement equations require their own reviewed approval before freeze.
The model → SUMO S-P → SUMO S-L ladder stays approved and closed at S3-M1.

The next allowed action is a bounded terminal-service qualification plan
and, when opened, its evidence review. This closure task does not start that
review. Step 4, simulator implementation, installations and traffic
experiments remain unopened; the ramp line stays closed.

[Traffic rationale, shared example and retained alternative](vsl_step3_merge_feedback_and_completion_response.md)

[Overall review status](vsl_review_progress.md)

## Closure work and checks

Created this decision record and its validation JSON. Updated the live
candidate inventory, protocol, Step 3 plan, progress, Step 2 prospective
reopening note, source audit, main response and package entry notices.
Archived the user choice in the opening dialogue. Historical proposals
and evidence remain identifiable as delivery records.

Assumption: the user's acceptance of option 1 approves the representation
direction and explained local objective. It does not approve an unspecified
equation or authorise implementation. No new literature was read and no
scientific numerical result was produced.

Used read-only `cat`, `sed`, `rg` and `git status --short`, documentary
`apply_patch`, and:

```text
python3 /tmp/vsl_step3_coupled_point_decision_checks.py
```

Checks cover current decision consistency, local links/anchors and the
unchanged accepted H1/T1 source/PDF hashes. They do not validate traffic,
gradients or a runnable reference. No user feedback, production source,
dependencies, mathematical artifact or existing scientific result changed.
Preexisting root AGENTS.md/PLANS.md/memo.txt edits are left unchanged.

[Closure verification metadata](vsl_step3_coupled_point_decision_validation.json)

All closure checks passed: 20 Markdown files, 387 local links and 29
heading anchors. Both accepted H1/T1 mathematical artifact hashes are
unchanged. These are documentary checks only.

## Subsequently authorised continuation

The user then directed opening the next step. The C-P plan and initial
source/interface pass were executed to VSL-CP-G1/CP-D1. The choice of C-P
and local completion remains closed; the new dependent question is the
service-closure philosophy. No replacement law or experiment is approved.

[Opened review and first findings](vsl_cp_first_findings_and_gate.md)

The user subsequently selected P-H on 2026-10-15. CP-D1 is closed; a concrete
continuous recovery-work candidate is now delivered at CP-D2. This leaves
the accepted C-P point/local-completion choice intact and does not approve
the exact reduction by implication.

[Current P-H selection and scope](vsl_ph_selection_and_scope.md)

[Exact candidate findings and confirmation gate](vsl_ph_recovery_work_findings_and_gate.md)
