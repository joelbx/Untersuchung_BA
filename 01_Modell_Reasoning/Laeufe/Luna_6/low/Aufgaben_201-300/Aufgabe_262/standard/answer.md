Implemented `ALLOWED_COVER_HOSTS` and `process_cover_url` in [openlibrary/catalog/add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py). Both new and matched edition imports now validate cover hosts case-insensitively and remove the `cover` key before saving or fetching.

The add book test modules passed: **109 passed**. `git diff --check` also passed.