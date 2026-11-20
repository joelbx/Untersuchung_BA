# Checkpoint

Issue: imported edition cover URLs must be validated against `ALLOWED_COVER_HOSTS` before coverstore processing.

Implemented:
- Added `ALLOWED_COVER_HOSTS` with the Archive.org host used by the repository's IA cover URL generation.
- Added `process_cover_url`, which removes `cover` when present and returns it only for HTTP(S) URLs whose hostname matches an allowed host case-insensitively.
- Applied the validator to both new/overwritten edition imports and matched edition enrichment.
- Updated the existing matched-edition cover fixture to use the supported Archive.org host.

Verification: `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/add_book/tests/test_load_book.py` — 109 passed.
