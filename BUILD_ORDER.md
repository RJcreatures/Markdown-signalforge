# SignalForge — Two-Person Build Sequence (authoritative task map)

**Roles:** **Teammate A = you**. **Teammate B = your partner**. “Both” means pair integration and mutual review.
**Reference:** 56-task MVP implementation playbook. Ownership preserved from that playbook, with your identity clarified.
**Status:** All starter functions are placeholders and all starter tests skip until personally implemented.
**Source policy:** Official issuer IR / NSE / BSE are priority leads; availability, current access and usage rights must be confirmed during coding. Search snippets are not numerical evidence.
**Plan:** FOCUS on CORE tasks first, deliver the mandatory Round 1 PDF regardless of optional MVP status. HARDEN tasks are deferred unless they block correctness.

## First thing each teammate does

**A (you):** install Python+Git, create branch `feature/acquisition`, complete A01 then A02; own config, safe download, storage, math and CLI.

**B (partner):** clone repo, create branch `feature/evidence`, complete B01 then B02; own typed research contracts, PDF evidence quality, model interface, graph and reporting.

Agree typed contracts (T03–T04) before either teammate changes the same data object. The other teammate reviews each merge.

## Exact file and task map

| Task | Priority | Owner | Learn before coding | Dependencies | Edit here | Required deliverable / acceptance |
|---|---|---|---|---|---|---|
| T01 Repository and environments | CORE | Both | A01 | none | `README.md / pyproject.toml / .gitignore` | Both machines install project and run test command. |
| T02 Run configuration | CORE | A | A01 | T01 | `src/signalforge/config.py` | Bad or missing settings fail with useful messages. |
| T03 Core source and issuer contracts | CORE | B | B01 | T01 | `src/signalforge/contracts.py` | Ambiguous issuer, missing URL and missing document hash fail validation. |
| T04 Observation and hypothesis contracts | CORE | B | B01 | T03 | `src/signalforge/contracts.py` | Missing period/basis/units cannot pass as a validated number. |
| T05 Test layout and fixture catalog | CORE | A | A01 | T01 | `tests/fixtures/README.md` | A basic test runs on both machines. |
| T06 Track-company resolution | CORE | A | A04 | T03 | `src/signalforge/companies.py` | Unknown, similarly named and valid issuer inputs behave predictably. |
| T07 Query-template builder | CORE | B | B02 | T06 | `src/signalforge/source_search.py` | Two companies generate different correct queries with same code. |
| T08 Search-provider adapter | CORE | A | A04 | T02,T07 | `src/signalforge/source_search.py` | Malformed/empty API replies do not crash; result count bounded. |
| T09 Source URL classifier | CORE | B | B02 | T08 | `src/signalforge/source_search.py` | Same filing mirrored on two sites is not independent evidence. |
| T10 Safe public HTTP downloader | CORE | A | A02 | T02,T09 | `src/signalforge/downloads.py` | 404, HTML masquerade, timeout and size limit handled. |
| T11 Content hash and durable store | CORE | A | A03 | T10 | `src/signalforge/storage.py` | Same bytes twice map to one original artifact. |
| T12 Metadata and issuer cross-check | CORE | B | B01 | T09,T11 | `src/signalforge/source_validation.py` | Wrong-company PDF cannot become accepted evidence. |
| T13 Source fallback policy | HARDEN | A | A03 | T10,T12 | `src/signalforge/downloads.py` | One blocked host never creates invented data or endless retries. |
| T14 PDF page text extraction | CORE | B | B03 | T11 | `src/signalforge/pdf_extract.py` | Retrieved text can be located again on the saved PDF page. |
| T15 XLSX/CSV intake (optional source format) | HARDEN | B | B04 | T11 | `src/signalforge/spreadsheet_extract.py` | Selected cell maps to original sheet and header. |
| T16 Page passage segmenter | CORE | B | B03 | T14 | `src/signalforge/pdf_extract.py` | Quoted passage is recoverable within original page text. |
| T17 Extract document dates and basis | CORE | B | B03 | T14 | `src/signalforge/pdf_extract.py` | Unknown tags remain unknown, not defaulted to consolidated. |
| T18 Numeric observation extractor | CORE | A | A06 | T16,T17 | `src/signalforge/observations.py` | Wrong column or unit is rejected. |
| T19 Extracted table quality gate | CORE | B | B04 | T18 | `src/signalforge/extraction_quality.py` | Shifted column fixture fails; real checked row passes. |
| T20 Unit and period normalizer | CORE | A | A06 | T17,T18 | `src/signalforge/observations.py` | Mixed unit, 15-month versus 12-month, and stock/flow mismatch fail. |
| T21 Management/event claim extractor | HARDEN | B | B07 | T16 | `src/signalforge/claims.py` | Any quoted words not grounded in stored passage rejected. |
| T22 SQLite tables and links | CORE | A | A05 | T03,T04 | `src/signalforge/storage.py` | Stored records preserve relationships and uniqueness. |
| T23 FTS5 full-text index | CORE | A | A05 | T16,T22 | `src/signalforge/storage.py` | Can locate trade-receivables/revenue passage by query and identify page. |
| T24 Evidence retrieval API | CORE | B | B06 | T23 | `src/signalforge/retrieval.py` | Cross-company leakage and irrelevant fiscal periods filtered. |
| T25 Source independence and duplicate origin | HARDEN | B | B06 | T12,T22 | `src/signalforge/retrieval.py` | Mirrored same filing counted once; peer issuer filing is separate origin. |
| T26 Comparable revenue growth | CORE | A | A07 | T20 | `src/signalforge/finance.py` | Hand-calculated fixture passes; period/basis mismatch fails. |
| T27 Receivable days proxy | HARDEN | A | A07 | T20,T26 | `src/signalforge/finance.py` | Correct days-in-period handling; no false precision. |
| T28 Financial anomaly candidate | CORE | A | A07 | T26 | `src/signalforge/finance.py` | No metric/no comparable period → no fabricated anomaly. |
| T29 Narrative divergence candidate | HARDEN | B | B08 | T21,T28 | `src/signalforge/planner.py` | Cannot be marked discovery merely from same press release. |
| T30 Investigation capability selector | HARDEN | B | B08 | T24,T28 | `src/signalforge/capability.py` | Missing volume does not yield invented price-volume decomposition. |
| T31 LLM provider + structured output | CORE | B | B07 | T02,T04 | `src/signalforge/llm.py` | Malformed JSON or API failure never becomes a validated hypothesis. |
| T32 Four-node graph state | CORE | B | B09 | T04,T22 | `src/signalforge/graph.py` | A fixture run traverses nodes and terminates. |
| T33 Candidate planner prompt | CORE | B | B08 | T28,T31 | `src/signalforge/planner.py` | Plan references available IDs; no invented numeric inputs. |
| T34 Targeted supporting-evidence search | CORE | A | A08 | T24,T33 | `src/signalforge/investigation.py` | Search returns actual sources or explicit no-results. |
| T35 Contradictory search and alternate hypotheses | CORE | B | B10 | T33,T34 | `src/signalforge/investigation.py` | At least one real contrary evidence query executed or recorded unavailable. |
| T36 Graph routing and stopping rules | CORE | B | B09 | T32,T35 | `src/signalforge/graph.py` | No infinite loop; exhausted time yields report or justified fail. |
| T37 Persistence/idempotent retry | HARDEN | A | A05 | T11,T22,T32 | `src/signalforge/storage.py` | Interrupt/rerun does not double count source evidence. |
| T38 Hypothesis lifecycle | CORE | B | B10 | T04,T35 | `src/signalforge/claims.py` | Rejected candidate cannot publish by mistake. |
| T39 Claim-to-observation mapping | CORE | B | B10 | T35,T38 | `src/signalforge/claims.py` | Claims cannot cite unrelated period/company row. |
| T40 Deterministic publication gates | CORE | A | A08 | T19,T20,T39 | `src/signalforge/verifier.py` | Injected false number, wrong period and missing passage all fail. |
| T41 Corporate events/confounders | HARDEN | A | A08 | T34,T40 | `src/signalforge/investigation.py` | Growth claim qualified/rejected if material unresolved event. |
| T42 Peer direction/definition check | HARDEN | A | A07 | T20,T34 | `src/signalforge/finance.py` | Unmatched peer metric not used to strengthen claim. |
| T43 Evidence-strength rationale | CORE | B | B10 | T39,T40 | `src/signalforge/verifier.py` | Strong not possible with missing critical gate. |
| T44 Inconclusive branch | CORE | B | B10 | T36,T40 | `src/signalforge/verifier.py` | Missing data cannot be presented as found financial insight. |
| T45 Eight-field report contract | CORE | B | B11 | T39,T43 | `src/signalforge/reporting.py` | All eight fields populated or explicit inconclusive wording. |
| T46 Jinja2 standalone HTML | CORE | B | B11 | T45 | `templates/report.html.j2` | Opens without backend and hyperlinks to URLs; no uncited new numbers. |
| T47 Citation and number audit after rendering | CORE | A | A09 | T46 | `src/signalforge/reporting.py` | Fake citation and value modified in prose fail. |
| T48 One-command end-to-end CLI | CORE | A | A09 | T32,T46 | `src/signalforge/cli.py` | Same command works on two selected companies without code edits. |
| T49 Two-minute demo capture | HARDEN | Both | TEAM01 | T48 | `docs/DEMO_CHECKLIST.md` | Show actual running behavior; identify warm cache if used. |
| T50 Submission PDF and naming | CORE | Both | TEAM01 | T01 | `docs/ROUND1_SUBMISSION.md` | PDF ≤2 pages, actual submit to Unstop by Oct 19 23:59 IST. |
| T51 Second-company generalization | CORE | Both | TEAM01 | T48 | `tests/test_end_to_end.py` | No issuer-specific analysis paths needed. |
| T52 Unseen-company holdout | HARDEN | Both | TEAM01 | T51 | `tests/test_end_to_end.py` | No code or prompt patching after selection. |
| T53 Adversarial invalid-input suite | CORE | B | B05 | T40,T47 | `tests/test_adversarial.py` | All critical false-publication tests block invalid claim. |
| T54 Cold/warm runtime and budgets | HARDEN | A | A09 | T48,T51 | `docs/DEMO_CHECKLIST.md` | Budget exhausted → safe termination; no claimed 35-second guarantee. |
| T55 Source fallback and rescoped angles | HARDEN | A | A09 | T13,T30 | `src/signalforge/downloads.py` | No silent substitution or inaccurate old record. |
| T56 Demo and Q&A rehearsal | HARDEN | Both | TEAM01 | T52,T54 | `docs/DEMO_CHECKLIST.md` | Both students explain every core module and limitations. |

