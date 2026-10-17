# SignalForge — Study guides T01–T56

**You = Teammate A; your partner = Teammate B.** All guides follow the existing `BUILD_ORDER.md` contracts and the eight-level hint ladder.

## Instructions

1. Find the next CORE task you own in `BUILD_ORDER.md`; check its coding dependencies, not just its lesson label.
2. Open `study/TXX.md`. Follow every topic in order: read documentation, watch the named direct video links (only specified chapters), then try the practical exercise.
3. Write the program in the named scaffold file; do not paste finished code. Run a positive and a negative test.
4. Ask the other teammate to review. For Level 8, ask for the complete solution to **one task** only.
5. HARDEN tasks may follow later, unless they are required for safety or correctness.

**Video links:** Each of the 172 topic entries now has at least one direct video URL (no YouTube search queries). When a specialist topic lacks a video demonstrating the exact library API, its video is clearly marked as conceptual/background and the written reference is mandatory. Playback restrictions, removals, and video changes cannot be guaranteed.

**Learning audit:** The old task map says T03 and T04 are ready after B01. That is incomplete: both require Python classes and Pydantic, while T04 also requires Enum/Decimal. This pack adds those concepts **before** the tasks. Other tasks also include just-in-time prerequisites independent of legacy lesson codes.

## Task index

