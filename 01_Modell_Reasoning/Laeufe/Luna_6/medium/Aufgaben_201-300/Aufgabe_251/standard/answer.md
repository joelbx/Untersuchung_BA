Implemented structured validation results with field paths, descriptive messages, and YAML source locations. JSON output now uses the supplied writer, and the validator API returns all errors reported by CUE.

Added regression coverage for field paths, locations, and JSON serialization. `go test ./internal/cue ./cmd/flipt` and `git diff --check` pass.