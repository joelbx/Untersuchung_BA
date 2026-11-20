# Checkpoint

Resolved author matching across date formats. `extract_year` finds a standalone four-digit year; author lookup checks exact names, alternate names, then surname when both years are valid, and compares extracted years. Name queries escape literal asterisks; surname queries use year wildcards. Honorific removal now accepts and returns a string, handles exceptions and lone honorifics, and runs before import. New author candidates retain input fields.

Verification: `pytest -q openlibrary/catalog/add_book/tests openlibrary/tests/catalog/test_utils.py` -> 250 passed, 1 xfailed. `ruff check` passed; `git diff --check` passed. No delegation used.
