# Feedback 7: let the traffic interaction determine admission and service

**Current O-R qualification, 2026-10-15:** the user selects recent-mass
renewal, closing RE-O1. R-E and current-state S-E-P remain. The bounded
recovery candidate/analytical pass is complete at **OR-Q1**: physical
update/state, local causal coupling, derived positive service and clearance
bounds, and a regular full-cohort family with A delay and active retirement.
This does not establish realistic parameters, the whole original action
range, applied MP6 or useful gradients. The complete joined review and
Step 3 remain open; J4 follows review of this checkpoint. Earlier reports
retain delivery-time meaning. No implementation or traffic experiment.

[Selected renewal, analytical evidence and recovery checkpoint](vsl_or_recovery_qualification_and_checkpoint.md)

[Executed S-E model, reachable contrast and current allocation gate](vsl_se_admission_findings_and_gate.md)

[Fixed queues, refined S-E and approval scope](vsl_se_fixed_queue_configuration_response.md)

[Current selection and precise approval scope](vsl_a1c_selection_and_scope.md)

[Current executed findings and new state-closure gate](vsl_a1c_service_work_findings_and_gate.md)

Date: 2026-10-15. Conceptual response and revision of the open terminal
candidate. **M2 remains selected; M2-A1 and the full Step 3 remain open.**
No exact replacement law or priority amendment is approved by this response.

## Your criticism identifies the missing physical explanation

I agree with the central point. The previous choices specified who may
receive service, but did not sufficiently explain how the traffic states
make that service usable. A conservative allocation can be mathematically
sound and still be a weak behavioral model across different traffic regimes.

Your two examples give a better starting point: **an E stream that must
join a much faster A stream faces a different interaction from two similarly
slow streams taking turns at a lane end**. A useful reduced model should
distinguish those situations without requiring individual vehicle dynamics.

I would revise the preferred candidate around that traffic dependence,
rather than ask you to choose a fixed share now. The strict-priority
exclusion result remains correct; recommending a positive constant share
as the next sufficient physical choice was too narrow.

## What the two examples mean for the model

| Traffic situation | Behavioral interpretation to examine | What the model should explain |
|---|---|---|
| **E is slow/queued; A is moving much faster** | Joining A can require a compatible gap, E waiting or speed adjustment, and possibly A yielding. A successful slow entry may also impede followers during recovery. | The rate at which E can actually enter, and the current/later shared-service burden of the interaction. Neither follows merely from unused average capacity. |
| **Both approaches are slow, with comparable states and sustained demand** | The speed-matching problem is smaller. Interleaved passage and more comparable allocations are plausible, with possible extra burden from E's lateral movement. | A justified allocation in that regime and its total discharge. Similar shares do not imply undisturbed capacity or zero merging cost. |
| **Intermediate or changing conditions** | Admission opportunities, speeds, queueing and recovery evolve together. | A causal response to predicted traffic state, rather than an unexplained switch between two fixed quotas. |
| **Benign compatible passage** | Both streams can pass without a disruptive interaction. | No automatic E slowdown, fixed loss per E, or manufactured queue. |

These are behavioral targets for qualification, not claims that every
large speed mismatch suppresses merging or that every pair of queues should
share equally. The relevant situation includes absolute speeds, usable
space/opportunities, demand and the interaction with A, as well as the
speed difference.

## Why even a variable priority weight is not enough by itself

The earlier sharing formula redistributes a service budget already assumed
usable. Suppose that budget is 600 and unqueued A offers 450, with E waiting.
E receives the remaining 150 under both an E priority weight of one quarter
and one tenth. Reducing the weight does not reduce that residual admission.

Consequently, making the weight depend on speed difference alone would not
necessarily represent your first example. The missing physical rule also
concerns **whether E can use the apparent spare service, and what the
interaction does to effective total service**. This is an exact static
property of the allocation template, not a traffic simulation or a proposed
numerical task.

The preferred model therefore needs a joined admission/service closure.
It may use an aggregate opportunity or interaction description internally,
while presenting one shared effective-service account. One account does not
mean that all nominal residual capacity is always usable by E. The closure
must also separate lack of demand from a real service restriction.

## How strongly the traffic evidence supports your picture

Hidas's inspected discussion supports examining speed mismatch and both
drivers' adjustments, including the following traffic's response. It does
not establish a macro formula for our endpoint.

