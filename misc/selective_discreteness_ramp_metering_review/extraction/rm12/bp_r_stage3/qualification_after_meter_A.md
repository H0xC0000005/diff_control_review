# BP-R Stage 3 — qualification after upstream-admission approval

**Subsequent source update:** the first two originals have now been supplied and
read. Their CM/local IT laws supersede this pass's access limitation. Read
[supplied-original qualification](supplied_originals_audit.md) and the current
[S3-G2-N gate](../../../reporting/rm12/bp_r_stage3/merge_allocation_gate.md).
The dated findings below remain historical; the third construction is still
unverified, not a blanket blocker for a source-grounded adaptation.

Date: 2026-10-06. **S3-G2.A and S3-G2-M.A approved; stopped at source qualification.**
This is a bounded source/static review. No traffic run or new physical law is adopted.

## What A now means

The common open-loop rate limits admission from counted waiting into a finite
KW ramp approach. Ramp travel and congestion separate actual admission from
later entry into the freeway. A rate reduction does not directly stop mass that
has already entered that approach. All waiting remains in the complete objective.
The [selected interface](../../../synthesis/rm12/bp_r_stage3/upstream_admission_interface.md)
transcribes this decision without importing an ACTM merge law.

This first formulation concerns the ramp approach's aggregate traffic state and
the disturbance generated at freeway entry. It does not claim to resolve
individual red/green release, physical stop-line launch or acceleration before
the merge. A first-order approach can carry congested sending conditions without
being an independently validated model of stopped vehicles accelerating from a
signal. This limitation was explicit in the approved A candidate.

## Evidence followed and access level

| Source | Selected evidence read this pass | Consequence and limitation |
|---|---|---|
| RM0011, [2004 working paper](https://escholarship.org/content/qt8w70q261/qt8w70q261.pdf), Sections 2–3; references 12, 16, 20, 29–30 | Continuous lane conservation and current-state demand/receiving; discretionary IT allocation; sending-lane speed initializes a disturbance; mechanical/downstream constraints on motion. The full motion algorithm is referred to other sources. | Supports the structure, not a complete implementation-independent motion/allocation transcription. Mandatory lane changes are explicitly not treated by this working paper's allocation discussion. |
| RM8-P01, [2005 conference manuscript / 2007 chapter](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf), Sections 2–4; references 22–25 | KW ramp, point merge, finite lane capacity, priority adjustment; empirical metering/discharge observations and source tests with varied ramp inputs. Source distinguishes queued and unqueued ramp regimes. | A is an upstream input adaptation. Source evidence makes a consequential mechanism plausible but does not establish this adaptation's full-TST benefit. Exact mandatory-entry allocation still refers to another source. |
| RM12-S3-A01, 2006 journal version, DOI 10.1016/j.trb.2005.04.003 | Institutional record and indexed original introduction confirm the appendix contains CM. CiteSeer original PDF fetch returns 403. | Existing metadata/preview record reused; no newly read appendix. The working paper and journal version are not silently equated. |
| RM12-S3-MA01, Laval 2004 dissertation, *Hybrid models of traffic flow: impacts of bounded vehicle accelerations* | Author-uploaded metadata identifies the dissertation cited by RM0011 reference 29. Public download/read links were followed; browser retrieval failed. A normal direct download failed inside the sandbox on DNS, then the same escalated command returned HTTP 403. | A legitimate alternative source lead, not newly obtained full methods. No access restriction was bypassed and no local full thesis is claimed. |
| RM12-S3-MA02, Laval–Daganzo 2003 submitted/TRB manuscript, *A hybrid model of traffic flow: impacts of roadway geometry on capacity* | RM0011 reference 20 and indexed author institutional publication list identify this CM antecedent. Direct institutional page retrieval failed with 502. | Bibliographic lineage only. Neither a published final method nor an accessible complete source was established. |
| RM12-S3-A03, 1995 gridlock report / related 1996 chapter | Institutional metadata confirms the report; RM8-P01 reference 25 identifies the 1996 chapter, pages 629–646, as its merge-boundary antecedent. | No full boundary construction newly read. The report and chapter require version comparison if either is supplied. |
| RM12-S3-A02, 1997 IT article | Prior institutional citation/access record retained; actual allocation need reconfirmed by the working paper. | No full-method upgrade in this pass; do not infer the complete algorithm from its abstract. |

Six executed nearest-citation searches in two batches are in the
[meter-A continuation log](../../../search/rm12_bp_r_stage3_meter_A_query_log.csv).
The [source records](../../../screening/rm12_bp_r_stage3_meter_A_records.csv)
separate reused methods, indexed introductory evidence and new bibliographic
leads. Secondary model descriptions were excluded from technical qualification.
Search failure does not prove that these original works are unavailable elsewhere.

## Mechanism and limits after the approved adaptation

The source's credible causal hypothesis is: regulate incoming ramp traffic;
change the approach's congestion and actual entry conditions; change the
accelerating disturbances and induced freeway lane changes; change downstream
discharge. Under A, travel and receiving mediate the first two links. Complete
TST then depends on the resulting exit history and all retained waiting.

RM8-P01 Figure 6 and Section 4 provide a particularly relevant warning against
using input flow alone as the closure: the reported source simulations can have
different discharge under the same ramp input flow, with different ramp-queue
regimes. This is source-model evidence for a state-dependent effect. It is not
an equal-observation-history certificate, proof that a compact queue/speed-memory
model fails, or a common-offered-population TST comparison of our selected A.

Metering can change where waiting sits. If complete exit histories remain the
same, full TST also remains the same. Consequently a source's higher freeway
discharge or shorter freeway queue cannot alone demonstrate net benefit. A
well-posed comparison could test whether earlier exits compensate for holding
cost, but a task whose motion/allocation law remains unbound cannot be delegated
to an experiment to supply that missing law.

## Exact unresolved source transfer

1. **Motion/flow coupling:** how a new trajectory is constrained by acceleration
   and downstream traffic, how overlapping restrictions interact, and how it
   modifies the continuous flow. A guessed minimum-speed clamp is not a qualified
   substitute for CM.
2. **Competing flows:** the actual IT update and mandatory ramp merge allocation.
   The 40% adjustment is a source priority/device parameter, not an extra 40%
   supply budget or an automatically known fixed merge fraction.
3. **Ownership and timing:** confirm where transferred mass is carried while
   disturbance descriptors move, and how threshold births are located/timed.
   The continuous balance supports counting mass once, but that does not prove
   exact equivalence of every proposed overlay to the full source.

These are source qualification dependencies S3-E1.C, not permission to change
the approved actuator or a demand to execute SUMO. The
[source qualification checkpoint](../../../reporting/rm12/bp_r_stage3/source_qualification_checkpoint.md)
bundles the smallest missing originals and distinguishes source access from a
new scientific adoption decision.

## Disposition

S3-E2.M's admission/holding accounting is transcribed. The physical mechanism
remains supported in principle; exact E1/C coupling and dependent E2/E3 laws are
not frozen. Independent reduction obligations and complete-objective limits
are explicit, without claiming their performance has been resolved. Stage 3 is
incomplete and Stage 4 unopened. This is an evidence/access-limited checkpoint,
not a new structural negative or a closed review result.
