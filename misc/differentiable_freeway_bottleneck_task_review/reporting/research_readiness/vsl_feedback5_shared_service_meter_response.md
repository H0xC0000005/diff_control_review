# Feedback 5: one shared service meter, with a causal recovery rule

**Subsequent decision:** the user accepted M2 and directed continuation.
CP-D2's direction choice is closed. The first M2 source/speed pass has now
reached CP-M2-D1's physical-activation choice; neither new route is selected.
The response below retains its discussion-time status and recommendation.

[M2 selection and executed continuation](vsl_m2_selection_and_scope.md)

[Current findings and activation gate](vsl_m2_first_restriction_findings_and_gate.md)

**Yes: one shared effective-service meter is a coherent point-model
interface.** It expresses exactly the coupling we need: whatever reduces
service at the merge affects the combined passage of A and E. A priority
rule then decides how that available service is shared.

Your picture also exposes a distinction my earlier options did not explain
clearly. **One meter reading does not mean one fixed response, one scalar
state, or one independent constraint per past merge.** The existing exact
P-H candidate already produces one shared service ceiling. Its separate
history contributions are added to determine that ceiling; they are not
separate restrictions applied to each stream.

Your proposal fits **Option 2's traffic-dependent aim** more closely because
it asks the update to account for discharge amount, speed and the interaction
being represented. Its single shared meter is compatible with both options.
The suggested contribution from slow A discharge is an additional physical
question; it needs the qualification explained below.

This response refines the still-open CP-D2 discussion. It selects no new law,
does not close Step 3, and leaves the exact mathematical artifacts unchanged.

## What the meter measures

The reading means **the total service currently available to A and E if
enough eligible traffic wants to pass**. It is a ceiling on passage, not the
observed number actually passing. For this task its undisturbed ceiling is
the already declared ordinary shared budget. Calling it “free-flow capacity”
does not require changing that budget to the full fundamental-diagram
capacity or making it vary with advice.

Ordinary A traffic uses some of that available service now. Under the
proposed reference law, an undisturbed A passage does not additionally lower
future service. Thus “no effect on the reading” is sound if it means no new
restriction; it cannot mean that A occupies none of the shared service.

Similarly, a low observed outflow can simply mean that little traffic is
present. It must not automatically be interpreted as a lower service
capability. The meter and the demand for its service have different roles.

## Slow A traffic: a reasonable concern, with an important distinction

Imagine a slow E entry has already reduced the reading and made A queue.
There are now two possible statements about A:

- **A is moving slowly because the existing restriction holds it back.**
  That is already a consequence of the low reading. Automatically lowering
  the reading again because the queue is slow can count the same restriction
  twice or create a self-sustaining slowdown by assumption.
- **A's actual discharge introduces an additional physical restriction.**
  For example, a separately justified acceleration/recovery or following
  mechanism could affect later passage. Such a contribution can be represented
  through the same meter. Its additional effect must be identified rather
  than inferred solely from the existence or low speed of the upstream queue.

The standard continuous-LTM demand formulation permits a lane with eligible
queued traffic to offer capacity demand; downstream service determines what
actually leaves. Queueing alone therefore does not prescribe another reduction
of the node's capacity. This is a modeling distinction, not a denial of
observed capacity-drop or startup phenomena.

