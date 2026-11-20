Implemented configurable tracing sampling and propagators in [tracing.go](/app/internal/config/tracing.go) and initialized their defaults in [config.go](/app/internal/config/config.go). Validation rejects ratios outside 0–1 and unsupported propagators with the required error messages.

Verification: `go test ./internal/config` passes, and `git diff --check` passes.