| Task | Owner | Priority | Legacy lesson | Concepts | Guide |
|---|---|---|---|---|---|
| T01 — Repository and environments | Both | CORE | A01 | Git basics, branches,, Python virtual environments | [T01](study/T01.md) |
| T02 — Run configuration | A — you | CORE | A01 | Configuration variables, Pydantic BaseModel, Field | [T02](study/T02.md) |
| T03 — Core source and issuer contracts | B — your partner | CORE | B01 | Python classes, objects, Pydantic BaseModel, Field | [T03](study/T03.md) |
| T04 — Observation and hypothesis contracts | B — your partner | CORE | B01 | Pydantic BaseModel, Field, Pydantic field/model validators | [T04](study/T04.md) |
| T05 — Test layout and fixture catalog | A — you | CORE | A01 | pytest assertions, fixtures,, pytest mocking | [T05](study/T05.md) |
| T06 — Track-company resolution | A — you | CORE | A04 | Python classes, objects, URL parsing, domains | [T06](study/T06.md) |
| T07 — Query-template builder | B — your partner | CORE | B02 | HTTP requests, status codes,, URL parsing, domains | [T07](study/T07.md) |
| T08 — Search-provider adapter | A — you | CORE | A04 | HTTP requests, status codes,, MockTransport | [T08](study/T08.md) |
| T09 — Source URL classifier | B — your partner | CORE | B02 | URL parsing, domains, Evidence provenance | [T09](study/T09.md) |
| T10 — Safe public HTTP downloader | A — you | CORE | A02 | HTTPX timeouts, streaming,, Binary files | [T10](study/T10.md) |
| T11 — Content hash and durable store | A — you | CORE | A03 | Binary files, SHA-256 file hashing | [T11](study/T11.md) |
| T12 — Metadata and issuer cross-check | B — your partner | CORE | B01 | PyMuPDF text extraction by page, Evidence provenance | [T12](study/T12.md) |
| T13 — Source fallback policy | A — you | HARDEN | A03 | HTTPX timeouts, streaming,, MockTransport | [T13](study/T13.md) |
| T14 — PDF page text extraction | B — your partner | CORE | B03 | PyMuPDF text extraction by page, Binary files | [T14](study/T14.md) |
| T15 — XLSX/CSV intake (optional source format) | B — your partner | HARDEN | B04 | openpyxl workbook, CSV parsing | [T15](study/T15.md) |
| T16 — Page passage segmenter | B — your partner | CORE | B03 | PDF text coordinates, Regular expressions | [T16](study/T16.md) |
| T17 — Extract document dates and basis | B — your partner | CORE | B03 | Datetime, reporting period,, Financial statements, period/basis, | [T17](study/T17.md) |
| T18 — Numeric observation extractor | A — you | CORE | A06 | PDF text coordinates, Decimal for deterministic numeric calculations | [T18](study/T18.md) |
| T19 — Extracted table quality gate | B — your partner | CORE | B04 | PDF text coordinates, openpyxl workbook | [T19](study/T19.md) |
| T20 — Unit and period normalizer | A — you | CORE | A06 | Datetime, reporting period,, Decimal for deterministic numeric calculations | [T20](study/T20.md) |
| T21 — Management/event claim extractor | B — your partner | HARDEN | B07 | LLM tools, Untrusted retrieved content | [T21](study/T21.md) |
| T22 — SQLite tables and links | A — you | CORE | A05 | SQLite Python CRUD, keys, SQLite foreign keys | [T22](study/T22.md) |
| T23 — FTS5 full-text index | A — you | CORE | A05 | SQLite FTS5 search indexes, SQLite Python CRUD, keys | [T23](study/T23.md) |
| T24 — Evidence retrieval API | B — your partner | CORE | B06 | SQLite FTS5 search indexes, Information retrieval, RAG | [T24](study/T24.md) |
| T25 — Source independence and duplicate origin | B — your partner | HARDEN | B06 | SHA-256 file hashing, Evidence provenance | [T25](study/T25.md) |
| T26 — Comparable revenue growth | A — you | CORE | A07 | Decimal for deterministic numeric calculations, Comparable revenue growth | [T26](study/T26.md) |
| T27 — Receivable days proxy | A — you | HARDEN | A07 | Decimal for deterministic numeric calculations, Receivable days (DSO) definition | [T27](study/T27.md) |
| T28 — Financial anomaly candidate | A — you | CORE | A07 | Comparable revenue growth, Adversarial / negative testing | [T28](study/T28.md) |
| T29 — Narrative divergence candidate | B — your partner | HARDEN | B08 | Claim-to-evidence entailment, Prompt design | [T29](study/T29.md) |
| T30 — Investigation capability selector | B — your partner | HARDEN | B08 | Financial statements, period/basis,, Claim-to-evidence entailment | [T30](study/T30.md) |
| T31 — LLM provider + structured output | B — your partner | CORE | B07 | LLM tools, Pydantic BaseModel, Field | [T31](study/T31.md) |
| T32 — Four-node graph state | B — your partner | CORE | B09 | LangGraph StateGraph nodes, Pydantic BaseModel, Field | [T32](study/T32.md) |
| T33 — Candidate planner prompt | B — your partner | CORE | B08 | Prompt design, Information retrieval, RAG | [T33](study/T33.md) |
| T34 — Targeted supporting-evidence search | A — you | CORE | A08 | Information retrieval, RAG, HTTP requests, status codes, | [T34](study/T34.md) |
| T35 — Contradictory search and alternate hypotheses | B — your partner | CORE | B10 | Information retrieval, RAG, Claim-to-evidence entailment | [T35](study/T35.md) |
| T36 — Graph routing and stopping rules | B — your partner | CORE | B09 | Conditional routing, Python logging | [T36](study/T36.md) |
| T37 — Persistence/idempotent retry | A — you | HARDEN | A05 | Replay, checkpointing, SQLite foreign keys | [T37](study/T37.md) |
| T38 — Hypothesis lifecycle | B — your partner | CORE | B10 | Enum, dates,, Pydantic field/model validators | [T38](study/T38.md) |
| T39 — Claim-to-observation mapping | B — your partner | CORE | B10 | Claim-to-evidence entailment, Evidence provenance | [T39](study/T39.md) |
| T40 — Deterministic publication gates | A — you | CORE | A08 | Pydantic field/model validators, Adversarial / negative testing | [T40](study/T40.md) |
| T41 — Corporate events/confounders | A — you | HARDEN | A08 | Financial statements, period/basis,, Information retrieval, RAG | [T41](study/T41.md) |
| T42 — Peer direction/definition check | A — you | HARDEN | A07 | Financial statements, period/basis,, Comparable revenue growth | [T42](study/T42.md) |
| T43 — Evidence-strength rationale | B — your partner | CORE | B10 | Claim-to-evidence entailment, Adversarial / negative testing | [T43](study/T43.md) |
| T44 — Inconclusive branch | B — your partner | CORE | B10 | Claim-to-evidence entailment, Conditional routing | [T44](study/T44.md) |
| T45 — Eight-field report contract | B — your partner | CORE | B11 | Jinja2 HTML templating, Pydantic BaseModel, Field | [T45](study/T45.md) |
| T46 — Jinja2 standalone HTML | B — your partner | CORE | B11 | Jinja2 HTML templating, HTML links, tables | [T46](study/T46.md) |
| T47 — Citation and number audit after rendering | A — you | CORE | A09 | Jinja2 HTML templating, Adversarial / negative testing | [T47](study/T47.md) |
| T48 — One-command end-to-end CLI | A — you | CORE | A09 | Python argparse command-line application, LangGraph StateGraph nodes | [T48](study/T48.md) |
| T49 — Two-minute demo capture | Both | HARDEN | TEAM01 | OBS screen recording, Integration, regression | [T49](study/T49.md) |
| T50 — Submission PDF and naming | Both | CORE | TEAM01 | Round 1 brief, Technical demo narratives | [T50](study/T50.md) |
| T51 — Second-company generalization | Both | CORE | TEAM01 | Integration, regression, Git basics, branches, | [T51](study/T51.md) |
| T52 — Unseen-company holdout | Both | HARDEN | TEAM01 | Integration, regression, Adversarial / negative testing | [T52](study/T52.md) |
| T53 — Adversarial invalid-input suite | B — your partner | CORE | B05 | Adversarial / negative testing, pytest mocking | [T53](study/T53.md) |
| T54 — Cold/warm runtime and budgets | A — you | HARDEN | A09 | Profiling Python, Python logging | [T54](study/T54.md) |
| T55 — Source fallback and rescoped angles | A — you | HARDEN | A09 | MockTransport, HTTPX timeouts, streaming, | [T55](study/T55.md) |
| T56 — Demo and Q&A rehearsal | Both | HARDEN | TEAM01 | Technical demo narratives, Integration, regression | [T56](study/T56.md) |

## Start sequence

- **Both:** T01 — setup and Git.
- **You (A):** T02 and T05 while B starts T03.
- **B:** Before T03, study classes → Pydantic models → validators → Enum; then T04 needs Decimal.
- **Next integration:** T06–T12 for real company/source evidence.
- **Round 1 PDF:** T50 proceeds in parallel even if optional MVP is incomplete.
