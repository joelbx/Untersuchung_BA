# Checkpoint

Task: add OCI-backed filesystem snapshot source and make SnapshotSource.Get context-aware.

Plan:
- Inspect OCI store and existing source implementations/callers.
- Update the shared interface, all source implementations, and callers.
- Implement OCI snapshot fetch, refresh, and subscription behavior.
- Run focused existing tests and record results.
