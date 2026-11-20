# Checkpoint

- Task: normalize ISO-639-1 codes and English/native language names in `format_languages`, then deduplicate canonical keys in input order.
- Located implementation in `openlibrary/catalog/utils/__init__.py` and existing tests in `openlibrary/tests/catalog/test_utils.py`.
- Implemented site-backed ISO-639-1 and English/native name lookup with a fallback to the repository's existing code map, then deduplicated canonical codes in first-seen order.
- Added language fixtures and cases covering mixed identifiers, case and accent normalization, order, invalid tokens, and a conflicting fallback entry.
- Verified: 242 catalog, load-book, add-book, and upstream tests passed together; Ruff and `git diff --check` passed.
