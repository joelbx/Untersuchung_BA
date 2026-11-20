Updated `flipt validate` to report each failure with its field path, a specific message, and the corresponding YAML file, line, and column. The validation API now returns a structured `Result` with all findings, and text and JSON output include the complete result.

Verified with `go test ./internal/cue ./cmd/flipt -count=1` and `git diff --check`.