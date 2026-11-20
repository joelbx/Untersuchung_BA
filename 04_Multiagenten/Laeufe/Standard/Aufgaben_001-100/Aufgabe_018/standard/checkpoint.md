Task: Fix whitespace parsing of scalar strings into []string configuration fields in internal/config/config.go.
Status: Complete. Replaced comma-only decode hook with whitespace splitting for string to []string. Updated advanced fixture and tests for YAML, ENV, empty strings, and unchanged non-string/sequence inputs.
Verification: go test ./internal/config passed; git diff --check passed.
