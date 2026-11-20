Author imports now match by Open Library key first, then external IDs, then name and dates. Matching authors gain nonconflicting IDs; conflicting IDs raise `AuthorRemoteIdConflictError`. New authors retain supplied IDs, and ties resolve consistently. The import also applies the requested Wikisource date exemption.

Verified with 154 relevant tests, Ruff, and `git diff --check`.