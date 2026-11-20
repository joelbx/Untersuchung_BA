# Checkpoint

Implemented exact `${VARIABLE_NAME}` substitution as the first configuration decode hook in `internal/config/config.go`. It uses `os.LookupEnv`, preserving unmatched strings, missing references, empty environment values, and non-string inputs according to the hook's type check. Existing Viper environment overrides retain precedence.

Added `internal/config/env_decode_test.go` to cover multiple references in YAML, integer and duration conversion, log encoding, conventional overrides, malformed and missing references, and a non-string YAML value.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` exited 0 (`ok go.flipt.io/flipt/internal/config 0.466s`). `git diff --check` exited 0. Initial focused test revealed a panic on a defined string type; the hook was corrected and the focused test and full package suite passed on rerun.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `grep` and `find` for local inspection. No downloads were requested.
