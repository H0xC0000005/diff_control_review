# RM9.50 — Candidate B adopted; observation-contract gate

Date: 2026-10-02. Status: **UG3.B approved; continuation completed to RM9-UG4.
RM9 remains open.** Only the residual rate-resource clause of G2 was amended.
UG1.A remains Default; X1–X3 remain Deferred.

## Outcome and evidence

Recorded [UG3.B approval](../discussion/rm9_resource_b_approval_and_continuation.md)
and made the separate-resource law current. After bounded lateral redistribution,
forward sending/receiving are recomputed from lane occupancy. Mainline and ramp
still share their common longitudinal receiver under the Default allocator.
There is no original-rate-minus-lateral cap and no newly added disruption term.

The [mathematical handout](../synthesis/rm9/rm9_separate_resource_and_observer_audit.pdf)
and [TeX](../synthesis/rm9/rm9_separate_resource_and_observer_audit.tex) contain the
adopted update, conditional bounds, exact hand arithmetic, observation-stage
proofs and sensitivity/accounting path. The
[claim ledger](../extraction/rm9_separate_resource_claims.md) separates these
reviewer results from physical/source/gradient claims.

| Product | Result of this continuation | Strict limitation |
|---|---|---|
| Mass and finite storage | Separate lateral and forward stages satisfy the accepted bounds; paired transfers conserve mass | Whole ramp/boundary geometry still requires transcription; conservation is not calibration |
| Recipient forward sending | It can increase after lateral arrivals; the automatic one-for-one debit is removed | Physical capacity does not automatically increase; realized receiving can still bind |
| Free-flow information | Known distinct lane mobilities plus cell total and unimpeded total flow reconstruct the post-lateral state | Not automatically the pre-lateral state, congested branch or actual detector map |
| Prior-history information | Identified prior post-lateral state and actual per-lane fluxes reconstruct the next current state | Requires complete supported observations and audited ramp balance; not a universal whole-task result |
| False hidden-information check | An admissible lateral map can collapse distinct pre-states to one post-state; with controls acting after it, those states have identical action responses | An unreconstructible pre-coordinate is not necessarily useful; no matched history claimed |
| Gradient path | Strict-branch composition and complete-time/departure sensitivity are explicit | No numerical derivative verification or independent one-step usefulness |
| Core review question | Still unanswered in the full task | No feasible exact strong-history/useful-action certificate yet |

The previous free-flow reconstruction of the residual kernel is a result about
that historical kernel. It cannot be reused unchanged after B's amendment.
Likewise, a post-lateral flow measurement is not a measurement of the stored
pre-lateral state. Completed past flow may inform the current decision; the
future flow caused by a candidate action cannot be given to its initial observer.

No timestep/propensity restriction was added to force inverse uniqueness.
The hand counterexample respects the current CFL/storage conditions. It warns
against misinterpreting a stage-dependent lost coordinate; it does not invalidate
B's conservation or prove physical fidelity/failure.

## RM9-UG4 — what does the strong observer's speed actually measure?

**Classification / owner:** Type 2, RM9-G1, user adoption of the observation
contract. Source extraction and algebra are Type 1 reviewer evidence.
Dependencies: adopted G2 law, inherited G0 strong information; G3/G4 wait on
consistent observer/initialization and geometry.

**Problem statement:** Specify the road-total speed measurement and its spatial,
temporal and update-stage support before deciding whether lane information is
hidden from complete aggregate history.

**Assumed model-chain function:** Completed density/flow/speed/count and ramp
histories, known forcing/geometry/parameters and prior rates inform a common
open-loop action comparison. The approved B dynamics then determine accepted
flows and complete system time. Observations are inputs to the information
comparison, not a new control actuator.

**Core gap:** The approved first-order kernel supplies storage and accepted
boundary flow, but has not supplied an independent physical detector passage-speed
map for congested or receiving-limited states. Density, flow and speed may be
measured at different supports or stages. The same flow can be produced by
different capped offers; speed/history may resolve them, but the free-flow proof
does not answer that question. Silently defining speed as aggregate flow divided
by density would change the admitted information. Silently using a future flow
at the decision epoch would create look-ahead.

FB0030's printed 1768–1769 measurement section distinguishes time/space means and
uses detector flow/speed to estimate density. It does not establish independent
true cell storage plus our exact transient passage-speed function.
[Primary source](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae).
This is a concrete G1 specification boundary, not a demand to install/run SUMO
or choose numerical settings.

### Candidate A — explicit idealized first-order observation benchmark

First approve an idealized exact observer for analytic information testing:
true road-total mass in each declared cell, complete declared ramp history,
boundary counts, completed-step aggregate face flows and independently formed
passage-weighted speeds. Keep known geometry/parameters/forcing and all prior
rates from the common initial epoch. Retain the current decision-epoch totals;
report flow and speed from completed steps, with the lateral/forward stage
indices explicit. Initial lane decomposition may differ only if every admitted
initial/history observation agrees; no private forcing or hidden prehistory.

