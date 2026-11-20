Configuration values matching `${VARIABLE_NAME}` now resolve during parsing, before type conversion. Other values stay unchanged, and existing `FLIPT_` environment overrides still take precedence.

Added coverage for multiple references, integer and duration conversion, string values, and invalid or missing references. `go test ./internal/config -count=1` passes.