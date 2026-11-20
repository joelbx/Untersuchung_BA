# Checkpoint

Task: improve YAML validation diagnostics and command output.

Implemented:
- Structured `Result` and `FeaturesValidator.Validate` API with all CUE validation errors.
- Field paths and YAML key positions for each issue, including corrected source columns.
- JSON and text output through the supplied writer; failure status and read error reporting in the command.
- Tests for multiple errors, locations, range constraints, output formats, valid input, and malformed YAML.

Verification:
- `go test ./internal/cue ./cmd/flipt -count=1` exited 0 (`internal/cue` passed; `cmd/flipt` has no test files).
- `go run ./cmd/flipt validate -F json internal/cue/fixtures/invalid.yaml` emitted field path, constraint, and location, then exited 1 as expected.
- `git diff --check` exited 0.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.
