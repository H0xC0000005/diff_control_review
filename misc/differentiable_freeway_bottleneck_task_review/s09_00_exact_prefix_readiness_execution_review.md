# S09.00 — Exact-prefix readiness and execution review

Date: 2026-09-29. Status: **Superseded as an active continuation by the user's
methodology-only scope correction; DG-R6 is withdrawn.** Parent:
[S08 closure](reporting/s08/s08_99_exact_prefix_planning_sprint_closure.md). Current
authority: [S09.35 scope correction](reporting/s09/s09_35_scope_correction_and_methodology_alternatives.md).

## Objective

Execute the approved S08 full dual-step exact-prefix screen without changing its
scientific contract. Establish the actual reference provider and harness first;
only after readiness passes, run all 18 preparations at 0.5 s and 0.25 s and
stop with the complete pair evidence before any advice action.

## Fixed execution order

1. Discover the installed provider/version and matching Python API read-only.
2. Report absence or incompatibility; do not install, reconfigure or substitute
   a reference engine without a new user decision.
3. If a provider exists, create only the review-local immutable input,
   `readiness`, `prefix`, and `summarize` harness specified by S08.
4. Use at most 24 readiness invocations for contract conformance.
5. If readiness passes, execute the 36 frozen prefix invocations.
6. Stop at the result gate with the complete pair registry or a pre-registered
   failure label.

## Scope boundaries

The [approved exact-prefix contract](synthesis/s08/s08_exact_prefix_feasibility_contract.md)
is authoritative. No advice-action evaluation, broader preparation, approximate
matching, held-out context, candidate differentiable model, gradient work or
production-project change is included. Provider installation and configuration
were not authorized by opening this sprint.

## Reached stop

Read-only discovery found no usable SUMO executable, network builder or Python
API in the active environment, standard system locations or available Conda
environments. The sprint therefore stopped before harness construction or a
traffic invocation. See [S09 findings and DG-R6](reporting/s09/s09_20_exact_prefix_readiness_findings_and_gate.md).

## Subsequent scope correction

The user clarified that concrete execution is not part of this methodology-only
review. The provider audit is retained as historical bookkeeping, but it is not
a readiness gate and no provisioning decision is required. The methodological
alternatives and corrected interpretation are in [S09.35](reporting/s09/s09_35_scope_correction_and_methodology_alternatives.md).
