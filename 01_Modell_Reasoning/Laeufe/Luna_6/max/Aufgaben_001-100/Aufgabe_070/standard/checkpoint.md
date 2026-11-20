# Checkpoint

Issue: normalize non-MARC language identifiers in `format_languages` and deduplicate canonical results while preserving first-seen order.

Implemented in `openlibrary/catalog/utils/__init__.py`:
- Preserve direct case-insensitive MARC key lookup.
- Resolve aliases with the existing MARC mapping, ISO-639-1 catalog lookup, and English/native translated language names.
- Validate the resolved language key and deduplicate it while preserving first occurrence.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests/test_load_book.py`: 34 passed.
- Combined focused run of `openlibrary/tests/catalog/test_utils.py` and `openlibrary/catalog/add_book/tests/test_load_book.py`: 124 passed, 4 failed. The four language utility cases have no `web.ctx.site` fixture in this test module and fail before exercising behavior; the existing implementation also requires `web.ctx.site` for those calls.
- `git diff --check`: passed.
