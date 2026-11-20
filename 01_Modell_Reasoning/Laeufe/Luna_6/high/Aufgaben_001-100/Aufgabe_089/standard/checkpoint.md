# Checkpoint

Implemented referential validation for variant and segment references in flag rules and boolean rollouts, with per-error source locations and multi-error unwrapping. The `validate` CLI now consumes the error-only validator API. Filesystem snapshots expose `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths`, and reject unresolved references during construction.

Compatibility note: filesystem import fixtures are intentionally less strict than the CUE schema, so snapshot constructors enforce referential integrity there while `FeaturesValidator.Validate` also performs full CUE validation.

Verification: `go test ./internal/cue ./internal/storage/fs ./cmd/flipt` passes.
