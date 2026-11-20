# Checkpoint

Task: Fix validation of configuration references and make `internal/cue.Validate` and filesystem snapshots return structured, source-located errors consistently.

Implemented:
- Added package-level and validator `Validate` APIs returning one multi-unwrappable error, with `cue.Unwrap` and individual errors formatted as `message (file line:column)`.
- Added missing variant and segment checks for flag rules and segment checks for boolean rollouts.
- Exported `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths`; both constructors validate every selected input before snapshot assembly.
- Updated `flipt validate` to display unwrapped errors and `flipt import` to validate all input before any storage changes.
- Updated valid/reference fixtures and snapshot fixtures to satisfy the validation rules.

Verification: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt` passes. `git diff --check` passes.
