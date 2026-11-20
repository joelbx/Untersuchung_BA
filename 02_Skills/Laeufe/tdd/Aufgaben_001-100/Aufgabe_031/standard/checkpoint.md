# Checkpoint

Task: Make `config.Load("")` load defaults with `FLIPT_` environment overrides, and make startup use that loader when no config file exists.

Implemented:
- `internal/config/config.go`: skip reading a file for an empty path; keep existing Viper defaults, environment binding, decoding, and validation.
- `cmd/flipt/main.go`: always call `config.Load(path)` after path detection.
- Regression tests cover default values, `FLIPT_LOG_LEVEL` and `FLIPT_SERVER_HTTP_PORT` overrides without a file, file plus environment precedence, and startup without a file.

TDD evidence:
- `GOPROXY=off go test ./internal/config -run 'TestLoadWithoutPath|TestLoadFileAppliesEnvironmentOverrides' -count=1` failed before the loader fix: `loading configuration: Config File "config" Not Found in "[]"`; passed after the fix.
- `GOPROXY=off go test ./cmd/flipt -run TestBuildConfigWithoutFileAppliesEnvironmentOverrides -count=1` failed before the startup fix: expected `DEBUG`, got `INFO`; passed after the fix.

Verification:
- `GOPROXY=off go test ./internal/config ./cmd/flipt -count=1` passed.
- `GOPROXY=off go test ./...` ran and failed only in `go.flipt.io/flipt/internal/cache/redis`: `TestSet`, `TestGet`, and `TestDelete` could not start a Redis container because Docker is unavailable (`Cannot connect to the Docker daemon at unix:///var/run/docker.sock`). These unrelated tests remain unverified in this environment.
- `git diff --check` passed.
