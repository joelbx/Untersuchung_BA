Added a decode hook that resolves YAML values matching `${VARIABLE_NAME}` before other conversions. Values with an invalid pattern, non-string values, and references to unset variables stay unchanged; existing `FLIPT_` overrides retain precedence.

Added tests for multiple references, integer port conversion, string values, and edge cases. `go test ./internal/config -count=1` passes.