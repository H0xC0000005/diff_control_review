# Forced merging, continuing traffic and where the task should end

Your consideration is sound. The merging cost can fall on drivers already
in the continuing lane, as well as on drivers waiting in the ending lane.
The important distinction is where that cost develops and whether the
chosen model and completion section account for it. My previous J-P/J-F
comparison put too much weight on junction geometry; it did not resolve
this causal requirement.

**Latest decision, 2026-10-14: C-P selected; S3-M2's representation/completion
choice closed.** The user accepted coupled point merging with choke-line
completion. G3's nominal zero-A-delay restriction is reopened for bounded
successor qualification; no replacement equations are approved yet. S3-M1's
ladder remains fixed. The rationale and alternatives below preserve the
proposal's delivery-time status; Step 3's full freeze remains open.

[Accepted direction and exact gate-closure scope](vsl_step3_coupled_point_decision.md)

Here, the entering stream is the **dropping mainline lane E**, not a newly
opened on-ramp task. The physical analogy to slow ramp insertion is useful,
but this discussion does not resume the closed ramp review.

## The traffic logic, including one qualification

Suppose a queued E driver restarts and enters A at a lower actual speed
than A's approaching traffic. A following driver may brake to maintain a
safe gap. Further followers can slow in turn; if their arrival demand is
high enough, a queue can grow upstream. The entering driver can also remain
slow after the merging line while accelerating. That downstream recovery
can limit the stream and affect vehicles that have already crossed the line.

Those are related effects, not a guarantee that every forced merge creates
a backward shock or spills back into preparation. If entry speeds nearly
match and gaps are sufficient, the disturbance may dissipate. Growing
congestion depends on demand relative to the realised service, duration
and storage. Common speed advice also does not make E permanently slower:
the relevant difference is actual motion after waiting or braking.

The literature supplies two kinds of support. Bertini and Leal observe
capacity reduction and upstream-moving congestion at freeway lane drops.
That establishes the practical relevance of through-traffic disturbance,
without isolating slow insertion as its only cause. Laval and Daganzo,
and the inspected Leclercq et al. manuscript, explain how lane-changing or
slow inserting vehicles with limited acceleration can reduce effective
service and interact with upstream traffic waves. The latter's on-ramp
domain is mechanism evidence, not a ready lane-drop closure.

