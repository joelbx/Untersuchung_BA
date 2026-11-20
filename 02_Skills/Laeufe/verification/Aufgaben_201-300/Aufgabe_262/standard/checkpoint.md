# Checkpoint

Task: restrict imported cover URLs to allowed hosts and expose `process_cover_url`.

Implemented in `openlibrary/catalog/add_book/__init__.py`: `ALLOWED_COVER_HOSTS`, a callable that removes and validates `cover`, and use of that callable in both new and matched edition import paths. Added unit and import-path coverage in `openlibrary/catalog/add_book/tests/test_add_book.py`.

Local verification:
- `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py` — 89 passed, 3 dependency deprecation warnings, exit 0.
- `ruff check openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py` — all checks passed, exit 0 (configuration deprecation warning).
- `git diff --check` — exit 0.

Search tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `grep`/`find` instead. No other checks blocked.
