# Checkpoint

Task: Resolve YAML `${VARIABLE_NAME}` environment variable substitution in configuration parsing.

Implemented: added an exact `${NAME}` matcher and environment lookup as the first entry in `DecodeHooks`. It replaces only string values with a valid placeholder when the referenced environment variable exists, allowing later decode hooks and scalar decoding to consume its string value.

Verification: `go test ./internal/config` passed; `git diff --check` passed.
