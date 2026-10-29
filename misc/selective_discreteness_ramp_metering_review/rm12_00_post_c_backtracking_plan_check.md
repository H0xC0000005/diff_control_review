# Post-C backtracking check and proposed next-review sequence

Date: 2026-10-06. **Planning discussion revised; recommendations provisional.**
RM11 is [closed by the user's acceptance](reporting/rm11/c0_user_closure.md).
The RM12 label reserves a successor planning record; no substantive successor
review or changed scientific contract is approved by writing this check.
The user subsequently challenged R's breadth, then the assumed fixed recovery
backtracking position. The [four-position comparison](rm12_20_backtracking_point_comparison.md)
is now the current selection proposal. The
[bounded recovery proposal](rm12_10_bounded_next_step_proposal.md) remains
conditional BP-M material; R is an unselected umbrella direction.

## 1. Earlier alternatives and their actual decision status

The common agreement is method-first selection, genuine task evidence, minimal
necessary changes, strong fair competitors, full available history and complete
population accounting. It is not an agreement to execute every alternative in
sequence. RM9–RM11 are closed scoped reviews, not failed implementations.

| Direction | What backtracking changes | Actual prior status / current implication |
|---|---|---|
| R: representation and gradient fidelity | Replace necessity under an ideal full-history controller with the value of explicitly declared model reductions relative to a richer reference | Discussed in RM11, unselected. Preserves rate control and TST; explicitly changes the strong irreducibility claim. Umbrella direction, not a sufficiently bounded immediate stage |
| T: gap-aware release timing | Revisit the rate/fixed-release-shape actuator to time releases relative to usable gaps; review sensing/safety separately | Discussed in RM11, unselected. Direct source lead, but neither a matched-information benefit nor useful gradients are established |
| Earlier RM9-UG5.B: genuine incomplete initialization | Keep the existing laws/strong observer and look for a justified initial knowledge epoch whose entire available history leaves ambiguity | Unselected; user deprioritized depth-first pursuit. A bounded source/domain check could become relevant if the strict information claim is retained; no automatic reopening |

The older RM7 coordinated **multi-ramp candidate C** is different from the now
closed finite-lane C. It remains a possible extension **after a positive local
result**, with separate approval. That prerequisite has not been met. Feedback
gain optimization/PID and MPC were also discussed earlier, but changing to them
alone supplies no hidden-information certificate and they are not selected as
the next rescue task. The older downstream route-access alternative is unselected;
it would change task geometry/objective attribution and needs its own proposal.
Parking the line remains possible, without treating the core question as answered
positively.

Decision lineage: [RM7 task selection](reporting/rm7_20_method_first_task_formulation_and_gate.md),
[post-selection designs](synthesis/rm7_post_selection_design_inventory.md),
[RM9 B limits](reporting/rm9_71_candidate_b_purpose_and_limits.md), and
[RM11 C/T/R comparison](rm11_00_post_a_direction_check_proposal.md).

## 2. Does a shared contract explain the repeated negative admissions?

**Reviewer inference: the hypothesis is supported for several conditional
domains, but not proved for the whole local ramp task.** Three passes share
contracts and source families; they are not independent samples establishing
a universal failure probability. RM9 contains genuine conditional identification
results. RM10/RM11 add both simpler-model sufficiency checks and richer-family
evidence gaps. Repeating an unestablished obligation is not proof it is impossible.

### Evidence supporting the hypothesis

1. **The information target is stronger than “a macro representation discards
   useful detail.”** The inherited contract asks whether the detail remains
   unresolved even after strong mass/flow/speed/ramp observations, all available
   history and public dynamics. In RM9, exact mass plus the admitted equilibrium
   speed often identifies lane split within a known FD branch. Known initial
   modes or completely observed homogeneous states similarly undermine some A
   hidden-state proposals; appropriate spatial inventories undermine some C
   whole-zone position examples. These are restricted results, not global ones.
2. **Complete physical initialization can exclude the desired information
   advantage regardless of added physics.** With exact deterministic public
   laws/inputs, knowing the complete physical state fixes future action responses.
   Adding recovery or geometry cannot make that known state unknown. Crucially,
   this is not a theorem about knowing only initial aggregate statistics, and
   complete fine knowledge was not proved to hold in every possible source task.
3. **Hidden detail and useful rate leverage are different requirements.** Even
   when local interaction detail survives a snapshot, a coarse rate schedule
   may not exploit it. Under common arrivals and complete TST, metering that only
   changes queue location without changing cumulative exits cannot improve TST.
   A continuously busy, fixed-service isolated bottleneck is an important
   conditional example; all ramp tasks are not assumed to have that property.
   The public source context similarly distinguishes capacity/discharge effects
   from preventing downstream exit obstruction. [RM0001, Introduction and Section 4](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/80J_Gomes_TRC06.pdf)

Together these contracts can leave a narrow admissible set: extra physical detail
must be genuinely unresolved *and* change useful common rate actions. This
explains why another mechanism alone is a poor next search strategy. It does not
identify rate control, determinism, TST or CTM individually as universally invalid.

### Evidence against a blanket systematic-impossibility conclusion

- Aggregate-only initialization is outside the complete-state theorem. RM9
  retains possible mixed/congested snapshot roots; their persistence and action
  relevance are unresolved. Determinism does not itself identify an unknown
  initial state.
- Richer physics can affect genuine control behavior. A capacity-drop-aware
  CTM control study reports differences from a controller neglecting that
  mechanism; this is evidence of model adequacy/control relevance, not of
  irreducible hidden information or our gradient claim.
  [RM0003, original paper](https://arxiv.org/pdf/2106.10347)
- The reviewed analytical merge study distinguishes good mean-capacity
  approximation from heterogeneous transient flow dynamics (Section 5,
  Figure 5). This leaves representation-fidelity questions worth examining,
  although its differing flow histories do not establish the old matched-history
  claim. [S12A005, author manuscript](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)
- The inspected gap-metering task directly connects detected opportunities to
  release decisions, but changes sensing and timing. It supports a T planning
  lead, not a theorem defeating the known-state result or a clean matched
  information experiment. [RM8-P02, control concept and detector specification](https://repository.tudelft.nl/file/File_c446bd9b-9a19-494b-9989-3d11f96fbb1a)

The negative findings therefore diagnose **claim/information and actuator/task
contracts**, not a prohibition on freeway control research. Modeling physics
poorly can still damage predictions or sensitivities even when detailed state
is known or reconstructible in principle. A reconstructible coordinate need
not be faithfully represented by a chosen reduced law.

The strength of those diagnoses differs: conditional information sufficiency is
established in restricted domains; inadequacy of the current rate actuator is
only a hypothesis to check. “Open-loop rate” does not itself imply coarse timing.
Its temporal resolution and operational meter mapping were not fully frozen.
A sufficiently resolved rate parameterization might encode some release patterns;
the actual boundary must be audited before declaring T a necessary actuator change.

## 3. Where to backtrack

The **RM7/RM8 research-claim and information contracts** explain important
shared restrictions; another RM9 allocator tweak or added geometry does not
automatically repair them. The initial recommendation was to adopt a claim
direction first, with R as the smallest discussed change retaining rate/TST.
The user correctly observes that this still names an overall objective rather
than a finite review obligation. No claim direction was adopted.

The first revision recommended a **bounded local discharge-recovery
task/control audit**: determine whether source-supported rate actions can alter
exit timing beneficially after all-stream waiting and clearance are counted.
This uses the physical recovery lead already reviewed in RM10, without repeating
its closed hidden-history admission question. It requires neither a hidden-state
construction nor adoption of R. Its output and stops are in the
[new proposal](rm12_10_bounded_next_step_proposal.md).

The later user question correctly identifies that this still assumes a
backtracking position. The current comparison examines physical service,
operational information, actuator mapping and claim/comparator positions before
selecting one. It provisionally favors the information-contract admission audit
if the strict hidden-information question remains the priority. Physical recovery
has no demonstrated immunity to the strongest information obstruction.

If that task survives, decide whether the later contribution requires irreducible
missing information under ideal history access or preservation of physical detail
in declared model reductions. R changes what must be proved; that remains an
explicit decision before a representation comparison.

If strict information necessity remains the aim, first find an independently
supported operational initialization/measurement contract and retain every
available observation. That is related to B's domain issue, not a license to
delete detectors, history or public inputs. It need not reopen a long current-law
classification campaign. Failure to ground the domain should stop that route.

Next, if genuine detail exists but rate actions cannot exploit it, backtrack to
the **RMD-G1 rate/fixed-release-shape boundary** and review T. Finer release
timing, sensing, safety and information effects must be separated. T is not an
automatic cure for ideal full-state sufficiency. Feedback or more ramps alone
do not repair either obstruction.

Keep finite receiving/conservation, fair common actions within each comparison,
strong relevant rivals, and complete waiting/clearance accounting. Do not lower
the metric or degrade a baseline to obtain a positive result. No claim is made
that selectively retained lane metadata rather than a compact aggregate state
must win under R.

## 4. Earlier decomposition — conditional on selecting BP-M

1. **Admit the rate-control/discharge-recovery task.** Review one local source
   family, its conservative finite-queue transfer and an all-stream exit-time/TST
   comparison of common feasible rate actions. Output one concrete admission,
   scoped rejection or methodological gate. This is BP-M's possible first pass.
2. **Test the relevant dynamic reduction.** For an admitted task, compare a
   credible compact recovery/memory closure with the local state implicated by
   its transient response. Explicitly select the representation-fidelity or
   strict-information claim before this checkpoint; compact sufficiency is valid.
3. **Specify sensitivity and validation obligations.** Only for a consequential
   surviving representation difference, define gradient/event semantics,
   ablations, derivative correctness and independent one-step usefulness checks.
   Review planning does not perform experiments or implementation.

Checkpoints 2–3 are conditional. The first checkpoint does not answer the full
research question or adopt R. If an actuator change becomes necessary, stop for
a concrete T decision. There is no automatic R → T → multi-ramp progression or
promise of positivity. The earlier four-step recommendation is preserved in the
dated dialogue/validation record as planning history, superseded by this revision.
The current four-position comparison precedes this decomposition; no fixed
recovery-first backtracking point is selected.

## Planning ownership and approval status

This record supplies the backtracking context. The current four-position proposal
records alternatives, stable question IDs, evidence ownership, dependencies and
bounded outputs. The recovery proposal is conditional material. Target selection, claim/knowledge
changes, actuator changes and physical-law adoption are Type 2/user decisions.
Source transcription and static accounting checks are Type 1 work once authorized;
they may not silently adopt a changed law. R/T/B execution and changed contracts
remain unapproved. The current authorized planning revision is complete.
