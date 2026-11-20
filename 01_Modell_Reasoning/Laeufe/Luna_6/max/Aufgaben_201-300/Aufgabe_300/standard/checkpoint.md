# Checkpoint

Task: Add explicit `override-validation` support to the import API validation flow, and expose `is_promise_item(rec)` in `openlibrary/catalog/utils/__init__.py`.

Implemented:
- `validate_record(rec, override_validation=False)` skips publication year, independently published, and required ISBN validations only when the override is true.
- `load(..., override_validation=False)` forwards the value to `validate_record`.
- Generic `/import/api` POST reads the URL query parameter `override-validation`, interprets only case-insensitive `true` as true, and passes it to `load`.
- `is_promise_item(rec)` recognizes case-insensitive `promise:` prefixes in source records.
- Added tests for validation bypass/preservation, load and API forwarding, and promise item matching.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/tests/catalog/test_utils.py openlibrary/plugins/importapi/tests/test_code.py` — 114 passed.
- `pytest -q openlibrary/plugins/importapi/tests` — 30 passed.
- `git diff --check` — clean.
