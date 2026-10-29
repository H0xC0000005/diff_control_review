# From through-lane conditions to feasible merging: the next review

The next review will determine whether the approved P1 replacement can make
merging respond to traffic conditions while keeping the VSL task elementary.
Its central axis is **through-lane traffic state → available receiving service
→ completed ending-lane merging**. A completed merge changes the target lane's
traffic, so this dependence must continue through later opportunities. It
cannot be justified by assigning a receiving budget at the start and leaving
its subsequent evolution unexplained.

The larger purpose remains the first information/gradient verification alongside
the urban task. Before asking whether a gradient gives useful speed advice, we
need a defensible account of what that advice changes. Common speed affects
traffic progress and service opportunities; feasible merging changes later
traffic and unfinished merging; those effects determine time until the whole
cohort exits. The review must establish this causal connection without assuming
that slower advice helps or that a full lane representation is necessary.

Date: 2026-10-13. Review identifier: **VSL-B2**. Status: **Concrete review plan
opened under the approved P1 direction; evidence pass not executed in this
planning task.** This is the execution brief for the accepted direction, not
another broad choice between modeling programs.

[P1 approval and accepted causal emphasis](vsl_p1_approval_and_review_readiness.md)

## What the review needs to establish

P1 separates wanting to merge from completing a merge. Locally available
ending-lane traffic requests transfer. The adjacent continuing lane serves its
own feasible forward traffic first, then uses its remaining receiving budget
for merging. Accepted traffic leaves the ending lane and enters the adjacent
lane in equal mass; unserved traffic remains present. The first candidate is
Carey's own-lane-priority allocation, R1.

That allocation supplies only part of the required model. The review must also
explain where the receiver's budget and its own competing demand come from,
how accepted traffic changes the next state, and how the same common speed
action enters these relationships. A queue or occupied downstream space can
restrict acceptance even when merging traffic is ready. Adding traffic to the
adjacent lane can restrict later acceptance even when the first merge was
feasible. These are dependencies to qualify, not additional mechanisms already
selected by writing this plan.

The intended outcome is the smallest source-supported candidate that connects
those dependencies consistently, together with a clear account of which
existing stack interfaces can remain. If that requires a further methodological
choice, the review should explain the smallest necessary change and stop there.

### A concrete example of the question

Reuse P1's single-opportunity illustration. Six units of ending-lane traffic
are ready to merge; four units of continuing traffic request their own advance.
Each accepted merge consumes twice the receiving work of an ordinary advance.
These are illustrative quantities, not adopted parameters.

| Receiving budget at that opportunity | Continuing traffic served first | Merging completed | Traffic still needing to merge |
|---|---|---|---|
| Ten units of receiving work | Four units | Three units | Three units |
| Four units of receiving work | Four units | Zero | Six units |

The allocation can distinguish these cases. The next review must explain why
the adjacent lane has ten units of receiving work in one case and four in the
other, using a declared traffic model. It must then follow the accepted traffic
into the target lane and account for its later effects. Otherwise the new rule
would merely replace one unexplained completion assumption with an unexplained
service input.

This example establishes neither a speed-control advantage nor an information
collision. Those stronger conclusions require the complete dynamics, admitted
observations and full time accounting.

## How the review follows the causal chain

**First, form the joined local transfer and receiving candidate.** Recheck the
principal source's available traffic, longitudinal demand, receiving limits,
priority allocation and residual update together. Identify the physical inputs
that determine the receiver's acceptance and its own traffic's claim on that
acceptance. All transfers must share consistent donor and receiver budgets at
the same location and over the same interval. Receiving work must remain
distinct from vehicle-equivalent mass.

Then trace common advice through this candidate on fixed road geometry. The
review must explain how advice changes actual traffic availability and service,
including the physical interpretation of transfer opportunities. Repeating a
request on arbitrary numerical ticks or changing road-cell length with advice
cannot by itself supply this interpretation. A constant nonbinding branch may
be valid under restrictions, but those restrictions must cover the declared
traffic and advice range. Slower advice may increase, decrease or leave total
completed merging unchanged.

The key reduction question is what the candidate needs to know about the
adjacent lane. Assess whether the existing ending/continuing grouping can
provide that information under justified conditions. If a compact receiving
statistic could suffice, state what predicts its evolution; supplying future
receiving externally would violate autonomous prediction. If extra state is
necessary, show why and stop for that methodological choice before adopting it.
These are the main tasks under MP1–MP3.

