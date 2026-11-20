Added exact `${VARIABLE_NAME}` substitution as the first configuration decode hook, so substituted values can be converted to types such as integer ports. Missing variables, nonmatching values, and nonstring values remain unchanged. Existing `FLIPT_*` overrides still take precedence.

Added integration tests and ran `go test ./internal/config -count=1` successfully.