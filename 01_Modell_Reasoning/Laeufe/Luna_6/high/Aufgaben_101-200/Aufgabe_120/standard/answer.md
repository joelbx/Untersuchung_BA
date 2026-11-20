Implemented zip based cover archival with zero padded IDs, size specific archive URLs, batch upload verification, retry safe zip writes, and database finalization. Added `failed` and `uploaded` columns and indexes, and updated cover retrieval to read Archive.org URLs. The naming scheme and workflow are documented in the README.

Verification: focused coverstore tests passed (18 passed, 7 skipped); compile, diff checks, and a zip layout and deduplication smoke check passed.

Checkpoint: [checkpoint.md](/app/.codex-role-output/checkpoint.md).