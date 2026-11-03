# Zhang task fit: the common controller fits; the aggregate predictor needs a terminal choice

**Scope choice resolved by the user:** verify the matched B pair first;
A is explicitly deferred. The first-verification specification is now
consolidated at its review checkpoint. Later A selection must respect
source assumptions/backbone and intended behavior, and may prefer a simpler
established method. The earlier alternatives below are historical.

[Current B-first specification](vsl_b_pair_elementary_verification_specification.md)

2026-11-02. **The authorized task-fit review has reached a methodological
stop.** The common B controller is specified and analytically eligible under
the declared task adaptations. The separate aggregate reference A is not
yet qualified at the choke. No source model, experiment or implementation
is adopted by these findings.

**The remaining difficulty belongs to A's traffic prediction, not to the
identity of B0 and B-gradient.** Both B versions can issue exactly the same
advice and use the same complete objective. A's capacity-drop mechanism,
however, requires a density-bearing bottleneck cell. Our physical task
finishes at a free outlet at the lane drop. Reusing that cell at this boundary
needs an explicit modeling interpretation.

I recommend retaining the matched B pair for the first elementary
verification and leaving A for a subsequent, focused qualification.
That changes the first comparison's coverage and is a user choice, not
an automatic deletion of a previously requested benchmark.

## What is now precise for the common controller

Zhang et al. represent candidate control through segment speed settings
and evaluate their simulated performance; their separate CTM branch uses
enumeration. We borrow the speed-setting design rather than the whole
published microscopic/CTM study.
[Source, Section 3.2 and Section 4.3](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=12)

For our first task, B has one continuous parameter: the common advised
speed. Choose it separately for each initialized case, apply it to all
modeled road rows and lanes, and hold it for the entire episode. Both
versions use the same allowed interval, currently 30–60 km/h.

| Element | Qualified common specification |
|---|---|
| **Advice map** | The parameter is the issued speed everywhere throughout the episode. No state-dependent branch or source-specific spatial profile is added to either version. |
| **Forward dynamics** | The same selected Subraveti/Han/Carey-led lane-cell plant in both versions. No second traffic model is imported for B-gradient. |
| **Initial condition** | The same full continuous cohort, initialized independently of advice; no later arrivals. Each query resets it. |
| **Objective** | The same complete remaining-population TST, including the exact residual. |
| **Optimizer access** | B0 receives costs. B-gradient additionally receives the qualified complete derivative. Neither receives raw lane arrays as controller features. |
| **Execution identity** | At the same speed parameter, the advice, forward trajectory and TST are identical by construction. Different final tuned parameters are an intended optimization outcome. |

The shared adaptation replaces the source's spatial/discrete settings and
its boundary constraints with this task's common continuous advice. It is
not claimed to be a feasible subset of every source constraint. The source
objective and demand setting are also replaced identically in both arms.
These changes do not establish source-performance transfer; they define
one adapted controller consistently.

The advice map itself is differentiable. Gradient compatibility then
depends on the target plant and objective, rather than on differentiating
a source enumeration or genetic algorithm. The existing analytical review
already supplies the complete derivative on regular advice intervals.
Consequently the common continuous controller can support the proposed
gradient extension without borrowing another controller.

[Existing complete objective and derivative, Section 7](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Existing regularity analysis, Section 3](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf)

This closes the specification-level B task-fit question under its declared
adaptations. Numerical AD correctness, useful directions, optimization
advantage and physical fidelity remain future evidence. Maximum-advice
optima and a zero gradient benefit remain valid outcomes.

## What can already be matched for aggregate reference A

The intended A is a separate published aggregate traffic predictor plus
speed selection. It does not become the evaluator used inside B0.

Three task adaptations are straightforward to define without changing its
traffic law:

- Initialize each upstream aggregate cell with the sum of the three physical
  lane stocks at that row. If its API uses per-lane density, divide by that
  row's length and lane count. This preserves physical traffic quantity.
- Set subsequent external inflow to zero. Retain the same physical road
  locations, positive advice interval and prescribed initial cohort.
- Define the target score as complete time before crossing our choke line.
  Replacing a finite-period performance criterion is a declared objective
  adaptation, not an assertion that the criteria are equivalent.

The X/Z diagnostic states have the same row sums, so this projection gives
A identical initial inputs for them. A deterministic predictor and tie rule
would therefore choose the same advice from those inputs. B0 may nevertheless
distinguish cases through fine-simulator costs. That is why A versus B0
is a predictor/query-access comparison, while the matched B pair concerns
derivative-enabled tuning.