**Second, check what this changes in the rest of the task.** Trace the accepted
merges and unserved requests far enough to assess the existing travel and exit
reductions. Own-lane priority protects immediate continuing service when it is
feasible; it does not establish unchanged later receiving or a common traversal
time. Determine whether preparation waiting, changed exit arrivals or downstream
restrictions invalidate those reductions. If they do, identify the smallest
affected state, timing or boundary contract rather than silently adding an
adapter.

Keep the complete-time objective: travel and waiting for every cohort member
until exit. Final clearance or total receiving work alone cannot replace average
completion time when arrivals or departure priorities differ. The review must
also explain how unmerged traffic is held and eventually served at the permanent
lane end, and whether early and late receiving-work assumptions can coexist.
This is the consistency check under MP4–MP5, not an instruction to replace the
exit component in advance.

**Third, assess one joint operating regime.** MP6 asks whether the candidate's
conditions hold together for the same finite cohort, fixed three-to-two geometry
and common bounded advice range. The request policy, speed response, receiving,
grouping, preparation costs and exit treatment must describe the same traffic.
Evidence for each part in a different regime does not qualify their combination.
If an elementary joined regime cannot be justified, report that limitation.
If merging finishes immediately under every admitted action, loss of S13's
extra-time preparation benefit is an acceptable finding.

These are the reasoning order within one bounded review. Its depth centers on
the joined state/service/transfer relationship. Neighboring components receive
the checks needed to determine compatibility; a new choice there ends this
pass rather than opening a separate construction program.

## Evidence, comparisons and decision ownership

Carey remains the principal source for this candidate: inspect the complete
relevant R1 update and its longitudinal sending/receiving context, not just the
spare-receiving expression. Reuse the accepted S13, B1 and component-audit
records as the starting evidence. Subraveti remains a separate lane-drop/domain
check if needed; its equations are not spliced into Carey. Further primary
reading should answer a specific gap in this candidate rather than restart a
general VSL survey. Maintain a reference list of every paper actually viewed
in the review, with inspected locations and access limitations.

The review should compare its information requirements with the strongest
compact explanation. Ending mass plus a receiving statistic may suffice in
a justified restriction; full lane profiles and discrete order are not presumed
necessary. Strong aggregate/history/capacity-drop rivals remain relevant to the
eventual verification. Their full protocol and a new reachable equal-history
witness follow qualification of the traffic contract, rather than being claimed
from the local example. Analytical references, finite-difference sensitivities
and direct search remain serious rivals for the one scalar action.

MP1–MP6 retain their accepted definitions, dependencies and **Type 2** ownership.
G3/VQ3-P/T/S govern shared traffic and interface meaning; G2 governs information
fairness; G4 governs complete accounting and gradient evidence. The reviewer
organizes evidence and proposes a contract; the user owns any further
methodological adoption. Source indices, unit transcription and notation are
**Type 1** details only after their global meaning is settled. This plan creates
no new scientific decision inventory.

[Existing question definitions and ownership](vsl_r1_modeling_problem_inventory.md)

[Previous source evidence and paper reference list](../../extraction/research_readiness/vsl_b1_source_and_interface_audit.md)

## The report and its stopping gate

The main report will lead with **what model can be formed, why its traffic
behavior follows, and how it fits the existing stack**. It should explain the
example above using the qualified state-to-service relationship, then state
what changes under common advice. An old/new component comparison must separate
the approved component-4 and component-5 delta from any newly required change.
Each MP result should give a direct answer or a specific unresolved dependency;
MP6 must receive one joint disposition. Detailed extraction and mathematics
belong in supporting documents.

Planned outputs are a findings/gate report under `reporting/research_readiness/`,
a source/reduction audit with the viewed-paper reference list under
`extraction/research_readiness/`, and a work record. If substantial equations
are needed, retain a LaTeX source and verified PDF under
`synthesis/research_readiness/`. These are future review outputs, not findings
delivered by this plan.

The stopping gate is **VSL-B2-G1: can the approved transfer direction join its
receiving and time interfaces within an elementary task?** A successful pass
provides a source-supported candidate, consistent budgets and state evolution,
explicit interface/domain conditions and a defensible MP6 disposition. It may
instead expose a necessary amendment or an unresolved elementary-regime gap.
Those are useful review outcomes, not reasons to continue expanding the model.

Stop earlier if the evidence requires switching priority, adding consequential
state, changing motion or departure meaning, adopting a new lane-end service
law, changing the observer/objective, or enlarging the task. Present that smallest
choice with its problem, role in the causal chain, evidence gap, alternatives,
Pros, Cons, dependencies and provisional recommendation. Do not adopt the
change or carry out dependent work before the user decides.

