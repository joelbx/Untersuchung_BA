# Checkpoint

Implemented environment variable substitution as the first entry in the existing `DecodeHooks` slice. It replaces only string values that exactly match `${NAME}` where names start with an ASCII letter or underscore and continue with ASCII letters, digits, or underscores. `os.LookupEnv` preserves missing references and supports intentionally empty environment values. Because substitution runs before other hooks, downstream conversions handle numeric ports, durations, and enums.

Verification: `go test ./internal/config` passed. `git diff --check` passed. Reverted the `go.work.sum` working-tree changes created by the test run; the intended code change is in `internal/config/config.go`.
