# S10 claim–evidence sufficiency matrix

Date: 2026-09-29. Scope: static audit of the approved S08 future protocol and
the previously reviewed action/gradient chain. No experiment or new traffic model.

| Claim/product | Proposed evidence | What a valid positive result would support | Remaining limitation | Static verdict |
|---|---|---|---|---|
| Reachable preparation | Empty start, fixed intended demand, safe road-start insertion, retained insertion delay and native motion | The tested preparations are generated without forced relocation, discarded demand or post-entry lane commands | Provider-specific feasibility and realized insertion queues remain empirical | Contract adequate; future readiness required |
| Exact declared information collision | Complete declared lane-blind history; elementwise equality; same known future inputs; two time steps | Existence of a pair indistinguishable through the declared sampled channel in the frozen synthetic domain | Not equality for every conceivable sensor, continuous time or controller that knows past lane assignments | Adequate for the bounded declared-channel claim |
| Hidden-state contrast | Different final-400 m three-lane occupancy plus retained gaps/leaders/lane-change audit | The exact-match pair contains omitted lane-resolved state | Occupancy is a selection marker; gaps, order and lane-change memory also differ and causality is not isolated | Adequate for a hidden-state bundle, not occupancy sufficiency |
| Outcome-blind discovery | Complete 15-pair registry per time and dual-step intersection before selection | Avoids selecting preparations because their later actions look favorable | Small frozen bank can miss other cases; failure is preparation-specific | Methodologically sound and deliberately bounded |
| Negative prefix result | Pre-registered labels for no exact pair, zero contrast, step instability or invalidity | Identifies why this bank did not supply the required pair | Does not establish aggregate sufficiency, generic observability or impossibility | Interpretation adequately bounded |
| Information-to-decision distinction | Future common-action evaluation with all intended vehicles, source waiting and common-action regret | A bounded finite-menu distinction if acceptable-action sets are disjoint and no tested common action is acceptable | Current action stage is not approved/frozen; held-100 omission remains; finite open-loop probes cannot prove continuous/feedback-policy failure | Incomplete beyond prefix feasibility |
| Causal role of lane information | Compare outcomes for an exact lane-blind match with hidden differences | Shows the omitted hidden-state bundle has decision relevance in that case | Does not identify which hidden coordinate is necessary or sufficient; preparation changes gaps/order as well as occupancy | Requires later ablation/compression study |
| Minimum refinement | Candidate statistics such as ending-lane mass/location and continuing-lane balance | At most motivates candidates after positive decision evidence | No sufficiency, necessity or compression-failure test is currently specified | Not formulated as an accepted experiment |
| Internal gradient correctness | Differentiable candidate plus float64 AD/JVP versus central finite differences away from boundaries | Numerical derivative correctness for the candidate model in fixed regimes | No candidate lane/merge closure or freeway gradient implementation exists | General method known; task-specific product absent |
| Gradient fidelity/usefulness | Compare macro/refined directions and evaluate small perturbations in an independent richer reference | Whether retained information improves prediction of useful downstream changes | A prefix match or finite action ranking is not derivative evidence; cross-fidelity perturbation and held-out tests remain future work | Not supported by S08 or the action diagnostic |

## Interpretation rules

1. Past lane-entry assignments are disclosed preparation differences but hidden
   from the declared controller channel. A positive pair therefore establishes
   information loss only for that observer/input boundary; it is also an
   unknown-input example if another controller would know those assignments.
2. Equality at both 0.5 s and 0.25 s strengthens numerical robustness but is not
   a continuous-time observability theorem.
3. Exact-pair failure is a failure of this construction, not proof that a strong
   aggregate history always recovers lane state.
4. A positive pair precedes decision evidence. Different forward trajectories or
   a two-action ranking reversal are insufficient if another common action works.
5. A decision distinction precedes representation and gradient claims. It does
   not by itself select lane occupancy, order, gaps or response class as the
   smallest retained state.

## Product-level conclusion

S08 is a complete and defensible **future prefix-feasibility protocol** for one
bounded declared-channel claim. It is not a complete information-to-decision
experiment, minimum-state study or gradient study. The current methodology review
can close honestly with those staged obligations. Additional analytical work
would be a new conditional model study, not completion of a missing clerical
detail in S08.
