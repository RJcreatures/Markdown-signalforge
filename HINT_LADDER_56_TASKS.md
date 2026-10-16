# Progressive hints (six levels) — one concept at a time

Read H1 before trying the assigned task. Only move to the next hint if stuck. No implemented code is provided.

## T01 Repository and environments — Both / A01
- **Level 1 — Objective:** Set up shared repo, Python env, ignore secrets/cache, define main package layout.
- **Level 2 — Boundaries:** Find this task in `README.md / pyproject.toml / .gitignore`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Both machines install project and run test command. Explain to the opposite teammate why the observed output meets this gate.

## T02 Run configuration — A / A01
- **Level 1 — Objective:** Define track, current timeouts, download limits, max sources, budgets and provider names as configuration.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/config.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Bad or missing settings fail with useful messages. Explain to the opposite teammate why the observed output meets this gate.

## T03 Core source and issuer contracts — B / B01
- **Level 1 — Objective:** Design Company, Document and Passage field sets, including source-group independence.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/contracts.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Ambiguous issuer, missing URL and missing document hash fail validation. Explain to the opposite teammate why the observed output meets this gate.

## T04 Observation and hypothesis contracts — B / B01
- **Level 1 — Objective:** Define Observation, CalculatedMetric, Claim, Hypothesis and Run state statuses.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/contracts.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Missing period/basis/units cannot pass as a validated number. Explain to the opposite teammate why the observed output meets this gate.

