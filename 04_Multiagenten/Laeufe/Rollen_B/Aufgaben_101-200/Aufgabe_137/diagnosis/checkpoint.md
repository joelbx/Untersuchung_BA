# Fault localization progress

Diagnosis complete. Project source and tests remain unchanged.

- `internal/config/tracing.go`: `TracingConfig` has neither requested field or propagator enum, sets no corresponding Viper defaults, and does not implement `validate()`. `Load` in `internal/config/config.go` discovers validators before unmarshalling and executes them afterward.
- `internal/config/config.go`: `Default()` initializes tracing without the new defaults. The existing decode hooks include string-to-slice handling, so mapstructure tags/defaults should support YAML and environment overrides; verify a configured `samplingRatio: 0.5` survives Viper decoding.
- `internal/tracing/tracing.go`: `NewProvider` hardcodes `AlwaysSample()` and currently takes no tracing config. `internal/cmd/grpc.go` calls it and hardcodes TraceContext+Baggage propagation. To make the settings operational, those call sites need wiring beyond config parsing.
- `config/flipt.schema.json`: tracing allows no additional properties and lacks the new settings, so schema should be considered for consistency.
- Existing `internal/config/config_test.go` has `TestLoad` default/advanced cases and `internal/tracing/tracing_test.go` covers exporter selection, but neither covers requested sampling/propagator behavior. Likely checks: both load paths, explicit 0 and 0.5, out-of-range exact error, every allowed propagator and invalid-entry exact error, then runtime sampler/propagator selection.
- Uncertainty: the issue specifies config requirements explicitly; whether runtime wiring and JSON schema are in the coordinator's patch scope should be decided there. Also clarify desired semantics of `none` mixed with other propagators and NaN input if accepted by the decoder.
