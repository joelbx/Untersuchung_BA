# Checkpoint

Task: Expand MARC contributor role parsing and preserve roles in new works.

Implemented:
- Added `ROLES` for MARC relator codes and common terms/abbreviations.
- `read_author_person` reads `$e` and `$4`, gives `$4` precedence, and omits unrecognized roles.
- `new_work` pairs edition author keys with record authors in order, preserves roles, and raises on count mismatch.
- Added targeted tests and updated MARC fixture expectations for mapped roles.

Verification:
- `python -m pytest openlibrary/catalog/marc/tests openlibrary/catalog/add_book/tests -q`: 290 passed, 3 deprecation warnings, exit 0.
- `ruff check openlibrary/catalog/marc/parse.py openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py`: all checks passed, exit 0.
- `git diff --check`: exit 0.
- `ruff format --check openlibrary/catalog/marc/parse.py openlibrary/catalog/marc/tests/test_parse.py openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py`: exit 1; formatter requests double quotes throughout the existing single-quote-style files, including unchanged lines. No formatting rewrite applied.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `grep` and `find`.
