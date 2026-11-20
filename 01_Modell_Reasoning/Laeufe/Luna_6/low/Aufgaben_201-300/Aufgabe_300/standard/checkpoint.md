# Checkpoint

Task: Add explicit import validation override plumbing and `is_promise_item` utility.

Initial discovery: `rg` is unavailable in this environment; using `find` and standard shell tools to locate relevant code and tests.

Implemented:
- `validate_record` accepts `override_validation=False`; enabled bypasses old/future publication year, independently published, and source ISBN checks.
- `load` forwards the flag, and `/import/api` reads `override-validation=true` from `web.input()` and passes it through.
- Added case-insensitive `is_promise_item(rec)` based on `source_records`.

Verification:
- `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py`: 48 passed.
- `pytest -q openlibrary/plugins/importapi/tests/test_code.py`: 6 passed.
- `git diff --check`: clean.
