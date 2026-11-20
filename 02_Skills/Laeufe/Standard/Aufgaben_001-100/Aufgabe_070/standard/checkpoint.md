# Checkpoint

Resolved `format_languages` normalization for MARC codes, ISO 639-1 codes, English and native names. Results use canonical MARC keys and preserve first-occurrence order while deduplicating. Added regression tests for aliases, native names, a two-letter code absent from the static mapping, unknown tokens, and ambiguous names. Existing tests now use a site fixture.

Verification:
- `pytest -q openlibrary/tests/catalog/test_utils.py openlibrary/catalog/add_book/tests/test_add_book.py`: 186 passed.
- `ruff check openlibrary/catalog/utils/__init__.py openlibrary/tests/catalog/test_utils.py`: passed.
- `git diff --check`: passed.

Tooling notes:
- `rg` was unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep` instead.
- `ruff format --check openlibrary/catalog/utils/__init__.py openlibrary/tests/catalog/test_utils.py` reported both files would be reformatted. Its diff changes many pre-existing single quotes throughout the files, so the unrelated full-file formatting changes were left out.
