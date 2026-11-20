# Checkpoint

Completed: CUE validation now returns one multi-error with file, line, and column for shape and reference errors. It checks rule variants, rule segments, and boolean rollout segments. CLI validation and import use the new API; import validates before mutating state. Filesystem snapshot constructors are exported and validate each input file.

Verification: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt` passed. `git diff --check` passed.
