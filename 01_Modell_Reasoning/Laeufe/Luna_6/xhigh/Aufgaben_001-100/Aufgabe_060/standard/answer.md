Implemented author identifier matching.

- Added [Author.merge_remote_ids](/app/openlibrary/core/models.py:776) and `AuthorRemoteIdConflictError` for conflicting values of the same identifier type.
- Author imports now match by Open Library key, then remote IDs, then name and dates. Multiple matches use identifier agreement and author key for stable tie breaking.
- Imports preserve identifiers on new authors and save nonconflicting additions to matched authors. Added the requested `wikisource` suspect date exemption in [add_book](/app/openlibrary/catalog/add_book/__init__.py:79).

Verification: 141 relevant tests passed; `ruff check` passed.