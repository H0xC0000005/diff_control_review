# Fixed service locations favor a compact S-E boundary rule

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

## The observation is useful, with a distinction about what a queue means

The established task has a particularly simple **service topology**. After
H1's early-merging cutoff, A and E travel through their finite terminal
approaches. No further early lateral transfer occurs there. Remaining E
must merge at the choke; A passes the same service boundary. The far lane,
B, has its own continuing exit. No other internal restriction, downstream
recovery reach or moving bottleneck is introduced.

Consequently, one waiting balance per approach is sufficient to describe
**eligible traffic awaiting exit** at this interface. A and E can both wait
under the selected coupled-service direction. B has a balance in the general
notation, but **B's waiting balance remains zero in the retained primary
demand domain**: it starts empty, its eligible arrival rate fits its separate
exit service, and A/E interaction does not restrict B. Changing that would
require an explicit amendment, not follow from choosing S-E.

Thus “at most three queue accounts, tied to fixed exits” is sound. More
specifically, the present primary task has **two potentially active coupled
waiting balances, plus B's unaffected passage**. H1's unmerged ending mass
is a preparation stock, not another stopped queue.

The stronger physical picture needs care. T1 distinguishes the mass still
inside a terminal lane from the mass that could have reached its exit at
free speed but has not departed. The latter is its eligible waiting balance.
It is neither the exact mass currently stopped nor a geometric measurement
of a connected physical jam. T1 retains minimum travel, storage and delayed
boundary histories; it does not assert uniform traffic inside the terminal.

“The queue shrinks toward its fixed server” is a useful boundary-queue
picture when departures exceed eligible arrivals. It is **not an established
theorem that every physical congested region has one fixed head and a tail
that retreats monotonically to the choke**. A growing queue can extend
upstream; during recovery, changes in discharge can propagate through traffic
that is already delayed. The present reduction need not track those fronts
as additional states, but fixed geometry alone does not eliminate them.
We therefore use **fixed service locations**, rather than a new assumption
of stationary physical queues.

[Accepted finite-terminal definitions, sections 3–4](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.pdf)

[Selected coupled point and local-completion meaning](vsl_step3_coupled_point_decision.md)

## What can be simplified

Your observation gives a stronger reason to begin with S-E. The model need
not solve a separate problem of locating or counting queues. Its existing
terminal histories already supply the exit eligibility and waiting balances.
The new work belongs at the **single A/E service boundary**: what can enter,
how the available service is shared, and how recent interactions affect
later service.

The compact starting description is therefore:

> Two coupled fluid waiting balances at one choke, supplied by the existing
> finite-terminal travel histories, and one shared admission/recovery account.
> B continues through its separate exit without queueing in the primary domain.

“Fluid” means continuous vehicle-equivalent mass. It does not mean that the
physical terminal is replaced by an infinite vertical buffer. No spatial
cells, independently tracked queue-head/tail positions or vehicle-following
states are required merely to represent this queue configuration. The
storage and minimum-travel interfaces remain.

The number of balances is not the number of all required states. Two moments
can have the same A/E waiting amounts but different recent merge histories,
so the approved P-H/M2 recovery account may predict different available
service. Delayed terminal entry histories also remain relevant. The fixed
configuration supports a compact interface, not a proof that two or three
instantaneous queue lengths form a sufficient Markov state.

## Improved S-E: state a local rule for each empty or waiting approach

The shared problem is to determine **causal admission and discharge**, not
to choose where congestion lives. S-E should now be qualified in that narrow
form. Its proposed behavioral rules are:

1. **An empty approach offers its eligible arrivals.** Evaluate the current
   physical admission opportunities, compatible boundary state and retained
   account. If those arrivals can all pass, keep its waiting balance empty.
   E may still face an actual insertion restriction without an existing queue;
   this rule does not require an external slowing seed.
2. **A service shortfall creates waiting at that boundary.** Only the
   difference between eligible arrivals and admitted departures accumulates.
   An alternative slow/queued solution that would sustain itself is not,
   by itself, an admissible reason to switch regimes.
3. **A waiting approach offers its available sending capacity.** The single
   coupled service rule limits actual A/E departures. Waiting grows or shrinks
   according to arrivals minus departures. An A queue alone does not impose
   an extra service penalty; any state-dependent burden needs a physical basis.
4. **Clearance is an actual zero crossing of the waiting balance.** At
   clearance, re-evaluate feasible passage under the current arrivals and
   account; do not serve unavailable mass or reset the recovery account simply
   because a queue vanished. Simultaneous A/E events need an explicit rule.
