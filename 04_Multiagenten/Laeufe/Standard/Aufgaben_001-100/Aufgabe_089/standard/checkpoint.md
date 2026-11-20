# Checkpoint

Task: Fix reference validation for flags and filesystem snapshots, update the Validate error API, and make import failures repeatable.

Completed:
- `internal/cue.Validate` returns a single error with individually unwrap-able, positioned schema and reference errors.
- Unknown variant and segment references, including boolean rollouts, are reported with flag, rule index, file, line, and column.
- Corrected the three valid CUE fixtures to declare their referenced variants.
- Exported `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths`; snapshots validate references before construction.
- `flipt import` checks references before modifying state, so repeated invalid imports fail consistently.
- Updated CLI validation output and added regression tests.

Verification: `go test ./internal/cue ./internal/storage/fs ./cmd/flipt` passed; `git diff --check` passed.
