# Coverstore archive checkpoint

- Implemented canonical 10-digit cover IDs, 4-digit item IDs, 2-digit batch IDs, size-specific ZIP paths/URLs, and uncompressed deduplicated ZIP staging.
- Added batch file locks, batch closure and member validation, upload verification, transactional DB URL reconciliation, and retryable cleanup manifests.
- Added legacy tar reconciliation that verifies all tar/index files before replacing old offsets with remote URLs.
- Added failed/uploaded columns, indexes, migration SQL, and workflow documentation; updated retrieval to respect DB remote URLs.
- Added SQLite integration tests for staging, upload, finalization, interrupted cleanup, remote retrieval, and legacy reconciliation.
- Final checks: coverstore suite 23 passed, 7 skipped; ruff and git diff checks passed.
