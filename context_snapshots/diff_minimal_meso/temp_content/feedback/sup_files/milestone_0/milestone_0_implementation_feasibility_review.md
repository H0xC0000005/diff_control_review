# Milestone 0 Supplementary Implementation Feasibility Review

**Status:** Supplementary Phase A/B feedback only  
**Scope:** Implementation provenance and reuse feasibility for Milestone 0  
**Relation to proposal:** This file does **not** modify or supersede `phase_A_proposal.md`. It only supplements the proposal with a rough implementation-source plan.

## 1. Reuse-first policy

Milestone 0 should prefer, in this order:

1. **Direct reuse of an established implementation** when its traffic semantics, numerical convention, differentiation framework, and future extension points match the project.
2. **Port/adapt an established implementation or published algorithm** when the traffic method is established but the available software stack does not fit the project architecture.
3. **Thin local implementation of established mathematics** when the component is too small to justify an external dependency.
4. **Fresh project-specific implementation** only for orchestration, validation utilities, or functionality for which no established implementation exists.

The key rule is:

> Do not invent traffic-model behavior when an established model exists.  
> However, reusing an established algorithm is not the same as blindly adopting an entire external simulator whose architecture would later obstruct the mesoscopic extension.

For every traffic component, the approved implementation plan should identify:

- **scientific source**: the paper/model whose semantics are authoritative;
- **implementation source**: direct software reuse, port/adaptation, or thin local implementation;
- **required modifications**: framework translation, data-layout adaptation, or interface glue;
- **forbidden modifications**: traffic semantics that must remain unchanged;
- **external reference tests**: paper examples and/or executable comparisons;
- **project-specific code**: only the minimum glue that cannot be borrowed.

---

## 2. Whole-stack reuse candidates

### 2.1 UNsim — closest existing differentiable macro stack

UNsim (`toruseo/UNsim`) is currently the closest open-source whole-stack candidate to the Milestone 0 target. It provides:

- Link Transmission Model;
- a general Incremental Node Model;
- JAX-based end-to-end automatic differentiation;
- cumulative-count state;
- dynamic network loading and route-choice infrastructure;
- MIT license.

Therefore, **UNsim must be considered explicitly before implementing the macro stack locally**.

However, direct adoption as the Milestone 0 production core is not currently the preferred choice because:

1. its differentiable implementation is JAX-based while the current proposal is PyTorch-oriented;
2. the repository explicitly labels itself as early development and warns that the AD API may change;
3. its simulator state includes route-choice and other machinery outside Milestone 0;
4. later milestones require a project-specific ordered route-mass ledger and per-lane local interaction zone;
5. adopting UNsim as a whole would make those later extensions depend on its internal state layout and execution model.

**Recommended role of UNsim in Milestone 0:**

- source-level implementation reference;
- executable reference for selected LTM/node cases;
- source for porting an established node algorithm if the chosen semantics match;
- independent comparison target for cumulative-count and node outputs;
- **not** an unmodified required runtime dependency unless Phase B deliberately chooses JAX/UNsim as the long-term project architecture.

If direct UNsim adoption is reconsidered, Phase B should explicitly evaluate whether Milestones 1–3 can be implemented cleanly inside its architecture before committing to it.

### 2.2 UXsim — mature traffic-behavior reference, not the planned differentiable LTM core

UXsim (`toruseo/UXsim`) is a more mature open-source macro/mesoscopic simulator with:

- Newell/X-model traffic propagation;
- Lagrangian Incremental Node Model;
- traffic signals;
- visualization and analysis tools;
- MIT license.

It is useful for:

- independent merge/diverge/node examples;
- scenario construction ideas;
- visualization conventions;
- later behavioral cross-checks.

It is **not** a direct replacement for the proposed cumulative-count differentiable LTM baseline, because its primary simulation representation differs from the planned Milestone 0 architecture.

### 2.3 Recommended whole-stack decision

Current preferred strategy:

> **Use established LTM/node/signal mathematics and existing implementations as references, but own a small PyTorch baseline whose interfaces are deliberately designed for the later ordered-ledger/local-zone extension.**

This is **not** a from-scratch traffic-model design. The scientific components remain borrowed. The project-owned code is mainly a compact framework translation and integration layer.

---

## 3. Component feasibility summary

