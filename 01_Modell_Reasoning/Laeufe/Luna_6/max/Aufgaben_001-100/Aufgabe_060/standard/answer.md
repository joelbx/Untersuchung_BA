Implemented identifier aware author imports.

- Author matching now checks Open Library keys, then exact remote identifiers, then existing name and date rules. Candidate ties use stable identifier overlap and key ordering.
- Added [Author.merge_remote_ids](/app/openlibrary/core/models.py:769), which preserves new identifiers, counts exact matches, and raises `AuthorRemoteIdConflictError` on conflicts.
- New authors retain supplied remote IDs; changed IDs on matched authors are saved with the import.
- Added the Wikisource suspect date exemption in [add_book](/app/openlibrary/catalog/add_book/__init__.py:79).

Verification: 141 existing tests passed; `compileall` and `git diff --check` passed. Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).