# N2 metadata/version audit — access history and resumption

Date: 2026-09-16. Existing manifest rows/texts preserved; four new rows appended.
The access-pause notes below are historical; the resumption section supersedes
their pending-access/inspection status without deleting the audit trail.

- FB0001: original arXiv identifier is 1310.2658; archived first page dates the
  manuscript October 29, 2018. N1 registry's 2013 is original-submission lineage,
  not the inspected version date. Cite version/location explicitly in N2.
- FB0003: archived TU Delft cover identifies the final published 2018 paper,
  IFAC-PapersOnLine 51(9), 343–348, DOI **10.1016/j.ifacol.2018.07.056**.
  Corrected N1 findings report's erroneous .062 hyperlink; no substantive N1
  conclusion, archive entry, or source file was rewritten.
- FB0007: inherited cover/title/authors checked; actuator boundary remains
  direct connected-automated-vehicle speed control, not primary infrastructure
  advice. No new N2 usefulness conclusion is claimed.
- FB0013: author-university metadata verifies authors, 2020 issue, 146(8),
  04020074, and DOI. Full-text methods remain E1 until access succeeds.
- FB0021: primary publisher discovery and authorized abstract metadata verify
  Chen/Ahn, 2015, TRC 51, 210–230, DOI .2014.10.015. Full text not inspected.
- FB0022: official Wiley full HTML, first published April 23, 2025;
  DOI 10.1111/mice.13492. Stable methods/results locations recorded below.
- FB0023: open UF author PDF title differs from a discovered published-title
  lead. Publication/version reconciliation is pending, not silently asserted.
- FB0024: open UMD PDF lead; DOI 10.1061/JTEPBS.0000481. Detailed methods
  extraction remains pending.

## New web-only full-text notes

FB0020: [author text](https://www.researchgate.net/publication/321448438_Integrated_control_of_highway_traffic_flow),
Zhang/Ioannou, DOI 10.1080/23307706.2017.1402715, online 2017/issue 2018.
Introduction and sections 3.1–3.3 inspected; full results extraction pending.
No local full-text snapshot was archived in this access-stop pass.

FB0022: [official full HTML](https://onlinelibrary.wiley.com/doi/10.1111/mice.13492),
Wei/Han/Wang, 2025. Sections 1.2/2.1: entry-time speeds coexist in a link,
with scalar noncompliance and no overtaking/lane changing. Binary distance-based
exit selection and a duration-triggered capacity-drop indicator appear in
2.1.1/equation 10. Section 3.2 compares forward results with SUMO and
instantaneous-adoption CTM; 3.3 uses real constant-speed-limit data for drop
assessment. These checks do not establish our gradient contract. No local
snapshot or new manifest hash is claimed. Quantitative results were not adopted.

New available author/university PDFs FB0023/FB0024 were opened at their abstracts,
not archived or upgraded to methods-level E3. Access URLs and inspection limits
are in [n2_access_log.csv](../../search/n2_access_log.csv).

## Resumption after user supply — 2026-09-16

- FB0013: final published 15 pages, title/authors/DOI/article identity match;
  unencrypted, every page extractable. Full methods/results inspected. E3.
- FB0021: final published 21 pages, TRC51:210–230, January6-2015 online date,
  title/authors/DOI match, Appendix A present, every page extractable. E3.
- File sizes and SHA256 are in the manifest and main findings. Hashes establish
  supplied-file identity, not byte authenticity against a publisher checksum.
- FB0026: author report19-022, 23 PDF pages; cover cites TRC100:15–33 March2019,
  DOI10.1016/j.trc.2019.01.001. Archived with new unique filename/hash. Same
  research lineage as FB0003, explicitly stated by the introduction.
- FB0030: final university copy, 24 pages including covers. DOI and page range
  agree; repository/copyright2019 versus article header2020 retained, not resolved
  by guessing. New unique filename/hash.
- FB0024: full university PDF methods/field evaluation now inspected, E3 at
  those locations; no local snapshot/hash claimed. FB0004 author full text now
  inspected at methods, likewise web-only. FB0020 remains selected-methods only.
- FB0033: title/authors/DOI verified; July15-2026 version of record verified
  on publisher notes. Publisher-provided full text on ResearchGate inspected
  at methods/results/data statement despite primary-page429. Web-only, no local
  snapshot/hash claimed. Data by request does not count as acquired data.
- RM0025 final title verified on inherited cover: Discrete adjoint gradient
  computation for multiclass traffic flow models on road networks. Published
  August20-2026 on Springer. Reused in place, no closed-package modifications.
- Recent arXiv metadata rechecked: FB0007 v2 August10-2026; FB0008 v1 January9,
  related DOI10.1109/FISTS67319.2026.11421764; FB0009 v1 March9-2025; SEO2026
  v3 April29-2026. Old PDF hashes untouched. These are boundary/version checks,
  not certification that every inherited PDF is the latest content.
- FB0023 version/title correspondence and FB0027 exact full methods unresolved;
  FB0028/31/32 are labeled leads. No gate conclusion depends on uninspected
  source equations or absence of their results.

Rich claim context and original/adapted model boundaries are in
[claim context](../../extraction/n2_claim_context.csv) and linked source studies.
No closed source archive, user feedback, original result or mainline file edited.
