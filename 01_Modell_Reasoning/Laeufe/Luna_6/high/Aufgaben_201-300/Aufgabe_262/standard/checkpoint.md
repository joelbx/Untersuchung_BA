# Checkpoint

Implemented `ALLOWED_COVER_HOSTS` and the public `process_cover_url` helper in `openlibrary/catalog/add_book/__init__.py`. The helper removes `cover` whenever present, accepts only HTTP/HTTPS URLs with a case-insensitive hostname match, and preserves the edition unchanged when `cover` is absent. Both new edition imports and matched-edition enrichment now use this validation before coverstore processing.

Added helper tests for absent, unsupported, uppercase-host HTTP, and HTTPS URLs.

Verification: `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py` passed (82 tests). `python -m compileall -q openlibrary/catalog/add_book` completed successfully.
