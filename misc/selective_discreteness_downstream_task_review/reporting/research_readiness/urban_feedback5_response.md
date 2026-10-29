# Strong aggregate information and a local explanation of sensitivity

26 October 2026. Response to feedback 5. The checkpoint **“Comparison, sensitivity and scientific credit: agreement on principles”** can close on the meanings below. This settles the principles, without claiming that the concrete information projection, traffic laws or derivatives have been completed.

Follow-up clarification, 26 October: original fine-grained time-series access is allowed through a model's declared conversion to macro state. Observation updates do not make a rival illegitimate or non-macro. The [clarification response](urban_macro_time_series_clarification.md) corrects the overly restrictive reading of the earlier test distinction; the live paragraphs below and mathematical companion are synchronized.

Your comparison proposal supplies the organizing principle that my earlier candidates lacked: define the strongest allowed aggregate information first, then assess concrete rivals within that boundary. Your sensitivity proposal also supplies the right explanatory order: establish what a service change does at one timestep, then follow those state changes into complete total system time (TST). Both source-credit approaches are now agreed.

## Give aggregate models every allowed aggregate advantage

I adopt your proposal as **Candidate C: a common maximum aggregate information boundary**. Rivals may access the original fine-grained series through a declared method that omits fine detail or converts it into macro state. Physically defined lane/bay masses, movement totals, aggregate queue measures/speeds and model-defined aggregate estimates may use that record and its history. A native model may use a subset. Its conversion and retained representation are part of the method being compared; it need not receive only a preselected common projection.

This is stronger as a comparison principle because it separates two questions: what information an aggregate predictor is allowed, and what a particular model can actually exploit. Failure of one chosen model is weaker evidence than failure inherent in the information boundary itself. Conversely, a credible aggregate model that reproduces the relevant effects and sensitivities would weaken the case for retaining additional order in that regime.

The old candidates now have supporting roles. Candidate A describes how to compare actual rivals, with their declared subsets of the allowed information. Candidate B seeks a clean witness to an information limit: two admissible traffic situations with identical complete allowed aggregate records but different relevant responses. Neither replaces your proposed boundary.

One example makes the distinction clear. Suppose two queues have the same bay mass, adjacent-lane mass and every other admitted aggregate observation. A turner can reach the opening in one queue but is obstructed in the other. If the allowed histories also fail to distinguish them, any predictor using only that record must give the same prediction for both. A sufficiently large reference-response difference then establishes a limit independent of the chosen aggregate equation. We have **not yet constructed such a pair** under the full proposed observation boundary; matching just two mass totals would not establish it.

“Aggregate” therefore needs a declared representation, resolution and retained memory. Reading original records to construct macro quantities or estimate blockage is allowed. If a successful macro summary recovers the relevant effect, acknowledge it rather than prohibit the inference. A method that also retains an exact packet-order ledger must disclose that mesoscopic memory; the scalar form of its final output alone does not establish an order-free representation. The actual aggregation/history rules belong in the concrete model definition.

One-step tests, macro-state updates from an observation series and forecasts without later observation updates are all legitimate comparison setups. They establish different predictive capabilities. The earlier wording incorrectly suggested that every legitimate TST comparison had to use the last setup. The input source does not determine model resolution. Record the macro conversion and observation schedule, and distinguish retrospective/updated-state evaluation from a forecast made before later outcomes were observed. For a new-allocation response, also state what data are held fixed and how changing future traffic states are accounted for.

An information-limit bound is conditional on the declared retained record. Equality under one common aggregation does not rule out another legitimate macro summary of the original series. A universal claim would need the corresponding equality across the admitted representation class; that has not been established here.

### What the literature already establishes

