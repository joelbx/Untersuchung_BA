Author import now checks an Open Library key first, then external identifiers, then name and dates. It merges compatible identifiers into matched authors, raises `AuthorRemoteIdConflictError` for conflicts, and preserves identifiers on new author candidates. I also added `SUSPECT_DATE_EXEMPT_SOURCES = ["wikisource"]`.

The relevant existing tests and new focused tests pass: **58 passed**.