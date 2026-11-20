Task: Normalize alternative language identifiers in format_languages and deduplicate canonical results.
Status: Implemented and verified.
Approach: Resolve MARC codes directly; resolve ISO codes through the active site's English language names and existing MARC fallback; resolve English and native names through active site records and Babel autonyms; validate canonical keys and preserve first occurrence.
Verification: pytest -q openlibrary/tests/catalog/test_utils.py openlibrary/catalog/add_book/tests/test_load_book.py (134 passed); ruff check and git diff --check passed.
Constraints observed: Local repository only; no downloads or external research; git history, index baseline, and harness configuration unchanged.