The broad claim that macro models cannot handle blockage needs correction. Liu and Chang's lane-group formulation explicitly represents queue interactions and lane blockage; Wright and colleagues' macroscopic node model supplies a partial-FIFO mechanism for localized restrictions. These are already relevant aggregate alternatives in the accepted review. [Liu and Chang, author-hosted paper](https://attap.umd.edu/wp-content/uploads/2022/05/TRC522.pdf), [Wright et al., primary preprint](https://arxiv.org/abs/1601.01054v3).

These sources do not establish that an aggregate rival matches the exact order-conditioned responses or useful gradients required here. The defensible open hypothesis is narrower: **does retained order improve those predictions and control responses beyond the strongest declared aggregate information, especially in the access-sensitive cases?** An expectation of success remains a hypothesis, not evidence of a universal aggregate limitation.

Matching B3 at one service allocation would also be insufficient. The comparison concerns nearby service responses and complete TST, and the richer reference must check whether the shared prediction is credible. B3 itself is not the ground truth.

## Start with what happens when the service knob moves

I agree with your local-first ladder. My earlier use of “trajectory” meant the sequence of whole-system traffic states, not separate packet paths whose trip gradients must be computed and summed. That wording, and leading with terminal treatment, obscured the actual traffic question. The explanation will now begin with the one-step causal response.

I read “make the cycle longer on this leg” as **increase that group's effective-service fraction while compensating elsewhere in the fixed budget**. Absolute cycle length remains outside the present average-service task. The desired derivative describes the change in discharge, queue/state or TST caused by that feasible service reallocation.

At a given starting state, the model must explain who can reach service, which demand/service/receiving constraint binds, how much leaves, and what state is left for the next step. Merely having a queue does not imply a small response: a reachable queue with adequate downstream room can use extra service fully. A downstream jam or inaccessible bay can instead make the current movement response zero.

| Physical situation at the start of a step | What more service can do |
|---|---|
| Turners are ready, downstream room is available, and their service allowance binds | Increase current left-turn discharge, subject to the chosen lane-resource law |
| The bay opening is inaccessible to waiting turners | Extra left service may have no current use; through service may change the obstruction and later access |
| Downstream receiving is the binding restriction | Extra service may leave current discharge unchanged |

These are conditional mechanisms, not newly selected access equations or executed fixtures.

Three related sensitivities must remain distinct:

| Question | What changes and what is held fixed? |
|---|---|
| **What would changing service now do?** | Hold the starting traffic state fixed; inspect current discharge and the resulting next state. |
| **What would changing service last step have done to this step?** | Change the previous transition, carry its altered state into this step, and inspect the resulting response. |
| **What does changing the fixed allocation do to complete TST?** | Apply the changed allocation throughout its declared control window and propagate all resulting state changes through completion. |

The second question is the bridge to the third. In the bay example, extra through discharge can alter the next available access state; that can admit turners later and change upstream/source waiting. The derivative over time is obtained by composing those local responses. It does not require differentiating individual physical trajectories, and it cannot be obtained by summing current-step responses while resetting each future state to its original value.

### Why a one-step TST response can be zero

There is one accounting detail worth making explicit. Under the inherited left-interval convention, this step's TST charge uses source plus network mass at the start of the interval. With that state fixed, changing service does not change a time charge already determined by it. Discharge and the **next** state can nevertheless respond, changing later time charges. An internal transfer also moves traffic within the system rather than immediately completing its trip.

Thus a zero direct derivative of the current TST charge does not establish an unhelpful control gradient. Discharge, queue and next-state responses explain the local mechanism; complete TST remains the primary control objective. Replacing it with immediate discharge would be a different objective and is not proposed. The existing [objective convention](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_0_ltm_baseline.md#L649) and [macro implementation](../../../../context_snapshots/diff_minimal_meso/src/diff_minimal_meso/objectives.py#L22) make this distinction explicit.

### What still has to follow the local calculation

The selected local laws must carry continuous responses through allocation shares, admissions, residual order, storage and receiving, including a valid zero response when another constraint binds. Changes of active constraints or traffic fronts need separate boundary treatment; the local-first approach does not make every derivative smooth.

Over time, the same state account includes source waiting, moving mass and queues through completion. The existing D2 default uses a common fixed clearance continuation after the control/inflow window. Earlier state sensitivities survive that handoff even though the continuation is read as independent of the candidate allocation. A common sufficiently long horizon and a completion-based calculation remain possible treatments of the same complete objective. **Feedback 5 selects the local-to-system explanation; it does not select one numerical horizon/endpoint treatment.** Those details can be specified with the concrete model, without another broad principle discussion now.

The mathematical companion defines the three sensitivities, the aggregate-information limit and the complete state-response calculation. It states the assumptions and does not supply a missing urban traffic law.

[Mathematical explanation: information limits and local-to-system sensitivity](urban_feedback5_information_and_sensitivity.pdf)

[Retained LaTeX source](urban_feedback5_information_and_sensitivity.tex)

## Scientific credit and the current conclusion

Your agreement selects both reporting approaches: explain the mechanism and source/adaptation beside each component, supported by a complete equation/source map. This is an agreed presentation principle. Exact credit still depends on the selected equations; the VSL report remains a useful example.

The three current principles can therefore be recorded as agreed:

- **Comparison:** define a common maximum aggregate information boundary that removes the packet-order distinction; individual rivals may use subsets. Judge sufficiency honestly if aggregate information can reproduce the relevant response.
- **Sensitivity:** explain and derive the one-step traffic response first, then compose its state effects to obtain the complete TST response to the declared service allocation.
- **Credit:** combine adjacent causal/source explanation with a complete supporting source map.

The concrete comparison must still specify each model's aggregation/retained history and observation schedule. Raw time-series access through that boundary is permitted, including observation-updated macro models. The concrete traffic model still needs access, service and local responses. Margins, numerical horizon treatment and useful-gradient evidence remain open. These are concrete scientific questions, not reasons to repeat the settled principles.

[Current agreed decisions](../../temp_content/research_readiness/review_decisions.md)

[Work record, source scope and verification](urban_feedback5_work_report.md)
