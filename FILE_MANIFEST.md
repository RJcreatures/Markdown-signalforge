# Complete source-file inventory

**A = you; B = your teammate.** All starter files below are included in the ZIP. They are scaffolds and documents, not implemented research software.

```text
.env.example
.gitignore
.pytest_cache/.gitignore
.pytest_cache/CACHEDIR.TAG
.pytest_cache/README.md
.pytest_cache/v/cache/nodeids
BUILD_ORDER.md
FILE_MANIFEST.md
HINT_LADDER_56_TASKS.md
LESSONS_AND_TASKS.md
README.md
TASK_SLOT_INDEX.json
config/research_policy.json
data/.gitkeep
docs/DEMO_CHECKLIST.md
docs/FINANCIAL_RULES.md
docs/LEARNING_AGREEMENT.md
docs/ROUND1_SUBMISSION.md
docs/SOURCE_POLICY.md
docs/TEST_PLAN.md
docs/WORK_LOG.md
output/.gitkeep
prompts/claim_extractor.md
prompts/contradiction_search.md
prompts/research_planner.md
pyproject.toml
src/signalforge/__init__.py
src/signalforge/__main__.py
src/signalforge/capability.py
src/signalforge/claims.py
src/signalforge/cli.py
src/signalforge/companies.py
src/signalforge/config.py
src/signalforge/contracts.py
src/signalforge/downloads.py
src/signalforge/extraction_quality.py
src/signalforge/finance.py
src/signalforge/graph.py
src/signalforge/investigation.py
src/signalforge/llm.py
src/signalforge/observations.py
src/signalforge/pdf_extract.py
src/signalforge/planner.py
src/signalforge/reporting.py
src/signalforge/retrieval.py
src/signalforge/source_search.py
src/signalforge/source_validation.py
src/signalforge/spreadsheet_extract.py
src/signalforge/storage.py
src/signalforge/verifier.py
templates/report.html.j2
tests/fixtures/README.md
tests/test_adversarial.py
tests/test_company_and_source.py
tests/test_config.py
tests/test_downloads.py
tests/test_end_to_end.py
tests/test_finance.py
tests/test_llm_and_graph.py
tests/test_observations.py
tests/test_pdf_and_spreadsheets.py
tests/test_report.py
tests/test_storage_and_retrieval.py
tests/test_verification.py
```

## Files created later *by your implementation*

- `.env` (locally from `.env.example`, with real credentials; never commit).
- `data/signalforge.sqlite` (after T22).
- `data/originals/<hash>.pdf` and optional `.xlsx` (after acquisition).
- `output/<run_id>_report.html` and possibly a PDF (after T46–T48).
- Your own test fixtures in `tests/fixtures/` (after T05/T53).
- Mandatory Round 1 PDF `TeamName_TrackC_Round1.pdf` (T50; created from separate editable proposal).

These runtime/submission files are not included here, because no code or real financial results have been produced.
