Added `${VARIABLE_NAME}` substitution as the first configuration decode hook, so values resolve before ports, durations, and other types are decoded. Exact references resolve when the variable exists; other values stay unchanged. Existing `FLIPT_` overrides still take precedence.

Added integration tests for multiple references, typed values, missing and empty variables, invalid patterns, and overrides in [config_test.go](/app/internal/config/config_test.go). The hook is in [config.go](/app/internal/config/config.go).

Verification: `go test ./internal/config ./config -count=1` passed.