## T05 Test layout and fixture catalog — A / A01
- **Level 1 — Objective:** Create test locations for good PDF, HTML instead of PDF, invalid table, period mismatch and mock model response.
- **Level 2 — Boundaries:** Find this task in `tests/fixtures/README.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** A basic test runs on both machines. Explain to the opposite teammate why the observed output meets this gate.

## T06 Track-company resolution — A / A04
- **Level 1 — Objective:** Accept arbitrary issuer name/ticker; resolve official legal issuer and selected-track match.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/companies.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Unknown, similarly named and valid issuer inputs behave predictably. Explain to the opposite teammate why the observed output meets this gate.

## T07 Query-template builder — B / B02
- **Level 1 — Objective:** Generate reusable searches for annual report, latest quarter, presentation and exchange filing.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_search.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Two companies generate different correct queries with same code. Explain to the opposite teammate why the observed output meets this gate.

## T08 Search-provider adapter — A / A04
- **Level 1 — Objective:** Call one documented web search provider using configuration; parse URLs/titles.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_search.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Malformed/empty API replies do not crash; result count bounded. Explain to the opposite teammate why the observed output meets this gate.

## T09 Source URL classifier — B / B02
- **Level 1 — Objective:** Distinguish issuer IR, exchange, peer issuer, industry and aggregator source classes.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_search.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Same filing mirrored on two sites is not independent evidence. Explain to the opposite teammate why the observed output meets this gate.

## T10 Safe public HTTP downloader — A / A02
- **Level 1 — Objective:** Download allowed HTTPS file with limits, retry/backoff and safe redirect checks.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/downloads.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** 404, HTML masquerade, timeout and size limit handled. Explain to the opposite teammate why the observed output meets this gate.

## T11 Content hash and durable store — A / A03
- **Level 1 — Objective:** Write completed bytes safely; compute SHA-256; recognize duplicate content.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Same bytes twice map to one original artifact. Explain to the opposite teammate why the observed output meets this gate.

## T12 Metadata and issuer cross-check — B / B01
- **Level 1 — Objective:** Confirm filename/doc text matches intended legal issuer and document type/period.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_validation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Wrong-company PDF cannot become accepted evidence. Explain to the opposite teammate why the observed output meets this gate.

## T13 Source fallback policy — A / A03
- **Level 1 — Objective:** When official exchange fetch fails, try discovered issuer IR document; log failures.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/downloads.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** One blocked host never creates invented data or endless retries. Explain to the opposite teammate why the observed output meets this gate.

## T14 PDF page text extraction — B / B03
- **Level 1 — Objective:** Use PyMuPDF to extract per-page text, page indexes and flags.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/pdf_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Retrieved text can be located again on the saved PDF page. Explain to the opposite teammate why the observed output meets this gate.

## T15 XLSX/CSV intake (optional source format) — B / B04
- **Level 1 — Objective:** When issuer provides official XLSX/CSV, preserve sheets, rows and raw cells.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/spreadsheet_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Selected cell maps to original sheet and header. Explain to the opposite teammate why the observed output meets this gate.

## T16 Page passage segmenter — B / B03
- **Level 1 — Objective:** Split page text into retrievable contextual excerpts; preserve page and surrounding labels.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/pdf_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Quoted passage is recoverable within original page text. Explain to the opposite teammate why the observed output meets this gate.

## T17 Extract document dates and basis — B / B03
- **Level 1 — Objective:** Recognize financial year/quarter coverage, report publication date, consolidation tags and currency scale.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/pdf_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Unknown tags remain unknown, not defaulted to consolidated. Explain to the opposite teammate why the observed output meets this gate.

## T18 Numeric observation extractor — A / A06
- **Level 1 — Objective:** Locate one chosen comparable metric from a correctly labeled row/period; attach exact source passage.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/observations.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Wrong column or unit is rejected. Explain to the opposite teammate why the observed output meets this gate.

## T19 Extracted table quality gate — B / B04
- **Level 1 — Objective:** Check row-label/column-heading relationships and printed totals where available.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/extraction_quality.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Shifted column fixture fails; real checked row passes. Explain to the opposite teammate why the observed output meets this gate.

## T20 Unit and period normalizer — A / A06
- **Level 1 — Objective:** Normalize lakh/million/crore and fiscal periods without losing original meaning.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/observations.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Mixed unit, 15-month versus 12-month, and stock/flow mismatch fail. Explain to the opposite teammate why the observed output meets this gate.

## T21 Management/event claim extractor — B / B07
- **Level 1 — Objective:** Use structured LLM response to capture exact dated management statements and event labels.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/claims.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Any quoted words not grounded in stored passage rejected. Explain to the opposite teammate why the observed output meets this gate.

## T22 SQLite tables and links — A / A05
- **Level 1 — Objective:** Create relational tables for docs, passages, observations, calculations, hypotheses and runs.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Stored records preserve relationships and uniqueness. Explain to the opposite teammate why the observed output meets this gate.

## T23 FTS5 full-text index — A / A05
- **Level 1 — Objective:** Index exact page/passage text with metadata ID join.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Can locate trade-receivables/revenue passage by query and identify page. Explain to the opposite teammate why the observed output meets this gate.

## T24 Evidence retrieval API — B / B06
- **Level 1 — Objective:** Given research question and metadata filters, return a bounded ranked list of passages.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/retrieval.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Cross-company leakage and irrelevant fiscal periods filtered. Explain to the opposite teammate why the observed output meets this gate.

## T25 Source independence and duplicate origin — B / B06
- **Level 1 — Objective:** Track document content hash, original issuer/publisher and underlying origin.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/retrieval.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Mirrored same filing counted once; peer issuer filing is separate origin. Explain to the opposite teammate why the observed output meets this gate.

## T26 Comparable revenue growth — A / A07
- **Level 1 — Objective:** Implement first deterministic growth metric using matched period lengths and identical financial definitions.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Hand-calculated fixture passes; period/basis mismatch fails. Explain to the opposite teammate why the observed output meets this gate.

## T27 Receivable days proxy — A / A07
- **Level 1 — Objective:** Compute optional approximate receivable days with compatible revenue flow and balance snapshots.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Correct days-in-period handling; no false precision. Explain to the opposite teammate why the observed output meets this gate.

## T28 Financial anomaly candidate — A / A07
- **Level 1 — Objective:** Create a reusable rule identifying meaningful changes and data gaps.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No metric/no comparable period → no fabricated anomaly. Explain to the opposite teammate why the observed output meets this gate.

## T29 Narrative divergence candidate — B / B08
- **Level 1 — Objective:** Contrast a management statement with independently validated metric/event records.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/planner.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Cannot be marked discovery merely from same press release. Explain to the opposite teammate why the observed output meets this gate.

## T30 Investigation capability selector — B / B08
- **Level 1 — Objective:** Enable investigation angles only when inputs available; rank data-supported alternatives.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/capability.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Missing volume does not yield invented price-volume decomposition. Explain to the opposite teammate why the observed output meets this gate.

## T31 LLM provider + structured output — B / B07
- **Level 1 — Objective:** Connect a single approved model via official SDK; enforce typed schema and timeout/call budget.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/llm.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Malformed JSON or API failure never becomes a validated hypothesis. Explain to the opposite teammate why the observed output meets this gate.

## T32 Four-node graph state — B / B09
- **Level 1 — Objective:** Define N1 acquire, N2 generate candidates, N3 investigate, N4 report; state contains IDs/budgets.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/graph.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** A fixture run traverses nodes and terminates. Explain to the opposite teammate why the observed output meets this gate.

## T33 Candidate planner prompt — B / B08
- **Level 1 — Objective:** Prompt model to propose precise research question and evidence needed from locked observations.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/planner.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Plan references available IDs; no invented numeric inputs. Explain to the opposite teammate why the observed output meets this gate.

## T34 Targeted supporting-evidence search — A / A08
- **Level 1 — Objective:** Convert missing evidence questions into FTS and public search queries with budget limits.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/investigation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Search returns actual sources or explicit no-results. Explain to the opposite teammate why the observed output meets this gate.

## T35 Contradictory search and alternate hypotheses — B / B10
- **Level 1 — Objective:** Generate bounded alternative explanations and search for contradicting passages/events.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/investigation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** At least one real contrary evidence query executed or recorded unavailable. Explain to the opposite teammate why the observed output meets this gate.

## T36 Graph routing and stopping rules — B / B09
- **Level 1 — Objective:** After verification choose success, revise/try next candidate, or inconclusive based on budget.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/graph.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No infinite loop; exhausted time yields report or justified fail. Explain to the opposite teammate why the observed output meets this gate.

## T37 Persistence/idempotent retry — A / A05
- **Level 1 — Objective:** Make repeated node ingestion idempotent; optional checkpoint after stable nodes.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Interrupt/rerun does not double count source evidence. Explain to the opposite teammate why the observed output meets this gate.

## T38 Hypothesis lifecycle — B / B10
- **Level 1 — Objective:** Implement candidate, investigating, revised, rejected, verified and unresolved statuses.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/claims.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Rejected candidate cannot publish by mistake. Explain to the opposite teammate why the observed output meets this gate.

## T39 Claim-to-observation mapping — B / B10
- **Level 1 — Objective:** Associate each material claim with supporting/contradicting passages, metric IDs and exact scope.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/claims.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Claims cannot cite unrelated period/company row. Explain to the opposite teammate why the observed output meets this gate.

## T40 Deterministic publication gates — A / A08
- **Level 1 — Objective:** Reject non-sourced numbers, unsupported scope, invalid periods, missing provenance or no contradiction effort.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/verifier.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Injected false number, wrong period and missing passage all fail. Explain to the opposite teammate why the observed output meets this gate.

## T41 Corporate events/confounders — A / A08
- **Level 1 — Objective:** Search acquisitions, demergers, restatements, accounting policy, seasonality and category changes.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/investigation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Growth claim qualified/rejected if material unresolved event. Explain to the opposite teammate why the observed output meets this gate.

## T42 Peer direction/definition check — A / A07
- **Level 1 — Objective:** When peer data comparable, show direction/time comparison without tiny-sample Z-score.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Unmatched peer metric not used to strengthen claim. Explain to the opposite teammate why the observed output meets this gate.

## T43 Evidence-strength rationale — B / B10
- **Level 1 — Objective:** Map sufficient evidence and unresolved limitations to Strong/Moderate/Weak; no automatic confidence inflation.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/verifier.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Strong not possible with missing critical gate. Explain to the opposite teammate why the observed output meets this gate.

## T44 Inconclusive branch — B / B10
- **Level 1 — Objective:** Define understandable abstention output with investigated questions and reasons.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/verifier.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Missing data cannot be presented as found financial insight. Explain to the opposite teammate why the observed output meets this gate.

## T45 Eight-field report contract — B / B11
- **Level 1 — Objective:** Prepare discovery, 3–5 significance points, links, timeline, numbers, counterargument, falsifier and strength.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/reporting.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** All eight fields populated or explicit inconclusive wording. Explain to the opposite teammate why the observed output meets this gate.

## T46 Jinja2 standalone HTML — B / B11
- **Level 1 — Objective:** Make clean report with heading, dated timeline, one metric visual/table, clickable evidence rows, uncertainty.
- **Level 2 — Boundaries:** Find this task in `templates/report.html.j2`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Opens without backend and hyperlinks to URLs; no uncited new numbers. Explain to the opposite teammate why the observed output meets this gate.

## T47 Citation and number audit after rendering — A / A09
- **Level 1 — Objective:** Check displayed numbers trace to calculation IDs and each link to known documents/passages.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/reporting.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Fake citation and value modified in prose fail. Explain to the opposite teammate why the observed output meets this gate.

## T48 One-command end-to-end CLI — A / A09
- **Level 1 — Objective:** Accept company name only; run pipeline; give report path and log.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/cli.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Same command works on two selected companies without code edits. Explain to the opposite teammate why the observed output meets this gate.

## T49 Two-minute demo capture — Both / TEAM01
- **Level 1 — Objective:** Record start/company selection, autonomous retrieval/research, result and evidence click-through.
- **Level 2 — Boundaries:** Find this task in `docs/DEMO_CHECKLIST.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Show actual running behavior; identify warm cache if used. Explain to the opposite teammate why the observed output meets this gate.

