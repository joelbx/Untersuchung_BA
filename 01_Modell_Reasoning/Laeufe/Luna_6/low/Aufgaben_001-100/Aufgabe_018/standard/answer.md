Updated the `[]string` decode hook in [config.go](/app/internal/config/config.go) to split scalar strings on all whitespace. Blank strings produce an empty slice, and existing sequences and non-string sources pass through unchanged.

Updated the advanced config fixture and added hook coverage for whitespace, blank input, sequences, and non-string sources. The existing config tests exercise both YAML and ENV loading.

Verified with `go test ./internal/config` and `git diff --check`.