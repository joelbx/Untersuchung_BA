Implemented ZIP based cover archival in [archive.py](/app/openlibrary/coverstore/archive.py), with zero-padded paths, batch locking, upload verification, and database updates only after all four sizes pass validation. Cover retrieval now reads staged ZIPs or redirects to the stored archive.org URL. The [schema](/app/openlibrary/coverstore/schema.sql) adds `failed` and `uploaded` status; the [README](/app/openlibrary/coverstore/README.md) documents the layout and migration SQL.

**Verification:** 24 coverstore tests passed; 7 database-dependent tests were skipped. Ruff and `git diff --check` passed.

Existing tar batches can be reconciled to verified remote URLs, but their contents were not converted to ZIPs.