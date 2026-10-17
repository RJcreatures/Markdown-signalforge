# Progressive hints (eight levels) — one concept at a time

Read H1 before trying the assigned task. Reveal subsequent hints only if genuinely stuck. Levels 1–7 give instructions and API choices, not finished implementation code. **Level 8 = GIVE UP / SOLUTION UNLOCK:** if you explicitly request Level 8 for a task, the mentor may provide the complete reference implementation and matching tests for THAT task. It is not pre-filled into this starter project; you decide whether to use it. Each teammate must still read, understand, test and explain any revealed solution.

**Ownership:** Teammate A = you; Teammate B = your partner.

**Level 8 request template:** `Level 8 — GIVE UP on task TXX. Provide complete runnable code for the named function(s) in the existing boilerplate file, required imports, exact tests, and a concise explanation. Do not rewrite unrelated files. State unverified third-party API assumptions.`


## T01 Repository and environments — Both / A01
- **Level 1 — Objective:** Set up shared repo, Python env, ignore secrets/cache, define main package layout.
- **Level 2 — Boundaries:** Find this task in `README.md / pyproject.toml / .gitignore`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Both machines install project and run test command. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** Python 3.11+ `venv`, `pip`, Git (`init`/`clone`/`branch`/`commit`), `pyproject.toml`, `.gitignore`, `pytest`; verify the package imports on both computers. No company data or secrets in Git.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T01`, the mentor can provide a complete reference implementation for **Repository and environments — Both / A01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T02 Run configuration — A / A01
- **Level 1 — Objective:** Define track, current timeouts, download limits, max sources, budgets and provider names as configuration.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/config.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Bad or missing settings fail with useful messages. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `os.getenv`, `pathlib.Path`, `pydantic.BaseModel`/`Field` (or a validated dataclass), Python `datetime`; implement `config.load_settings()` and reject impossible budgets or absent required credentials.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T02`, the mentor can provide a complete reference implementation for **Run configuration — A / A01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T03 Core source and issuer contracts — B / B01
- **Level 1 — Objective:** Design Company, Document and Passage field sets, including source-group independence.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/contracts.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Ambiguous issuer, missing URL and missing document hash fail validation. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pydantic.BaseModel`, `Field`, `field_validator`, `model_validator`, `HttpUrl`, `datetime`, `Enum`; define source types via `contracts.define_company_and_document_contracts()`.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T03`, the mentor can provide a complete reference implementation for **Core source and issuer contracts — B / B01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T04 Observation and hypothesis contracts — B / B01
- **Level 1 — Objective:** Define Observation, CalculatedMetric, Claim, Hypothesis and Run state statuses.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/contracts.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Missing period/basis/units cannot pass as a validated number. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pydantic.BaseModel`, `Field`, `model_validator`, `Enum`, `datetime`, `Decimal`; declare validation and hypothesis-state records in `contracts.define_research_contracts()`; rejected evidence never becomes `VERIFIED`.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T04`, the mentor can provide a complete reference implementation for **Observation and hypothesis contracts — B / B01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T05 Test layout and fixture catalog — A / A01
- **Level 1 — Objective:** Create test locations for good PDF, HTML instead of PDF, invalid table, period mismatch and mock model response.
- **Level 2 — Boundaries:** Find this task in `tests/fixtures/README.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** A basic test runs on both machines. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pytest`, `pytest.fixture`, `tmp_path`, `monkeypatch`, `pytest.raises`; create controlled sample PDFs/HTML, period/unit mismatch cases and expected model replies under `tests/fixtures/`.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T05`, the mentor can provide a complete reference implementation for **Test layout and fixture catalog — A / A01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T06 Track-company resolution — A / A04
- **Level 1 — Objective:** Accept arbitrary issuer name/ticker; resolve official legal issuer and selected-track match.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/companies.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Unknown, similarly named and valid issuer inputs behave predictably. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `companies.resolve_company()`, Python string normalization (`casefold`, `strip`), issuer ID/symbol fields from the Company contract; match to verified public issuer identifiers, reject ambiguous entities rather than using first result.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T06`, the mentor can provide a complete reference implementation for **Track-company resolution — A / A04** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T07 Query-template builder — B / B02
- **Level 1 — Objective:** Generate reusable searches for annual report, latest quarter, presentation and exchange filing.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_search.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Two companies generate different correct queries with same code. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `source_search.build_research_queries()`, f-strings/formatting, issuer legal name, quoted aliases, `annual report`, `financial results`, `investor presentation`, fiscal-year filters; produce bounded query objects, not company-specific results.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T07`, the mentor can provide a complete reference implementation for **Query-template builder — B / B02** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T08 Search-provider adapter — A / A04
- **Level 1 — Objective:** Call one documented web search provider using configuration; parse URLs/titles.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_search.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Malformed/empty API replies do not crash; result count bounded. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `httpx.Client` or the chosen search-provider official Python SDK, provider request parameters, `response.raise_for_status()`, `.json()`, `pydantic` validation; implement `source_search.search_public_sources()` with bounded, normalized results. Provider not selected—do not invent endpoints.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T08`, the mentor can provide a complete reference implementation for **Search-provider adapter — A / A04** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T09 Source URL classifier — B / B02
- **Level 1 — Objective:** Distinguish issuer IR, exchange, peer issuer, industry and aggregator source classes.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_search.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Same filing mirrored on two sites is not independent evidence. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `urllib.parse.urlsplit`, hostname/path parsing, verified issuer/exchange domain allowlist, source-origin metadata, content SHA-256 for duplicates; implement `source_search.classify_source()` without treating aggregator and mirrored filing as independent.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T09`, the mentor can provide a complete reference implementation for **Source URL classifier — B / B02** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T10 Safe public HTTP downloader — A / A02
- **Level 1 — Objective:** Download allowed HTTPS file with limits, retry/backoff and safe redirect checks.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/downloads.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** 404, HTML masquerade, timeout and size limit handled. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `httpx.Client.stream("GET", ...)`, `Response.iter_bytes()`, HTTP timeout/status checks, `urllib.parse`, `ipaddress`, DNS/private-target checks, PDF `%PDF-` header, controlled redirection; implement `downloads.download_pdf()` safely.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T10`, the mentor can provide a complete reference implementation for **Safe public HTTP downloader — A / A02** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T11 Content hash and durable store — A / A03
- **Level 1 — Objective:** Write completed bytes safely; compute SHA-256; recognize duplicate content.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Same bytes twice map to one original artifact. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pathlib.Path`, `tempfile.NamedTemporaryFile`, `hashlib.sha256`, `os.replace`; implement `storage.save_original_artifact()` as atomic, content-addressed file storage with deduplication.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T11`, the mentor can provide a complete reference implementation for **Content hash and durable store — A / A03** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T12 Metadata and issuer cross-check — B / B01
- **Level 1 — Objective:** Confirm filename/doc text matches intended legal issuer and document type/period.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/source_validation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Wrong-company PDF cannot become accepted evidence. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `source_validation.verify_document_identity()`, verified issuer metadata, PDF cover/title and report-period extraction, domain/origin class; return `verified/ambiguous/rejected` and never rely only on filename.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T12`, the mentor can provide a complete reference implementation for **Metadata and issuer cross-check — B / B01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T13 Source fallback policy — A / A03
- **Level 1 — Objective:** When official exchange fetch fails, try discovered issuer IR document; log failures.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/downloads.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** One blocked host never creates invented data or endless retries. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `downloads.fetch_with_approved_fallbacks()`, ranked approved issuer/exchange URLs, `httpx.TimeoutException`/`HTTPStatusError`, capped attempts/backoff, error ledger; stop on access denial rather than bypassing restrictions.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T13`, the mentor can provide a complete reference implementation for **Source fallback policy — A / A03** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T14 PDF page text extraction — B / B03
- **Level 1 — Objective:** Use PyMuPDF to extract per-page text, page indexes and flags.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/pdf_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Retrieved text can be located again on the saved PDF page. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pymupdf.open`, document `.page_count`, `page.get_text("text")` and indexed page iteration; implement `pdf_extract.extract_pages()` preserving page number, document ID and extraction errors.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T14`, the mentor can provide a complete reference implementation for **PDF page text extraction — B / B03** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T15 XLSX/CSV intake (optional source format) — B / B04
- **Level 1 — Objective:** When issuer provides official XLSX/CSV, preserve sheets, rows and raw cells.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/spreadsheet_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Selected cell maps to original sheet and header. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `openpyxl.load_workbook(read_only=True, data_only=False/True)`, `Workbook.sheetnames`, worksheet `.iter_rows()` with coordinates; `csv.DictReader` for CSV; `spreadsheet_extract.extract_official_spreadsheet()` with original cell provenance.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T15`, the mentor can provide a complete reference implementation for **XLSX/CSV intake (optional source format) — B / B04** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T16 Page passage segmenter — B / B03
- **Level 1 — Objective:** Split page text into retrievable contextual excerpts; preserve page and surrounding labels.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/pdf_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Quoted passage is recoverable within original page text. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pdf_extract.segment_page()`, Python string positions / `re.finditer`, bounded character windows and offset metadata; keep each passage tied to its original full page.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T16`, the mentor can provide a complete reference implementation for **Page passage segmenter — B / B03** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T17 Extract document dates and basis — B / B03
- **Level 1 — Objective:** Recognize financial year/quarter coverage, report publication date, consolidation tags and currency scale.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/pdf_extract.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Unknown tags remain unknown, not defaulted to consolidated. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pdf_extract.extract_reporting_context()`, `re` for fiscal dates, calendar-date validation with `datetime`, exact `consolidated/standalone` phrases; return `unknown` when ambiguous.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T17`, the mentor can provide a complete reference implementation for **Extract document dates and basis — B / B03** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T18 Numeric observation extractor — A / A06
- **Level 1 — Objective:** Locate one chosen comparable metric from a correctly labeled row/period; attach exact source passage.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/observations.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Wrong column or unit is rejected. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `observations.extract_numeric_observation()`, `Decimal`, `re.fullmatch` / carefully scoped parsing, typed Observation records; require matched row label, column, header, unit and evidence ID.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T18`, the mentor can provide a complete reference implementation for **Numeric observation extractor — A / A06** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T19 Extracted table quality gate — B / B04
- **Level 1 — Objective:** Check row-label/column-heading relationships and printed totals where available.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/extraction_quality.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Shifted column fixture fails; real checked row passes. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `extraction_quality.validate_table_observation()`, `Decimal`, column/header context, printed totals, parentheses/footnote flags; fail closed if row alignment or expected aggregation cannot be established.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T19`, the mentor can provide a complete reference implementation for **Extracted table quality gate — B / B04** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T20 Unit and period normalizer — A / A06
- **Level 1 — Objective:** Normalize lakh/million/crore and fiscal periods without losing original meaning.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/observations.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Mixed unit, 15-month versus 12-month, and stock/flow mismatch fail. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `observations.normalize_observation()`, `Decimal`, explicit INR lakh/million/crore conversions, `datetime.date`, period duration, stock-versus-flow distinction; reject incompatible bases or a 15-month vs 12-month comparison.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T20`, the mentor can provide a complete reference implementation for **Unit and period normalizer — A / A06** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T21 Management/event claim extractor — B / B07
- **Level 1 — Objective:** Use structured LLM response to capture exact dated management statements and event labels.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/claims.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Any quoted words not grounded in stored passage rejected. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `claims.extract_qualitative_claims()`, structured LLM reply through `llm.request_structured_reasoning()`, stored page passages, normalized exact-quote checking; retain date and speaker/source IDs.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T21`, the mentor can provide a complete reference implementation for **Management/event claim extractor — B / B07** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T22 SQLite tables and links — A / A05
- **Level 1 — Objective:** Create relational tables for docs, passages, observations, calculations, hypotheses and runs.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Stored records preserve relationships and uniqueness. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `sqlite3.connect`, SQL `CREATE TABLE IF NOT EXISTS`, PRIMARY KEY/UNIQUE/FOREIGN KEY/CHECK, connection transactions; implement `storage.initialize_evidence_database()` for all referenced records.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T22`, the mentor can provide a complete reference implementation for **SQLite tables and links — A / A05** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T23 FTS5 full-text index — A / A05
- **Level 1 — Objective:** Index exact page/passage text with metadata ID join.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Can locate trade-receivables/revenue passage by query and identify page. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `sqlite3` FTS5 `CREATE VIRTUAL TABLE ... USING fts5`, `INSERT`, `MATCH`, `bm25()`, `JOIN` to passage metadata; implement `storage.index_passage_text()` and a page-linked query fixture.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T23`, the mentor can provide a complete reference implementation for **FTS5 full-text index — A / A05** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T24 Evidence retrieval API — B / B06
- **Level 1 — Objective:** Given research question and metadata filters, return a bounded ranked list of passages.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/retrieval.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Cross-company leakage and irrelevant fiscal periods filtered. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `retrieval.retrieve_evidence()`, parameterized SQLite FTS5 `MATCH`, `bm25`, metadata filters for company/period/source class, `LIMIT`; return actual passage IDs, not model-generated citation text.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T24`, the mentor can provide a complete reference implementation for **Evidence retrieval API — B / B06** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T25 Source independence and duplicate origin — B / B06
- **Level 1 — Objective:** Track document content hash, original issuer/publisher and underlying origin.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/retrieval.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Mirrored same filing counted once; peer issuer filing is separate origin. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `retrieval.determine_source_independence()`, stored SHA-256, canonical document/origin IDs, publisher class `ISSUER/EXCHANGE/PEER/INDUSTRY/AGGREGATOR`; group mirrors before counting corroboration.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T25`, the mentor can provide a complete reference implementation for **Source independence and duplicate origin — B / B06** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T26 Comparable revenue growth — A / A07
- **Level 1 — Objective:** Implement first deterministic growth metric using matched period lengths and identical financial definitions.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Hand-calculated fixture passes; period/basis mismatch fails. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `finance.compute_comparable_growth()`, `Decimal`, validated period/basis/metric-definition equality, formula `(current/prior)-1`; reject zero denominator and incompatible periods.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T26`, the mentor can provide a complete reference implementation for **Comparable revenue growth — A / A07** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T27 Receivable days proxy — A / A07
- **Level 1 — Objective:** Compute optional approximate receivable days with compatible revenue flow and balance snapshots.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Correct days-in-period handling; no false precision. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `finance.compute_receivable_days_proxy()`, `Decimal`, `datetime.date` difference, average receivables only if two matched balance dates exist, period-matched revenue; label as sales-based proxy if credit sales unavailable.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T27`, the mentor can provide a complete reference implementation for **Receivable days proxy — A / A07** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T28 Financial anomaly candidate — A / A07
- **Level 1 — Objective:** Create a reusable rule identifying meaningful changes and data gaps.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No metric/no comparable period → no fabricated anomaly. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `finance.screen_financial_anomalies()`, validated calculated metrics, Python comparisons and bounded sorting (`sorted` with a score key); never create candidate from missing or unverified data.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T28`, the mentor can provide a complete reference implementation for **Financial anomaly candidate — A / A07** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T29 Narrative divergence candidate — B / B08
- **Level 1 — Objective:** Contrast a management statement with independently validated metric/event records.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/planner.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Cannot be marked discovery merely from same press release. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `planner.generate_narrative_divergence()`, stored management-claim IDs plus comparable metric IDs, structured output and contradiction keywords; a management quote by itself is not a discovery.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T29`, the mentor can provide a complete reference implementation for **Narrative divergence candidate — B / B08** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T30 Investigation capability selector — B / B08
- **Level 1 — Objective:** Enable investigation angles only when inputs available; rank data-supported alternatives.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/capability.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Missing volume does not yield invented price-volume decomposition. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `capability.select_investigation_capabilities()`, explicit required-evidence sets, Boolean eligibility checks, available Observation/Passage IDs; do not attempt price–volume decomposition without defined volume disclosure.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T30`, the mentor can provide a complete reference implementation for **Investigation capability selector — B / B08** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T31 LLM provider + structured output — B / B07
- **Level 1 — Objective:** Connect a single approved model via official SDK; enforce typed schema and timeout/call budget.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/llm.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Malformed JSON or API failure never becomes a validated hypothesis. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `llm.request_structured_reasoning()`, one chosen provider SDK with JSON/schema mode when supported, Pydantic `model_validate`/`model_validate_json`, capped tokens/timeouts; reject malformed replies. Provider unspecified—check actual SDK API.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T31`, the mentor can provide a complete reference implementation for **LLM provider + structured output — B / B07** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T32 Four-node graph state — B / B09
- **Level 1 — Objective:** Define N1 acquire, N2 generate candidates, N3 investigate, N4 report; state contains IDs/budgets.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/graph.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** A fixture run traverses nodes and terminates. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `langgraph.graph.StateGraph` and `START`/`END`, state `TypedDict`, `add_node`, `add_edge`, `compile`; implement `graph.node_acquire_validate`, `node_generate_candidates`, `node_investigate_challenge`, `node_report_export`, and `build_research_graph()`. Persist only IDs/status in graph state.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T32`, the mentor can provide a complete reference implementation for **Four-node graph state — B / B09** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T33 Candidate planner prompt — B / B08
- **Level 1 — Objective:** Prompt model to propose precise research question and evidence needed from locked observations.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/planner.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Plan references available IDs; no invented numeric inputs. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `planner.plan_next_investigation()`, candidate/evidence IDs, `prompts/research_planner.md`, schema-constrained LLM planning, max hypothesis and query budgets; validate referenced IDs against storage.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T33`, the mentor can provide a complete reference implementation for **Candidate planner prompt — B / B08** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T34 Targeted supporting-evidence search — A / A08
- **Level 1 — Objective:** Convert missing evidence questions into FTS and public search queries with budget limits.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/investigation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Search returns actual sources or explicit no-results. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `investigation.search_supporting_evidence()`, `retrieval.retrieve_evidence()`, accounting synonym bank, follow-up FTS5 queries and dated source filters; log no-result searches.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T34`, the mentor can provide a complete reference implementation for **Targeted supporting-evidence search — A / A08** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T35 Contradictory search and alternate hypotheses — B / B10
- **Level 1 — Objective:** Generate bounded alternative explanations and search for contradicting passages/events.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/investigation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** At least one real contrary evidence query executed or recorded unavailable. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `investigation.search_opposing_evidence()`, FTS5 queries for restatement/acquisition/seasonality/peer trends, structured counterevidence IDs, recorded search coverage; require substantive contradictions rather than model self-critique.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T35`, the mentor can provide a complete reference implementation for **Contradictory search and alternate hypotheses — B / B10** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T36 Graph routing and stopping rules — B / B09
- **Level 1 — Objective:** After verification choose success, revise/try next candidate, or inconclusive based on budget.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/graph.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No infinite loop; exhausted time yields report or justified fail. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `graph.route_after_investigation()`, `StateGraph.add_conditional_edges`, `langgraph.graph.END`, iteration/time/call counters, status enums; terminate on accepted, exhausted, or unrecoverable states.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T36`, the mentor can provide a complete reference implementation for **Graph routing and stopping rules — B / B09** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T37 Persistence/idempotent retry — A / A05
- **Level 1 — Objective:** Make repeated node ingestion idempotent; optional checkpoint after stable nodes.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/storage.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Interrupt/rerun does not double count source evidence. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `storage.record_idempotent_step()`, SQLite `UNIQUE` key for run + operation + artifact and transactional `INSERT ... ON CONFLICT`, SHA-256 identity; rerunning a LangGraph node must not duplicate evidence.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T37`, the mentor can provide a complete reference implementation for **Persistence/idempotent retry — A / A05** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T38 Hypothesis lifecycle — B / B10
- **Level 1 — Objective:** Implement candidate, investigating, revised, rejected, verified and unresolved statuses.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/claims.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Rejected candidate cannot publish by mistake. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `claims.transition_hypothesis()`, `Enum` lifecycle states, a Python allowed-transition mapping, record rejection reason and audit time; only allowed verified states can publish.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T38`, the mentor can provide a complete reference implementation for **Hypothesis lifecycle — B / B10** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T39 Claim-to-observation mapping — B / B10
- **Level 1 — Objective:** Associate each material claim with supporting/contradicting passages, metric IDs and exact scope.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/claims.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Claims cannot cite unrelated period/company row. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `claims.link_claims_to_support()`, typed claim/evidence/observation IDs, SQLite joins on company/period/basis and source excerpt; reject unsupported or unrelated links.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T39`, the mentor can provide a complete reference implementation for **Claim-to-observation mapping — B / B10** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T40 Deterministic publication gates — A / A08
- **Level 1 — Objective:** Reject non-sourced numbers, unsupported scope, invalid periods, missing provenance or no contradiction effort.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/verifier.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Injected false number, wrong period and missing passage all fail. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `verifier.apply_publication_gates()`, deterministic checks for identity, passage, numeric validity, independent origins, comparison scope, actual counter-search and complete eight-field output; return per-gate failures.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T40`, the mentor can provide a complete reference implementation for **Deterministic publication gates — A / A08** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T41 Corporate events/confounders — A / A08
- **Level 1 — Objective:** Search acquisitions, demergers, restatements, accounting policy, seasonality and category changes.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/investigation.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Growth claim qualified/rejected if material unresolved event. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `investigation.check_corporate_event_confounders()`, stored source passages + FTS5 searches for `acquisition`, `demerger`, `restatement`, `scheme of arrangement`, timeline validation; unresolved material events restrict conclusions.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T41`, the mentor can provide a complete reference implementation for **Corporate events/confounders — A / A08** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T42 Peer direction/definition check — A / A07
- **Level 1 — Objective:** When peer data comparable, show direction/time comparison without tiny-sample Z-score.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/finance.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Unmatched peer metric not used to strengthen claim. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `finance.compare_peer_directions()`, `Decimal`, aligned peer metric definitions, periods and comparable company class; report peer values/directions without treating two peers as a reliable Z-score sample.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T42`, the mentor can provide a complete reference implementation for **Peer direction/definition check — A / A07** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T43 Evidence-strength rationale — B / B10
- **Level 1 — Objective:** Map sufficient evidence and unresolved limitations to Strong/Moderate/Weak; no automatic confidence inflation.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/verifier.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Strong not possible with missing critical gate. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `verifier.assess_evidence_strength()`, completed publication-gate outcomes, counterevidence status and source independence; assign Strong/Moderate/Weak with a written evidence rationale.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T43`, the mentor can provide a complete reference implementation for **Evidence-strength rationale — B / B10** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T44 Inconclusive branch — B / B10
- **Level 1 — Objective:** Define understandable abstention output with investigated questions and reasons.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/verifier.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Missing data cannot be presented as found financial insight. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `verifier.prepare_inconclusive_result()`, structured missing-evidence and attempted-investigation record, refusal reason, partial verified observations; must not label unsupported hypotheses as discoveries.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T44`, the mentor can provide a complete reference implementation for **Inconclusive branch — B / B10** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T45 Eight-field report contract — B / B11
- **Level 1 — Objective:** Prepare discovery, 3–5 significance points, links, timeline, numbers, counterargument, falsifier and strength.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/reporting.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** All eight fields populated or explicit inconclusive wording. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `reporting.build_eight_section_report()`, Pydantic report contract and referenced claim/metric IDs; fill exact eight brief sections with clickable source locations and falsification condition.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T45`, the mentor can provide a complete reference implementation for **Eight-field report contract — B / B11** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T46 Jinja2 standalone HTML — B / B11
- **Level 1 — Objective:** Make clean report with heading, dated timeline, one metric visual/table, clickable evidence rows, uncertainty.
- **Level 2 — Boundaries:** Find this task in `templates/report.html.j2`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Opens without backend and hyperlinks to URLs; no uncited new numbers. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `jinja2.Environment`/`FileSystemLoader`, Jinja2 `autoescape`, `templates/report.html.j2`, safe HTML formatting, source URLs and 8-section layout; do not calculate new financial values inside template.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T46`, the mentor can provide a complete reference implementation for **Jinja2 standalone HTML — B / B11** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T47 Citation and number audit after rendering — A / A09
- **Level 1 — Objective:** Check displayed numbers trace to calculation IDs and each link to known documents/passages.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/reporting.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Fake citation and value modified in prose fail. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `reporting.audit_rendered_report()`, parsed report/claim registry, ID-based number and citation audits, `Decimal` conversions; reject unreferenced numbers or source URLs not present in stored records.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T47`, the mentor can provide a complete reference implementation for **Citation and number audit after rendering — A / A09** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T48 One-command end-to-end CLI — A / A09
- **Level 1 — Objective:** Accept company name only; run pipeline; give report path and log.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/cli.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Same command works on two selected companies without code edits. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `cli.run_company_research()`, `argparse.ArgumentParser`, validated settings, `graph.build_research_graph().invoke()` (or tested sequential fallback), run metadata, output file path/error status.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T48`, the mentor can provide a complete reference implementation for **One-command end-to-end CLI — A / A09** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T49 Two-minute demo capture — Both / TEAM01
- **Level 1 — Objective:** Record start/company selection, autonomous retrieval/research, result and evidence click-through.
- **Level 2 — Boundaries:** Find this task in `docs/DEMO_CHECKLIST.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Show actual running behavior; identify warm cache if used. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** Built-in screen recorder or OBS, a genuinely working NIFTY50 Track C run, `docs/DEMO_CHECKLIST.md`, ≤2-minute screen capture showing source citation inspection; label cache transparently.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T49`, the mentor can provide a complete reference implementation for **Two-minute demo capture — Both / TEAM01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T50 Submission PDF and naming — Both / TEAM01
- **Level 1 — Objective:** Finish separate required two-page solution report, team name, Track C, milestone dates.
- **Level 2 — Boundaries:** Find this task in `docs/ROUND1_SUBMISSION.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** PDF ≤2 pages, actual submit to Unstop by Oct 19 23:59 IST. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** Word/Google Docs or equivalent editor, print/export-to-PDF, official brief sections and `docs/ROUND1_SUBMISSION.md`; enforce ≤2 pages, team name, Track C and `TeamName_TrackC_Round1.pdf` via Unstop.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T50`, the mentor can provide a complete reference implementation for **Submission PDF and naming — Both / TEAM01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T51 Second-company generalization — Both / TEAM01
- **Level 1 — Objective:** Run exact same code on HUL and ITC or other distinct Track C issuers.
- **Level 2 — Boundaries:** Find this task in `tests/test_end_to_end.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No issuer-specific analysis paths needed. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pytest.mark.parametrize`, fixed same-source adapters, `tests/test_end_to_end.py`; run unmodified CLI on two issuer inputs and compare traceable outcome/failure reasons.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T51`, the mentor can provide a complete reference implementation for **Second-company generalization — Both / TEAM01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T52 Unseen-company holdout — Both / TEAM01
- **Level 1 — Objective:** Reserve a company not used in debugging; run only company input.
- **Level 2 — Boundaries:** Find this task in `tests/test_end_to_end.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No code or prompt patching after selection. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** Hold out a third Track C company until after implementation; use `pytest` integration run and immutable prompts/settings; track source acquisition and legitimate abstention.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T52`, the mentor can provide a complete reference implementation for **Unseen-company holdout — Both / TEAM01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T53 Adversarial invalid-input suite — B / B05
- **Level 1 — Objective:** Run wrong issuer, mirror filing, HTML in PDF, shifted table, mixed periods, malicious document text, API timeout.
- **Level 2 — Boundaries:** Find this task in `tests/test_adversarial.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** All critical false-publication tests block invalid claim. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `pytest.parametrize`, `monkeypatch`, table misalignment, forged citation, mismatch period/basis, prompt-injection sample, `tests/test_adversarial.py`; invalid findings must fail closed.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T53`, the mentor can provide a complete reference implementation for **Adversarial invalid-input suite — B / B05** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T54 Cold/warm runtime and budgets — A / A09
- **Level 1 — Objective:** Time fresh vs cached runs; log source calls, model calls and stage errors.
- **Level 2 — Boundaries:** Find this task in `docs/DEMO_CHECKLIST.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Budget exhausted → safe termination; no claimed 35-second guarantee. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `time.perf_counter`, JSON logs, fixed run budgets and `docs/DEMO_CHECKLIST.md`; measure cold vs warm fetches and terminate cleanly, not assume a published speed.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T54`, the mentor can provide a complete reference implementation for **Cold/warm runtime and budgets — A / A09** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T55 Source fallback and rescoped angles — A / A09
- **Level 1 — Objective:** Recover from blocked source by approved IR/exchange alternate; skip unavailable metrics.
- **Level 2 — Boundaries:** Find this task in `src/signalforge/downloads.py`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** No silent substitution or inaccurate old record. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** `downloads.retry_research_with_available_sources()`, available source IDs + capability records + remaining budget; choose a valid alternate period/document/angle without inventing missing fields.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T55`, the mentor can provide a complete reference implementation for **Source fallback and rescoped angles — A / A09** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

