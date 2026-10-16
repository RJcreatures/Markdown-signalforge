# Source discovery and provenance — implementation plan

**Never imply sources were fetched by the scaffold.** These are proposed source classes, not guaranteed automated endpoints.

## Priority order
1. Issuer investor relations financial reports, annual reports, quarterly results, presentations and company announcements.
2. NSE/BSE public company filings and financial results (when permitted and technically accessible).
3. Separate peer issuer filings for meaningful comparisons.
4. Government/industry/regulatory publications for independent context.
5. Credible news and aggregators as research leads — **not** the final numeric authority.

## Document processing chain
Company identity → generic search queries → ranked candidate URLs → URL and issuer source classification → permitted download → byte hash and raw store → page-level text / official XLSX cells → document date, fiscal coverage and consolidation basis → passage segmentation → structured observation candidates → row/column validation → normalized unit/period record → SQLite and FTS5 index.

A published claim requires independent original evidence, a correct calculation, and a citation that supports that specific claim.
Do not equate an aggregator and its linked issuer filing with independent sources.

## Availability caution
URLs and access rules change. Do not assume direct NSE/BSE JSON endpoints or third-party aggregation allow bulk automated access. Prefer permitted official PDFs/XLSX and respect robots, terms, rate limits and copyright. If blocked, use another approved public location; don't bypass restrictions.
