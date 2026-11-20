# Checkpoint

Task: Add explicit import API validation override and promise item utility.
Status: Implemented and verified.
Changes: POST reads override-validation from URL query; load forwards it to validate_record; the flag skips year, publisher, and ISBN checks; is_promise_item checks case-insensitive promise: prefixes.
Verification: python -m pytest -q openlibrary/catalog/add_book/tests openlibrary/plugins/importapi/tests (99 passed, 1 xfailed); git diff --check passed.
