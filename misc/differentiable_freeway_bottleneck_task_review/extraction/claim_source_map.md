# Claim-to-source map

- **F1 task and B0:** FB0001 directly analyzes VSL at a lane-drop with capacity
  drop using LWR/link-queue models; FB0011 establishes the work-zone lane-closure
  operating context.
- **Compliance without vehicle discreteness:** FB0003 puts compliance/capacity
  effects in a macroscopic VSL model; FB0005 shows compliance mattered in a
  field advisory deployment; FB0007 represents composition uncertainty in an
  extended macroscopic model, although its actuator is direct CAV control.
- **Why test lane groups:** FB0004 directly models lane-changing/VSL coupling at
  a lane drop and evaluates in SUMO. FB0010 shows richer closure behavior but
  bundles vehicle speed harmonization with merge priority; it is boundary
  evidence, not the proposed task.
- **Derivative feasibility versus usefulness:** FB0002 supports VSL gradient
  optimization; SEO2026 supports reverse AD through piecewise LTM updates.
  Neither establishes that a resolution-dependent F1 gradient ranks actions
  better in an independent microscopic evaluator. That separation is the open
  contribution.
- **F2 strong baseline and stop:** RM0024 and RM0025 establish first-order and
  multiclass network discrete adjoints. FB0008 and FB0009 add recent fair
  feedback and data-driven nonlinear MPC comparators. FB0012 supplies storage
  and queue-management constraints. No included E3 source supplies the missing
  decision-relevant lane/order-state failure.
- **Recovery:** FB0006 reports that incident-time effects and post-clearance
  recovery effects can differ, making F4 part of the scenario rather than a
  separate action.

The statements about what the bounded search did not find are search results,
not universal literature claims.
