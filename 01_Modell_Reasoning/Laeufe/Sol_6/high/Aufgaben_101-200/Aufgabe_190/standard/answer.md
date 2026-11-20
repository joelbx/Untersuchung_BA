Implemented `preview=true` for the `/import` and `/ia_import` endpoints. Preview runs the import pipeline with `save=False`, returns `preview: true` and an `edits` list with temporary keys for new records, and skips saves, cover uploads, and Archive.org metadata updates.

The import code now exposes case-insensitive cover host validation, normalized author matching, and edition construction through the requested public functions. Preview reports whether a cover URL is accepted; a cover ID remains unavailable until an actual upload.

**Verification:** 134 relevant tests passed, Ruff lint passed, and `git diff --check` passed.