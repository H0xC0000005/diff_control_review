# Continuous lane family: transferable structure and nontransferable rules

Date: 2026-10-01. Claims RM8-C05/06.

**RM0004**, [repository final paper](https://repository.tudelft.nl/file/File_3728cefd-b910-49de-a341-d342fbbd5369),
Sections 2.1–3: incentive-driven lateral CTM flows, D-ALINEA feedback, joint
lane-change control. Incoming ramp flow is prioritized; the authors exclude
mainline congestion spilling onto the ramp. The SQP variables are lane-change
flows, and origin queues are included in the objective. Those rules/gains cannot
be inherited as proof for finite-receiving, rate-only open-loop control.

**FB0030**, [source publication](https://doi.org/10.1080/21680566.2019.1700846):
continuous lane-density conservation and finite lateral receiving are useful
candidate structures. The [existing source audit](../../../differentiable_freeway_bottleneck_task_review/extraction/n2_source_studies/FB0030.md)
records empty-density denominators, mode changes and the distinct branch at
printed equation 17. Methods pages were rechecked locally. No smoothing,
branch repair or full published-model adoption is approved.

**Review inference:** First audit a compact shoulder/rest grouping against the
published detailed laws. A physically defensible reduction must conserve mass,
share receiving budgets and preserve ramp feasibility. The group/rest relation
must be tested dynamically; a plausible state name is not a valid closure.
