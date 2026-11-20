Tracing now accepts a `samplingRatio` from 0 to 1 and a validated list of the eight supported propagators. Both settings have defaults and are applied to the tracer provider and context propagation. The schema and example config are updated.

Verification passed: `go test ./internal/config ./internal/tracing ./internal/cmd -count=1` with network access disabled.