# Checkpoint

Implemented a narrowly scoped mapstructure decode hook in `internal/config/config.go`: only scalar strings targeting `[]string` are split, using `strings.Fields`; empty/whitespace-only input returns a non-nil empty slice. Existing sequences and other target types pass through unchanged. Since the hook is used by Viper's unmarshal path, it handles both YAML values and environment variable strings.

Updated the advanced config fixture to exercise whitespace-separated origins, and added hook coverage for tabs/newlines, repeated and surrounding whitespace, empty input, sequences, and unrelated targets.

Verification: `go test ./internal/config` passed. `git diff --check` passed.