The present task opens and saves this concrete plan. The next allowed action
is to carry out the bounded VSL-B2 review under P1's approval. S13's conditional
certificate and scalar sufficiency, the urban closure and ramp closure remain
intact. The review admits no simulator implementation, dependency installation,
traffic experiment or automatic successor pass. Useful gradients require their
later correctness and independent decision evidence.

[Plan work record and document checks](vsl_b2_plan_work_report.md)

## Execution disposition — 2026-10-13

The user subsequently directed execution of this plan. The review established
the conditional local state → receiving → merging relationship and stopped at
VSL-B2-G1, where selecting an autonomous receiver/motion representation would
change the shared methodological stack. Its examples, MP1–MP6 dispositions and
the provisional compact/spatial alternatives are in the executed report. The
earlier planning status and prospective wording above are retained as the
delivery-time brief.

[Executed review and stopping gate](vsl_b2_joined_service_findings_and_gate.md)

## Continued qualification and original-scope status — 2026-10-13

The user subsequently selected compact A, travel-history A-H and homogeneous
H1 as successive qualification restrictions. These choices continue this
same joined-service/interface question; they do not close the successor's
modeling-chain stage or open its verification protocol.

The H1 pass now provides a concrete conditional upstream state-to-spare-service-
to-merging candidate with explicit physical opportunity and response adaptations.
It establishes homogeneous invariance only in its admitted free-flow/no-boundary-
holding domain, and scalar sufficiency under retained initial continuing
symmetry. Finite footprint arrivals make the terminal service interface
consequential. The nonblocking joined limit gives the same fastest action for
every hidden merge state; a delay-producing terminal remains unqualified.

This fulfills the original plan's requirement to identify the smallest
necessary neighboring amendment and stop. **The bounded H1 evidence pass is
finished at VSL-B2-G1; a fully joined elementary model is not admitted.**
The gate asks whether to close on the limiting member or authorize a compact
arrival-aware terminal qualification, retaining H1. It does not add a new
methodological question set or authorize spatial B, implementation or runs.

[H1 findings and original system-interface gate](vsl_h1_homogeneous_window_findings.md)

[Roadmap progress and exact remaining closure burdens](vsl_review_progress.md)

## K2 execution: the concrete forced boundary — 2026-10-14

The user approved K2's compact arrival-aware terminal qualification. It was
executed within this same B2/Pass 2 scope. A one-queue own-lane-first server
now specifies compulsory completion, available traffic, residual receiving,
held mass, departures and finite clearance. Finite terminal boundary histories
give a sufficient no-spillback domain compatible with homogeneous H1.

The candidate is conditional on a physical terminal reach and a fixed
early-transfer handoff, or alternatively on an explicitly virtual no-feedback
approximation. These are the specific shared meanings awaiting adoption,
including the proposed terminal priority. The bounded K2 pass is finished
at the original VSL-B2-G1 gate; Pass 2 is not closed as an adopted complete
model and Passes 3–4 have not begun. A forced queue alone does not guarantee
the desired interior optimum, and no parameters were selected for that result.

## T1 selected; original evidence review completed — 2026-10-14

The user selected the finite physical terminal section with its reviewed
handoff and restricted one-queue member. The remaining qualification was
executed, rather than opening another broad plan. One exact H1/T1 document
now consolidates population, opportunity, density/service evolution, physical
travel/storage, forced priority, departures, complete TST and information
sufficiency. A joint analytical family includes active early receiving and
positive forced waiting without holding H1, across the same advice range.

This completes this brief's bounded evidence review at **VSL-B2-G1's final
contract confirmation gate**. The assembled exact equations and conservative
domain await confirmation before freeze. No new shared modeling choice was
needed after T1 selection. Original Pass 3's observer, derivative and
independent-usefulness review is not opened; applied MP6 remains unestablished.

[Current complete model and confirmation gate](vsl_t1_joined_model_and_gate.md)

## Step 2 user closure and Step 3 opening — 2026-10-14

The user explicitly approved closing the assembled conditional H1/T1
contract and opening Step 3. This original B2 execution brief is closed
successfully at its modeling gate; no equation or domain was changed for
acceptance. Calibration and useful-gradient claims remain separate evidence.

Step 3 was then begun with complete-history, scalar-equivalence,
decision/sensitivity and reference-fitness work. Its current stop is the
new independent-reference choice; it does not reopen B2 by default.

[Approved closure and frozen artifact identity](vsl_step2_model_closure.md)

[Executed Step 3 opening and current gate](vsl_step3_findings_and_gate.md)

[Concrete forced-merge model, complete MP answers and adoption gate](vsl_k2_forced_merge_findings_and_gate.md)
