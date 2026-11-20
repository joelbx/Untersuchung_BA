The fault is centered in [tracing.go](/app/internal/config/tracing.go:14): `TracingConfig` lacks the sampling and propagator fields, their defaults, and validation. [Default()](/app/internal/config/config.go:486) also needs the requested values. `Load` already runs each section’s validator after decoding.

For the settings to affect traces, [NewProvider](/app/internal/tracing/tracing.go:33) must use the configured sampling ratio, and [grpc.go](/app/internal/cmd/grpc.go:376) must build the configured propagators. The [tracing schema](/app/config/flipt.schema.json:928) currently rejects both new properties.

Existing tests do not cover these settings. The fix should check defaults, preservation of `samplingRatio: 0.5`, boundary values, all eight propagator options, and the exact validation errors. The behavior of `none` when combined with other options is unspecified.

I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md). This diagnosis-only role did not change project source or tests.