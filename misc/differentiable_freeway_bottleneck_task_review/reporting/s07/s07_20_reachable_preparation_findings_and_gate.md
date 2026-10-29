# S07.20 — Reachable near-drop preparation findings and contract gate

Date: 2026-09-29. Status: **DG-R4 closed by explicit user approval of Candidate A;
S07 and the subsequent S08 planning sprint are closed.** Parent: [S06 closure](../s06/s06_99_reference_bridge_sprint_closure.md).
No provider/server check, implementation, traffic run, or gradient work occurred.

## Main finding

**A populated near-drop snapshot is easy to schedule; a hidden consequential
snapshot is still uncertain.** Moving the decision into the peak-arrival window
repairs the empty/sparse 40/60/80-second design. It does not remove the central
observability tension: native strategic lane changing can begin far upstream and
can change speeds that are present in the exact aggregate history.

The retained [analysis PDF](../../synthesis/s07/s07_reachable_preparation_analysis.pdf)
and [source](../../synthesis/s07/s07_reachable_preparation_analysis.tex) establish the
following bounded results:

1. **Reachability:** strict fastest-arrival screens remain 71.8200 s and
   77.1619 s. Advice-aware nominal road-start travel to the final 400 m is
   74.0937 s with desired-speed insertion or 79.4356 s from rest. Nominal region
   residence is 14.4134 s.
2. **Useful timing window:** the 4,050 veh/h peak first reaches the region near
   194.1–199.4 s and fills one nominal residence interval near 208.5–213.8 s.
   Decisions 220/240/260 s each have a nominal 16–17 vehicles in the region under
   both screened entry conventions. These are arithmetic screens, not native
   predictions.
3. **Insertion confounding:** the old ending-lane quotas create peak lane rates
   ranging from 675 to 2,700 veh/h. Safe insertion capacity depends on entry
   speed, step and placement. Preparation-specific insertion queues would appear
   in the retained source-waiting and cumulative-entry history, so later decision
   times alone do not repair the old bank.
4. **Small low-confounding bank:** use a common balanced lane sequence everywhere
   except one six-vehicle block. Six permutations each allocate two vehicles per
   lane and preserve the same nominal per-lane rate. At the three decisions,
   peak indices 16–21, 38–43 and 61–66 form contrast blocks whose members lie in
   the final 400 m under both nominal travel conventions. This gives 18 prefixes
   rather than 48.
5. **No exact-match certificate:** current official documentation lists a
   3,000 m strategic lookahead, longer than the approach, while the primary
   LC2013 method makes urgency and speed adjustment depend on distance, speed
   history, lane offset, occupation and blockers. The actual future version must
   be pinned, but it is already unsafe to assume that lane-entry permutations
   remain invisible until the final 400 m. Exact matching must remain the first
   empirical stop.

The [source/method audit](../../extraction/s07_reachable_preparation_source_audit.md)
separates official capabilities, primary native methodology and original
arithmetic. No decision-critical source is inaccessible.

## Rejected shortcuts

- **Simply use later times with the old quota bank:** later times add traffic but
  retain unequal insertion burdens and longer preparation-specific histories.
- **Disable or shorten native strategic lane changing:** this manufactures the
  desired collision by changing reference physics.
- **Use mid-link insertion or a nonempty lane-hidden warm start:** this can make
  an immediate lane-blind collision, but it introduces an artificial source or
  hidden initial state and reopens DG-G1/G2 rather than repairing Candidate A.
- **Accept near-equality:** this changes the approved information claim and must
  reopen DG-G2 with an observer/error contract.

## S07-UG1 / DG-R4 — Which near-drop preparation should be frozen for a later exact-match screen?

### Problem statement

Should a later empirical feasibility screen use the smallest localized balanced
contrast, use a broader balanced contrast window to seek more lane difference,
or defer because native anticipation makes an exact collision unlikely?

### Assumed model-chain function

Preparation supplies multiple physically reachable prefixes from an empty road.
The exact strong aggregate/history channel selects pairs without seeing action
outcomes. Only a surviving pair with different near-drop lane configuration may
advance to common-advice action evaluation. Preparation must avoid creating an
obvious lane-specific source-queue signal.

### Core gap

Documentary and kinematic evidence can make the prefix bank defensible but cannot
show whether native longitudinal trajectories remain exactly identical. A very
short differing block reduces observable contamination but may leave too little
lane contrast. A broader differing window increases contrast and interaction but
also increases the chance that full history distinguishes the states.

### Candidate A — freeze the localized one-block road-start preparation (provisional recommendation)

Keep the accepted geometry and demand clock. Explicitly use base road-start
position, desired-speed insertion, all insertion safety checks and retained
departure delays. Use decision times 220/240/260 s. All preparations use the same
balanced two-per-lane six-vehicle sequence except for one decision-specific
six-vehicle contrast block; evaluate its six balanced permutations. All future
departures are identical. The bank has 18 prefixes and stops before actions if
no exact pair with a nonzero final-400 m lane contrast exists.

