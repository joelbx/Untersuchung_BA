# Checkpoint

Task: Fix author matching for honorifics, date formats, and special characters.

Implemented:
- `remove_author_honorifics(name: str) -> str` now removes leading English, French, Spanish, and German titles, preserves title-only names, and checks the exception frozenset without case or punctuation sensitivity.
- `build_query` normalizes each author name before import.
- Author lookups proceed through exact name, alternate name, then surname candidates. Candidates require matching extracted birth/death years when those years are supplied. Surname lookup requires two valid four-digit years and queries year substrings.
- Literal asterisks no longer broaden name searches; new author candidates keep input fields and preserve names containing asterisks.
- `extract_year` returns the first standalone four-digit sequence. Shared date matching compares extracted years.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/tests/core/test_helpers.py openlibrary/tests/catalog/test_utils.py`: 138 passed.
- `python -m ruff check` on changed Python files: passed (repository configuration deprecation warning only).
