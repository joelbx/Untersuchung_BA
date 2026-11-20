# Checkpoint

Resolved author matching in `/app`.

- `remove_author_honorifics` accepts and returns a string, preserves honorific-only names and punctuation-insensitive exceptions, and is applied before author import in `build_query`.
- Name searches escape literal asterisks. Exact, alternate, and surname candidates are prioritized after birth/death year comparison. Surname searches require both extracted years and use wildcard year queries.
- New author records retain source fields. The mock Infobase query matcher now interprets escaped asterisks as literals.
- Existing `extract_year` already returns the first four-digit sequence or an empty string; added regression coverage.

Checks run:
- `python -m pytest openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/tests/catalog/test_utils.py openlibrary/tests/core/test_helpers.py -q` — 135 passed.
- `python -m ruff check openlibrary/catalog/add_book/load_book.py openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/mocks/mock_infobase.py openlibrary/tests/core/test_helpers.py` — passed (existing configuration deprecation warning).
- `git diff --check` — passed.

Initial `rg` search could not run because `rg` is not installed; used `grep` and `find` for inspection. Initial test runs exposed an f-string syntax error and outdated tests, both resolved; final suite passed.
