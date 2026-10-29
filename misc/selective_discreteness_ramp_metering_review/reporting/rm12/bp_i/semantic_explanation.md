# BP-I conclusion in traffic terms

Date: 2026-10-06. Explanation of the completed result, not a new review pass or
scientific decision. [Current findings and gate](findings_and_gate.md) remains
authoritative. Subsequent [user closure](user_closure.md) records BP-R selection;
the explanation and evidence limits remain unchanged.

The core result is that a real controller uses coarse traffic summaries, but
we have not established that the detail omitted by those summaries remains
unknown after a controller uses everything legitimately available to it.
Neither has this step established that the omitted detail changes useful common
metering-rate decisions. The candidate therefore has not qualified as a positive
hidden-information task. This is a failure of positive admission on the bounded
evidence, rather than proof that the information is always recoverable.

## A traffic example of the distinction

For illustration only, suppose a detector reports six cars in thirty seconds,
with a mean speed of 90 km/h. Six cars spaced fairly evenly and six cars arriving
in two close groups with a long interval between groups could produce the same
count and mean-speed report. Their merge opportunities can differ. This example
shows how averaging can erase spacing; it is not an equal-full-history witness,
a reconstruction failure proof or an adopted traffic/control scenario.

If individual passage times are accessible, the two arrangements would already
be distinguishable at that detector. Other station records, earlier observations
or a known complete starting state under exact public deterministic dynamics
might also distinguish them or determine the relevant current traffic. Conversely,
we have not established that the actual reference installation supplies enough
information for that reconstruction. The published algorithm's use of averages
does not settle this wider knowledge question.

Even a quantity not directly sensed can sometimes be recovered from history:
in a closed road section known to start empty, twenty recorded entries and twelve
recorded exits imply eight remaining vehicles, assuming complete boundary
records and conservation. This recovers total inventory only; it does not by
itself recover lane allocation, positions or gaps. It illustrates why a missing
instantaneous measurement is not sufficient evidence of hidden information.

## What this step actually adds

The earlier idealized section observations cannot automatically be identified
with real point-detector averages. That is a genuine transfer limit. The bounded
source audit nevertheless leaves actual initial physical knowledge, all
accessible earlier records, lane/event formats and ramp release/entry coverage
incomplete. Some logging is supported, so its absence cannot be assumed.

The still-missing positive chain is: a genuine shared information setting;
different current traffic compatible with all that information; a difference
that matters to the same available metering-rate decisions and complete TST;
and a credible representation/gradient study. The illustrative spacing example
establishes none of the latter links. Targeting particular gaps also raises an
actuator issue; its benefit is not automatically a benefit of common rate actions.

A richer model cannot gain privileged knowledge of actual gaps merely by having
more state variables. If detail is truly unobserved by both controllers, its
estimation, uncertainty treatment or justified information source is a separate
obligation. If detail is accessible, an aggregate model with memory deserves the
opportunity to use it.

BP-R would explicitly ask a different, more bounded question: when initial
traffic information is declared and shared fairly, does compressing the traffic
into a qualified aggregate/memory representation preserve its response to
changes in metering? This assesses representation adequacy. It does not settle
the original ideal-history information claim, and still requires a genuine
control-relevant task. The user has now approved the BP-R claim/direction;
its [bounded protocol](../../../rm12_50_bp_r_stage2_protocol.md) records the
subsequently completed audit. [BP-R findings and BPR-G3](../bp_r/findings_and_gate.md)
is the current handoff; the Stage 1 explanation remains unchanged.

Sources and locations: [operational audit](../../../extraction/rm12/bp_i/operational_source_audit.md).
The reference averages and processing distinction are supported by
[Klomp et al., printed pp. 92–93](https://repository.tudelft.nl/file/File_c446bd9b-9a19-494b-9989-3d11f96fbb1a).
The numerical examples are reviewer illustrations, not field findings.
