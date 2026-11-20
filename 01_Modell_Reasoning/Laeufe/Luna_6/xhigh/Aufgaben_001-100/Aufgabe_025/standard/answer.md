Implemented `${VARIABLE_NAME}` substitution as the first decode hook in [config.go](/app/internal/config/config.go:35). It supports multiple references, leaves nonmatching values and missing variables unchanged, and runs before type conversion so environment values can populate integer and enum fields.

`go test ./internal/config` passed.