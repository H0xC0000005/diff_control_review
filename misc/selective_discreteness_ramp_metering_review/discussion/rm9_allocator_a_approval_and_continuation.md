# RM9-UG1.A approval and conservative continuation

Date: 2026-10-01. Decision: **Candidate A approved as Default; RM9-UG1 closed.**

The user endorsed automatic allocation of unused receiving capacity, called the
model good to go as a default, and instructed continuation with Candidate A.
The user also requested a clearer understanding of how service rules affect the
control outcome. This closes the allocation-family question without another
confirmation. It does not close RM9 or approve an entire local lane-flow model.

## Adopted contract

Use positive structural input priorities independent of current offers and the
meter action. Unused supply is redistributed among inputs physically eligible
for the same receiver. Respect each donor and the shared receiver. Hold priorities
and their declared interpretation common across comparisons; retain priority
ratios as parameters, not values chosen to create a positive result.

**Decision vocabulary:** the allocation family is Default, as explicitly stated
by the user. Changing it for evidence-based reasons requires a documented
reconsideration; it must not be silently promoted to Fixed. Existing fixed
conservation, finite receiving and comparison/accounting contracts remain fixed.

Automatic redistribution allocates physical supply; it is not a new lane-control
actuator, guaranteed ramp entry or a license to use spare capacity on another
lane without a permitted transfer. The meter still sets upstream release
permission; propagation determines the later offer at the merge.

## Work completed after approval

Transcribed the two-input one-receiver law, proved its offer/receiving bounds and
work conservation, derived its ordinary derivatives away from branch ties, and
prepared hand calculations explaining queue redistribution versus total service.
Audited source transfer and receiving branches and screened an existing
multi-lane control predecessor. No simulation, production code or numerical
traffic/gradient experiment was performed.

The continuation reached **RM9-UG2**, a distinct local-physics adaptation decision.
The approved allocator does not specify autonomous lateral offers, their
conservative coupling to longitudinal motion, or capacity-loss physics.
See the [continuation findings and gate](../reporting/rm9_30_allocator_contract_and_control_chain.md)
and [mathematical PDF](../synthesis/rm9/rm9_priority_allocator_and_control_effects.pdf).
The core history/action and useful-gradient claims remain unestablished.
