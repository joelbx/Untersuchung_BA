# Checkpoint

Issue: Support `${VARIABLE_NAME}` exact-value environment substitutions in YAML configuration during Viper decoding, with substitutions applied before type conversion hooks.

Implemented: Added an environment substitution decode hook at the start of `DecodeHooks`. It replaces only exact `${NAME}` references whose names match the required identifier format and whose variables exist; the result proceeds through subsequent type conversion hooks.

Coverage: `TestLoadEnvironmentVariableSubstitution` exercises multiple values, integer port conversion, enum/string substitution, unset/malformed references, and partial strings.

Verification: `go test ./internal/config` passes.