Defining the correct score does not yet make A's evaluation complete.
Its clearance and residual-time argument must follow its own settled
update/boundaries. The fine plant's exact residual cannot simply be copied.

## The choke is a traffic-model question, not an indexing convention

Zhang's CTM assigns a special capacity-drop rule to a bottleneck cell,
activated by that cell's density. It also distinguishes VSL cells from
the bottleneck cell.
[Source, Section 4.3 and Figure 14](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf#page=20)

To check whether this was merely omitted notation, I followed the paper's
cited FD source. Hadiuzzaman and Qiu explicitly distinguish the upstream
discharge region from a finite bottleneck region; equations (3)–(4) use
the bottleneck's own density for its demand/supply.
[Author-uploaded primary paper, Section 4.2](https://www.researchgate.net/publication/263387345_Cell_transmission_model_based_variable_speed_limit_control_for_freeways)

This is source tracing for A's existing law, not another controller or
a new component added to the selected stack. Delle Monache remains excluded.

Our target instead has three-lane traffic up to the completion line,
two continuing outlets at that line, no physical downstream cells, and
free outlet boundary values. The inspected source does not uniquely
identify which of our states should play the bottleneck-cell role.

Consider a crowded final upstream row while a putative downstream
bottleneck cell is initially empty. A density-triggered rule using the
empty cell need not activate capacity loss at that moment. A rule using
the crowded upstream row may activate it immediately. Replacing one
density with the other is therefore a behavioral choice.

Several seemingly small transcriptions have different consequences:

| Proposed transcription | Why it needs explicit qualification |
|---|---|
| Move the source bottleneck rule onto our final upstream row. | Choose a new location/state for the density trigger and map three-lane storage against two-outlet service. The source has not proved this equivalent to its original bottleneck cell. |
| Retain an extra bottleneck cell beyond the choke as predictor-only state. | Its occupancy can feed back into predicted choke service after traffic has crossed our completion line. Such auxiliary downstream dynamics differ from the target's free outlet and need a declared interpretation. |
| Count traffic until it leaves that extra cell. | Add post-choke time and move the completion boundary, changing the accepted task. |
| Replace the missing cell with a constant outlet capacity. | Remove the state-dependent capacity-drop mechanism that made A a meaningful published congestion predictor. |

Uniform advice also requires specifying its relation to the special
bottleneck rule rather than silently combining two cell types.
No unique complete terminal adapter has been established from the inspected
sources. This does not prove that a compatible A is impossible, or that
the source model is invalid in its native setting. It means A cannot yet
be handed to development as a settled source reproduction or adaptation.

## The decision now needed

The same physical case makes the tradeoff clear: the matched B pair can
already ask whether its fine-model derivative helps choose a speed for
the initialized queue. A would add a second question about advice selected
by an aggregate traffic predictor, whose terminal interpretation remains
unresolved.

| Choice | First result and consequence |
|---|---|
| **Start with the qualified common B pair; keep A pending — recommended.** | Consolidate the elementary verification around the same source-derived controller, complete fine evaluator, value-only tuning and gradient tuning. Maximum advice and strong scalar enumeration remain references. This can test numerical sensitivity and tuning usefulness, but cannot yet claim competence against A or a benefit over aggregate traffic prediction. A remains a later review item, not a completed benchmark. |
| **Require A in the first comparison.** | Continue a focused source-supported terminal-model review before completing the elementary specification/handoff. It preserves the broader published-predictor comparison at the outset, but needs an explicit boundary/state choice and a separate complete-time argument. It does not authorize changing the selected fine plant or inventing an uncredited law. |

My recommendation favors the user's elementary-first aim and retains one
controller in the gradient ablation. It changes the former intention to
check B0 against A before interpreting that broader performance contrast;
that check must remain explicitly deferred if this choice is accepted.

**Stop here for that scope decision.** The current task-fit pass has produced
a positive common-controller result and isolated the remaining A interface.
The elementary verification is not yet consolidated under an assumed choice,
and the private handoff has not been updated. No traffic simulation,
optimization, AD experiment or dependency installation was performed.

[Primary readings and evidence limits](../../extraction/research_readiness/vsl_zhang_task_fit_sources.md)

[Updated active comparison contract](vsl_per_case_matched_controller_contract.md)

[Work and document checks](vsl_zhang_task_fit_work_record.md)

