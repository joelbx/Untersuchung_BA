# Checkpoint

Task: Report source-located referential errors during validation, import, and filesystem snapshot creation.

Completed: `FeaturesValidator.Validate` returns one unwrap-able error with located CUE and reference issues. Rule checks cover scalar and list segment references, variants, and boolean flag rules. Import checks rule references before creating resources, so repeated attempts fail consistently. `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths` are exported; both constructors validate before loading. Existing CUE fixtures now have valid variant keys, and the CUE schema accepts the existing snapshot rollout forms.

Verification: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt` and `go test ./internal/storage/fs/...` passed with GOPROXY=off and GOSUMDB=off. CLI smoke checks passed for valid input and JSON validation errors. `git diff --check` passed.