| Component | Preferred source | Implementation strategy | Fresh traffic semantics? |
|---|---|---|---|
| **0.1 Traffic units + triangular FD** | Newell/Yperman triangular FD | Thin local implementation of established equations | No |
| **0.2 Cumulative-count LTM link** | Newell/Yperman LTM; UNsim as executable/source reference | Port/adapt established algorithm into project interface | No |
| **0.3 Fixed movement-demand projection** | Standard multi-commodity/node formulation | Thin local tensor implementation | No |
| **0.4 Generic first-order node solver** | Tampère generic class + selected established class member; INM is alternative | Port/adapt established published algorithm; avoid ad hoc design | No |
| **0.5 Continuum fixed-time signal service** | Han continuum signal + selected node model's signal/internal constraints | Thin local mapper + adaptation to established node semantics | No |
| **0.6 Deterministic rollout/scheduler** | Standard LTM DNL update order; UNsim as implementation reference | Project-owned orchestration around borrowed components | No traffic-model novelty |
| **0.7 Objective/metrics/gradient harness** | Project validation requirements + PyTorch/pytest | Fresh project utility code using standard AD/numerical tools | Not a traffic-model component |

The node solver is the component where direct algorithmic borrowing is most important. LTM is also an established algorithmic port, but its equations are compact enough that a local implementation is still preferable to an opaque runtime dependency.

---

## 4. Component 0.1 — traffic units and triangular fundamental diagram

### Scientific source

Use the standard triangular fundamental diagram/Newell/LTM definitions for:

- free-flow speed;
- backward-wave speed;
- jam density;
- critical density;
- capacity;
- jam storage;
- free-flow travel time;
- backward-wave travel time.

### Recommended implementation

**Thin local implementation of established mathematics.**

A validated immutable parameter record plus algebraic derivations is enough. Importing an external traffic package solely for this component would create more dependency surface than useful reuse.

UNsim may be inspected as an executable/source reference for parameter relations, but its exact parameterization should not silently override the approved formulation.

### Modifications allowed

- datatype/container adaptation;
- explicit units;
- validation checks;
- conversion to the selected tensor framework.

### Modifications not allowed

- alternative fundamental diagram;
- silent capacity/wave-speed approximations;
- unapproved delay rounding semantics.

### Differentiability

In Milestone 0 these quantities are structural constants. No special gradient implementation is needed.

---

## 5. Component 0.2 — cumulative-count LTM link

### Scientific source

Use the standard Newell/Yperman cumulative-count LTM formulation as the authoritative traffic model.

### Recommended implementation

**Port/adapt the established LTM algorithm into the project's own PyTorch interface.**

Do not invent a different link-propagation model.

Direct import of UNsim's LTM internals is not preferred initially because:

- it is JAX-native;
- link state is embedded in a larger simulator data model;
- its delay/interpolation convention may not match the approved Milestone 0 convention;
- later local-zone coupling requires a stable project-owned link-boundary API.

### What to borrow from existing implementations

Inspect UNsim for:

- cumulative-history organization;
- sending/receiving computation;
- delay-offset handling;
- boundary initialization;
- AD-safe immutable/update patterns;
- relevant tests.

### External correctness strategy

Use all three:

1. hand-computed pulse/storage cases;
2. equation-level comparison with the source literature;
3. executable comparison with UNsim where numerical conventions can be matched.

UNsim should be a reference, not the sole oracle, because its current repository explicitly labels the AD implementation early-stage.

### Differentiability

For fixed delay/index structure, LTM arithmetic is piecewise differentiable through subtraction, addition, `min`, and `max`. Ordinary AD should give the correct local branch derivative away from active ties.

The important exception is **parameter-dependent delay indexing**. If a future differentiated parameter changes the historical index itself, ordinary AD through a fixed integer index does not capture that time-shift derivative. This does not affect Milestone 0 green-split differentiation because link travel-time parameters are fixed.

---

## 6. Component 0.3 — fixed movement-demand projection

### Scientific source

Use the standard fixed turning-fraction projection:

`D_ij = beta_ij * S_i`.

### Recommended implementation

**Thin local tensor implementation.**

This is too small to justify an external dependency.

### What is borrowed

- movement-oriented demand definition;
- conservation of turning fractions;
- standard node-interface semantics.

### Project-specific work

Only:

- compact movement indexing;
- validation of incidence and `beta`;
- tensor shape and dtype handling.

### Differentiability

Linear in sending flow; no special treatment is required. Turning fractions remain structural in Milestone 0.

---

## 7. Component 0.4 — generic first-order node solver

This component should have the **strongest reuse requirement**.

### Scientific source

The solver should be a concrete member of the **Tampère et al. generic first-order node-model class**, not an ad hoc allocator.

The generic class defines admissibility requirements, but a concrete solver still requires an established supply-constraint interaction rule (SCIR) and, where applicable, internal node constraints.

Two plausible established choices are:

1. **Tampère et al. oriented-capacity-proportional model and exact solution algorithm**;
2. **Incremental Node Model (INM)** of Flötteröd & Rohde, which lies in the same generic first-order node-model lineage and has open-source implementations in current traffic simulators.

