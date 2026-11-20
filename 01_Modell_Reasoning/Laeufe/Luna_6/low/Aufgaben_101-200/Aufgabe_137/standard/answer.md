Added `SamplingRatio` and `Propagators` to tracing config, with defaults and validation for the 0–1 range and supported propagator values. The exact requested error messages are returned.

`go test ./internal/config` did not finish within the available run window, so I can’t confirm the test result.