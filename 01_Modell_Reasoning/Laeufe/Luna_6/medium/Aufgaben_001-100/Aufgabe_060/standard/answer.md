Implemented author matching by Open Library key, then external identifiers, then the existing name and date logic. Matched authors merge nonconflicting remote IDs; conflicting values raise `AuthorRemoteIdConflictError`. New author candidates retain their supplied IDs, and ties between identifier matches resolve consistently by match count and author key.

Added `SUSPECT_DATE_EXEMPT_SOURCES = ["wikisource"]` in the requested module.

Verification: `python -m pytest openlibrary/tests/core/test_models.py openlibrary/catalog/add_book/tests/test_load_book.py -q` passed (56 tests). `git diff --check` passed.