The exact choice remains a Phase B methodological decision.

### Recommended implementation strategy

After the concrete node model is selected:

1. identify the published algorithm;
2. identify an open implementation with matching semantics if available;
3. map the published algorithm to the project node API;
4. **port/adapt the algorithmic structure rather than redesigning it**;
5. preserve priority, FIFO, active-constraint, and redistribution semantics;
6. retain a small independent reference implementation/test formulation.

### What should not be done

Do not:

- replace the published node rule with a generic LP for convenience;
- invent a new proportional allocator;
- change tie/priority semantics merely to simplify AD;
- smooth active constraints;
- silently change full/partial FIFO behavior.

Any of those would amount to introducing a new node model.

### Tampère versus INM feasibility

**Tampère oriented-capacity-proportional model**
- closest to the paper already chosen as project methodological basis;
- paper includes an exact computational algorithm;
- clean interpretation as "generic class + specific SCIR";
- likely requires more local porting work.

**INM**
- established first-order node model;
- designed for general intersections;
- executable implementations are available in UNsim/UXsim lineages;
- stronger direct software-reference path;
- adopting it changes the concrete node semantics and therefore must be a scientific choice, not a software shortcut.

### Signal interaction

Before Component 0.5 is frozen, Phase B should check whether the selected node model already provides a signalized/internal node-constraint formulation.

If the Tampère signalized instance is used, prefer to borrow its internal-node-constraint treatment and let the continuum signal component provide the continuous capacity parameter. This is preferable to inventing an unrelated `mu_ij` cap mechanism whose FIFO effects may differ from the source model.

### Differentiability

Within a stable active set, the solver consists of tensor arithmetic and piecewise branch logic. Default AD should give the local derivative of the selected branch.

Active-set changes are nonsmooth algebraic events. They do not imply a missing continuous-time saltation term.

---

## 8. Component 0.5 — continuum fixed-time signal service

### Scientific source

Use the continuum-signal approximation from Han et al. and the selected node model's established interpretation of signal/internal capacity constraints.

### Recommended implementation

**Thin local mapper plus node-model adaptation.**

The green-to-service map is algebraically small and does not justify a standalone dependency.

Borrow:

- continuum average-service interpretation;
- saturation-flow/service-capacity semantics;
- signalized-node/internal-constraint semantics from the selected node model.

### What should remain local

Only the small mapping from approved green variables to movement/node service parameters.

### What should not be introduced

- on/off switching;
- startup loss;
- clearance loss;
- offset;
- actuated phase logic;
- new signal priority semantics.

### Differentiability

The mapper is naturally differentiable in green split. Ordinary AD gives the exact derivative **of the continuum approximation**.

A disagreement with a finite-cycle on/off simulator would be model-approximation error, not necessarily an AD bug.

---

## 9. Component 0.6 — deterministic rollout and scheduler

### Scientific source

Use the standard LTM/DNL causal ordering:

1. compute link sending/receiving;
2. project movement demand;
3. compute signal/internal node constraints;
4. solve node flows;
5. update cumulative boundary counts;
6. update source/sink accounting.

### Recommended implementation

**Project-owned orchestration around borrowed components.**

This is the main layer that should remain local because later milestones must insert:

- ordered route-mass state;
- local per-lane interaction state;
- finite storage/accessibility logic.

Directly adopting an external simulator's world/scheduler abstraction would couple those future extensions to that simulator's internal representation.

### What to borrow from UNsim

Inspect its differentiable scheduler for:

- separation of static topology and differentiable state;
- cumulative-history handling;
- fixed-step scan organization;
- source demand queue handling;
- memory-management ideas.

Do not copy advanced memory/JIT optimizations into Milestone 0 unless needed. The baseline should favor transparency.

### Differentiability

A fixed-step recurrence composed of differentiable component operations is naturally handled by reverse-mode AD. No custom adjoint is required at this stage.

---

## 10. Component 0.7 — diagnostic objective, metrics, and gradient/reference harness

### Origin

This is project-specific validation infrastructure, not traffic-model methodology.

### Recommended implementation

**Local utility code using standard framework tools.**

Reuse as-is:

- PyTorch reverse-mode AD;
- `torch.func.jvp` if approved;
- pytest;
- standard numerical comparison primitives.

Do not implement:

- a custom AD engine;
- a custom optimizer library;
- a custom finite-difference framework unless the standard small implementation is insufficient.

The diagnostic objective must remain explicitly temporary and must not become the later scientific signal-control objective by implementation inertia.

---

