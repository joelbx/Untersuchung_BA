Implemented priority based author matching: Open Library key, remote identifiers, then name and date. Identifier matches use identifier count and numeric author key for deterministic selection.

Matched authors merge nonconflicting IDs and save them with the import; conflicts raise `AuthorRemoteIdConflictError`. New author candidates preserve incoming IDs. Added the `wikisource` suspect date exemption.

Validation passed: 141 relevant tests, and `git diff --check`.

Changed [load_book.py](/app/openlibrary/catalog/add_book/load_book.py), [models.py](/app/openlibrary/core/models.py), and [add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py).