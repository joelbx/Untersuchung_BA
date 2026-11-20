# Checkpoint

Resolved book import cover URL validation in `openlibrary/catalog/add_book/__init__.py`.

- Added `ALLOWED_COVER_HOSTS` from locally evidenced archive, Open Library, and Amazon cover sources.
- Added `process_cover_url` to remove `cover` and return it only for HTTP(S) URLs with a case-insensitive allowed hostname.
- Applied validation to both new-edition and matched-edition cover upload paths.
- Added helper, new-edition, and matched-edition coverage.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests`: 150 passed, 1 xfailed.
- `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py`: 88 passed.
- `ruff check openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py`: passed (configuration deprecation warning only).
- `git diff --check`: passed.

Tooling note: `rg` was unavailable (`/bin/bash: rg: command not found`); used `grep` and `find` for local inspection.
