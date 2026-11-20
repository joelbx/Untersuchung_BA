Implemented identifier-aware author imports. Matching now prioritizes an explicit Open Library key, then remote identifiers, then existing name and date matching. Matching Authors receive nonconflicting incoming IDs; conflicts raise `AuthorRemoteIdConflictError`. New author candidates preserve supplied remote IDs, and ambiguous identifier matches use a deterministic key tie-break.

Also added `SUSPECT_DATE_EXEMPT_SOURCES = ["wikisource"]` and regression tests.

Verification: 60 relevant tests passed; `git diff --check` passed.