Implemented configurable tracing sampling and propagators. `TracingConfig` now defaults to a sampling ratio of 1 and TraceContext+Baggage, validates the requested range and propagator options, and accepts `samplingRatio` as an alias for `sampling_ratio`. Runtime tracing uses the configured ratio and propagators.

Updated the config schema and the existing load fixture to cover a 0.5 ratio and custom propagators.

Verification passed:

- `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing`
- `GOPROXY=off GOSUMDB=off go test ./internal/cmd`

Offline `go mod tidy` could not resolve unrelated dependencies missing from the local cache.