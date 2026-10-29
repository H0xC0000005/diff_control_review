# Feedback 11: first report-improvement batch

28 October 2026. **This revision batch is complete.** The report is rewritten for research colleagues, with the existing VSL-derived section order retained. The alternative structures requested in feedback 11 are proposed separately and have not been applied.

[Revised urban methods report](urban_compact_methods_report.pdf)

[Synchronized mathematical companion](urban_methodology_specification.pdf)

[Structural alternatives — proposal only](../../temp_content/research_readiness/report_structure_options.md)

The representative approach now has two physical upstream lanes and three stop-line lanes: an inside left/through feeder branches to a left-only bay and through-only continuation; a parallel through/right feeder continues to its shared stop-line lane. The bay opening stays inside the local zone. Through traffic chooses between the two feeders when admitted from the aggregate road. Once occupying a feeder, traffic cannot switch to the other lane. This represents partial blockage without granting a fictitious path around a resident head. Compared models and V2/V3 use matched geometry and permissions. The smaller case remains a diagnostic.

The core idea now precedes every displayed main-text equation. Sending is introduced as traffic that has travelled far enough, receiving as space whose availability has propagated back to the entrance, allocation as feasible mass followed by queue balancing, service as head clearance and shared downstream opportunity, and sensitivity as the accumulated state consequences of a service change. The causal explanation leads into the symbols, rather than asking the reader to infer the traffic story from them.

Equation 4 explicitly defines its purpose and unknowns. V is the total mass admitted from the current packet during the update. Lambda is the common queue-load filling level found by the solver so lane additions total V. It is measured in vehicle-equivalent mass, while individual lane admission bounds limit the additions. A small numerical example makes the distinction visible. The physical output is the unique vector of additions; lambda can be nonunique when every usable lane is capped.

The compact candidate-list sentence is replaced by an independent-access example. The report now says directly that sending limits actual transfers, while inspecting later independently accessible movements remains possible. It also says that unserved mass keeps its original entry/travel history and relative residual order, so waiting does not restart travel time. Physical lane obstruction remains explicit.

References to our private agreement, approval history and candidate debates are removed from the main narrative. Attribution remains: readers can identify the inherited propagation/route machinery, the local allocation/access composition and the limits of the baseline sources. The companion is updated so its permissions, examples and formulas do not contradict the main report. The shared left/through service example is explicitly a V1 diagnostic; it does not imply left-turn permission on the representative through-only lane.

All 18 labeled main equations are unchanged. In the companion, only the geometry display changes; the other 27 labeled equations are preserved. This is a geometry and explanation revision, not new traffic, optimization or numerical-gradient evidence. Build, equation, local arithmetic, artifact and layout checks are recorded in the work report.

The structural note offers a mechanism-first account, a model/study-design separation, and an organization around the information/decision/gradient claims. My provisional recommendation is mechanism-first because it gives each equation a purpose in a traffic problem the reader already understands. The current order remains in place until a different one is selected.

**Current topic: review of the revised methods report.** The requested batch is ready to read. Alternative report structures remain proposals; numerical calibration, implementation and experiments remain later work.
