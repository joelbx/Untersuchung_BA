Added tracing `SamplingRatio` and supported `Propagators` settings, with defaults in `Default()` and file loading. Validation returns the required error messages, and the config schema now includes both settings.

Added a test confirming that a configured ratio of `0.5` is preserved and updated the existing default expectation. `go test ./internal/config` and `git diff --check` pass.