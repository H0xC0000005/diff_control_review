# Feedback 3: what the existing VSL framework can still support

Date: 2026-10-13. Status: **Existing-framework diagnosis delivered for
discussion. This response selects no replacement component, equation or state.**

## The main finding

Your requested order is sound: first identify what the existing model assumes,
which findings those assumptions cannot cover, and where the responsibility
lies; then discuss concrete changes. The original framework's scientific roles
still make sense. The main difficulty is how it reduces traffic interactions,
not the existence of a preparation stage, an exit stage or a complete-time
objective.

S13 predicts merging from the ending-lane mass and elapsed preparation time.
It then predicts exit time from the unfinished merging and a prescribed batch
service rule. This is a complete conditional calculation. But it cannot
generally answer two questions exposed by the review: **can the actual adjacent
lane accommodate the requested merging, and when does each part of the traffic
leave?** Those questions can affect the whole-population time and its response
to common speed advice.

That diagnosis does not mean that every component must be replaced. A component
may remain correct if another component establishes the conditions it needs.
For example, an objective that counts time until everyone exits remains the
right objective even if the old formula used to calculate it becomes invalid.
Likewise, grouping the continuing lanes may remain a valid reduction if the
traffic model establishes that their differences cannot affect service.

The earlier proposal did not make these component responsibilities explicit
enough before presenting an interface choice. The receiving/timing direction
came from specific findings, but its old-to-new implications were not laid out
for you to assess. This response corrects that order. The previously proposed
B1-R/B1-L alternatives remain unselected; they are not a binary decision you
must make before discussing this diagnosis.

One factual clarification: B1-R already allowed revision of the transfer law
while requiring a justified sequential/grouped reduction. It did not require
keeping S13 unchanged. B1-L allowed examination of receiving and timing
distinctions without choosing their equations or state. These were different
bounds on qualification; neither supplied the explicit component comparison
you are now requesting.

## What the findings do and do not invalidate

There are three different judgments here:

- **The original equations remain correct under their assumptions.** The
  accepted S13 certificate, complete accounting and scalar sufficiency are
  preserved. No conservation defect or incorrect batch calculation was found.
- **Some reductions fail when extended beyond those assumptions.** Combined
  continuing mass does not generally determine the adjacent lane's receiving
  opportunity. Final receiving work and final clearance do not generally
  determine average completion time. These are concrete limits on generalizing
  the reductions.
- **Some applied assumptions lack joint justification.** The inspected evidence
  does not establish the fixed per-second completion fraction, ideal speed
  response, upstream spare receiving and proportional exit batch together over
  the intended advice range. That is a qualification gap, not proof that every
  restricted use of any one assumption is physically impossible.

Your expectation that the primary model will evolve is reasonable. Success
means a defensible elementary information/gradient task. Which components
change depends on the coupled evidence; it does not follow in advance that all
nine need revision, that fuller lane state is necessary, or that a useful
preparation benefit must survive. A compact sufficient model or a negative
speed-preparation result remains a legitimate outcome.

[Accepted S13 result and limits](../s13/s13_99_m2_certificate_sprint_closure.md)

[Review findings and their evidence limits](vsl_b1_lane_change_model_and_gate.md)

## Component-by-component diagnosis of the original model

The numbering below is the same as the feedback-1 starting-point audit. These
are methodological components, not simulator modules or implementation tasks.
The first column records the old contract; the last column states whether the
current evidence forces a change to that component itself. It does not specify
a new contract.