5. **Use only the justified local boundary-speed interpretation.** A free or
   queued flag is not a measurement of average lane speed, and “both queued”
   does not prove equal entry speeds. The admission/speed/work law must select
   a compatible boundary state and a unique causal continuation.

These are the target semantics for qualification, not a completed formula
set. In particular, rules 1 and 5 still need a defensible physical insertion
law and an unambiguous solution where state and discharge depend on each
other. Nonnegative queue accounting alone does not prove uniqueness: the
previous diagnostic already had one fixed queue and still admitted arbitrary
queue birth. The current improvement narrows the missing closure to local
admission and boundary-state selection; it does not erase that finding.

## How both options improve through the same example

Imagine a short burst of E reaching the choke while A is flowing freely.
An actual entry restriction briefly prevents all E arrivals from being
served. E starts waiting; the shared service effect may also make A wait.
Later the burst ends and the waiting traffic clears. Any justified recovery
effect can outlast that clearance without keeping fictitious vehicles in a
queue or adding their post-line travel time to the objective.

| Question | Refined S-E: local equilibrium boundary rule | Refined S-V: additional local speed dynamics |
|---|---|---|
| **What represents waiting in that example?** | The same two A/E balances and existing terminal histories. | The same balances and histories; no extra queue locations. |
| **What describes entry conditions?** | A compatible equilibrium boundary state, selected by explicit admission and empty/waiting/clearance rules. | Independently evolving local approach/entry speed state where finite-rate adjustment is shown necessary. |
| **What is the main benefit?** | Concentrates the new model at the only coupled boundary and retains the smaller first-order amendment. | Can represent gradual deceleration or approach-speed recovery that is not determined by the equilibrium boundary state and retained service account. |
| **What is the main cost?** | It may omit meaningful transient speed adjustment; equilibrium and event selection still need justification and proof. | It adds physical state, initial values, adjustment parameters and population-changing update semantics. Fixed geometry does not supply them. |
| **What would justify the larger option?** | A specific intended behavior that this equilibrium closure cannot represent adequately. | A demonstrated need for independent speed memory, with a concrete macroscopic interpretation and evidence. |

**Recommendation and status.** Begin qualifying the refined S-E rule set.
The user's acceptance closes A1-C-S1's direction choice at that scope.
S-V remains an unselected return route if the first-order closure proves
inadequate. Neither the geometry nor this response approves dropping T1,
resetting P-H memory, restoring a constant merge share, selecting equal-work
fairness, or adding speed dynamics. No new methodological choice is required
merely to adopt the clearer fixed-boundary formulation.

## Source check and limits

Jin's continuous LTM formulation derives exit demand, eligible queue and
vacancy from cumulative boundary histories, with a separate junction rule.
That supports retaining T1's boundary formulation instead of adding queue
position states. It does not establish our state-dependent merge law or
prove the proposed S-E continuation unique.

[Jin (2015), primary preprint, section 3.1 empty-link case and section 3.3](https://arxiv.org/pdf/1405.7080)

A useful simpler rival is Jin's link queue model, which uses aggregate link
density to define demand and supply. The paper distinguishes it from LTM:
the latter retains delayed histories, while the link queue model omits
within-link wave dynamics. Substituting that whole-link density model would
be another modeling choice; it is not implied by the small number of queues.

[Jin, *A link queue model of network traffic flow*, primary preprint, sections 2.4, 3 and 4](https://arxiv.org/pdf/1209.2361)

The prior boundary-selection precedent was also rechecked. Its explicit
entropy rule selects a physical solution in its own capacity-drop model;
its phenomenological drop and uniqueness result are not transferred here.

[Jin, Gan and Lebacque, primary preprint, sections 2.1–2.2](https://arxiv.org/pdf/1310.2660)

Only these selected primary sections were inspected in this check. No full
new literature survey, native simulator audit, traffic experiment or new
mathematical proof is claimed.

## Progress and next allowed work

This observation check is complete. S-E is the selected starting direction
inside the existing Type 2 G3 return. The exact admission/boundary-state,
shared recovery and joined qualification pass remains unfinished, as does
Step 3. The next work is to qualify those S-E rules against the unchanged
T1/H1 interfaces, then the shared recovery and MP6/evidence obligations.
This response does not execute that full next pass.

[Work, changes and documentary checks](vsl_se_fixed_queue_work_report.md)