## Time-boxed build order and integration gates

**Gate 1 — One source reaches disk:** T01/T02/T03/T05/T06/T07/T08/T09/T10/T11/T12. The application can correctly obtain one authentic issuer document or records a real blocker. Pair review.
**Gate 2 — One citation-grounded number:** T14/T16/T17/T18/T19/T20/T22/T23/T24/T26. One observation tied to row, column, period, basis, PDF page and hash; a mismatch fails.
**Gate 3 — One minimal research candidate:** T28/T31/T32/T33/T34. One candidate can be formulated from validated facts; no unsupported numeric facts enter prompt.
**Gate 4 — One rejection:** T35/T36/T38/T39/T40/T43/T44. Inject contrary evidence and confirm candidate is rejected/weakened; no endless retry.
**Gate 5 — Real report:** T45/T46/T47/T48/T51. One-command run yields sourced eight-field HTML report OR a transparently inconclusive report, with logs.
**Round 1 required gate (parallel):** T50. Two-page maximum PDF, team name + Track C, submitted before 19 October 23:59 IST. Optional T49 video only if a working demo exists.
**Finals hardening:** T13/T15/T21/T25/T27/T29/T30/T37/T41/T42/T52/T53/T54/T55/T56; expand after viable MVP.

## Four-node graph contract

| Node | Entrypoint | Primary responsibility | Status/route |
|---|---|---|---|
| N1 Acquire/Validate | `graph.node_acquire_validate` | Company→candidate sources→stored source IDs→valid observations | No source→known failure or fallback |
| N2 Generate Candidates | `graph.node_generate_candidates` | Deterministic anomalies + narrative angles→bounded candidate IDs | No candidates→inconclusive |
| N3 Investigate/Challenge | `graph.node_investigate_challenge` | Retrieved support, countersearch, calculations and publication gates | PASS→N4; alternate+budget→N2; otherwise N4 |
| N4 Report/Export | `graph.node_report_export` | Exactly eight fields from accepted records, or honest inconclusive result | END |

## Completion reporting format for every task

Write in `docs/WORK_LOG.md`: task ID; developer; lesson completed; functions edited; tests run; actual test results; edge cases; source URLs if used; blocker; reviewer verdict. Avoid invented scores.

## Strict learning rule

For each lesson: read provided documentation → watch video/course → perform a 10–20 min unrelated toy practice → implement only the assigned placeholders → write real tests → exchange code for review. Escalate through Hint Level 1–6 only if stuck.
