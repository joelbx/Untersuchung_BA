Updated [config.go](/app/internal/config/config.go) so scalar strings decoded into `[]string` split on whitespace, including repeated spaces, tabs, and newlines. Empty strings produce an empty slice; sequences and other source types pass through unchanged.

Updated the CORS fixture and added YAML, ENV, and decode hook coverage. `GOPROXY=off go test ./internal/config` and `git diff --check` passed.