| Original component and contract | What the review finding means for it | Does this component itself have to change? |
|---|---|---|
| **1. Geometry, population and initial preparation.** One permanent three-to-two drop, one finite cohort, an ending lane and a symmetric continuing group. | The physical setting is still suitable. The grouping can conceal crowding in the adjacent receiver, and initial balance need not persist after that lane receives merges. | **Keep the setting and finite population. Reassess the grouping assumption.** Its adequacy depends on the service model; the finding does not force a full lane profile or a different scenario. |
| **2. Common action and realized response.** One bounded common speed advice, assumed to equal the shared travel speed during preparation. | Common advice remains the intended actuator. Binding receiving can prevent traffic from advancing at that speed; the old ideal response is therefore a restricted assumption. | **Keep the action; qualify the response mapping.** The ideal mapping may remain in a justified nonbinding preparation regime. No compliance or acceleration model is automatically required. |
| **3. Longitudinal propagation.** A common zone length and speed give one traversal duration and a synchronized handoff to exit service. | This reduction carries travel time but no preparation waiting, staggered exit arrivals or backward queue influence. It cannot represent those effects if they matter in the admitted task. | **Change is conditional on the retained traffic interactions.** If the common-traversal and batch conditions hold, the reduction can remain. If they do not, its timing prediction needs revision; a full spatial backbone is not yet justified. |
| **4. Mandatory preparation transfer.** A fixed fraction of the remaining ending mass completes merging per elapsed second; equal mass enters the continuing group. | It treats completed merging as available whenever the clock runs. Source demand fractions and road-location incentives do not establish that completion law, especially as available traffic and receiving change. | **Reopen the completion assumption itself for the primary applied model.** Better exit service cannot repair an earlier infeasible transfer. Preserve paired conservation. The exact formula could survive only as a separately justified restricted branch, not as an unquestioned applied default. |
| **5. Preparation receiving conditions.** The target can accommodate preparation transfers without an additional receiving delay. | Early merging also uses the adjacent lane's service opportunity and can delay its continuing traffic. A downstream queue can remove space previously available upstream. | **Reopen the nonbinding-receiving assumption.** It may remain if the rest of the model establishes sufficient receiving throughout preparation and the advice range. Otherwise the preparation prediction must account for its constraints and delays. |
| **6. Choke receiving and departure allocation.** Unfinished merging has extra receiving work; a fixed work rate and simultaneous proportional batch determine departures. | The resource interpretation remains useful. The particular batch rule is what makes average service time half of final clearance; equal work does not preserve that average under different arrivals or priorities. | **No wholesale replacement is forced.** Keep the supported resource idea; qualify the fixed rate, arrivals and allocation together. Departure prediction must change if its batch conditions fail. A receiving-work factor alone cannot settle that issue. |
| **7. Objective and terminal treatment.** Count all cohort travel and waiting until complete exit, using the fixed-mass total or mean time. | The objective is complete inside S13. A revised traffic model may generate waiting and departure patterns that its old closed formula does not describe. | **Keep the objective and complete-clearance requirement.** Its calculation must follow the admitted traffic trajectory. The forward model must supply any new waiting; changing the objective cannot repair a missing traffic interaction. |
| **8. Observer and comparator initialization.** Compare aggregate history, that history plus initial ending mass, and equivalent grouped state; forecast autonomously. | One initial ending-mass statistic is exactly sufficient for S13. Receiving-dependent dynamics may require other information, but the review has not established the minimum or a new equal-full-history witness. | **Keep the fairness and autonomous-prediction contract.** Reassess sufficiency and matching only after the traffic contract is known. Neither automatic full-lane necessity nor transfer of S13's certificate to a new model is justified. |
| **9. Sensitivity and decision evidence.** Differentiate the common physical advice with preparation and metadata fixed; assess feasible perturbations. | S13's analytical direction remains correct for S13. A changed traffic law can change or remove that direction and needs its own derivative and independent-usefulness evidence. | **Keep the evidence standard and physical control variable.** Re-derive the result if the model changes. More detailed state or a finite derivative does not itself prove useful advice. |

[Original component definitions and completeness audit](vsl_feedback1_starting_point_audit.md)

## Why responsibility does not imply replacing the named component

### A better choke cannot make an earlier merge feasible

Suppose the ending-lane mass and elapsed preparation time are the same, but
the adjacent continuing lane is clear in one case and crowded in another.
The old transfer law predicts the same completed merging in both. Changing the
exit priority or charging more late work cannot tell that law that some earlier
merges lacked space. If this difference is within the intended task, components
4 and 5 are directly implicated, with the grouping in component 1 also relevant.

There is nevertheless a distinction between changing an equation and changing
the conditions under which it is used. Establishing that receiving never limits
the relevant transfers can remove this particular feasibility problem. It does
not, by itself, establish that elapsed time is the correct opportunity scale
or that the completion fraction stays fixed as advice changes. The receiving
question and the preparation-clock question must both be answered.

[Transfer meaning, receiving and source-adaptation evidence](../../extraction/research_readiness/vsl_b1_source_and_interface_audit.md)

### Grouping is a shared assumption, not merely an initialization choice

Two continuing lanes can have the same combined traffic but different traffic
in the lane that receives the merge. Also, a merge adds traffic to that lane
first, so equal initial occupancies need not remain equal. A promise of symmetry
in component 1 is insufficient if components 4–6 subsequently make the lanes
behave differently.

The responsible issue is whether the grouping preserves the service prediction
throughout evolution. If receiving is insensitive to the omitted difference,
or a valid dynamic equivalence is established, the grouped state can remain.
If not, the reduction is inadequate. The existing evidence establishes this
conditional limit; it does not determine how much additional state is needed.

### The time objective can remain while its convenient formula cannot