[Hidas (2005), primary publisher excerpts](https://www.sciencedirect.com/science/article/pii/S0968090X04000671)

Marczak, Daamen and Buisson's two-site analysis relates gap acceptance to
gaps and relative speeds. Its fitted relative-speed association does not
follow a simple universal mismatch penalty; the authors explain it through
how rejected gaps are sampled. This supports state dependence, not a fixed
monotonic admission rule inferred from lane-average speeds.

[Primary paper, §6–7, printed pp542–545](https://mocopo.ifsttar.fr/fileadmin/contributeurs/Mocopo/Documents/Other_documents/Article_-_Merging_behaviour_-_Empirical_comparison_between_two_sites_and_new_theory_development.pdf)

Bar-Gera and Ahn report approximately lane-count-related merge ratios at
fully congested freeway-to-freeway merges, with residual differences. That
supports comparable sharing as a restricted-regime benchmark. Their
upstream-and-downstream congestion and connector geometry differ from our
lane end; they do not establish exact equality or a small E penalty here.

[Author-institution abstract and citation](https://cris.bgu.ac.il/en/publications/empirical-macroscopic-evaluation-of-freeway-merge-ratios/)

The source claims above are deliberately limited. We should not declare
either fixed allocation universally unrealistic: a fixed share may be useful
and defensible in a qualified regime. It remains a strong simple reference.
What it does not supply is the transition between the regimes you describe.

## The qualifications I would retain

**Comparable queues are not automatically comparable speeds.** Queues may
have different discharge conditions, traffic composition or histories. We
should use the justified predicted traffic states, not a binary “both queued”
label as a substitute for them. The common speed advice is also not the
actual speed of queued traffic.

**The approximate balance and slight E disadvantage are hypotheses.** They
are sensible limits to investigate under sufficiently similar conditions,
not universal constants. Even similar entry speeds do not remove the need
for room to merge, nor the acceleration/recovery of a slow combined stream.

**A difficult maneuver and willingness to accept a gap are different.**
Available gaps, speed adjustment, urgency and cooperation affect what happens.
The causal burden of a successful slow entry need not have the same dependence
as its admission probability. We should distinguish them without constructing
independent penalties for the same interaction.

**A macro treatment remains plausible, not yet proved sufficient.** Aggregate
lane states and finite recovery information may suffice. Their actual speed,
opportunity and memory closure must be made explicit and qualified. No
microscopic trajectories, new spatial cells or privileged future SUMO input
are implied by this proposal.

## Revised preferred candidate: traffic-conditioned A1-C

Keep the existing two physical terminal approaches and singleton service
account. Revise A1-C from a proposed fixed positive priority weight to
**admission and service conditioned on the traffic interaction**:

1. Predicted approach/entry state determines which E passages are feasible
   in the aggregate and how A/E compete for service. It must distinguish
   slow E beside fast A from comparable slow approaches and benign passage.
2. The actual interaction and discharge kinematics determine current service
   use and continuing recovery. Count a physical effect once, whether it is
   represented in admission, effective service or retained influence.
3. Qualify the resulting joint law within the already approved chain:
   conservative departures, sufficient state, causal well-posedness, finite
   clearance, full local time, MP6, fair information/gradient comparisons and
   the model → SUMO S-P → SUMO S-L ladder.

This revises **component 6**, not several separate parts of the stack.
H1 preparation, its own-lane priority and cutoff, finite terminal storage,
initial information, one advice and the choke-line objective retain their
approved meanings. A changed terminal admission law still requires explicit
G3 confirmation; feedback 7 is not treated as that completed approval.

Do not freeze a linear interpolation, smooth transition, E work multiplier
or loss kernel now. A specific formula must earn its interpretation from
the source/reduction review. The pointwise demand/budget checks on the old
allocation template remain useful where that template is used, but they
do not prove an endogenous state-dependent joint law well posed.

### How the candidates now stand

| Candidate | Useful role after feedback 7 | Strength | Limitation and consequence |
|---|---|---|---|
| **A1-S: strict A-first remainder** | Retained inherited contract and restricted reference. | Exact and simple; identifies the consequence of absolute A priority. | Excludes E passage during A backlog and lacks the requested traffic-conditioned interaction. It is not a sufficient behavioral answer merely because it is feasible. |
| **Fixed-share version of A1-C** | Allocation template, simpler rival and possible qualified-regime limit. | Compact; unused service redistributes; restricted empirical merge-ratio evidence makes it a serious baseline. | A constant quota does not explain regime changes or E's ability to use residual service. It is no longer the preferred full behavioral closure. |
| **Revised A1-C: traffic-conditioned admission/service** | **Provisional preferred qualification target.** | Directly addresses the user's contrasting traffic situations within one point component/account. | Exact state, admission/kinematics, service/recovery relation and evidence remain unresolved; no equation, parameter or macro-sufficiency result is approved. |

**Recommendation:** develop the revised A1-C within the existing joined
review, keeping strict and fixed-share versions as explicit limits/rivals.
The next scientific question is the justified joint traffic-state law,
not a numerical choice between absolute A priority and one constant quota.

**Status:** feedback 7 answered; living candidates and the M2-A1 framing
revised, not closed by selection. The valid exclusion/allocation calculations
are preserved. The approved three-part review and Step 3 remain in progress;
this response does not execute or approve a new full law. No simulator work,
installation or traffic experiment is opened.

[Viewed references and access/inference limits](../../extraction/research_readiness/vsl_feedback7_traffic_state_source_audit.md)

[Files, checks, preservation and next allowed action](vsl_feedback7_work_report.md)
