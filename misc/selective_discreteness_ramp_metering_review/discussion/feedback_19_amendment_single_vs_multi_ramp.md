# Feedback 19 amendment — single versus multiple ramps

Date: 2026-09-14. Discussion response; no change to approved project methodology.

## Short answer

Your intuition identifies a real opportunity, but it combines three different claims: **route identity matters**, **lane occupation/access matters**, and **fine traffic order matters**. Multiple ramps can make the first two more visible without establishing the third. A route-aware macroscopic model may already explain the effect. Moreover, a ledger records identity/order; it does not supply the physical law by which traffic changes lanes.

One isolated metered merge has established traffic-engineering value, but its value as this project's selective-discreteness experiment is unproven. B1 is already more than that isolated merge: it has one controlled entrance and a downstream exit. It is a reasonable minimal candidate for testing arrival control of route-sensitive blockage. Multiple entrances/exits could add a stronger persistent-route or interaction question, but should be introduced for that specific reason, not because more ramps automatically make the ledger necessary.

**Recommendation:** retain approved B1 as the first mechanism check. Also distinguish a possible one-meter/two-exit extension from coordinated multiple-meter control. Do not adopt explicit weaving or broaden the active task yet. The amendment warrants this comparison, not automatic approval of its alternatives.

## 1. What does “single ramp” mean?

| Construction | What changes | Potential scientific role |
|---|---|---|
| Isolated merge: one on-ramp, no downstream route split | Meter controls entry into a common downstream stream | Merge/reference correctness; physical merge-capacity effects only if their dynamics are modeled |
| Approved B1: one metered on-ramp and one downstream exit | One control; downstream route-specific receiving/access restriction | Indirect arrival/composition control of fixed downstream service |
| Several entrances/exits, only one optimized meter | Richer fixed routes and downstream interactions, unchanged number of controls | Persistence of route information across successive nodes |
| Several optimized meters | Multiple interacting control inputs as well as geometry | Coordinated admission, competition for storage, cross-control sensitivities |
| A compact weaving section | Crossing lateral movements interact over a shared road segment | Lane-change/access dynamics and their capacity consequences |

Neither multiple ramps nor multiple meters necessarily means a weaving section. Conversely, one entrance followed closely by one exit can already create weaving. Separating the ramps spatially is a candidate approximation strategy, not proof that lateral behavior becomes irrelevant.

## 2. What value can one meter bring?

### Established value is not yet project-specific evidence

