# Deferred: retaining departure histories between timesteps

**Scope correction, 27 October 2026: this is not a current decision or a drafting blocker.** The user limits the present sensitivity work to timestep states and updates. Retain the established M0 boundary histories and interpolation; event-resolved histories are deferred. The original comparison below remains a numerical-refinement diagnostic, not a required new research question.

A timestep-only gradient can still depend on the existing interpolation: a fixed travel or backward-wave delay can make the next timestep update query an interior point of a stored past interval. That interpolation is already defined by M0 and requires no new choice here. I had shown that another reconstruction changes predictions, but had not established that the current task requires replacing the existing one.

The selected elapsed/current-head calculation remains an internal way to compute one step's discharge. Its internal head-clearance times do not become a new history representation or observation target. Boundary cumulative counts and the inherited reconstruction remain authoritative for propagation; ledger/eligibility transcription must respect that convention.

The selected average-rate server follows the actual head: a slow left block clears, then through traffic uses its own rate. This determines departure times inside an interval. The inherited LTM, however, saves counts at timestep boundaries and reconstructs the intervening departures at a uniform rate. Those histories can predict different later travel readiness or upstream room.

Consider an already-ready shared lane after preparation. Left mass 0.1 is followed by ample through traffic. Their effective rates are 0.2 and 0.4 mass per second. In a one-second illustrative interval, left clears after 0.5 seconds; through then serves 0.2. Both descriptions record total discharge 0.3.

| Departure history | Discharged by 0.4 seconds | Discharged by 1 second |
|---|---:|---:|
| Keep the elapsed-service crossing times | 0.08 | 0.30 |
| Reconstruct uniformly between timestep boundaries | 0.12 | 0.30 |

The difference matters when a later propagation calculation asks what had left at 0.4 seconds. In a storage-limited example, these histories give **0.08 versus 0.12 of upstream receiving** in the next interval. A feasible small service transfer also gives different local receiving sensitivities, away from event ties. These are hand calculations, not simulation results or a claim of different complete TST in this isolated case. The example changes neither initialization from empty nor the selected average-service abstraction.

**Keep the service-time history.** Retain the piecewise departure curve produced by ordered service, and query it after the physical travel/backward-wave delay. The same crossings then determine service, later eligibility and when cleared space propagates upstream. This retains the aggregate first-order LTM/Newell physics, but extends the inherited history representation beyond uniformly interpolated timestep totals. Its derivative must include changes in the service-event times.

**Keep the inherited boundary reconstruction.** Use the ordered server to determine each interval's discharged amounts, then reconstruct those departures uniformly for subsequent propagation. This preserves M0's current numerical convention and bounded history grid. It is a declared coarse approximation: later traffic follows the reconstructed crossing times, and route eligibility must be made consistent with that reconstruction. This is a viable reconstruction direction, subject to that consistent coupled transcription; the two histories cannot be described as interchangeable.

**Earlier recommendation withdrawn for the current scope.** Retaining service-time histories is a possible later refinement, if a stated fidelity/sensitivity requirement justifies it. This comparison alone does not justify making it part of the present task.

**Disposition:** keep M0's boundary reconstruction for the current model. No answer is needed on this note, and no event-history change or production amendment is opened.

The remaining work is the capability-aware timestep allocation/update law, its composed sensitivity and comparison/reference checks. Feedback 9 settles the new-allocation dependency and withdraws the later fixed-target A/B gate. The user requests only that feedback answer, so no further work is opened here.

[Feedback 9 response; the admission binary is no longer a current gate](../../reporting/research_readiness/urban_feedback9_response.md)

[Agreed receiving timing — unchanged](receiving_priority_timing.md)

[Supporting source and hand-calculation record](../../extraction/research_readiness/urban_unified_methodology_sources.md)
