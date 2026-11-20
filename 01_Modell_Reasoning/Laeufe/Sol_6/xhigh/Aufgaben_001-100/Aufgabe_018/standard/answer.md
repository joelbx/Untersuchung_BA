Updated the config decode hook so scalar strings become `[]string` values by splitting on whitespace, including spaces, tabs, and newlines. It also preserves comma-separated values. Empty strings produce an empty slice; sequences and non-string values pass through unchanged.

Updated the CORS fixture and tests for YAML and ENV parsing. `go test ./internal/config` and `git diff --check` pass.