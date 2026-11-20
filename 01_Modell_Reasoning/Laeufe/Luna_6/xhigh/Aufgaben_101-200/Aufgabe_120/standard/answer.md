Implemented ZIP based cover archival with zero padded ID helpers, archive.org URL generation, per batch locking, idempotent ZIP writes, upload verification, and database finalization after all four sizes are confirmed. Added `failed` and `uploaded` columns and indexes, updated cover routing, and documented the ID and path schema.

Relevant changes are in [archive.py](/app/openlibrary/coverstore/archive.py), [code.py](/app/openlibrary/coverstore/code.py), [schema.sql](/app/openlibrary/coverstore/schema.sql), [schema.py](/app/openlibrary/coverstore/schema.py), and [README.md](/app/openlibrary/coverstore/README.md).

Verification: coverstore tests passed (**18 passed, 7 skipped**); `git diff --check` passed.