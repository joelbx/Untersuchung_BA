Task: add tracing sampling ratio and propagator configuration.
Status: added tracing fields, defaults, validation, schema entries, focused load tests, ratio-based tracer sampling, and runtime selection of all supported propagators from locally cached OpenTelemetry modules. Local tests passed: go test ./internal/config ./config ./internal/tracing ./internal/cmd (with GOPROXY=off, GOSUMDB=off). git diff --check passed.
Constraints: local repository and existing tests only; do not alter git history, index, or harness.
