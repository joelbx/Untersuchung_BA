# Checkpoint

Implemented configurable tracing sampling and propagation settings.

- Added `SamplingRatio` and `Propagators` to `TracingConfig`, with Viper and `Default()` defaults of ratio `1` and `tracecontext` plus `baggage`.
- Added the supported `TracingPropagator` string constants and validation for ratios in `[0,1]` (including rejecting NaN) and unsupported propagator names.
- Updated the advanced config expectation to account for the defaults.

Verification: `go test ./internal/config` passes. `git diff --check` passes.
