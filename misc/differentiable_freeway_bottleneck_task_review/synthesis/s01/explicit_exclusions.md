# Explicit exclusions and boundary effects

- **F2 coordinated ramp metering:** stopped as the primary resolution task. It
  remains a possible operational comparator only if a later selected task needs
  one; that is not authorized here.
- **F3 joint VSL plus ramp control:** not used to rescue either candidate. It
  confounds action-family complementarity with representation value.
- **F5 cooperative lane-change/merge control:** excluded because lane commands,
  merge priorities, and discrete maneuvers change the action. FB0004/FB0010 are
  used only to motivate or bound lane-state effects.
- **Vehicle-specific CAV speed commands/moving actuators:** excluded from the
  primary F1 definition; their feasibility and response semantics differ from
  infrastructure speed advice.
- **Closure design:** lane, location, start, end, and reopening are exogenous;
  no closure scheduling or topology optimization.
- **Routing, diversion, RL, and generic incident management:** excluded.
- **Exact vehicle order/gaps:** not admitted into B2 by default. Their addition
  would require a demonstrated B2 failure and a new minimum-state decision.
- **Discrete display-sign optimization:** excluded from differentiation; any
  display quantization is a post-optimization sensitivity.
- **Safety claim:** speed variation or surrogate metrics may be guardrails, but
  N1 does not authorize a crash-risk or microscopic safety model claim.
- **Single-site implementation novelty:** insufficient. The prospective claim
  must be about resolution-dependent forward and gradient usefulness.
- **Control-dependent discrete probability shifts and saltation-requiring
  hybrid dynamics:** avoided by default in the differentiable candidate under
  the user's Gap 7 clarification. They require evidence that no adequate
  continuous/deterministic alternative exists, explicit reopening and approval
  of the derivative contract, and dedicated gradient-fidelity work under the
  relevant shifts/events. This restriction does not exclude continuous traffic
  mass transfer, deterministic constraint kinks, or exogenous fixed scenarios.

No distinct third candidate met the admission rule.
