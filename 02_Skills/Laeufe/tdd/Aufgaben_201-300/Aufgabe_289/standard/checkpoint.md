# Checkpoint

Task: expose default config and decode hooks; make default configuration decode and validate against CUE.

Progress:
- Added `TestDefaultConfigDecodesWithExportedHooks`. The first run (`GOPROXY=off go test ./internal/config -run '^TestDefaultConfigDecodesWithExportedHooks$' -count=1`) failed as expected with undefined `DefaultConfig` and `DecodeHooks`.
- Moved the complete default fixture into exported `DefaultConfig`; existing load tests now use it.
- Exported `DecodeHooks` and composed them in `Load` alongside the experimental skip hook.
- Changed storage Local and Git to pointers, added nil validation, and updated tests using struct literals.
- Added the version mapstructure tag.
- Focused regression and `GOPROXY=off go test ./internal/config -count=1` pass.
- `GOPROXY=off go test ./...` is in progress.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `grep` and `find`.

Final verification:
- `gofmt -w internal/config/config.go internal/config/config_test.go internal/config/storage.go internal/config/defaults_test.go`: completed.
- `git diff --check`: passed.
- `GOPROXY=off go test ./internal/config -count=1`: passed.
- `GOPROXY=off go test ./...`: failed in `go.flipt.io/flipt/internal/server/cache/redis`: `TestSet`, `TestGet`, and `TestDelete` could not start Redis because `Cannot connect to the Docker daemon at unix:///var/run/docker.sock`. All other packages shown in the output passed or had no tests. The Redis tests remain unverified in this environment.
- Extended the regression test to decode the entire `DefaultConfig()` struct through the exported hook composition; focused test and full `internal/config` suite pass after this final test change.
