# Checkpoint

Task: add configurable trace sampling ratio and context propagators to the repository's tracing configuration and runtime.

Completed:
- Added `SamplingRatio` and the supported `TracingPropagator` values to `TracingConfig`, with defaults and exact validation errors.
- Initialized the same defaults in `Default()` and updated the tracing schema.
- Passed the configured ratio into the trace provider and applied configured propagation formats at startup.
- Added local propagator adapters for B3, B3 multi-header, Jaeger, X-Ray, and OTTrace; the OpenTelemetry trace context and baggage implementations remain in use for their options.
- Updated the existing full tracing-config test fixture to include the newly required defaults.

Verification:
- `go test ./internal/config ./internal/tracing ./internal/cmd` passed.
- `git diff --check` passed.