[Primary LTM demand and junction conditions, §3.1–3.2](https://arxiv.org/pdf/1405.7080)

Jin, Gan and Lebacque's separate capacity-drop boundary illustrates that an
extra congestion-related capacity rule can be introduced, but its magnitude
and immediate activation are explicit phenomenological assumptions. It does
not establish the particular A-speed update proposed here.

[Primary capacity-drop model, §2.1 and its stated limits](https://arxiv.org/pdf/1310.2660)

My recommendation is therefore to **allow the shared rule to represent a
justified additional A effect, while keeping “an A queue exists” separate
from “A has created another service restriction.”** This preserves your causal
concern without adopting an unexplained extra penalty.

## One meter can still need recovery memory

At a particular instant there can be one reading. To predict its future,
the model may need more information than that number alone.

For example, the same reduced reading could follow a recent small burst or
an older larger burst whose influence is nearly over. Their present totals
can agree while their subsequent recovery differs. In the existing exact
candidate, the ages of recent admissions supply that information. Compressing
it to one scalar would be a new reduction requiring justification.

This does not require many simultaneous service constraints or a spatial
recovery zone. Several pieces of retained temporal information can jointly
determine one shared ceiling. A genuinely sufficient scalar recovery state
would also be acceptable if it can be qualified; it is not yet established.

Recovery also needs to occur when no new disturbance is admitted. Completed
traffic must not disappear from the service calculation immediately, and
an empty arrival period must not freeze the reading permanently at its
last reduced value.

## How discharge and speed would enter the model

The model should distinguish current service use from the recovery effect
left for later traffic. The current meter, lane demand and priority determine
conservative A/E admissions. The admitted amounts and their relevant
kinematics then contribute to the retained restriction, while existing
influences recover. The exact continuous or discrete formulation must make
that feedback causal and well defined.

The current H1/T1 boundary counts provide amounts and timing, but not a
uniquely specified physical exit-speed field. Advice is a free-speed
parameter, not automatically the actual speed of queued traffic crossing
the choke. A traffic-dependent meter therefore needs an explicit speed
interpretation and prediction rule; future SUMO speeds cannot be supplied
as an oracle.

The slow-insertion literature supports studying entry speed and bounded
acceleration, but does not supply our complete finite continuous update.
Its recovery/interaction mechanism motivates the question rather than
validating a chosen scalar formula.

[Primary point-insertion and recovery basis, Leclercq et al., §2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

Stream identity can matter because E performs a lateral merge or follows
a different discharge process. The corresponding distinction needs a
physical interpretation. A source label by itself is not an explanation
of an additional loss. Likewise, one shared budget still requires lane
availability, minimum travel, conservation and an allocation rule. These
remain ordinary admissibility rules, rather than additional copies of the
same recovery penalty.

## Revised options: what changes the single reading?

**Shared problem.** Determine how actual traffic passage changes the one
shared service ceiling, and how that ceiling recovers. Both candidates keep
the point, physical A/E queues, existing priority and choke-line completion.
The unresolved part is the update law and its sufficient predicted state.

### M1: a shared meter driven by a representative E response

This is the existing exact conditional candidate, formerly Option 1. Each
unit of admitted E leaves the same assumed recovery profile; recent losses
add to one shared restriction. A consumes current service and can queue,
but adds no separate recovery burden. Actual entry speed does not change
the assumed profile within this member.

- **Pros:** complete equations and analytical conservation, storage,
  uniqueness and clearance support; limited change to the stack and a
  clear reference for the more general question.
- **Cons:** the fixed E response and additive combination may miss the
  state and speed dependencies in your picture. It cannot explain an
  independent slow-A recovery effect.
- **Scientific consequence:** a usable conditional reference with explicit
  assumptions. Its proofs apply to this law; it is still unapproved as the
  primary successor.

### M2: a shared meter driven by the traffic actually being discharged

This makes your physical picture a more concrete qualification target for
the earlier Option 2. The size and persistence of a new restriction should
have a supported relationship to admitted mass, relevant crossing/insertion
speed and recovery conditions. A and E feed the same service account;
an A contribution is included only for a separately identified additional
mechanism. Overlap may be combined through retained aggregate state/history;
there is no requirement for a separate constraint per entry.

This is a **proposed modeling direction**, not a completed alternative law.
It does not yet establish the speed map, the combination rule, or whether
a scalar state suffices. A fixed response could survive in a restricted
regime if those dependencies can be defensibly neglected.

- **Pros:** directly asks what physically changes the meter, and avoids
  treating every E admission as the same event regardless of its kinematics.
  It can encompass a justified A-discharge effect through the same interface.
- **Cons:** the necessary speed and recovery closure is unresolved. A
  self-reinforcing queue penalty or a same-time circular update would need
  to be ruled out. Additional retained state may be necessary, and M1's
  analytical guarantees do not transfer automatically.
- **Scientific consequence:** further bounded G3 qualification is required
  before exact-law acceptance. No new spatial model, observation privilege
  or expanded objective is approved by choosing this direction.

### Straight comparison in one traffic episode

An E burst enters slowly, A builds a queue, E stops arriving, and A continues
to discharge while the disturbance recovers.

| Aspect | M1: representative E response | M2: discharge-dependent response |
|---|---|---|
| **Number of shared service readings** | One. | One. |
| **What lowers it?** | The amount/timing of admitted E with a common assumed response. | A qualified relation to actual admitted traffic and its relevant kinematics. |
| **What does slow A discharge do?** | Uses the remaining service; adds no new recovery burden. | May add a justified extra effect; queue-induced slowness is not automatically a second loss. |
| **What happens after E stops?** | Recent E influences continue fading; A queues drain as service allows. | Recovery follows the eventual qualified state rule, including any independently justified continuing influence. No quantitative law is supplied yet. |
| **Does one reading imply one state?** | No: the exact candidate uses recent admission history. | No: sufficient temporal state remains a review question. |
| **What is established now?** | A complete conditional mathematical member. | A clearer physical target and interface, without a completed law or higher-fidelity result. |

**Updated provisional recommendation: qualify M2 as the primary direction,
with M1 retained as the exact conditional reference.** This updates the
previous recommendation of Option 1. The reason is that the model you now
describe asks for discharge- and speed-dependent service, beyond merely
retaining a typical E restriction. Its common meter is already compatible
with M1; the stronger update semantics are the reason to examine M2.

This recommendation does **not** adopt an A-queue capacity penalty or promise
one-state sufficiency. Those are the main issues to resolve within the same
gate. If the intended requirement is only a single shared ceiling, M1 already
meets it and that alone gives no reason to replace its update.

## Current decision and scope

**CP-D2 remains open, Type 2 under G3.** It now asks whether to keep M1's
representative update as the primary conditional law or qualify the clarified
M2 update using actual predicted boundary kinematics. A new independent
A-discharge effect is proposed for assessment, not approved by CP-D1's
E-driven P-H selection. S3-M1 and S3-M2 remain closed.

Dependent work must clarify speed meaning, recovery memory, an A contribution
versus double counting, and causal service/allocation. These belong to the
same terminal-law question, not new roadmap stages. Unknown initial memory
would reopen G2; loss of H1 handoff protection would reopen its G3 interface;
a widened objective would reopen G4/S3-M2. None is adopted here.

The response stops at this refined methodological choice. No revised equations,
calibration, proof transfer, simulation or implementation is performed. The
terminal amendment and full Step 3 remain open.

[Viewed-reference recheck and reading limits](../../extraction/research_readiness/vsl_ph_source_and_adaptation_audit.md#feedback-5-recheck-one-shared-service-budget)

[Work and documentary verification](vsl_feedback5_work_report.md)
