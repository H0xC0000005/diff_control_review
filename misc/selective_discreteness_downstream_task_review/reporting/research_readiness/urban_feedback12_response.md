# Feedback 12: second report-improvement batch

28 October 2026. **The batch is complete.** Added and rewritten passages are marked in moderately saturated bright red, `#D13F43`, in the main report and mathematical companion. The existing five-part report order remains in place.

[Revised report](urban_compact_methods_report.pdf)

[Mathematical companion](urban_methodology_specification.pdf)

[Component provenance and reading depth](../../extraction/research_readiness/urban_feedback12_component_provenance.md)

The grid and ledgers were indeed underexplained. They now have their own model subsection. The long-link ledger tracks route-labelled continuous mass and entry/readiness times; each realized lane has its own ordered ledger; the movement grid represents that lane's continuous composition and load. A grid bin can mix movements, so its totals cannot replace the exact sequence used for head service and bay access. The grid and ledger describe one physical mass, counted once.

There is one qualification to “CTM based.” The earlier project plan explicitly chooses cumulative-mass/rank bins rather than physical-space CTM cells. The report now cites CTM as the cell-based lineage and explains this coordinate adaptation. Physical travel, storage and spillback continue to use LTM section histories. The restored overlap formula and its derivative show the intended grid without inventing a second propagation law or changing the agreed physics.

The report credits the lane-equilibrium idea to Gong, Bliemer and Raadsen and distinguishes the present raw-queue, constrained entry rule from their original exit-node model. It also identifies the average-service, first-order-node and identity-tracking sources beside the relevant components. The particular current-head sharing priorities and continuous ledger/grid construction are identified as model-specific definitions. A citation is no longer left to imply that an entire composed operator came from that paper. A related author correction identifies the individual-tracking paper as de Souza et al. (2025), while retaining Yperman as the LTM thesis source.

Around the sharing equations, theta is now the multiplier that distributes the output's usable rate between legs, and eta is explicitly the common uncapped lane rate within a leg. The report gives its units and the 0.3/0.3 versus 0.1/0.5 example. Entry-rank notation is changed from the easily confused rate symbol r to mass offset z. The entry interval names its first and last entry times explicitly. Free-flow time is defined again where it is used. Derivatives now use the explicit d/d-alpha form, with alpha defined as the amount of a feasible service reallocation.

The rate-to-amount section begins with the missing traffic question: how much of an ordered lane can discharge during the timestep if its head clears early? The example defines the front mass, both rates, available time and ample downstream room before calculating the two transferred amounts. It then explains why a changed head can change the receiving shares of competing lanes. The sigma/delta formula follows that logic. The irrelevant “neither phase clock nor history replacement” sentence is removed.

The entry-time section now explains why a lane count is insufficient: the next update must identify which packet portions have travelled far enough to reach service. The two-element interval assigns when the packet's front and tail entered, and adding the locally defined free-flow delay gives their earliest readiness. The previously compressed route/merge/grid sentences are replaced by a component explanation. Route progress is explained through the physical distinction between entering a bay and actually crossing onto the next road.

The TST equation repeats every core variable: existing source waiting, newly available release, mass on each physical road section, timestep and common clearance horizon. Its terms are explained as charging everyone still in the system; the units and source-to-road ownership transfer are explicit. Adding the grid display moves the former equation 11 to equation 12; equations 6–10 retain their numbers.

The scenario table now states the purpose of each mechanism ablation. The neutral case, order-only case and storage-only case establish the separate explanations before the combined access/order case. This is a progressive study design with two separate controls, rather than a strictly nested sequence in which every row adds all earlier mechanisms. V4 is the robustness extension, not another ablation. It reserves combinations of demand, turn shares, bay geometry/storage, arrival order and downstream receiving—including asymmetric approaches—from calibration and tuning. A concrete short-bay/high-left-demand/reduced-receiving example makes “reserved” understandable without inventing numerical scenario-bank settings.

The internal comparator codes are removed from both PDFs. Comparison models are named by what they represent: aggregate links, movement queues, lane/storage aggregates and selective ordered mass. Their relationship to the ablations is stated directly: queue/storage models should explain effects that need only those quantities; the combined case tests the additional value of realized order. The original-series aggregate-inference agreement is retained in a short scientific statement, with detailed data-protocol conditions in the companion.

Finally, sensitivity opens with the whole causal path: service allocation, current discharge, ledger masses/times and lane grids, later sending/receiving and access, source waiting/sink exit, then TST. The analytical state chain comes before the module derivatives. The companion includes the grid-overlap and LTM-history derivative paths. Fixed metadata remain distinct from continuous masses and times; numerical correctness and useful control gradients are still evidence to establish later.

**Current topic: review of the red-marked report.** No new scientific question batch, implementation or experiment is opened by these changes. Numerical calibration and exact baseline qualification remain later work. The earlier structural alternatives remain unselected.
