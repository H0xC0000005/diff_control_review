# S08.20 — Exact-prefix planning findings and execution-scope gate

Date: 2026-09-29. Status: **Closed; DG-R5 Candidate A approved.** Parent:
[S07 closure](../s07/s07_99_reachable_preparation_sprint_closure.md). Closure:
[S08.99](s08_99_exact_prefix_planning_sprint_closure.md).

## Planning result

DG-R4 Candidate A is now transcribed into a complete proposed prefix-feasibility
contract. The [contract annex](../../synthesis/s08/s08_exact_prefix_feasibility_contract.md)
freezes 18 preparation IDs, exact rational departure/block indices, six balanced
lane patterns, base/desired safe insertion, the full observation channel,
elementwise equality, complete pair registry, outcome-blind selection, failure
labels, provider/readiness boundary, budgets and durable outputs.

No scientific input remains to be invented during implementation. The only
current decision is how much time-step symmetry to require in the first exact-
matching screen. Both viable choices stop before advice actions. Per the user's
clarification, exact invocation count is operational metadata rather than a
scientific selection criterion unless a candidate changes algorithmic
complexity.

## S08-UG1 / DG-R5 — How should the exact-prefix feasibility screen be executed?

### Problem statement

Should every prefix be evaluated at both approved time steps before pair
selection, use the 0.5 s bank as discovery and validate only selected pairs at
0.25 s, or defer empirical reference work?

### Assumed model-chain function

The reference prefix stage determines whether the accepted preparation supplies
an exact information collision with nonzero near-drop lane contrast. It must
separate preparation feasibility from action benefit and must not search action
outcomes, additional banks or approximate matches.

### Core gap

Native exact equality is untested. Full dual-step screening evaluates the same
candidate set symmetrically. Staged screening lets the 0.5 s discretization
determine which pairs receive the second check. Their 14-run difference is a
constant-factor operational difference, not an algorithmic-complexity change,
so it does not govern the recommendation.

### Candidate A — full dual-step prefix bank (provisional recommendation)

After provider/readiness approval, run all 18 prefixes at 0.5 s and 0.25 s.
Intersect exact-history/nonzero-contrast pairs across steps, then select at most
two by the frozen contrast/lexical rule. Cap: 24 readiness plus 36 prefixes = 60.

**Pros:** Symmetric evidence; selection occurs after both numerical resolutions;
complete residual/failure map at both steps; avoids a primary-step discovery
filter; still far below the old 480-run full-diagnostic cap.

**Cons:** Exact cross-step pair survival may be rare; provider/harness work is
required before the scientific screen and a negative result remains
scenario-specific. It also executes 14 more bounded prefix instances, recorded
for logistics but not treated as a methodological disadvantage here.

**Dependencies and consequences:** Explicitly authorize read-only provider pin,
prefix-only implementation/readiness and at most 60 invocations. Installation,
action evaluation, held-out contexts, held100/cap504 and gradients remain outside.

### Candidate B — staged 0.5 s discovery and selected-pair 0.25 s check

Run all 18 prefixes at 0.5 s, select at most two pairs, then run only their
distinct states at 0.25 s. Stop if they fail; do not search unrun 0.25 s states.
Cap: 24 readiness plus at most 22 prefixes = 46.

**Pros:** Preserves exact matching and time-step confirmation for any reported
pair; failure rules are simple; it can be retained as a resource-constrained
execution variant if an actual feasibility limit later appears.

**Cons:** Pair discovery is conditional on 0.5 s; another pair that would survive
both steps can be missed. The 0.25 s bank is incomplete, weakening diagnosis of
why discretization changes matching.

**Dependencies and consequences:** Same provider/implementation boundary as A
with the lower cap. The selected-pair rule and no-second-search stop must remain
fixed.

### Candidate C — defer empirical prefix work

Archive the exact contract without inspecting a provider or implementing/running
the prefix screen.

**Pros:** Preserves a complete future plan if provider or implementation
feasibility cannot be established.

**Cons:** Leaves the central native exact-collision feasibility question open;
neither lane refinement nor aggregate sufficiency follows.

**Dependencies and consequences:** Explicit deferral. S07 Candidate B and
approximate matching do not activate automatically.

### Provisional recommendation

**Candidate A.** It selects pairs only after both approved resolutions are known,
providing the cleanest evidence and the simplest non-adaptive execution. The
full bank remains prefix-only and feasible within the frozen bounded design.
The constant-factor invocation saving of Candidate B is not a reason to accept
its discovery filter under the user's stated priority.

**User decision:** Candidate A approved. The full dual-step bank is fixed; the
staged discovery filter is not selected. See the [closure and next-step
boundary](s08_99_exact_prefix_planning_sprint_closure.md). No provider check,
implementation or traffic execution starts automatically.
