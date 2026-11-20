Implemented exact `${VARIABLE_NAME}` substitution as the first entry in `DecodeHooks` in [config.go](/app/internal/config/config.go:34). It supports multiple variables, preserves unmatched or unset placeholders, and lets later hooks convert substituted values to their target types.

Verification: `go test ./internal/config` passed; `git diff --check` passed.