Implemented zip based cover archival in [archive.py](/app/openlibrary/coverstore/archive.py). Covers now use zero-padded batch paths, verified uploads, batch locks, and database URLs that switch to archive.org only after validation. Legacy tar batches can be reconciled after their remote files are verified. The [README](/app/openlibrary/coverstore/README.md) documents the workflow.

Existing databases need the [upload-state migration](/app/openlibrary/coverstore/migrations/2026-10-17-cover-upload-state.sql) before using the new process. It was added to the repository but not applied to a database.

Validation: 23 coverstore tests passed, 7 were skipped; Ruff and `git diff --check` passed. Live archive.org uploads were not exercised.