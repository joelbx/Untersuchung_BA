Updated [config.go](/app/internal/config/config.go) so scalar strings decoded into `[]string` split on whitespace. Empty strings produce an empty slice, and non-string sources remain unchanged. The updated CORS fixture and tests cover YAML and ENV inputs, including tabs, newlines, and repeated spaces.

`go test ./internal/config` and `git diff --check` passed.