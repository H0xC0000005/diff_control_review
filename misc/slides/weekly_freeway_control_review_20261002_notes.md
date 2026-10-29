# Weekly freeway-control review deck — request 6

Date: 2026-10-02. Colleague-facing methodology/findings, from VSL task definition to the current ramp-metering review. Two boilerplate and 12 substantive slides; white background, Calibri 32/18 pt.

## Content and claim boundaries

Objective clarification: slide 8 uses J for VSL mean cohort time (total time divided by fixed mass); slide 13 uses J for ramp total system time. Their labels now make the normalization explicit. The [three-page explanation](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_mean_time_and_speed_derivative_explained.pdf) defines all VSL symbols and derives the linear-batch cost and speed gradient. Its editable LaTeX source is retained alongside it. These are explanatory corrections, not changed model semantics.

VSL is complete as a conditional analytical task/certificate, not an empirical or full model-family study. The closed proof preserves one common lane-uniform action. Ending-lane fraction can alter the initial optimal action and gradient under its stated inherited history collision and transfer/receiving regime. Its exponential transfer and batch service are analytical adaptations, not a calibrated law from one paper.

Ramp metering is active at the observer-contract decision. The separate resource kernel is approved for analytic review; the idealized speed map remains proposed. No complete ramp equal-history/action witness or independently useful gradient is claimed. Gate labels and sprint chronology are kept out of visible slides.

The normalized VSL plot evaluates the existing certificate's closed-form illustration only. It is not a new traffic simulation, calibration or parameter experiment. All diagrams are grouped native shapes or one vector picture object. Sources and detailed qualifications are in each slide's PowerPoint speaker notes.

## Build and format

Generator: [generate_weekly_freeway_control_review_20261002.py](generate_weekly_freeway_control_review_20261002.py)

Build command:

    /home/zpz/miniconda3/envs/differential_sim/bin/python misc/slides/generate_weekly_freeway_control_review_20261002.py

Dependencies already installed: python-pptx 1.0.2, matplotlib 3.10.9, Pillow, lxml and NumPy. No installation or production changes.

PowerPoint text is editable Calibri. Mathematical expressions and the analytic plot use scalable SVG with a PNG fallback, following [Microsoft's SVG picture convention](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-odrawxml/7e1f1524-1569-4aa2-a6c9-aab2d855bd48). Equation sources remain in the generator and SVGs in the asset folder. No complex plain-text equation is used.

## Validation and rendering limit

Checks cover slide/boilerplate counts, Calibri 32/18 metadata, body lines (also conservatively counting equation lines), grouped diagrams, text width/height and slide bounds, source paths, ZIP/XML and embedded SVG relationship targets. All pass; see [validation JSON](weekly_freeway_control_review_20261002_validation.json).

Pillow layout proof reads the saved PPTX, including group transforms and PNG fallbacks. DejaVu Sans substitutes for locally unavailable Calibri; no Office/LibreOffice renderer is installed. This is an inspected layout proof, not a native PowerPoint-rendering claim.

Manual preview inspection checked all 14 slides, plus full-size transfer and gradient slides. Labels/titles were wrapped or shortened to fit without reducing the requested fonts; the two integral rows were spaced apart after inspection. No scientific simulation or numerical gradient test was required or performed. VSL remains closed at its conditional analytical scope; the ramp observer gate remains open. Next allowed review action is discussion of that gate.

## Slide-by-slide speaker notes

### 1. Freeway control and useful traffic gradients

Weekly colleague presentation requested in feedback item 6. Scope starts with VSL task definition and ends with the current method-first ramp review. The VSL result is a closed conditional analytical certificate; the ramp information/action test remains open. This is presentation synthesis, not a new review or experiment.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md)
- [misc/selective_discreteness_ramp_metering_review/reporting/rm9_current_handoff.md](../selective_discreteness_ramp_metering_review/reporting/rm9_current_handoff.md)

### 2. Contents

The order mirrors the requested syllabus. Method-first principles and research questions frame both tasks. VSL includes its causal mechanism, exact conditional information/action result, gradient and study boundary. Ramp metering receives the same treatment where evidence exists, with open claims clearly identified.

Sources:

- [temp_content/feedback/feedback.md](../../context_snapshots/diff_minimal_meso/temp_content/feedback/feedback.md)

### 3. Start from the control question

