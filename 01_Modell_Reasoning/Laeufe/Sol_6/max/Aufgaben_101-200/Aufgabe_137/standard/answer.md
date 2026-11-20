Added tracing sampling ratio and propagator configuration with the requested defaults and exact validation errors. The settings now control the OpenTelemetry sampler and context propagators; configuration schemas and tests were updated.

The configuration, tracing, schema, and gRPC tests pass with network access disabled.