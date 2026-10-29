# RM9 brief next-step review plan

Date: 2026-10-05. Status: **Brief review flow accepted by the user;
source-first route and observer C approved; bounded R2/R3 and R5 pass completed.
RM9 remains open at UG5; no changed physical family admitted.**

The user's subsequent approval of a very brief A/C screen has been executed.
[Screen findings](../../reporting/rm9_72_a_c_brief_feasibility_screen.md) recommend
A as a planning lead and retain C as reserve. No deep task formulation or current
closure is approved; discussion remains at UG5. This is further bounded R5/R6
work within RM9, not a successor opening or altered physical model.

This is the current concise ordering reference. It consolidates the
[detailed proposal](rm9_information_gap_review_plan_proposal.md) and subsequent
discussion; earlier provisional recommendation/approval wording is historical.
The user confirms agreement with the plan and requests an explicit brief version.

## Principles

Prefer genuine, physically justified traffic settings and minimize additional
assumptions. Keep two mainline lanes by default; preserve the complete declared
aggregate information. Do not select assumptions solely to create hiddenness.
Unrefuted hypotheses are not established evidence. Positive, negative/sufficient
and unresolved findings are all valid outcomes. Review only: literature and
analytic reasoning, with no simulator implementation or traffic experiments.

## Questions, steps and purposes

| Step | Review sub-question | Next work and purpose |
|---|---|---|
| R1 — observation grounding | What mass/density, flow, speed and history are actually available, at what location, stage and time? | Bounded source-first audit using the existing packet and targeted gap checks; specify geometry, initialization and ramp balances. Produce an observation/task evidence matrix before admitting a concrete observer. Prevent ambiguous measurement semantics and look-ahead. |
| R2 — unchanged task | Does any genuine regime of the current two-lane task leave decision-relevant state unresolved by the entire admitted aggregate history? | Audit free flow, receiving limits, queues and transients under unchanged laws. Distinguish snapshot ambiguity from full-history ambiguity and ambiguity that survives until control acts. Record identification or scoped exclusions without constructing a favorable case first. |
| R3 — justified within-family assumptions, if needed | Can an independently motivated assumption identify a viable subcase without changing the task family? | State each assumption, physical rationale, evidence and affected contract. Label conclusions conditional; stop before adopting a change in scientific meaning. Avoid silently repairing an information failure through parameter restrictions or weaker sensing. |
| R4 — consequential information, wherever it survives | Does the unresolved state change useful common metering actions, and is there a credible sensitivity path to the objective? | Compare the same feasible actions with complete affected-population time accounting and strong aggregate/history competitors. Trace the general gradient path and identify event/branch limitations and future validation needs. Hiddenness alone is insufficient; this review does not establish numerical or independently useful gradients by execution. |
| R5 — alternatives if the present task is insufficient | Which credible alternative bridges the identified gap with the smallest scientifically meaningful changes? | Compare physical merge geometry, acceleration/recovery/composition, and gap-aligned timing. Explicitly list changes to state, laws, geometry, observations, actuator, objective and gradient semantics. Rank by evidence and actual scientific changes, not direction number or code reuse; scope sources in parallel if useful, without adopting an extension. |
| R6 — disposition and next decision | What is established, excluded or unresolved, and what should be admitted next? | Produce a concise findings matrix and a scoped current-task result. Present any concrete observer or task amendment, evidence, tradeoffs and remaining gaps for user discussion before adoption. A negative result does not automatically open an extension. |

Ordering: R1 prepares the observer contract needed for R2. R3 is conditional,
not mandatory rescue work. Apply R4 to any surviving candidate, including an
alternative later admitted under R5. R5 source scoping need not wait for an
exhaustive R2/R3 search. Do not treat the expected negative present-task result
as a predetermined conclusion.

## Immediate output and stopping point

### Placement in the review stages

The branch sequence remains **RM7 task planning (closed) → RM8 family admission
(closed) → RM9 formulation/information sufficiency (open) → a separately approved
successor only if warranted**. R1–R6 are work steps inside this RM9 continuation,
not six new review stages or repository implementation milestones. Where useful,
refer to them as RM9-R1 through RM9-R6 to avoid confusion with stage numbering.

| Work step | Existing RM9 contract / placement |
|---|---|
| R1 | G1 observation specification and UG4; evidence extraction precedes concrete observer adoption. UG4-R and UG4-O.C are closed; concrete site/initial-history domain remains unbound. |
| R2 | G1/G2 identifiability audit feeding G3; preserve the adopted dynamics and strong history. |
| R3 | Conditional assumption screening; reopen only affected G1/G2 clauses before using a consequential amendment. A small same-task amendment may remain in RM9. |
| R4 | G3 common-action relevance followed by G4 conceptual sensitivity review; numeric gradient validation is outside this methodology review. |
| R5 | Alternative source screening and comparison may be recorded in RM9. Developing a materially different state/law/control task needs explicit disposition of the present task and approval of an amendment or successor plan; it is not automatic RM10 execution. |
| R6 | G5 findings/disposition and user gate: observer/amendment choice, scoped closure, or proposal for a successor. Only user-approved closure closes RM9. |

The original RM9 protocol and approved UG1–UG3 decisions remain the backbone.
This plan refines continuation and adds bounded alternative comparison; it does
not reopen RM7/RM8, revive the historical implementation-anchored branch or
automatically open deferred VSL/multi-ramp work. Evidence and synthesis stay in
the ramp branch's existing extraction, synthesis/rm9, reporting and discussion
directories. A successor should use its own stage labels after scope approval.

### UG4 integration and acceptance

UG4 is contained in R1, not a separate prerequisite review. Its two decision
parts are now explicit:

- **UG4-R — route selection: Closed.** Acceptance of this flow selects the
  source-first review route (historical UG4.B). No duplicate route approval is
  required before conducting the bounded R1 source/measurement review.
- **UG4-O — concrete observer contract: Closed with C.** The user explicitly
  selects the section-aligned representative FD speed. Empty flags, stored-state
  timing and complete causal history remain as specified. It adds no dynamic
  speed state and does not compute or change TST. Concrete geometry and initial
  knowledge remain unbound; their public/source support is needed for a positive
  witness rather than silently selecting a favorable domain.

R1 delivered its source/task matrix and historical C/A/P proposal. After C
approval, the bounded R2/R3 pass found conditional aggregate sufficiency and no
established genuine full-history/action distinction; the uncertain-start domain
is not universally excluded. R4 has no new certificate to activate. R5 completed
lightweight physical-family comparison without adoption. R6 now presents
[UG5 disposition/scope choices](../../reporting/rm9_70_observer_c_findings_and_disposition_gate.md).
The next action is user discussion/selection there. RM9 is not user-closed, and
no successor or deferred extension has opened. The ordering and guardrails above
remain authoritative for this continuation.

Work record: consolidated the agreed ordering; synchronized proposal, handoff,
inventory and findings, and archived the discussion. Commands: sed reads,
apply_patch and Python local-link/status checks. No scientific test required
for planning text; no model, production, dependency or experiment change.
