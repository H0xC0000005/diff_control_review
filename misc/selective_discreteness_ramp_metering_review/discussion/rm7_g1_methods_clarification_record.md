# RMD-G1 methods and PID clarification

Date: 2026-10-01. Status: background discussion complete; G1 adoption remains open.

## User request and interpretation

The user endorsed the recommended set as a good initial planning direction,
then requested ramp-metering background for G1: established methods, other
variants, definitions of the two proposed formulations, feedback measurements,
the colleague's PID suggestion, and their pros/cons for the review question.

This permits the focused background lookup and candidate correction. It does
not open the full RM8 predecessor/mechanism pass or adopt a sensor/controller.

## Clarifications and candidate synchronization

- RMD-G1.A/B are optimization formulations of the same approved local traffic
  task, not an exhaustive ramp-method taxonomy.
- Added RMD-G1.C: MPC/repeated rate optimization. It is closed-loop operationally
  but ordinarily optimizes rates rather than fixed feedback-policy parameters.
- PID is a B subvariant. Published integral/PI lineage supplies a better-grounded
  first comparator than assuming all three PID terms are required.
- Proposed feedback interface: declared aggregate mainline occupancy/density
  near the merge/bottleneck, ramp queue information and controller memory.
  Observation aggregation/location, target, bounds, update time and queue
  management are still open.
- Distinguish detector time occupancy from lane allocation. Giving a controller
  richer lane/gap measurements requires a separate information-access comparison.
- Local versus coordinated coverage, and average rate versus physical release
  pattern, are separate design axes. Fine release-timing control would require
  action-contract discussion.
- The recommendation remains common rate perturbations/schedule first, with
  integral/PI feedback and aggregate MPC as strong comparator/predecessor
  families. These are recommendations, not equation/model adoption.
- RMT-R1 Candidate C remains the deferred multi-ramp extension. It is distinct
  from the newly added RMD-G1.C MPC formulation.

## Deliverables and source boundaries

Created:
- synthesis/rm7_g1_ramp_metering_methods_background.md
- extraction/rm7_g1_metering_methods_source_note.md
- search/rm7_g1_background_search_record.md
- discussion/rm7_g1_methods_clarification_record.md

Updated:
- synthesis/rm7_post_selection_design_inventory.md
- reporting/rm7_current_handoff.md
- README.md

Read the local inventory and historical source/claim records; browsed primary
agency pages, public paper PDFs and the PI authors' institutional abstract.
Source failures and evidence levels are recorded in the source note. No new
full texts were downloaded, and no formulas/model equations were adopted.
The main background uses prose, so no formula-heavy PDF is needed.

Commands/tools: rg, cat and apply_patch for document inspection/edits; web.run
for bounded primary-source verification; Python local-link/required-file checks
and git diff --check for documentation validation.

Validation: 71 local link targets checked with zero broken; all four background
artifacts are present and nonempty; git diff --check passed. No scientific or
simulation tests were run for this documentation discussion.

## Status and next allowed action

RM7 task selection stays closed with the local Candidate A approved. G1 is in
discussion. The user supported the initial planning direction; source-led
decisions and detailed contracts remain open. A bounded RM8 proposal can be
drafted. No RM8 full execution, simulator run or implementation has started.

## Later disposition — 2026-10-01

G1.A open-loop is now approved. The remaining initial review recommendations
were accepted and RM8 progressed to the model-family gate. This record's earlier
pending-G1 status is historical; see the
[continuation decision](rm7_open_loop_approval_and_rm8_opening.md).