## T56 Demo and Q&A rehearsal — Both / TEAM01
- **Level 1 — Objective:** Rehearse unknown company input, cite/source clicks, formulas, counterargument and failures.
- **Level 2 — Boundaries:** Find this task in `docs/DEMO_CHECKLIST.md`. Decide exact inputs, outputs, data dependencies and errors.
- **Level 3 — Concepts:** Identify Python control flow, typed records, HTTP/PDF/SQL/LLM calls (if relevant) and what can be deterministic.
- **Level 4 — Tools:** Read the associated lesson and its documentation; verify the API signature rather than guessing.
- **Level 5 — Algorithm design:** Write a numbered outline, then implement ONE responsibility and test a failure path before extending.
- **Level 6 — Acceptance:** Both students explain every core module and limitations. Explain to the opposite teammate why the observed output meets this gate.
- **Level 7 — Exact tools and APIs:** Timer, official 10-minute presentation/15-minute Q&A, screenshots or demo artifacts grounded in a real run, `docs/DEMO_CHECKLIST.md`; both students explain module and failure cases.
- **Level 8 — GIVE UP / reveal solution (optional):** If you explicitly request `Level 8 for T56`, the mentor can provide a complete reference implementation for **Demo and Q&A rehearsal — Both / TEAM01** in its existing placeholder(s), required imports, tests, and why each step works. Do not change other tasks or invent external API capabilities. Review and run tests before using it.

