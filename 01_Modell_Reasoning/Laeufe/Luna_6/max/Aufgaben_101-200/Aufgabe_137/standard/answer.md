Implemented configurable trace sampling and propagators. `TracingConfig` now validates the sampling ratio and supported propagator values, with defaults applied in both config loading and `Default()`. The configured ratio and propagators are wired into runtime tracing.

Updated the tracing schema and existing config fixture. Added local adapters for B3, B3 multi-header, Jaeger, X-Ray, and OTTrace.

Verification passed: `go test ./internal/config ./internal/tracing ./internal/cmd`; `git diff --check`.