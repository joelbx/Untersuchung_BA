# Checkpoint

Task: normalize `format_languages` inputs to canonical Open Library language keys, resolving ISO-639-1 codes and English/native language names, and deduplicate while preserving first-seen order.

Implementation: `openlibrary/catalog/utils/__init__.py` now keeps direct MARC validation, lazily resolves aliases through the repository's MARC map and language records, validates the resolved canonical key, and emits each canonical code once in first-seen order.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests/test_load_book.py`: 34 passed.
- Local mock-record smoke check for `German`, `Deutsch`, `es`, and `ger`: passed; output is `ger`, `spa` once each.
- `git diff --check`: passed.
- Focused cases in `openlibrary/tests/catalog/test_utils.py`: four fail because that test module leaves `web.ctx.site` unset; its empty-input case passes. This setup failure occurs before alias resolution.
