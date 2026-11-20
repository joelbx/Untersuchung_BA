# Checkpoint

Implemented `override_validation` through `validate_record`, `add_book.load`, and `/import/api` POST query parsing. The override skips publication year, independently published publisher, and required ISBN validation errors. Added case-insensitive `is_promise_item(rec)` to catalog utilities.

Verification: `python -m pytest openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/plugins/importapi/tests/test_code.py -q` passed (54 tests). `git diff --check` passed.
