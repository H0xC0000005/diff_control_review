# Milestone 2 review-methodology supplement — draft package

Status: **Draft for user review; non-authoritative; not migrated**  
Prepared: **2026-09-15**  
Staging location: `misc/milestone_2_review_methodology_supplement_draft/`

## Purpose

This package stages a non-intrusive handoff from the closed literature/novelty,
downstream-task, and ramp-metering reviews to the active Milestone 2 Phase B
discussion. It does not amend the project, choose any open component candidate,
close or reopen a Milestone 2 decision, approve Phase C, or authorize
implementation.

The package is deliberately outside the active Milestone 2 archive and is
ignored by Git through the repository's existing `misc` rule. No existing
project or review file was edited while preparing it.

## Decision summary

The package recommends accepting the closed review findings as **supplementary
methodology guidance for the remaining Milestone 2 planning**, without turning
them into new Milestone 2 decisions or implementation requirements. The active
component questions remain the only place where concrete interfaces and
acceptance contracts are decided.

The main effect is to ask the future Milestone 2 planning agent to preserve five
capabilities while resolving the already-open questions:

1. express the selected four-leg task through general structural APIs rather
   than hard-coding that one scenario;
2. distinguish matched split-domain neutrality from numerical differences
   caused by comparing against the original unsplit macro link;
3. expose disjoint physical-mass ownership so the later total-system-time
   objective counts every mass unit once, while treating the grid and ledger as
   non-additive views;
4. preserve the continuous derivative path and evidence needed for stable-active-
   signature AD/JVP/finite-difference checks; and
5. leave the service/removal seam neutral so Milestone 3 can later choose exact
   FIFO or an approved bounded bin-scale policy.

The package also records two scope guards: later baselines and richer evaluators
must remain separate realizations rather than Milestone 2 dependencies, and ramp
metering must not create new Milestone 2 requirements.

No finding conflicts with or reopens G1--G6. No component candidate is selected.

## File-by-file summaries

### 1. `milestone_2_review_findings_supplement_draft.md`

**What it does.** Translates the closed downstream-task and ramp-metering review
conclusions into seven bounded findings relevant to Milestone 2. For every
finding, it separates the accepted review conclusion, the recommendation for
Milestone 2, and the boundary of what the recommendation does not decide.

**Main content.** It explains that Milestone 2 is enabling infrastructure for
the later fixed-time service-allocation task, not the milestone that must prove
useful control gradients. It covers scenario/API separation, neutral-comparator
interpretation, single-count total-system-time readiness, continuous derivative
paths, the policy-neutral Milestone 2-to-3 seam, future baseline attachment, and
the exclusion of ramp metering as a parallel task.

**Most consequential point.** The future removal-plan/application interface
should not unnecessarily assume that every later service policy is expressible
only as one scalar lane prefix. Milestone 2 still retains exact ledger authority
and performs no lossy operation; this merely avoids blocking the already-agreed
Milestone 3 choice between exact FIFO and a bounded bin-scale policy.

**What approval means.** Approving this file accepts it as a faithful summary of
review implications to be consulted during Phase B. It does not approve any
component implementation or later experiment.

### 2. `milestone_2_component_crosswalk_draft.md`

**What it does.** Maps each of the seven review findings onto the existing
component-local questions C2.1-Q1 through C2.6-Q3. This prevents the review
requirements from being lost while avoiding edits to the active candidate
inventory.

**Main content.** It identifies where each issue naturally belongs—for example,
general scenario structure in C2.1/C2.5, physical accounting in C2.2/C2.3/C2.5,
and derivative signatures in C2.3/C2.4/C2.6. It then gives short question-specific
notes and seven final consistency questions for the ordinary pre-Phase-C audit.

**Most consequential point.** The crosswalk is advisory traceability, not a
second decision system. If a review requirement conflicts with a candidate, the
normal Phase B process must revise or reopen the smallest affected decision; the
crosswalk cannot settle it by itself.

**What approval means.** Approving this file accepts the ownership mapping and
the proposed final consistency checks. It does not endorse the currently
recommended candidate for any component question.

### 3. `migration_manifest_and_entrypoint_patch_draft.md`

**What it does.** Defines the exact non-intrusive migration operation that could
be performed after approval.

**Main content.** It proposes adding the two substantive files under a new
Milestone 2 `supplements/` directory. The only proposed change to an existing
file is a short entry-point section in `phase_B_revision.md` linking to those
supplements and explicitly stating that they do not alter decisions, status, or
implementation authority. It lists every file category that must remain
untouched and supplies migration acceptance checks.

**Most consequential point.** The active component-question register and working
Component 2.1 questions would not be edited. A future development agent would
incorporate any accepted methodological consequence through the ordinary Phase B
workflow rather than through this migration.

**What approval means.** Approving this file authorizes the proposed content and
layout for a later migration. Git staging, commit, and push remain separate
operations and occur only under explicit authorization.

## Recommended decision

Approve the package for migration if the following compact interpretation is
correct:

> The closed reviews supply a task-facing checklist for Milestone 2, while the
> active Phase B process retains full ownership of component choices. The
> supplements must be discoverable but non-authoritative, must not reopen G1--G6,
> and must not advance the milestone.

If this interpretation is accepted, line-by-line review is not necessary unless
one of the following four points is disputed:

- four-leg symmetry is a scenario default, not a reusable-API restriction;
- grid and ledger are synchronized views and cannot both be counted as physical
  occupancy;
- Milestone 3 must remain free to choose the exact or bounded bin-scale service
  policy through a policy-neutral Milestone 2 seam; or
- ramp metering is excluded as a task and creates no Milestone 2 obligation.

## Authority boundary

The active authority remains:

- repository policy and scientific invariants in `AGENTS.md` and
  `PROJECT_CONTEXT.md`;
- the roadmap in `PLANS.md`;
- closed Milestone 2 global decisions G1--G6 in
  `temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md`; and
- component-local decisions made through the active Phase B workflow.

The draft supplement reports accepted review findings and recommends what the
Milestone 2 planning process should preserve or expose. Where the review leaves
an implementation-dependent choice open, the draft leaves it open. A future
development agent remains responsible for presenting candidates, incorporating
approved decisions into the Phase B records, and advancing phases only when the
user authorizes that work.

## Approval boundary

Approval of the prose would authorize a later, separate migration operation,
not implementation or phase advancement. The proposed migration would:

- add two new supplementary Markdown files under the active Milestone 2 archive;
- add one short link-only entry point to `phase_B_revision.md`; and
- leave every other existing file unchanged.

Git staging, commit, or push is not performed by this draft task.