There is direct evidence that even an isolated merge can benefit from metering. **Cassidy and Rudjanakanoknad, _Increasing the capacity of an isolated merge by metering its on-ramp_ (2005; RM0014)** report field observation/experiments in which metering recovered higher merge discharge. Their abstract connects the mechanism to a shoulder-lane queue and lateral spreading; recovered high flows were not sustained beyond 13 minutes. This refutes a blanket claim that a single merge has no useful control problem. It does not establish that our current representation reproduces that mechanism. Access here is publisher-indexed abstract/introduction plus related 2004 repository metadata, not a full-method audit. [Publisher](https://doi.org/10.1016/j.trb.2004.12.001).

An aggregate merge can also test release constraints, merge allocation, queue conservation and backward congestion propagation. Those are valid fidelity/correctness questions, but do not demonstrate unique mesoscopic behavior. Existing accepted tests must be checked before adding redundant reference cases. An internally decreasing objective is likewise not evidence for the selective representation.

### Possible value of B1

B1 offers a different intervention from the closed TSC suite: the meter changes **arrivals reaching a restriction**, while that restriction's local service remains fixed. The TSC suite changes local effective service itself. Potentially, admitting a route mixture at different times changes downstream pocket filling, accessible through traffic and subsequent spillback. These are hypotheses, not effects already established for the proposed implementation.

**Muñoz and Daganzo, _The bottleneck mechanism of a freeway diverge_ (2002; RM0013)** report freeway observations of exit-queue blockage and discharge varying with arriving destination composition. This supplies empirical motivation for a route-sensitive exit, not a demonstration that finite ordered metadata or metering gradients are required. Only the publisher-indexed abstract/introduction was available in this pass; no geometry or calibration constants are adopted. [Publisher](https://doi.org/10.1016/S0965-8564(01)00017-9).

The counterweight is **Salehi, Somers and Seibold, _Off-Ramp Coupling Conditions Devoid of Spurious Blocking and Re-Routing_ (2017; RM0009)**. Its FIFOQ model adds aggregate queue-composition memory to address incorrect routing/blocking. The archived PDF, §§2–4, makes clear why a memoryless comparator is too weak. Its vertical queue is not a drop-in finite physical pocket. [Paper](https://arxiv.org/abs/1708.00529).

Therefore B1 can potentially test whether selective local information improves forward predictions and useful control sensitivity beyond **both route-memory and lane/storage aggregate alternatives**. It cannot establish that merely because it has different route labels. Information must affect a physically defensible access/service rule, and richer-reference perturbations must support the resulting prediction.

### A necessary accounting safeguard

Holding traffic on a ramp can simply move waiting upstream. For a total-time claim, include all source/ramp waiting and all moving/queued traffic, with comparable completion/terminal accounting. Require an actual mechanism that improves discharge or avoids harmful blocking; do not count reduced mainline delay alone as a system gain. A work-conserving fixed-capacity bottleneck may offer little opportunity for a total-time benefit. That is a conditional conceptual warning, not a theorem that every single-meter case is neutral.

## 3. Is lane-changing modeling unavoidable?

**Not for every ramp-metering task. It becomes necessary to represent its effects when those effects are the reason the task is valuable.** Three levels must remain separate:

1. **Aggregate merge transfer:** continuous demand/supply allocation at a boundary. It does not resolve actual trajectories or lane changes. It can support a legitimate aggregate control task, but cannot by itself validate lateral dynamics.
2. **Local lane intent, storage and accessibility:** compatible in principle with the planned M3 division of responsibilities. Its actual equations, service resolution and validity at a freeway location are still unresolved. Naming an operation “lane allocation” does not establish that it captures freeway weaving.
3. **Spatial lane-change dynamics:** lateral movement rates, crossing conflicts, gap acceptance, acceleration disturbance, or distributed lane occupation over a weaving segment. Explicit microscopic trajectories are one approach, not the only possible one; a lane-specific macroscopic model is another. Either can add dynamics outside the present local-zone contracts.

**Nagalur Subraveti, Knoop and van Arem, _Lane Change Control Combined with Ramp Metering: A Strategy to Manage Delays at On-Ramp Merging Sections_ (2021; RM0004)** studies one on-ramp with lane-specific incentive-based flow dynamics and combined control. This demonstrates that a single merge can already have a lane-dependent question; multiple ramps are not required. Its control/state machinery is not a ready-made justification for the current ledger. [Author repository](https://repository.tudelft.nl/record/uuid:2a3302e7-a804-46ee-a54e-0b273d6d6e7a).

If we make lane-changing-induced capacity recovery the target, an adequate model of that mechanism is required. We cannot claim it follows from route bookkeeping. But we cannot conclude that microscopic lane changing is universally unavoidable: an effective macroscopic law might suffice, subject to a separate compatibility/validation decision. A new capacity law could explain all benefit without demonstrating any need for selective order.

For B1, the open question is narrower: can localized access/storage and aggregate propagation adequately predict the intended downstream restriction without needing distributed lateral dynamics? We have not yet demonstrated that. Fixing route choices does not fix realized lane occupancy, and freezing unrealistic lane commitments merely to produce a ledger advantage would invalidate the inference.

## 4. Is a multiple-ramp case better?

It is better for some questions, not automatically for this project's central question.

**Schmitt, Ramesh and Lygeros, _Sufficient Optimality Conditions for Distributed, Non-Predictive Ramp Metering in the Monotonic Cell Transmission Model_ (2017; RM0002)** studies a freeway with multiple ramps using aggregate CTM states. Its §5 application has 10 entrances and 7 exits. Under its idealized monotonic conditions, distributed control can attain the optimum; its later analysis explains why ALINEA can approximate that behavior. This is strong evidence against inferring either a need for coordinated optimization or a need for fine order solely from ramp count. It is not a universal optimality claim outside those conditions. Archived PDF pp.16, 18–21. [Paper](https://arxiv.org/abs/1611.06766).

The plausible additional questions are reviewer inferences:

- **Persistent future destination:** traffic passing an early exit may share the same current movement but need different later exits. This tests whether future route identity survives node transitions. However, a route-aware multi-commodity aggregate baseline can preserve that identity too. It is a route-bookkeeping question first, not automatically an exact-order question.
- **Repeated local access/storage interactions:** an upstream restriction changes the stream reaching a later restriction. This may test localization and propagation of information beyond one node. Yet it also risks becoming an integration exercise equivalent in purpose to the excluded TSC corridor extension. A distinct representation contrast must be named.
- **Several controlled admissions:** one meter may alter the marginal effect of another. This can expose competition for storage or downstream service, but aggregate congestion already produces such interaction. More control dimensions do not prove mesoscopic necessity.
- **Weaving:** entry and exit streams compete for lateral access. This gives strong physical relevance, but also the highest risk of requiring exactly the distributed lateral behavior the present architecture excludes.

For fixed structural routes, control can still change admitted mass, timing and active merge/service constraints. A control-induced change in interleaving or active ordering may create a nonsmooth boundary. A multi-ramp task must not silently differentiate through route selection or pretend all realized ordering is invariant under arbitrary control perturbations.

## 5. Living candidate inventory

**Problem:** what is the smallest geometry/control scope capable of testing an additional representation question without changing the shared methodology?

**Assumed model-chain function:** metered admission changes route-mass arrival histories; propagation and local access/storage determine discharge, time and control sensitivity.

**Core gap:** neither B1 nor a multi-ramp extension yet has a verified, nonredundant representation contrast against capable aggregate baselines. Extra geometry alone cannot fill this gap.

### B1 — retain one meter and one downstream exit (approved for examination)

Use the already selected construction. Test arrival control of fixed route-sensitive access before adding another node.

**Pros:** smallest approved mechanism check; easier causal attribution and reference matching; does not introduce coordinated control.

**Cons:** may be explained by aggregate composition/storage memory or duplicate the TSC access question; lane-access approximation remains unverified.

**Dependency:** M3-consistent local service and credible richer-reference contrast. Approval is for feasibility examination, not adoption.

### B1-E — one meter and two separated downstream exits (new, provisional)

Retain one control; add a second fixed exit only if it creates an essential future-destination or repeated-access contrast that one exit cannot test. Non-exiting traffic at the first node may have different future destinations. Give the aggregate comparator equivalent route identities; remove only the information under investigation.

**Pros:** targets persistent route information without immediately adding coordinated control; a smaller expansion than a multi-meter corridor.

**Cons:** extra state, geometry and evaluator mapping; route-aware aggregates may suffice; repeated nodes may provide only integration coverage.

**Dependency:** an explicit contrast and justification for the additional exit, followed by user approval before replacing/expanding B1. It does not authorize distributed weaving physics.

### B1-C — two optimized entrances with downstream exits (new, provisional)

Use fixed routes and continuous admission at two locations to examine coupled control of route-sensitive restrictions.

**Pros:** stronger test of interacting interventions and distributed storage; closer to established multi-ramp control settings.

**Cons:** coordination is a separate source of benefit and confounding; more reference/control matching; no guarantee that order matters beyond aggregate dynamics.

**Dependency:** explicit expansion of the one-meter control scope and a documented incremental hypothesis. Current approval does not cover execution.

### B1-W — compact weaving-focused task (new, scope-dependent)

Make competing entry/exit lateral movements and their discharge effects the target, with an explicit adequate lateral-interaction model.

**Pros:** directly addresses the user's intuition about weaving and lane occupation; physically meaningful mechanism to evaluate.

**Cons:** likely requires additional spatial lane dynamics rather than just local ordered metadata; may change what simulator contribution is being tested.

**Dependency:** separate common TSC/ramp compatibility review if necessary dynamics exceed the shared contracts. Not executable under current authorization.

**Provisional recommendation:** keep B1 first; regard B1-E as the smallest possible expansion if a specific missing question warrants it. Do not choose B1-C or B1-W just to ensure the ledger appears useful. No reapproval of B1 is needed; the new alternatives are discussion candidates, not accepted plan changes.

## 6. Status and work record

The amendment is answered. It qualifies earlier “single ramp has little value” wording: that statement concerns diagnostic value for this representation, not established traffic-engineering usefulness. It also prevents the mistaken inference that multiple ramps necessarily require an ordered ledger or explicit microscopic lane changing.

B1 remains approved/open; the full conceptual feasibility check is not closed by this discussion. RM4 remains unopened. No institutional-access operation is needed for these qualified conclusions; obtaining full methods would be necessary before adopting the new empirical papers' detailed mechanisms or reconstructing their sites.

Changes: this response; package README/protocol/handoff and shortlist pointers; source metadata, search log, screening/extraction/manifest records for RM0013–RM0014. The original feedback text is preserved. All edits stay within this package.

Methods/commands: read current records and project contracts using `cat`, `tail`, `sed`, `rg`; reused archived PDFs with installed `pypdf` via the existing conda Python; targeted primary-source web searches and page opens; `apply_patch` edits. New retrieved metadata and source-access limits are retained in `../archive/metadata/feedback_19_amendment_sources.md`. No packages, simulations or project changes. Validation covers record IDs, CSV structure, local references and review status, not scientific performance. Next allowed action is the bounded B1 check; broader candidate execution requires its own approval.

Validation result: passed CSV structure, 14 unique and aligned source IDs across screening/extraction/manifest, all manifest file paths, 15 unique search IDs, and existence of the new response/source-note/handoff artifacts. `git status --short` continues to show only the pre-existing tracked `AGENTS.md` and `PLANS.md` modifications; neither was edited here. Scientific feasibility and gradient usefulness remain untested.
