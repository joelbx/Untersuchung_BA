Implemented import preview in `/app`. The `/import` and `/ia_import` endpoints now pass `preview=true` through as `save=False`. Preview responses include `preview: true`, the records assembled in `edits`, simulated UUID keys for new records, and `cover_accepted`. Preview skips saves, cover uploads, and Archive.org metadata writes.

The import pipeline now exposes the requested cover, author, and edition conversion functions. Cover hosts use a case insensitive allowlist; author lookup continues to alternate names when an exact name has mismatched dates.

Verification: **171 relevant tests passed**. Ruff and `git diff --check` passed.