The PDF proposes lane-local equilibrium fundamental-diagram speed, with one
representative speed per lane, and passage-weighting using actual accepted lane
flows. It explicitly approximates the upstream cell's speed as the lane speed at
the observed face. This yields the known free-flow diagnostic but is a new
**observation hypothesis**, especially for transient/congested traffic.
It retains a lane-sensitive speed moment rather than substituting a redundant
road-total flow/density ratio. No additional speed state or smoothing is adopted.
At zero passage flow the speed statistic is unavailable, not a fabricated value.

**Pros:** Makes the strong exact-information benchmark concrete with no added
traffic dynamics; supports bounded history/action analysis and exact rejection
of false hidden-state examples. Keeps the density, speed and history information
promised to the aggregate comparator.

**Cons:** Cell-to-face, equilibrium and within-lane speed idealizations need
explicit qualification. A result is conditional on this observer, not a
field-detector or physical gradient validation. The speed statistic might expose
the candidate lane state; a negative/sufficiency result remains valid.

**Dependencies / scientific consequence:** Adopt the observer hypothesis before
G3 construction. Transcribe full temporal/spatial supports, common geometry,
initial observations and ramp balances consistently. Source/physical claims must
remain narrower than the idealized benchmark. Reopen G1 if the speed approximation
is inconsistent; do not remove an informative channel to get a positive pair.

### Candidate B — targeted source/measurement-first speed-contract review

Preserve the strong information contract, but first inspect sources that define
station/window passage speed and its relation to independently represented
road-total density in transient/merge conditions. Seek a defensible map and
support specification before adopting one. Do not treat source detector-derived
density as exact independent cell storage, substitute an aggregate speed ratio,
or automatically introduce second-order speed states.

**Pros:** Secures physical measurement meaning first and can identify whether a
richer speed/measurement model is required. Avoids relying on an assumed
upstream-cell-to-face passage-speed identification.

**Cons:** Adds a bounded literature step and delays the compact analytic test.
May stop at an unresolved mapping or require another explicit state/observer
amendment; it is not guaranteed to produce a positive information result.

**Dependencies / scientific consequence:** Define a bounded static source audit
within RM9, reuse existing findings and stop before any new state, weaker
information, experiment or simulator execution. Current idealized/free-flow
results remain diagnostics until the physical map is adopted.

**Historical provisional recommendation, 2 October: A.** It is the smaller initial analytic benchmark,
with the measurement assumption openly declared. B is preferable if physical
detector grounding must precede the conditional mathematical test. Neither is
approved by UG3.B; that approval changed resource coupling, not speed semantics.

**Updated provisional recommendation, 5 October: B.** The user's planning
clarification rejects extra mainline lanes solely to defeat reconstruction and
asks for a genuinely grounded task rather than preserving the current model.
The [new discussion proposal](../synthesis/rm9/rm9_information_gap_review_plan_proposal.md)
therefore favors bounded source/measurement-first admission, then the current
two-lane task audit. A remains the faster conditional benchmark; source-first
may still justify an explicitly idealized observer later. This revises an
unapproved recommendation, not an approved contract. Both A and B remain
unapproved; no source-review execution, new state, actuator or extension is
opened by drafting the plan.

## Current status and next allowed action

Latest execution supersession, 5 October: the accepted source-first route has
now run as R1. Read the [current C/A/P observer gate](rm9_60_r1_observation_findings_and_gate.md).
Its new section-speed Candidate C is recommended but unapproved. The A/B route
discussion below is historical; UG4-O concrete observer adoption remains open.

Subsequent planning agreement: the [brief next-step plan](../synthesis/rm9/rm9_next_review_brief_plan.md)
consolidates the agreed source-first review ordering. It supersedes the earlier
unapproved-route wording for ordering only; the concrete observation map and
all physical amendments remain unadopted. Consolidation starts no execution.
The user subsequently explicitly accepts that brief flow. UG4-R route selection
is therefore closed with source-first B and incorporated in R1; the bounded
evidence review needs no duplicate route approval. UG4-O remains open for the
concrete observer map/support contract. Earlier instructions to discuss the
route before proceeding are superseded by this acceptance; no observer law is
adopted through it.

UG3 is closed; G2's residual resource amendment is approved and recorded.
G1's observer/support contract is now at UG4. Exact geometry and ramp coupling
remain to be transcribed consistently after the information benchmark is chosen;
no gate is raised merely for cell counts or numerical parameter values.
G3 exact-history/useful-action and G4 verified/independently useful gradients
remain unestablished. Discuss UG4 before adopting either observation route.
No RM10, implementation, simulation, numerical gradient test, deferred VSL
stage or extension is opened. Verification is in the
[work report](rm9_97_separate_resource_work_report.md).
