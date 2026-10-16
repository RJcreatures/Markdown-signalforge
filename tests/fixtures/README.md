# Test fixtures you must create yourselves

Use tiny **synthetic** files for failure behavior and freely accessed real filings for citation QA. Do not fabricate a real-looking market disclosure.

Planned paths (do not exist until you create them):
- valid_minimal.pdf — small generated valid PDF; declared synthetic
- html_in_pdf_response.html — HTML masquerade fixture
- truncated.pdf — broken PDF fixture
- financial_table_shifted.pdf — row/column error fixture (synthetic)
- periods_12_15_months.json — period mismatch synthetic fixture
- mixed_consolidation.json — statement basis synthetic fixture
- duplicate_same_origin.json — one issuer filing under two URLs
- malicious_instruction_passage.txt — prompt injection attempt (synthetic)
- heldout_company.txt — selected once before final tests; keep untouched

During implementation, record the original filing URL, retrieval date and permissions for any real document. Never commit confidential data or actual API credentials.
