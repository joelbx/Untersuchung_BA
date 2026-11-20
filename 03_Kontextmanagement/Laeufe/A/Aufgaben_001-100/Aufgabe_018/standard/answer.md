Updated [config.go](/app/internal/config/config.go) so scalar strings decoded into `[]string` split on whitespace, including spaces, tabs, and newlines. Empty strings produce an empty slice; existing sequences remain unchanged. Updated the CORS fixture and added YAML and ENV coverage.

Validation: `go test ./internal/config` and `git diff --check` passed.