The historical implementation-anchored approach sought a compatible freeway task. The independent reviews instead start with a task and a strong aggregate comparator, then ask whether unavailable information changes useful actions. Current project code is not a model-family admission constraint. This does not claim existing simulator implementation was invalid.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/01_review_recap_through_s06.md](../differentiable_freeway_bottleneck_task_review/01_review_recap_through_s06.md)
- [misc/selective_discreteness_ramp_metering_review/reporting/rm7_20_method_first_task_formulation_and_gate.md](../selective_discreteness_ramp_metering_review/reporting/rm7_20_method_first_task_formulation_and_gate.md)

### 4. Three questions guide both control tasks

These are the persistent core review questions. Information loss means a difference unavailable to the complete declared aggregate observation history, not merely different lane snapshots. All comparisons use the same action family, known forcing and complete population objective. Useful gradient evidence differs from differentiability or lower internal loss.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_35_study_sufficiency_and_extension_audit.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_35_study_sufficiency_and_extension_audit.md)
- [misc/selective_discreteness_ramp_metering_review/synthesis/rm8_predecessor_and_information_map.md](../selective_discreteness_ramp_metering_review/synthesis/rm8_predecessor_and_information_map.md)

### 5. VSL task: a permanent three-to-two lane drop

One shared lane-uniform infrastructure advice speed is varied over a bounded interval. The selected analytical branch converts advice to traversal time; this is not an assertion of universal field compliance. The permanent drop removes reopening/recovery bookkeeping. Keeping one actuator avoids confounding information value with extra lane-specific control authority. The final proof uses ending-versus-continuing groups under continuing-group symmetry.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_model_contract.tex](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_model_contract.tex)
- [misc/differentiable_freeway_bottleneck_task_review/extraction/s13_m2_source_to_equation_audit.md](../differentiable_freeway_bottleneck_task_review/extraction/s13_m2_source_to_equation_audit.md)

### 6. Preparation time can change receiving work

In the accepted fixed smooth branch, slower advice increases L/v and permits more mandatory ending-lane mass to transfer before the choke. The constant-rate exponential is an explicit analytical adaptation. Remaining mandatory-merge mass consumes alpha>1 receiving-work units per vehicle-equivalent under proportional homogeneous batch service. Receiving work is not additional vehicle mass. All action-induced traversal time and complete clearance are charged. If service is independent of action, the earlier fixed-service obstruction restores a common fastest action.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_model_contract.tex](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_model_contract.tex)
- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_20_m2_certificate_findings_and_gate.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_20_m2_certificate_findings_and_gate.md)

### 7. Hidden allocation can change the best advice

This is the accepted conditional VSL certificate, not a field finding. The two ending-lane fractions inherit exact predecision density, flow, speed and count history equality from the homogeneous conservative upstream construction. The spatial decision boundary is first entry to the common preparation zone. For the open parameter regime, unique actions differ over the entire speed interval: low p selects fastest, high p an interior slower action. Aggregate-history-only initial action has positive worst-state regret; later feedback may see divergence. The plot reproduces the certificate's normalized illustration: lambda=1, tau range [0.2,2], K=4, p_low=0.2, p_high=0.5. Curves are excess analytical mean time relative to each state's optimum, not simulation or calibration.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_certificate_analysis.tex](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_certificate_analysis.tex)
- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md)

### 8. VSL: follow the causal gradient path

