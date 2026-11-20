# Import API validation override

Task: Add explicit `override-validation=true` support to `/import/api`, pass it through `load()` to `validate_record()`, and add the reusable promise-item helper.

Initial state: working tree clean. Located validation and load in `openlibrary/catalog/add_book/__init__.py`; import API in `openlibrary/plugins/importapi/code.py`.

Implemented: explicit query flag forwarding through `POST()` and `load()`; conditional validation bypass with required fields retained; case-insensitive `is_promise_item()` helper. Added focused tests for each exception, API forwarding, end-to-end load, and helper behavior.

Verification: relevant import API, add_book, and catalog utility tests passed (142 passed, 1 expected failure). `git diff --check` passed. A broad Ruff check found an existing `UP035` warning for a `Mapping` import in catalog utils; this task did not change that import.
