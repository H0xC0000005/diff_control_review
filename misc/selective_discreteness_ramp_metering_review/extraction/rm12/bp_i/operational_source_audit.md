# BP-I Stage 1 — operational source and access audit

Date: 2026-10-06. Selected primary locations inspected under the approved
[protocol](../../../rm12_40_bp_i_stage1_protocol.md). Source facts below do not
adopt a new observation, traffic or actuator law. See the
[source ledger](../../../screening/rm12_bp_i_records.csv) and
[executed query log](../../../search/rm12_bp_i_query_log.csv).

## Source observations and their limits

| ID / version | Location and supported fact | Transfer limit |
|---|---|---|
| RM8-P02; final paper, 2021 online / 2022 issue, DOI 10.1177/03611981211033861 | Printed pp. 91–93: conventional control uses interval-aggregated loop data; obtaining individual gaps requires different processing. Printed p. 95: reference flow/speed detectors are 200 m upstream of merge start. Printed p. 97: reference parameters follow recorded specifications; site intensities were logged. | Algorithm inputs, processing capability and accessible archives are different evidence claims. No complete controller-knowledge contract follows. |
| RM8-P02, same version | Table 1, printed p. 94, inventories the proposed design and simulation use. Printed pp. 95–97 distinguish reference control from extra gap/class sensing and release logic, with sampled driver acceleration and lane-demarcation assumptions. | Do not attribute every proposed detector to the deployed reference. Do not transfer a sensing-and-actuation comparison into a common-rate representation result. |
| RM9-O01; FHWA Traffic Monitoring Guide 2022 | Traffic Data Collection, Individual Vehicle Records / Speed / Lane Occupancy / Headway and Time Gap: detector-zone time, passage speed and event records have distinct supports; individual reporting entails processing/storage choices. | Hardware capability does not certify this site's channel availability or retained history. These definitions alone prove neither reconstruction nor ambiguity. |
| RM9-O04; author report 17-001, journal publication 2018 | Sections 4.1–4.2: sequential point-to-section estimation carries initial/internal traffic; the multilane extension excludes lane changes. Assessment passage, PDF p. 20 / printed p. 19: first-window initial conditions are supplied rather than estimated. | A serious reconstruction rival, not an exact identification theorem for a merging region or proof that its initial conditions are operationally available. |
| RM12-I01; Klomp MSc thesis, 2020 | TU Delft metadata identifies the thesis and original PDF. An indexed primary excerpt of Section 2.3, printed p. 12, describes the general RWS algorithm's upstream/downstream and ramp detectors, and possible use of existing motorway-system loops. | Full PDF reads failed. The excerpt is general algorithm context, not confirmation of every sensor/access right at A13. No initialization or complete-history finding is based on inaccessible thesis sections. |
| RM12-I02; TrafficQuest third-generation TDI technical note, undated | Entire one-page primary infrastructure note: metering algorithm, process control and central management are separate interfaces; tools produce graphs/overviews from logs. Official tools page establishes the hosting provenance. | Logging infrastructure deserves inclusion in the strongest information rival. This note does not bind the A13 generation, log contents, retention, access latency or physical initial state. Its undated deployment counts are not used. |
| RM12-I03; dataset DOI 10.4121/14791917, available 2021 | TU Delft institutional metadata describes videos, some trajectories and coordinate calibration at Delft-North, recorded 2019-11-05. | Research observations do not become operational controller inputs. Dataset contents were not downloaded or audited as an event archive. |
| RM12-I04; RWS specification v1.09, 2013 | Exact title/version verified in RM8-P02 reference 14; thesis citation context also located. | Original specification not retrieved. Controller initialization, channel/record interfaces and site configuration remain unsupported by this lead. Citation verification is not a method read. |
| RM12-I05; RWS manual, 1996 | Agency search metadata identifies an older manual and publication date. | Page fetches failed. Not the 2013 specification; no scientific conclusion or site configuration is extracted from it. |

Primary links and exact access grades reside in the source ledger. Reused IDs
retain their versions. I01 is a separate thesis, not another independent field
study; I03 is the associated research-data metadata. Do not count either as
independent corroboration of hidden-state/control benefits.

## Operational channel inventory

“Unsupported” means the selected evidence does not settle the field; it does
**not** mean unavailable or absent. Interpret definitions with RM9-O01; site facts
with RM8-P02; general algorithm context with access-qualified RM12-I01.

| Channel / compartment | Quantity, support and units | Knowledge/access assessment |
|---|---|---|
| Reference mainline detector stream | Count/flow over a point-detector window; vehicle count or vehicle/time. Speed concerns passages at the station; occupancy concerns detector-zone time. | Reference flow/speed use supported. Exact window, timestamp convention, lane-resolved reporting, individual records and complete accessible channels unsupported. Retain them if available. |
| Mainline section inventory / section speed | Vehicles physically inside a declared road section at an instant; vehicle-equivalent mass and distance/time. | Exact current section mass or mass-weighted section speed is not certified as a directly supplied reference channel. No detector-to-section identity is adopted. |
| Additional motorway loops | Potential earlier/later point records around the control region. | General RWS possibility supported only by I01's excerpt. Actual A13 coverage, processing and access remain unsupported. Do not silently exclude them. |
| External demand and pre-meter ramp queue | Arrival counts and waiting inventory before the stop line. | General ramp detection context is available; exact reference queue estimates, storage inventory and upstream arrival history are unsupported. The proposed design table does not settle them. |
| Meter command and actual stop-line releases | Permission/cycle setting versus traffic actually crossing the stop line. | These must be separate interfaces. Complete command/release logs, compliance and timestamp alignment are unsupported; permission is not a measured flow. |
| Post-meter ramp / merge entry | Released traffic still approaching a merge versus traffic accepted onto the mainline. | Neither a complete post-meter inventory nor actual merge-entry history is bound for the reference by the inspected evidence. Do not identify release with entry. |
| Research trajectories / fine reference truth | Videos and trajectories used by researchers. | I03 supports research availability, not online controller access or an initialization oracle. |
| Central/historical records | Stored measurements, control states or other logs, depending on installation. | Site intensity logging and general tools are supported. Event/lane content, time span and access are unresolved, not assumed nonexistent. |

## Nearest-source frontier and access handling

Twenty-one searches were executed, following the paper's specification/data
citations, its author's thesis and the agency-collaboration tools documentation.
Broad numeric-ID and strict PDF-path searches sometimes returned unrelated work;
those results are excluded rather than treated as negative scientific evidence.
The old manual and differently dated specification citations were not substituted
for v1.09. No wider task-family search was opened.

Initial direct access to the TrafficQuest technical PDF failed; following the
official page's link succeeded. Thesis PDF access failed at both Edulab and TU
Delft, including a later retry; only metadata and the identified excerpt are
claimed. Dataset DOI access failed, while institutional metadata succeeded. An
RM8-P02 Table 1 screenshot failed; the text heading/context was read, and no
claim depends on ambiguous table-column alignment. Failures are retrieval limits,
not evidence that sensing, initialization or logging does not exist.

No paper binaries, videos, datasets, software or environment changes were made.