Fixed-active-regime chain: advice speed -> traversal time -> remaining mandatory-transfer mass -> receiving workload -> complete mean time. The displayed cost and derivative are exact for the proportional fluid batch. Hidden p changes e and can reverse the locally improving speed direction near fastest advice. Structural lane topology is not differentiated. Lane transfer structure is grounded in Nagalur Subraveti/Knoop/van Arem; gap-weighted receiving and proportional sharing in Carey/Balijepalli/Watling; common VSL lane-drop setting in Zhang et al. The exponential active branch, batch handoff and information/action/gradient certificate are review adaptations and deductions, not jointly established by one literature work. No AD/FD or independent reference evaluation occurred. J is total cohort system time divided by fixed cohort mass M, not last-departure time. All mass travels for tau and is then discharged as a homogeneous proportional batch. W=(M-e)+alpha*e is receiving work; discharge duration is W/mu. Linear mass discharge gives mean post-arrival time W/(2*mu). Hold M,p,L,lambda,alpha,mu fixed: de/dtau=-lambda*e and dtau/dv=-L/v^2 yield the displayed chain-rule derivative. Alpha is the total merge-work multiplier; alpha-1 is the extra part.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/extraction/s13_m2_source_to_equation_audit.md](../differentiable_freeway_bottleneck_task_review/extraction/s13_m2_source_to_equation_audit.md)
- [misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_certificate_analysis.tex](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_m2_certificate_analysis.tex)
- [misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_mean_time_and_speed_derivative_explained.tex](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_mean_time_and_speed_derivative_explained.tex)
- [Primary source](https://doi.org/10.1080/21680566.2019.1700846)
- [Primary source](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)
- [Primary source](https://doi.org/10.1080/23249935.2022.2033878)

### 9. VSL: an analytical task, with a study still ahead

VSL S13 is properly closed as a conditional decision-relevant certificate. It is more than just admitting a model family: observer, action, dynamics, complete accounting and gradient relevance are specified for one analytical member. It remains incomplete as a model-family or empirical research study. Remaining mandatory-merge mass compresses the consequential information to a scalar; full lanes, order, gaps and vehicle identity have not been shown necessary. Robustness/causal deletion, minimum-state comparison, traffic-domain and reference admission, derivative verification and held-out independent usefulness are deferred. Further VSL review is set aside for colleague discussion.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md)
- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_35_study_sufficiency_and_extension_audit.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_35_study_sufficiency_and_extension_audit.md)
- [misc/differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_deferred_research_readiness_review_plan.md](../differentiable_freeway_bottleneck_task_review/synthesis/s13/s13_deferred_research_readiness_review_plan.md)

### 10. Ramp metering: one local merge

The branch is reopened method-first, not as a compatible implementation extension. One finite-storage on-ramp enters a two-mainline-lane local merge candidate. The common action is a bounded open-loop infrastructure release-rate schedule. Open-loop isolates model gradient correctness and one-step usefulness before a feedback/PID/MPC controller is introduced. Meter permission caps upstream release, not necessarily downstream instantaneous entry after propagation/storage. Complete road-total density/flow/speed/count history and ramp history, common known forcing/geometry/parameters, all-stream time through clearance are retained. Multiple ramps and detailed gap-timed/CAV control are not this first task.

Sources:

- [misc/selective_discreteness_ramp_metering_review/reporting/rm7_20_method_first_task_formulation_and_gate.md](../selective_discreteness_ramp_metering_review/reporting/rm7_20_method_first_task_formulation_and_gate.md)
- [misc/selective_discreteness_ramp_metering_review/synthesis/rm7_post_selection_design_inventory.md](../selective_discreteness_ramp_metering_review/synthesis/rm7_post_selection_design_inventory.md)
- [misc/selective_discreteness_ramp_metering_review/reporting/rm9_current_handoff.md](../selective_discreteness_ramp_metering_review/reporting/rm9_current_handoff.md)

### 11. Ramp CTM: lateral and forward flow

The adopted kernel is a lane-aware cell-transmission model, with continuous vehicle-equivalent mass in each physical mainline lane and longitudinal cell, and discrete time steps. It is not one lumped mass for an entire lane or individual vehicle dynamics. Three adjacent cells are shown schematically, not as an approved cell count or completed network geometry. First apply bounded paired density-driven lateral transfers within every cell; these conserve its two-lane total. Then recompute ordinary CTM sending and receiving from post-lateral masses. At an ordinary interface, accepted lane flow is the minimum of upstream sending and downstream receiving. The time-step mass balance adds h times total accepted inflow f and subtracts h times outflow q. The ordinary min formula is not applied independently to each input at a merge: mainline and ramp still share one receiver under positive input priorities with unused-supply redistribution. Metered ramp releases must propagate through storage before entering that junction; exact ramp geometry and boundary transcription remain open. Transverse and longitudinal resources are separate in the approved adaptation: no original-budget-minus-lateral cap remains. Lane exchange changes occupancy and therefore flow offers and storage availability, not physical lane capacity; throughput improvement is not guaranteed. Nagalur Subraveti supplies lane-wise CTM/exchange antecedents and Wright et al. supplies the node allocator; their composition is an approved review adaptation, not a reproduced calibrated paper. The FD functions and accepted time-step/storage bounds are in the source audit. Diagram blocks are symbolic occupancy, not computed mass or traffic results. The visible lateral equations now retain the accepted bounded operator: A is a directed preference between zero and one, positive only when the density advantage passes the approved threshold; lambda is limited by that fraction of the donor pre-exchange sending and by recipient pre-exchange receiving in the same longitudinal cell. Multiplying the incoming-minus-outgoing lateral rate by h gives each lane's post-exchange mass. The terms cancel when summing lanes. This D/S-bounded exchange inherits the approved time-step/storage restrictions. A is not a new control action; the open-loop meter rate remains the common actuator. The exact normalized density-contrast preference, its propensity/threshold parameters and empty-cell convention remain defined by the existing source audit. Forward D/S are recomputed after the lateral stage, as displayed.

