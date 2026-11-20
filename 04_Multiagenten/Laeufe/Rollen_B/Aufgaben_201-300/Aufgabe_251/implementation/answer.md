Implemented structured validation results that report every finding with its field path, descriptive message, and original YAML file, line, and column. Text and JSON output now use those results, and the command reports unexpected errors before exiting.

Verified with `go test ./internal/cue ./cmd/flipt`, including new tests for multiple errors and JSON output.