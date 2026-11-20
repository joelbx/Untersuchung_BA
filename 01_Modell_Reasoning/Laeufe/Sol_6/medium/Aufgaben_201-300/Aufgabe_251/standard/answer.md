Updated `flipt validate` to report every schema error with its field path, descriptive message, and position in the original YAML. Text output shows each location and issue; JSON output contains the structured results. Validation failures retain a nonzero exit status.

Verified with `go test ./internal/cue ./cmd/flipt -count=1` and a CLI run against the invalid fixture.