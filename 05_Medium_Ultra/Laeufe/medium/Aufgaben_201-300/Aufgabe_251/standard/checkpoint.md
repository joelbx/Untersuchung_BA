# Checkpoint

Resolved YAML validation diagnostics in `internal/cue/validate.go` and `cmd/flipt/validate.go`.

- Added `Result`, `FeaturesValidator`, `NewFeaturesValidator`, and structured `Validate` errors with field paths, messages, and YAML key positions.
- Preserved all CUE validation findings, added a malformed YAML location fallback, and made text/JSON output use the provided writer. JSON success emits an empty result.
- CLI prints the failure reason to stderr and retains its configured issue exit code.
- Added focused tests for multiple errors, exact coordinates, output formats, valid results, and malformed YAML.

Verification: `go test ./internal/cue ./cmd/flipt -count=1` passed; `git diff --check` passed; `go run ./cmd/flipt validate -F json internal/cue/fixtures/invalid.yaml` returned exit status 1 and reported rollout at line 17, column 7.