**Pros:** Smallest repair to the failed timing contract; enough nominal traffic;
same per-lane block totals; localizes hidden forcing; reduces prefixes 48→18;
preserves the exact-information question and native reference.

**Cons:** Only six vehicles differ, so the surviving lane contrast may be small or
erased. Strategic lane changing can still alter aggregate speed/count history
well before decision. Desired-speed entry is explicit but synthetic, and a
negative exact-match screen would remain scenario-specific.

**Dependencies and consequences:** Approving A would amend DG-G4/C3 preparation
timing, entry-speed convention and bank only. It would not approve a provider,
runner, action stage, held100/cap504, model, or gradient. A separate empirical
plan must pin the actual engine version and exact arrays before any run.

### Candidate B — freeze a broader balanced multi-block contrast window

Use the same road-start, desired-speed, 220/240/260-second design, but apply each
balanced permutation over three consecutive six-vehicle blocks centered on the
Candidate A block. Every block remains two-per-lane, so nominal lane rates are
balanced; all other departures remain common. Keep the same six preparations per
decision rather than multiplying the bank.

**Pros:** Produces a stronger and more persistent lane-order perturbation without
returning to unequal lane quotas or increasing prefix count. More vehicles can
participate in pre-merge interactions and a measurable final-400 m contrast.

**Cons:** Preparation-specific behavior lasts longer, making exact aggregate
history equality less plausible. Some early/late contrast vehicles need not be
inside the final 400 m at decision, so this tests a broader interaction window.
Any apparent advantage could come from greater microscopic gap/order changes,
not ending-lane occupancy alone.

**Dependencies and consequences:** Same DG-G4/C3 amendment boundary as A, but
with a broader hidden-input duration. It does not relax exact matching. Selecting
B requires freezing the exact three blocks before any empirical plan.

### Candidate C — defer the native near-drop certificate

Retain S05's conditional hidden-information result, S06's mechanism basis, and
S07's preparation analysis without authorizing a native prefix screen.

**Pros:** Avoids spending experiment and provider effort on an exact collision
that documentary evidence suggests may be fragile; preserves all valid bounded
findings.

**Cons:** Leaves the accepted near-drop information-value hypothesis untested.
No aggregate sufficiency, impossibility, minimum-state or gradient conclusion
would follow.

**Dependencies and consequences:** Explicit deferral. Candidate B from DG-R3
does not become active automatically; reopening the upstream route remains a
separate user decision.

### Candidate D — pre-register A followed by a failure-specific B prefix screen

Run Candidate A's prefix/matching stage first. Candidate B may follow only if A
produces at least one exact-history pair but every such pair has zero final-400 m
lane contrast. This is the specific failure that B is designed to address. Freeze
both banks before running A and retain every A failure in the report.

Do not run B if A produces no exact-history pair: the broader B perturbation is
more observable and would become an adaptive search for a favorable cancellation.
Do not run B if A produces an exact pair with nonzero contrast; A has then passed
the preparation gate. Do not run B merely because that contrast looks small—the
current contract deliberately has no invented positive-magnitude threshold. Fix
only harness-conformance faults under the ordinary rules. If A later reaches an
action stage and fails to show a useful-advice distinction, B is not an automatic
outcome-driven fallback; that requires a new user gate and search/validation plan.

**Pros:** Preserves identity-first ordering; spends the broader bank only on the
failure it can plausibly repair; pre-registration prevents action-outcome fishing;
maximum A+B prefix count is 36, still below the old 48-prefix bank.

**Cons:** Adds adaptive preparation search and another stopping classification.
B cannot rescue an A observability failure and may still erase exact equality.
A later B success must be labeled staged discovery rather than evidence from a
single untouched bank.

**Dependencies and consequences:** Freeze A and B patterns, the exact trigger
matrix, reporting labels and prefix budget in the empirical plan. Matching and
contrast checks use predecision data only. No action result may trigger B.

### Provisional recommendation

**Candidate A remains the preferred first bank.** If one bank must be selected,
choose A. If the user wants to preserve B as a disciplined fallback now,
Candidate D is the recommended staged form: B is permitted only after exact
identity survives in A but the lane contrast is erased. Candidate B by itself
buys contrast by worsening the exact-observability problem. Candidate C is
reasonable if the expected value of a narrowly synthetic prefix screen does not
justify its setup cost.

**Planned stop reached.** Choose or adjust DG-R4. No empirical prefix run, action
evaluation, contract amendment, or subsequent sprint starts automatically.

**Subsequent user decision:** Candidate A approved. Candidate B may be reviewed
and manually added only by later mutual agreement; Candidate D's automatic staged
fallback is not selected. The user then instructed closure of S07 and continuation
to the next gate. See [S07 closure](s07_99_reachable_preparation_sprint_closure.md)
and [S08 planning findings](../s08/s08_20_exact_prefix_planning_findings_and_gate.md).
