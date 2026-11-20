# Checkpoint

Implemented exact `${VARIABLE_NAME}` substitution as the first entry in `internal/config.DecodeHooks`. The hook uses `os.LookupEnv`, validates the requested identifier pattern, only processes actual string values, and preserves missing references. Later decode hooks therefore receive the substituted value for conversions such as integer ports and enum-backed string settings.

Added `TestLoadEnvironmentVariableReferences` covering multiple references, conversion to an integer and log encoding, unchanged missing and partial references, and precedence of an existing `FLIPT_...` override.

Verification: `go test ./internal/config` passes; `git diff --check` passes. Go updated `go.work.sum` during the test invocation, and that generated change was restored.
