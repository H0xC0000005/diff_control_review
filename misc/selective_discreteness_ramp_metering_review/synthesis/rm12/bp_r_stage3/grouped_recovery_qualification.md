# M1 — grouped recovery state and its reduction contract

Date: 2026-10-07. **Bounded qualification completed to S3-G2-Q-G; no concrete
grouping law adopted.** M1 is approved, not rejected. See
[plain-language findings and gate](../../../reporting/rm12/bp_r_stage3/grouped_recovery_findings_and_gate.md),
[source audit](../../../extraction/rm12/bp_r_stage3/grouped_recovery_source_audit.md)
and [equations/proofs](grouped_recovery_math.pdf).

## 1. What the state expansion resolves

Joint position and speed information can distinguish which recovery state meets
which local traffic condition. Separate marginals cannot generally do this.
The source's sampled motion requires current realized speed, its desired-speed
phase, position, lane, fixed motion parameters and consistently computed own
downstream speed. A complete sample-boundary state may store realized speed and
derive the next desired speed; an intermediate phase cannot discard the desired
speed before the coupled traffic constraint is applied.

For a fixed admissible own-field estimate, the corresponding joint-state update
can be written as a pushforward. This qualifies a representation operation;
it does not prove existence/uniqueness of the previously partial joined
birth/node/crossing solver. An atomic measure retains every original state.
It is lossless and potentially large, not automatically a compact model.

G01 supplies related independent distribution dynamics under different kernels;
G02 supplies declared kinetic-to-moment approximations. Their native equations
are alternatives with different constitutive assumptions, not source-matched
ports. G03/S02 retain boundary-specific count/trajectory coupling; G04's
single-boundary stability theorem does not bound our grouped projection.
Source details and exact transfer limits are in the audit.

## 2. A concrete lossless grouping rule is conditional but defensible

Define a complete signature at a declared update phase: lane, exact position,
realized/required desired speed, fixed acceleration/type parameters and the
moving-count association or other service data required by the own coupling.
Records can share a group only if these are identical and no remaining source
rule depends on their names. Retain multiplicity separately from road mass.

Advance the common signature once using the group's own traffic field, the
unchanged CM and the same sample timing. Identical signatures have identical
updates if the coupled solution is well defined. Apply duplicate identical
zero-passing constraints once: duplicating the same constraint inequality does
not strengthen it. In a minimum-combination count solver, this is idempotence
of the identical contribution. Preserve each generating stream's birth phase;
grouping cannot replace those phases with one global ramp counter.

The ordinary road/ramp/waiting field continues to count every mass transfer.
The multiplicity records descriptor bookkeeping, not extra vehicles or an
extra service debit. Birth signatures are generated from this model's own
actual transfer, donor speed, declared location and source timing. They join a
group only if they really match; simultaneous births or a common cell do not
alone prove identical placement or service association.

This proves conditional reduction from duplicate records to distinct signatures.
It does not guarantee such duplicates occur naturally in a qualified task,
resolve nonidentical coincidences, or prove full model closure. Keeping a
temporarily nonbinding signature is still necessary unless future redundancy
has been certified. Earlier wave effects stay in the traffic field; deleting a
duplicate description does not erase or duplicate that field.

## 3. Nearby states need a reconstruction or a stronger certificate

The new static examples show two different gaps.

- **Joint association:** swap a slow and a faster state between locations with
  different downstream speed caps. Position and speed marginals stay the same,
  but the next realized-speed sum changes. A coarse spatial bin containing both
  locations can also miss this, even with separate velocity bins.
- **Within-group transport:** two position lists can have the same count and
  mean position inside a cell, with the same speeds, yet different numbers cross
  its boundary on the next source position update. Bin count plus mean does not
  determine its exact future transport.

These are local algebraic projection obstructions, not equal-history traffic
pairs or full-TST/control effects. More spatial detail, a subcell profile,
extra supported statistics, or a source-supported restricted family may resolve
them. There is no theorem here against every finite summary or approximate model.

Writing exact integrals over an unknown sub-bin distribution does not close the
grouped model. Calling the reference for that distribution would violate the
comparison. A closed approximate candidate must instead declare a reconstruction
from its own state, then derive its own transport and traffic coupling. Choosing
uniform occupancy, mean representatives or quadrature points is a scientific
adaptation, not a storage-format implementation detail.

Refining a bin later cannot reveal lost member locations. A refinement must be
derived from retained own information, preserve explicit uncertainty, or rely
on an approved reconstruction. Storing a hidden full trajectory list for later
refinement is detailed state and must be counted as such.

## 4. Service is a coupled constraint, not the sum of group penalties

The retained recovery state must supply the location-sensitive restriction to
the same conservative traffic field, including count association and local
speed feedback. A group count or its average speed alone is not an exit-flow
law. Distinct restrictions interact through waves and receiving. Independent
additive capacity debits would change that mechanism and are not adopted.

For already qualified trajectory contributions, lower/upper component bounds
give lower/upper minimum-count bounds. This is conditional algebra, not a new
certified grouping method. Coupled trajectory, domain-of-influence and event
errors must be bounded too. Bounds on cumulative counts cannot simply be
differentiated into pointwise flow bounds.

An activity certificate must show a group's restrictions impose no additional
constraint under the declared own coupling. Uncertain groups cannot be treated
as definitely active or inactive. A conservative extra penalty in a genuinely
inactive state can violate the current T1 requirement. Present nonbinding status
does not establish permanent removal.

## 5. Information, complexity and task consequences

Let K be descriptor count and H the count of distinct exact signatures. The
lossless candidate keeps H motion/service signatures and multiplicities, plus
the shared road state and per-stream birth phases. H can equal K. A hashing/
canonicalization organization can reduce duplicate motion evaluations, but
moving-boundary interaction work still depends on the source solver. No total
linear runtime, guaranteed reduction ratio or numerical cost target is claimed.

A finite-bin candidate keeps B joint position/velocity groups and its chosen
extra statistics; its state size can depend on B rather than K. Any hidden
member records, retained birth histories and adaptive substructure count toward
that size. Reconstruction and service work must be declared before making a
complexity comparison. An untruncated distribution is not finite-dimensional
merely because it has one name.

The lossless endpoint gives equivalence evidence, not a coarse-information
contrast. An approximate reduction can give a meaningful contrast, but a
discrepancy can include reconstruction/constitutive bias. The original
unresolved-information claim is not reinstated. Complete TST/action sensitivity
and gradients remain distinct obligations.

## 6. What is bound, and the next adoption boundary

**Supported reviewer deductions:** conditional identical-signature grouping;
the need for joint association in the displayed local update; transport
nonclosure of the displayed count/mean projection; conditional cumulative-count
and full-population finite-horizon TST relationships.

**Not qualified:** a reduced rule merging distinct nearby signatures under all
current source interactions; group-error/clearance bounds; a complete joined
compact competitor; rate leverage; useful gradients. The inspected literature
does not fill that exact transfer gap. This is an evidence limit, not absence
of all distribution models or a universal compactness impossibility.

The new **S3-G2-Q-G** decision distinguishes a source-preserving grouping contract
(G1, recommended first), a specified approximate reconstruction route (G2),
and accepting/parking this partial attempt (G3). None is adopted. G1 does not
admit the lossless endpoint as the sole genuinely compact rival; G2 does not
waive T1 or freeze a histogram. Existing reference/task/actuator contracts remain.
