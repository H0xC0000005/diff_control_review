# What would make the compact merging model physically credible?

**Scope amendment, 2026-10-19:** the user accepts the standalone formulation
as the current verification target and defers SUMO to an optional extension.
The remaining Step 3 blocks are information/action/full-objective gradient
qualification, then consistency and the user gate. This physical review
remains the latest completed evidence checkpoint. Its applied MP6 limits
are retained; its earlier mandatory SUMO continuation is superseded.

[Approved standalone scope and remaining questions](vsl_step3_standalone_scope_decision.md)

Date: 2026-10-16. **The planned physical/source and identifiability review is
complete at MP6-Q1. Applied MP6 remains open; Step 3 is unfinished.** This is
an evidence checkpoint, with no new model option awaiting selection.

The compact point model has a defensible traffic interpretation, but the
literature does not yet establish its complete physical operating range.
The main finding is that its ingredients must explain **different observable
parts of the same merging event**. Matching total travel time alone could
let one ingredient compensate for another, or count the same disturbance
twice. The review now identifies how to distinguish them before judging
control performance. It does not establish a calibrated parameter set.

## The central traffic story

Consider a slow E stream reaching the lane end beside A. Entering the shared
lane can use more room or time than simply continuing in it. After entry,
the slow traffic can also restrict following A traffic while it accelerates.
The selected model represents the first burden through **current maneuver
work**, and the second through **the remaining recovery restriction**.

These can be distinct physical effects. Their distinction is nevertheless a
hypothesis about our joined model, not something proved by citing two
papers. Carey's receiving-work formulation motivates an extra lane-changing
burden. Leclercq's insertion model motivates acceleration-related discharge
loss. Neither supplies our combined work, speed-mark and renewal law.
[Carey et al., Section 5](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf),
[Leclercq et al., Section 2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

A particularly useful comparison is the period **after the last E entry,
while A still waits**. There is no current E maneuver left to charge. In
the selected model, any continuing loss of A discharge then comes entirely
from the retained recovery account. This provides a way to test recovery
separately. Once that account is independently constrained, mixed A/E
discharge can test whether additional immediate maneuver work is needed.
If A has already cleared, low A flow only shows low demand; it does not
measure the remaining service capability.

Even this comparison cannot by itself prove the entire decomposition. The
same coefficients must subsequently predict mixed discharge and its recovery
tail together, without being adjusted again to obtain a favorable action.

## Direct findings

| Physical question | Core finding | Consequence for this task |
|---|---|---|
| **Is the modeled crossing speed already justified?** | Only partly. The congested flow-to-speed relation has a source precedent, but applying each stream's own served flow to its instantaneous insertion speed remains our equilibrium reduction. A queue does not itself verify that speed. | Compare predicted marks with actual crossing speeds separately from fitting discharge. An accurate flow fit cannot conceal an incorrect speed mechanism. |
| **Does the recovery formula describe a vehicle accelerating?** | Its acceleration parameter originates in that mechanism, but its square-root intermediate quantity is a transformed boundary quantity, not a vehicle-speed trajectory. | Test the predicted service loss against discharge; use actual acceleration and insertion-speed observations to check its physical inputs. Do not fit the square-root curve directly to vehicle speeds. |
| **Can immediate work and recovery be distinguished?** | Yes in informative conditions, especially a queued A tail after E ends, followed by mixed discharge with differing A flows and speed gaps. One total-time number or one steady mixture is insufficient to establish the separation. | Qualify recovery and speed marks before attributing the remaining mixed-discharge burden to maneuver work. |
| **Are preparation parameters identified by final E mass?** | A single final count cannot generally separate the preparation opportunity scale from the receiving penalty. A receiving-limited segment primarily identifies their product; an unconstrained segment can identify the opportunity scale separately. | Use development observations of where transfers occur and which constraint binds. Do not infer the whole preparation law from the terminal objective. |
| **Is a source-supported joint parameter range now established?** | No. The mathematical domain is nonempty, but the existing complete-delay witness can require extreme scales. Neither that witness nor isolated values from a source qualify the joined applied regime. | Keep applied MP6 open. One common parameter set must satisfy both the physical evidence and the existing full-advice domain conditions. |
| **Must another state or a spatial model be added now?** | This review provides no evidence requiring that change. The selected compact law can be tested with its present interfaces. Its speed reduction, E-only recovery source and retirement rule remain falsifiable assumptions. | Retain the current stack for qualification. A demonstrated structural failure would reopen the smallest affected contract, rather than trigger an automatic expansion. |

The source itself distinguishes its boundary quantity from physical speed.
Our use of it as a capped recovery profile is a further deduction and
adaptation, not a literal vehicle trajectory.
[Leclercq et al., equation (1) and accompanying text](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

There is also a limit to the earlier SUMO correspondence: matching a
stationary headway curve does not establish transient wave propagation,
actual compliance with advice, or the merging law. SUMO documents the
constant-speed assumptions and additional sources of headway variation.
[Official SUMO road-capacity documentation](https://sumo.dlr.de/docs/Simulation/RoadCapacity.html)

## What this establishes for MP6

The result is a **joint physical admission contract**, not applied admission
itself. It connects preparation, actual speeds, immediate work and retained
recovery to observations that can expose a wrong explanation. Development
trajectories may supply these observations; they are calibration and model
checking evidence, not extra inputs given to a controller at its decision.

Admission requires one parameter set across advice and preparations, with
fixed physical coefficients and the selected one-vehicle-equivalent renewal
normalization. Physical checks must precede held-out action/gradient
evaluation. An uninformative trace leaves a parameter unresolved; it does
not justify assigning a convenient value. A failed joint explanation cannot
be repaired by per-advice fitting, changing the objective, or selecting only
cases with an interior optimum. Strong simpler models remain eligible to
explain the observations better.

[Detailed admission contract, ownership and failure conditions](../../synthesis/research_readiness/vsl_mp6_joint_physical_admission_contract.md)

[Algebra explaining what the observations can identify, PDF](../../synthesis/research_readiness/vsl_mp6_physical_identifiability.pdf)

## Progress and stopping point

The user-approved continuation has now completed its first remaining block:
the physical/source review and the separation of testable mechanisms. It
has **not** closed applied MP6 or the whole of Step 3, and it has not changed
the selected model. No genuinely new methodological choice is forced by
the evidence inspected here.

Two protocol blocks remain: the information/action and full-objective
gradient comparison, then the updated model → SUMO S-P → SUMO S-L evidence
contract. They may be specified conditionally; their freeze must keep the
unexecuted joint physical admission visible. Actual admission and numerical
acceptance settings belong to a separately approved execution proposal.
No theory-only reclassification or applied-validity claim is adopted here.

The earlier statement that E cannot re-form a queue is explicitly conditional
on the accepted monotone H1 pulse, recovery law and primary domain. **A finite
cohort alone does not imply it.** Later or bursty E arrivals can form another
queue in wider settings, including a native reference. Such a native event
is evidence to interpret, not an automatic reference failure.

Stop at MP6-Q1 for review. Step 4 remains unopened. No simulator code,
dependency installation, traffic/ODE experiment, calibration, optimization,
numerical gradient or SUMO run was performed.

[References viewed and their limits](../../extraction/research_readiness/vsl_mp6_physical_source_audit.md)

[Work, commands and verification](vsl_mp6_physical_work_report.md)
