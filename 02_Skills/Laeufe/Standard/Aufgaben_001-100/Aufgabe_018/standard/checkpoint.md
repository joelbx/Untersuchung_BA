# Checkpoint

Task: restore whitespace parsing of scalar string values decoded into `[]string`, including YAML and ENV.

Implemented in `internal/config/config.go`: a decode hook applies only to string sources and `[]string` targets, uses `strings.Fields`, and returns a non-nil empty slice for empty input. The loader enables empty ENV values so they reach the hook. Updated the advanced YAML fixture and added focused hook and YAML/ENV tests.

Checks:
- Initial `GOPROXY=off go test ./internal/config` failed: the empty ENV case returned the default `[]string{"*"}` because Viper ignored empty ENV values. Fixed with `v.AllowEmptyEnv(true)`.
- Final `GOPROXY=off go test ./internal/config` passed.
- `git diff --check` passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); searches used `grep`/`find`.
