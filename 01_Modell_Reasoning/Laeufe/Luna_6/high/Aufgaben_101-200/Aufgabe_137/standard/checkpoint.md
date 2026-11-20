# Checkpoint

Implemented tracing sampling ratio and propagator configuration, validation, defaults, schema constraints, and runtime wiring. Added the locally available OpenTelemetry propagator modules. The advanced config fixture verifies that `samplingRatio: 0.5` survives loading while omitted propagators use defaults.

Verification passed: `go test ./internal/config ./internal/tracing ./internal/cmd`, `go test ./internal/config ./internal/tracing`, and `git diff --check`.