## T50 Submission PDF and naming — Both / TEAM01
- **Level 1 — Objective:** Finish separate required two-page solution report, team name, Track C, milestone dates.
- **Level 2 — Boundaries:** Find this task in `docs/ROUND1_SUBMISSION.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** PDF ≤2 pages, actual submit to Unstop by Oct 19 23:59 IST. Explain to the opposite teammate why the observed output meets this gate.

## T51 Second-company generalization — Both / TEAM01
- **Level 1 — Objective:** Run exact same code on HUL and ITC or other distinct Track C issuers.
- **Level 2 — Boundaries:** Find this task in `tests/test_end_to_end.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No issuer-specific analysis paths needed. Explain to the opposite teammate why the observed output meets this gate.

## T52 Unseen-company holdout — Both / TEAM01
- **Level 1 — Objective:** Reserve a company not used in debugging; run only company input.
- **Level 2 — Boundaries:** Find this task in `tests/test_end_to_end.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No code or prompt patching after selection. Explain to the opposite teammate why the observed output meets this gate.

## T53 Adversarial invalid-input suite — B / B05
- **Level 1 — Objective:** Run wrong issuer, mirror filing, HTML in PDF, shifted table, mixed periods, malicious document text, API timeout.
- **Level 2 — Boundaries:** Find this task in `tests/test_adversarial.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** All critical false-publication tests block invalid claim. Explain to the opposite teammate why the observed output meets this gate.

## T54 Cold/warm runtime and budgets — A / A09
- **Level 1 — Objective:** Time fresh vs cached runs; log source calls, model calls and stage errors.
- **Level 2 — Boundaries:** Find this task in `docs/DEMO_CHECKLIST.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Budget exhausted → safe termination; no claimed 35-second guarantee. Explain to the opposite teammate why the observed output meets this gate.

## T55 Source fallback and rescoped angles — A / A09
- **Level 1 — Objective:** Recover from blocked source by approved IR/exchange alternate; skip unavailable metrics.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/downloads.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No silent substitution or inaccurate old record. Explain to the opposite teammate why the observed output meets this gate.

## T56 Demo and Q&A rehearsal — Both / TEAM01
- **Level 1 — Objective:** Rehearse unknown company input, cite/source clicks, formulas, counterargument and failures.
- **Level 2 — Boundaries:** Find this task in `docs/DEMO_CHECKLIST.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Both students explain every core module and limitations. Explain to the opposite teammate why the observed output meets this gate.
