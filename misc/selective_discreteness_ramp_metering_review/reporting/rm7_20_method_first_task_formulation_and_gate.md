# RM7.20 — Method-first ramp task formulation and user gate

Date: 2026-10-01. Status: **RM7-UG1 / RMT-R1 closed; Candidate A approved.**
Parent: [RM7 method-first plan](../rm7_00_method_first_task_formulation_review.md).
Evidence: [source-reuse audit](../extraction/rm7_method_first_source_reuse_audit.md)
and [candidate matrix](../synthesis/rm7_candidate_task_matrix.md).

## Scope correction completed

RM6's gate is withdrawn. The new ramp review no longer asks which task can be
added to the current simulator. It asks which traffic/control task best isolates
the value of macro-hidden information. Model equations, simulator compatibility
and implementation cost are deliberately deferred.

Historical ramp findings are used as evidence rather than constraints:

- mature aggregate control and adjoints define the strong baseline;
- the old B1-P result warns against confusing remote ordered service with a new
  ramp mechanism;
- lane/gap/acceleration mechanisms remain candidates even if they require a
  future model different from current project code; and
- the old rejection of an orthogonal parallel implementation task does not
  decide this method-first research question.

## Recommended task

The strongest first task is **F1 — local on-ramp merge opportunity**:

> For one infrastructure-controlled on-ramp entering a multilane freeway, what
> minimum local merge information beyond complete road-total mainline and ramp-
> queue history is needed to predict useful metering perturbations under complete
> all-stream accounting?

The task contract is:

- **geometry:** one finite-storage ramp, one multilane mainline and one local
  merge/acceleration region;
- **action:** a bounded continuous metering rate or fixed-shape release schedule;
- **strong observer:** complete declared road-total mainline density, flow,
  speed and cumulative-count history, ramp queue/history, known geometry,
  demands and future forcing, without lane/gap decomposition;
- **candidate hidden information:** target-lane occupancy, usable merge
  opportunities and any lane-change/relaxation/order state later shown necessary;
- **primary outcome:** all-stream total system time/delay through common
  clearance, including ramp waiting and mainline delay;
- **guardrails:** ramp spillback, residual demand, merge feasibility and safety;
  and
- **future representation ladder:** strong aggregate/multiclass model →
  aggregate plus merge-pressure statistic → lane-group/local mesoscopic model →
  independent richer reference.

RM7 does not assert that any listed hidden coordinate is necessary. The next
review must determine whether the consequential state compresses to one scalar,
requires lane groups, needs finer local semantics or is already recoverable from
a strong aggregate history.

## Why F1 is the best starting point

F1 puts the infrastructure action and disputed mechanism at the same merge. It
can compare identical actions and objectives while adding information in a
controlled ladder. A microscopic or hybrid evaluator may later be admitted if
the evidence requires one; that possibility is no longer rejected because it
does not match current implementation.

F1 also has a genuine failure mode. Mature aggregate ramp models may already
capture every useful effect through density, ramp queue, capacity-drop state or
one merge-pressure statistic. That result would answer the minimum-information
question rather than make the task invalid.

## What remains unproved

- No exact aggregate-history collision has been constructed for the F1 geometry.
- The minimum consequential hidden variable is unknown.
- The action may not change effective service enough to overcome complete
  all-stream accounting.
- Safe-gap and lane-change state may introduce nonsmooth or stochastic behavior;
  no derivative treatment is selected.
- No model family, reference evaluator, scenario data or parameter regime is
  approved.
- Novelty and predecessor coverage require a fresh targeted review after task
  selection.

## RM7-UG1 / RMT-R1 — task selection

### Problem statement

Which ramp-metering task should receive the full method-first predecessor,
mechanism, information and evaluator review?

### Assumed model-chain function

Infrastructure metering changes the timing and amount of ramp traffic reaching
a freeway system. Hidden local traffic state changes realized service or
downstream access. Complete all-stream outcomes determine whether the control
effect is useful.

### Core gap

Ramp metering has strong aggregate controllers and gradients, but the branch has
not selected a traffic setting in which additional information can be isolated
fairly. Task selection must precede model-family selection and implementation
compatibility.

### Candidate A — local merge-opportunity task (recommended)

Select the F1 formulation above. Begin the next review with a fresh targeted
search of aggregate, lane-continuous, mesoscopic, microscopic and hybrid merge
models; identify the minimum hidden-information candidate and strong comparator
before equations are adopted.

**Pros:** Smallest causal setting; direct connection between meter and merge;
supports a clean aggregate-to-richer information ladder; accepts scalar
sufficiency and negative results; provides a clear independent-evaluator role.

**Cons:** The hidden state may be difficult to match exactly, safe-gap behavior
may be nonsmooth, and mature aggregate merge-pressure models may eliminate the
need for richer resolution.

**Dependencies and consequences:** Opens an RM8 predecessor/mechanism review
proposal. It does not select a model, require current-project compatibility or
authorize implementation.

### Candidate B — downstream route-access and spillover task

Use one meter to change the composition and timing arriving at a downstream
exit, restricted lane or finite pocket. Compare route-aware aggregate/cohort
models with lane/storage/order-aware alternatives.

**Pros:** Strong route and storage semantics; clear remote-control chain;
substantial historical evidence and an interpretable downstream objective.

**Cons:** Destination-aware aggregate and FIFOQ alternatives are already strong;
the task can repeat the signal-control ordered-service question; downstream
geometry makes attribution less direct than F1.

**Dependencies and consequences:** Requires a new matched route-access contract
that does not use bookkeeping serialization as physical order. The old B1-P
construction is evidence, not an approved ready-made task.

### Candidate C — coordinated multi-ramp local-merge task

Study several meters whose releases interact through corridor propagation,
finite queues and local merge opportunity. Seek whether localized hidden states
improve coordinated actions or gradients beyond aggregate corridor MPC.

**Pros:** Strong operational motivation and high-dimensional gradient value;
tests whether local information matters at network scale; can expose spatial
coupling absent from a single merge.

**Cons:** Coordination, forecasting, fairness and spillback can confound the
resolution question; aggregate coordinated control is mature; experiment and
calibration burden is much larger.

**Dependencies and consequences:** Best treated as an extension after a local
merge mechanism is established. Selecting it first requires a broader evidence
and comparison design.

**Provisional recommendation: Candidate A.** It parallels the VSL method-first
strategy: begin with a narrowly stated traffic/control question and a strong
baseline, then let the evidence determine the required model resolution.

## Gate disposition

The user approved **RMT-R1 Candidate A**. Candidate C is retained as a possible
future extension after positive Candidate A results and a separate user
decision. Candidate B remains unselected.

The [decision record](../discussion/rm7_candidate_a_approval_and_extension_record.md)
and [post-selection design inventory](../synthesis/rm7_post_selection_design_inventory.md)
record the closure and remaining choices. This approves task selection only.
A bounded RM8 proposal may follow; no model-family adoption, implementation or
experiment starts automatically.