Consider two service allocations that finish everyone at the same final time.
One may let many ordinary continuing units depart early; another may devote
early service to fewer units requiring more merge work. The amount of traffic
waiting at intermediate times can differ, so total population time can differ.

The objective in component 7 asks the right question. Components 3 and 6 supply
the chronology needed to answer it. S13's simple calculation remains exact if
its synchronized proportional batch survives qualification. If a different
arrival or allocation law is admitted, retaining final work while importing
the old average-time formula would be wrong. The required reconsideration is
of the traffic chronology and its calculation, not of complete-time accounting.

[Existing receiving and departure-time diagnostics, PDF](../../synthesis/research_readiness/vsl_b1_interface_examples.pdf)

### Early spare capacity and a constrained exit require one consistent regime

These conditions are possible at different places; they are not inherently
contradictory. But a downstream queue can change upstream receiving, and a
merge uses resources wherever it occurs. Components 3, 5 and 6 must therefore
support their assumptions together. Component 7 must count whatever time
those traffic interactions cause.

S13 already counts the extra common travel time caused by slower advice. Its
limitation is that additional preparation interaction delay is assumed absent,
not that an existing modeled delay was forgotten in the objective. Whether
that absence is a sound restriction remains unresolved. Resolving it could
preserve a component under a narrower regime or require its traffic prediction
to change; this response does not choose between those outcomes.

## How this covers MP1–MP6 without turning them into six repairs

| Question | Where its responsibility lies in the old framework |
|---|---|
| **MP1: merge opportunity and its clock** | Component 4's completion law, interpreted together with component 2's speed response and component 3's road progress. More elapsed time cannot be assumed to mean more completed merging. |
| **MP2: feasible completion** | Components 4–5, supported by component 6's downstream receiving conditions. Requests, available traffic and actual accommodation must be consistent. |
| **MP3: continuing-lane grouping** | Component 1's state reduction and the way components 4–6 use and evolve it. Initial symmetry alone cannot justify the reduction. |
| **MP4: early versus late costs** | Components 3, 5 and 6 determine the traffic costs; component 7 counts them. Fewer late merges alone do not establish a net saving. |
| **MP5: departures and average time** | Components 3 and 6 determine arrivals and service chronology; component 7 evaluates their complete time. Final work alone is insufficient. |
| **MP6: joint validity under common advice** | The compatibility of components 1–7 over the same population, geometry and advice range. This is a whole-model qualification, not a tenth mechanism to add. Components 8–9 then require fresh information/sensitivity evidence if those dynamics change. |

The component verdicts are preliminary methodological diagnoses, not adoption
decisions. MP1–MP6 and their ownership remain unchanged. They all affect shared
traffic meaning under G3/VQ3-P/T/S; observation consequences remain under G2,
and complete-time and evidence consequences under G4. This discussion does not
delegate a scientific choice to source transcription or implementation.

## What is settled here, and where this response stops

The existing framework needs reassessment of **completed-transfer opportunity
and preparation receiving first**, with continuing-lane grouping, travel/handoff
timing and choke allocation judged through their dependencies. The physical
setting, one common action, continuous conservation, complete-time objective
and fair evidence contracts can be retained. That is the substantive diagnosis;
it is not a commitment to preserve every old formula or replace every component.

No proposed component replacement is added in this response. The old contracts
are explicit above, and the earlier source candidates remain proposals. The
next allowed action is discussion of this diagnosis. A subsequent, separately
opened change proposal should pair each old contract with its proposed new
contract, the assumption that changes, its reason, and its consequences for
other components. That comparison should precede selection of replacement
laws or state; it is not carried out here.

The scientific checkpoint remains VSL-B1-G1, now with the user-requested
existing-model discussion before disposition of its earlier alternatives.
S13, urban and ramp closures remain intact. No simulator work, dependencies,
traffic experiments or evaluator execution are authorized by this response.

[Interpreted feedback and discussion record](vsl_successor_opening_dialogue.md)

[Work record and document checks](vsl_feedback3_work_report.md)

## Subsequent user response and improvement proposal

The user accepts the general flow and most details of this diagnosis and
explicitly requests at most three confident, feasible improvements, preferring
minimal component substitution. This is acceptance of the diagnostic direction,
not blanket approval of every conditional verdict or a new traffic law.

P1 now proposes one preparation-transfer substitution, with its old/new
completion and receiving-slack assumptions explicit. Receiver/state/motion
dependencies remain for the next review. The diagnosis above remains the
unchanged record of the previous task; its proposed-changes stop was followed
until the user explicitly opened this continuation.

[Current one-component improvement proposal](vsl_p1_preparation_transfer_improvement_proposal.md)
