# Checkpoint

Task: resolve author matching issues involving date formats, name wildcards, and honorifics.

Implemented:
- `remove_author_honorifics` accepts/returns strings, handles supported international titles case-insensitively, preserves title-only names, and honors punctuation/case-insensitive exceptions stored as a frozenset.
- `build_query` normalizes `author['name']` before author processing.
- Author lookup now validates exact name matches first, then alternate names, then surname plus matching birth/death years. Name/date comparisons use extracted years; surname fallback requires both input years and uses year wildcard queries.
- Literal asterisks use equality name queries so they cannot match arbitrary name text. New author candidates preserve input fields and wildcard names.
- `extract_year` returns the first standalone ASCII four-digit year or an empty string.
- Updated existing tests whose old wildcard and honorific-helper expectations conflicted with the requested behavior; the surname matching fixture now uses differing date formats.

Verification: `pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/tests/core/test_helpers.py` passed (37 tests). `git diff --check` passed.
