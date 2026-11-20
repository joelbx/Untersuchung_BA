# Checkpoint

Task: Add the `override-validation` option to the import API, conditionally bypass the specified record validations, and expose `is_promise_item` in catalog utilities.

Initial state: Repository inspection is underway. No source files have been changed yet.

Implementation progress: Added `override_validation` to `validate_record` and `load`, wired the `/import/api` POST query parameter through the call chain, and added the case-insensitive `is_promise_item` utility. The override defaults to false and disables only the requested validation errors.

Verification in progress: Running existing add-book and import API tests.

Verification complete: `python -m pytest openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/plugins/importapi/tests` passed (74 tests). One existing Python `cgi` deprecation warning was reported.