## 11. Recommended provenance fields for the revised Milestone 0 plan

Each component section in the formal plan should add:

```text
Scientific source:
    paper/model whose semantics are authoritative

Implementation source:
    direct reuse / port-adapt / thin local implementation

Existing implementation inspected:
    repository/package/version/commit if applicable

Required modifications:
    framework, interface, data layout, validation glue

Forbidden modifications:
    traffic semantics that must remain unchanged

Reference validation:
    paper hand case / external implementation / independent calculation

Project-specific code:
    only functionality not available from the borrowed component
```

For Component 0.4, these fields should remain provisional until the concrete node model is selected.

---

## 12. Recommended external-reference hierarchy

When implementing any borrowed component, use the following authority order:

1. **Primary paper/theory** for traffic semantics.
2. **Established open-source implementation with matching semantics** for executable guidance.
3. **Independent hand-computed cases** for auditability.
4. **Project implementation** after the above are understood.

If an external implementation disagrees with the paper, the discrepancy must be surfaced at the component checkpoint. Do not silently treat software behavior as authoritative.

---

## 13. Framework implication

The current proposal is PyTorch-oriented, while the strongest identified whole differentiable stack, UNsim, is JAX-based.

This creates a deliberate Phase B feasibility choice, not necessarily a new scientific question.

### Option A — retain PyTorch and port established traffic algorithms

**Current recommendation.**

Advantages:

- preserves the planned component interfaces;
- easier insertion of ordered ledger/local-zone state later;
- strong component-level HITL visibility;
- no dependency on an early-stage external AD API.

Cost:

- more local implementation work, especially node solver and scheduler.

### Option B — adopt JAX/UNsim as the baseline architecture

Only if Phase B determines that whole-stack reuse outweighs future extension cost.

Advantages:

- existing differentiable LTM/general node stack;
- less baseline code;
- mature JAX AD/JIT ecosystem.

Risks:

- UNsim's AD API is explicitly early-stage;
- later mesoscopic extensions must fit or fork its internals;
- project tests/data structures would need to be redesigned around JAX;
- concrete node semantics must still match the project's approved baseline.

The existence of UNsim means local implementation should be a **deliberate architectural choice**, not the result of failing to inspect available reusable work.

---

## 14. Bottom-line implementation recommendation

Milestone 0 should **not** be treated as building a macroscopic simulator from first principles.

The preferred construction is:

```text
Established triangular FD / LTM
        |
        +--> small local parameter layer
        |
Established cumulative-count LTM
        |
        +--> PyTorch port with project-owned boundary API
        |
Standard turning projection
        |
        +--> thin local tensor mapping
        |
Established generic node-model class member
        |
        +--> port/adapt published/existing algorithm
        |
Established continuum-signal + signalized-node semantics
        |
        +--> thin local service mapper
        |
Established LTM DNL update order
        |
        +--> project-owned scheduler/integration glue
        |
Standard PyTorch/pytest numerical tooling
        |
        +--> project-specific validation harness
```

The implementation principle should therefore be:

> **Borrow the traffic mathematics and the established node algorithm; own only the minimum tensor/interface/orchestration code needed for auditability, differentiation, and later mesoscopic extension.**

This gives the project the benefit of established traffic-model correctness without locking the later mesoscopic methodology into a whole external simulator whose architecture has not yet been shown to fit the ordered route-mass and per-lane local-zone design.

---

## 15. External sources to inspect during Phase B

1. **Tampère, Corthout, Cattrysse & Immers (2011)**  
   *A generic class of first order node models for dynamic macroscopic simulation of traffic flows.*  
   Transportation Research Part B 45(1), 289–309.  
   DOI: `10.1016/j.trb.2010.06.004`

2. **Flötteröd & Rohde (2011)**  
   *Operational macroscopic modeling of complex urban road intersections.*  
   Transportation Research Part B 45(6), 903–922.  
   DOI: `10.1016/j.trb.2011.04.001`

3. **Toru Seo (2026)**  
   *End-to-end differentiable network traffic simulation with dynamic route choice.*  
   arXiv: `2604.11380`

4. **UNsim**  
   `https://github.com/toruseo/UNsim`  
   MIT-licensed differentiable JAX LTM/INM implementation.  
   Current repository warning: early development; AD code/API may change.

5. **UXsim**  
   `https://github.com/toruseo/UXsim`  
   MIT-licensed macro/mesoscopic traffic simulator using Newell/X-model and an incremental node-model lineage.

6. **Han, Gayah, Piccoli, Friesz & Yao**  
   *On the continuum approximation of the on-and-off signal control on dynamic traffic networks.*  
   Use as the continuum-signal modeling basis and for its approximation limitations.
