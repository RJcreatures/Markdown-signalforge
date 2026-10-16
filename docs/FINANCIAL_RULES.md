# Financial correctness safeguards (to implement and test)

- Preserve source label, financial definition, units/currency, period start/end, duration, consolidated/standalone basis, segment and publication date separately.
- A number appearing on a PDF page is not enough; match the correct row label and period column.
- Financial growth requires compatible definitions, identical scope and comparable durations.
- Normalize lakh/million/crore explicitly while retaining original values and units.
- Revenue is a period flow; receivables are balance-sheet snapshots. Receivable-days is generally a proxy when credit sales are unknown.
- Never annualize transitional financial statements without a valid comparable disclosure and documented methodology.
- Never label consolidated minus standalone as subsidiary operating result.
- Never use two-peer Z-scores as compelling statistical proof.
- A changing metric is not automatically causal; investigate M&A, restatement, seasonality, changes in policy/definition, and peers.
- Missing volume data stays missing. No inference of volume from revenue alone.
- Validate all outputs against original source and calculations before reporting.