[Lane-drop field evidence: author-uploaded manuscript and abstract](https://www.researchgate.net/publication/228650849_Empirical_Study_of_Traffic_Features_at_a_Freeway_Lane_Drop)

[Laval and Daganzo: institutional abstract](https://its.berkeley.edu/publications/lane-changing-traffic-streams)

[Leclercq et al.: inspected author manuscript, introduction and assumptions](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

**Conclusion:** for natural compulsory merging, the model must permit
continuing traffic to be affected, or justify a restricted regime in which
that effect is negligible. The evidence does not require a particular
zone length, a second-order model, or an explicit acceleration law in every
predictor. Nor does it establish the effect's size in our finite-cohort task.
That remains qualification work, not an assumption selected to obtain an
interior speed optimum.

## Is this consistent with the existing stack?

It is consistent with the stack's **general architecture**: conservative
lane flows, demand/receiving competition, physical travel/storage and complete
time accounting. A boundary interaction can restrict departures and cause
waves on the existing terminal links. A point service location does not mean
a queue with zero physical length, and it does not require inserting a CTM
lattice into homogeneous upstream preparation.

It is **outside the accepted nominal forced-service member** in an important
respect. H1/T1 serves A as soon as its minimum terminal travel is complete;
only E waits. The larger E work factor makes E's residual service smaller,
but cannot slow A or produce a continuing-lane queue on that domain. There is
also no retained post-merge state that lets a departed slow E driver restrict
later A service. This is a deliberate analytical restriction, not a defect
in the earlier conservation proof.

Right-of-way can be retained while changing this restriction. Giving A
priority decides who is admitted when streams compete; it does not guarantee
that A never follows a slow vehicle once that vehicle has been admitted.
Consequently, merely increasing E's work factor, or replacing the priority
with a proportional split, does not establish the missing speed/recovery
mechanism.

SUMO already has native following and acceleration constraints and allows
priority traffic to be slowed by interactions. These effects need not all
occur on internal junction links. A short native connector is therefore
neither necessary nor sufficient for the coupling the user describes.
The reference must continue vehicles beyond the measurement line whenever
their subsequent motion can feed back into the assessed traffic.

[Native speed, following and acceleration semantics](https://sumo.dlr.de/docs/Simulation/VehicleSpeed.html)

[Junction interiors and right-of-way are distinct choices](https://sumo.dlr.de/docs/Simulation/Intersections.html#internal-links)

## When is completion at the merge line legitimate?

Completion is a measurement convention; it is not a declaration that the
departed vehicle ceases to affect traffic. In the reference, crossing a
detector must not remove the driver or erase its later influence on receiving.
The same distinction applies to any compact predictor closure.

Imagine E enters slowly. A following driver has a gap large enough to cross
the merge line before catching E. It then brakes downstream. An objective
that ends A's clock at the merge line misses that braking delay. If a queue
instead reaches A before it crosses the line, its pre-line delay is counted.
Both can happen with the same point merge geometry.

Therefore, the user's first direction is valid for a **merge-line completion
task with causal downstream influence retained**. It need not add downstream
travel to its objective. However, it cannot claim to count the whole
post-merge recovery burden just because the insertion began at the line.
An upstream effective service law can represent local throughput loss; that
does not by itself make omitted downstream vehicle-time equal to pre-line
waiting. Such an equivalence would need a separate derivation or evidence.

The second direction deliberately counts a wider part of the journey. A
fixed downstream completion section includes local recovery and continuing
traffic delay until that section. Its length must be physically motivated
and its advice response checked; a finite exit never automatically captures
every disturbance farther downstream. Extending the measured road also
adds travel time to the speed tradeoff, so it cannot be treated as a harmless
output setting.

## Direct answers to the philosophy questions

| User question | Answer and consequence |
|---|---|
| **Is the consideration sound?** | Yes. Compulsory insertion can delay A, not only E; service and propagation must be coupled when that burden matters. A backward-growing queue is conditional, not inevitable. |
| **Is it consistent with the stack?** | Yes at the architecture level. It changes the frozen nominal server that guarantees zero A delay; that part needs G3 reassessment. A later completion section also needs G4. |
| **Is it natural traffic behaviour?** | Yes. Slow insertion, follower braking and recovery are natural mechanisms. Which compact law represents them adequately is still open. |
| **Is modelling it necessary?** | Necessary as a capability or a defended exclusion for the natural-merging claim. Literature supports potentially substantial effects; it does not prove every finite cohort needs a spatial recovery zone. |
| **How should the proposal change?** | Make through-traffic disturbance the shared requirement. Then compare a coupled point model with a downstream recovery model, keeping the completion objective explicit. Internal junction geometry becomes a subordinate choice. |

## Revised S3-M2 proposal: two causal representations

**Problem statement.** What is the smallest compulsory-merge representation
that permits the relevant continuing-traffic disturbance, and where should
the objective stop counting its consequences?

**Assumed model-chain function.** H1 supplies the prepared E/A/B streams.
Component 6 accepts the residual merge and determines continuing and ending
departures; component 3 supplies physical propagation/storage; component 7
counts time to a declared common completion section. Those interfaces must
allow a slow admission or scarce shared service to affect continuing traffic.

**Core gap.** The existing one-queue server excludes that feedback. The
previous geometry alternatives do not specify it or establish that all
relevant delay precedes their proposed exit. We should not freeze Step 3
on that basis. The primary amendment is still a proposal, not an approved law.

### C-P: coupled compulsory service at a point, with merge-line completion

**Core idea:** keep the merging location and completion line at the choke,
but remove the assumption that A is immune to E's admission. Both streams
share realised service; merge speed/headway or its effective recovery state
may constrain continuing departures. Physical terminal histories retain
unserved E and A and propagate any upstream restriction. The primary research
work is to qualify the smallest source-supported service/state law.

**Old/new change:** previously, A crosses immediately and extra merging work
holds only E. The proposed model can hold A too and remembers whatever
influence is needed after a slow entry. This does not automatically require
position-indexed state in H1. In SUMO, keep the downstream continuation alive
and let native motion create the coupling; do not insert a Python copy of the
predictor's service law.

- **Pros:** closest to the existing finite-terminal/point architecture and
  original completion convention. It can capture through-lane queuing and
  backward propagation without first adopting a new spatial preparation model.
- **Cons:** the current work budget is insufficient as that law. The required
  effective service or recovery state must be justified and rechecked for
  conservation, well-posedness, clearance, observability and sensitivity.
  A point objective still omits delay incurred after crossing.
- **Dependency and consequence:** propose reopening only G3's compulsory
  service/terminal-domain restriction first. Retain the H1 handoff if a new
  storage/receiving check protects it. If feedback reaches preparation, that
  protection fails and the smallest additional G3 interface must reopen.
  Keep the original G4 endpoint only with an explicitly local claim.

A first-order point-capacity model is a serious simpler rival: Jin, Gan and
Lebacque demonstrate a boundary flux coupled to kinematic waves. Their
closure is phenomenological with an exogenous dropped capacity and does not
derive the speed of inserting vehicles. It proves that a point treatment
need not eliminate waves; it does not solve the present service-law review.

[Point-boundary kinematic-wave precedent, selected §2 reading](https://arxiv.org/pdf/1310.2660)

### C-Z: compulsory entry followed by a downstream recovery reach

**Core idea:** E enters at the choke, then E and A share a short ordinary
continuing-road reach. Traffic there retains enough state to represent slow
entry, following, acceleration/recovery and receiving feedback into the
compulsory boundary. All cohort clocks stop at its fixed downstream end.

**Old/new change:** the model now distinguishes admission from completion
and retains post-entry traffic. The new reach is for **recovery of already
merged traffic**, not another upstream early-merging zone. It need not be
SUMO's internal junction connector. No additional lateral opportunities or
control variables follow automatically.

- **Pros:** represents the user's mechanism where it physically persists and
  counts both pre-entry waiting and post-entry continuing delay. This is the
  clearer choice if recovery-inclusive time is the scientific target.
- **Cons:** introduces a length/endpoint and additional traffic dynamics.
  An ordinary fixed-diagram LTM segment alone does not guarantee finite
  acceleration or speed-dependent moving-bottleneck behaviour; the recovery
  law must be qualified. Extra travel itself affects the optimum.
- **Dependency and consequence:** requires G3's post-entry state/receiving
  contract and G4's measured domain to be approved together. State and advice
  exposure must be equal across peers, with G2 reconsidered only if new
  initial information is necessary. Conservation, full cohort accounting,
  storage, clearance, scalar sufficiency and derivatives must be rechecked.

| Shared slow E entry | C-P | C-Z |
|---|---|---|
| What carries the effect on A? | A coupled boundary service/state and existing terminal propagation. | Post-entry motion/recovery and its feedback to boundary service. |
| Can A queue before the choke? | Yes, if the qualified service falls below its demand. | Yes, if the recovery reach restricts receiving. |
| Is A's braking after crossing counted? | No in the merge-line objective; its causal influence still must persist. | Yes until the declared downstream completion section. |
| Main unresolved modelling burden | A compact service/recovery closure, not simply a larger E penalty. | A justified recovery law and physical completion length, not simply an extra link. |

**Updated provisional recommendation:** qualify C-P first as the smallest
amendment to compulsory service, retaining an honestly local completion
objective. Do not claim that it already covers all post-merge cost. If the
task is required to measure downstream slowing/recovery as well, choose C-Z
and amend the objective explicitly; C-P with a pre-line clock cannot meet
that wider requirement. C-Z remains the appropriate return route if compact
coupling cannot represent the decision-relevant effect. Neither law or route
is selected in this response.

## What changes at the gate and what remains fixed

S3-M2's former J-P/J-F geometry framing is superseded by this causal review.
Keep two explicit global issues under it: **S3-M2-A**, the continuing-service
coupling, under G3; and **S3-M2-B**, the completion/measurement domain, under
G4. Both are Type 2, with user-owned methodological selection. Their local
source/setting transcriptions are Type 1 only after those contracts close.
The old geometry choices can then be evaluated against the selected causal
contract; they are not two substitutes for it.

This is a **stage-level qualification challenge**. Step 3's prior evidence
pass was delivered, but its freeze readiness is withdrawn pending this gap.
Changing the primary requires a bounded return to Step 2's terminal contract,
then rechecking the dependent Step 3 certificates/protocol. The old analytical
results remain correct for their frozen member; they do not automatically
prove scalar sufficiency, the same history/action split or useful derivatives
for an amended member. An aggregate capacity/history rival may represent
through-traffic disturbance too, so the effect alone is not an information-
necessity or novelty claim.

The accepted model → S-P → S-L evidence roles stay closed. This clarification
selects no new law, objective, spatial preparation model or experiment.
Stop at the revised gate for discussion. Step 4, implementation, installations,
traffic experiments and the ramp line remain unopened.

[Frozen Step 2 contract and specific reopen conditions](vsl_step2_model_closure.md)

[Reference list and source-reading limits](../../extraction/research_readiness/vsl_step3_reference_and_evidence_audit.md#through-traffic-feedback-and-completion-recheck-2026-10-14)

[Response work and validation record](vsl_step3_merge_feedback_response_work_report.md)
