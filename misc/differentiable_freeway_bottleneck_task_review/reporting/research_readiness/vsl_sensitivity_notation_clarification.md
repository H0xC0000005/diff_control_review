# Sensitivity notation: reference the scalar work function explicitly

Date: 2026-10-20. **Requested editorial clarification completed.**

[Revised PDF](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_compact_methods_report.tex)

Part 5 now identifies H as the scalar service-work function from Section 3.3,
with a clickable reference to equation 5. It defines the three H-subscript
terms as first partial derivatives with respect to E discharge, A discharge
and A's representative boundary speed. They measure marginal changes in
required work with the other arguments fixed, at the current service solution.
The new paragraph is red under the continuing review instruction.

Only the current report source/PDF and dialogue change. All 11 displayed
equation groups, the service table and the seven IEEE references retain
their exact source. The feedback inbox is unchanged. Exact prior source/PDF
are retained in the [v3 archive](../../synthesis/research_readiness/vsl_report_versions/v3/README.md);
earlier records are preserved. No modeling assumption changes.

After initial label resolution, two final passes use the installed toolchain
from `synthesis/research_readiness/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_sensitivity_notation_latex vsl_compact_methods_report.tex
```

[Final build log](vsl_sensitivity_notation_build.log)

Artifact checks use the installed review Python/pypdf environment:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_sensitivity_notation_checks.py
git status --short
```

[Verification record](vsl_sensitivity_notation_validation.json)

The PDF remains four physical pages with about 3.42 methodology pages
excluding references, within the 3.5-page target; main text remains 10 pt.
The final build has no warnings or box problems. Checks verify the added
red paragraph, resolved equation-5 destination, unchanged mathematics/table/
references, archive/protected hashes and feedback preservation. PDF text
and drawing instructions are inspected; no raster inspection is claimed.

This is a Step 4 report clarification, complete for user reading. No new
methodological choice, simulator change, dependency installation or traffic
experiment occurs. The next allowed action is a requested report correction;
no subsequent review or implementation work starts automatically.
