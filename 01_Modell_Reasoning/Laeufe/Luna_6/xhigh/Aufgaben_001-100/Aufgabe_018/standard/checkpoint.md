# Checkpoint

Resolved the scalar-string to `[]string` decoding regression in `internal/config/config.go`.

- The decode hook applies only to string sources and exact `[]string` targets.
- It splits on Unicode whitespace and commas, ignores repeated/leading/trailing separators, and returns a non-nil empty slice for blank input.
- Updated the advanced config fixture to exercise whitespace-separated origins through both YAML and environment loading; added direct hook coverage for empty input and unchanged non-string/sequence cases.
- Verification: `go test ./internal/config` passed; `git diff --check` passed.