Sources:

- [misc/selective_discreteness_ramp_metering_review/discussion/rm9_resource_b_approval_and_continuation.md](../selective_discreteness_ramp_metering_review/discussion/rm9_resource_b_approval_and_continuation.md)
- [misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex](../selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex)
- [Primary source](https://repository.tudelft.nl/file/File_2c4359e7-5e5a-4651-964f-6f3610ab89ae)
- [Primary source](https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Wright_node_models_transportation_networks_Transportation_research_B_2017.pdf)

### 12. Ramp lane contrast is not yet certified hidden

Lane contrast is a candidate state omission, not an established hidden-information result. On the strict ordinary free-flow B branch, total post-lateral mass and aggregate actual flow reconstruct the two-lane split when known mobilities differ. A separate passage-speed observation is retained, not replaced by Q/K. The geometric illustration uses normalized c1=1,c2=1.5, masses (2,8) versus (6,4), both total 10 but flows 14 and 12. This is hand algebra, not matched history or calibrated traffic. A pre-transfer map can also collapse states; if all remaining state/forcing agree and actions act only afterwards, that lost coordinate cannot change actions. Congested/receiving-limited states need the full observation map and complete prior-history audit.

Sources:

- [misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex](../selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex)
- [misc/selective_discreteness_ramp_metering_review/extraction/rm9_separate_resource_claims.md](../selective_discreteness_ramp_metering_review/extraction/rm9_separate_resource_claims.md)
- [misc/selective_discreteness_ramp_metering_review/reporting/rm9_50_separate_resource_findings_and_observer_gate.md](../selective_discreteness_ramp_metering_review/reporting/rm9_50_separate_resource_findings_and_observer_gate.md)

### 13. Ramp gradients follow final departure timing

The conceptual chain is common meter parameter theta -> releases -> post-meter storage/propagation -> shared receiving -> accepted merge and lane response -> complete final departures -> all-stream system time. The displayed sensitivity identity assumes fixed common arrivals/initial mass and clearance horizon, complete population accounting and fixed active branches. E is final system exit flow, not local ramp merge entry; P is all waiting/road/ramp mass. Blocked meter perturbations may have zero derivative. Queue relocation with identical departures cannot improve total time. Smooth active-branch composition is available but whole-chain numerical correctness and independent usefulness remain unestablished; no numerical traffic or gradient tests are claimed.

Sources:

- [misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex](../selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_separate_resource_and_observer_audit.tex)
- [misc/selective_discreteness_ramp_metering_review/synthesis/rm8_task_gradient_reference_screen.md](../selective_discreteness_ramp_metering_review/synthesis/rm8_task_gradient_reference_screen.md)

### 14. Different evidence levels; one common test

Synthesis as of 2 October 2026: VSL S13 closed positively only as a conditional analytical member. Ramp RM9 is active at the G1 observer-contract gate; UG3.B resource amendment is approved, observer alternatives UG4.A/B are not. Idealized FD passage-speed benchmark is recommended but not adopted; measurement/source-first review is the other route. No complete ramp history/action witness or independently useful gradient exists. The next measurement decision may alter identifiability and therefore cannot be assumed. Both tasks allow aggregate-plus-scalar sufficiency rather than require full lane resolution, vehicle identity or discreteness. This slide deck does not advance any research gate or authorize experiments.

Sources:

- [misc/differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md](../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md)
- [misc/selective_discreteness_ramp_metering_review/reporting/rm9_current_handoff.md](../selective_discreteness_ramp_metering_review/reporting/rm9_current_handoff.md)
- [misc/selective_discreteness_ramp_metering_review/reporting/rm9_50_separate_resource_findings_and_observer_gate.md](../selective_discreteness_ramp_metering_review/reporting/rm9_50_separate_resource_findings_and_observer_gate.md)

