# Checkpoint

Task: separate configuration warnings from Config through Result, add explicit-key deprecations including ui.enabled, update callers and tests.

Initial inspection: loader is in internal/config/config.go; main caller is cmd/flipt/main.go. `rg` is unavailable, so local searches use grep/find.

Changes: `Load` returns `*Result` with `Config` and `Warnings`; warnings are collected from explicit file keys before defaults. The CLI logs `Result.Warnings`. Added `ui.enabled` deprecation, updated existing warning tests, and added fixtures for both UI values and expiration alone.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/config ./cmd/flipt` — exit 0; config tests pass, CLI package compiles (no test files).
- `git diff --check` — exit 0.
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./...` — exit 1. The three Redis cache tests (`TestSet`, `TestGet`, `TestDelete`) fail during container setup with `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`. Other packages in this run passed or had no tests. The Redis tests remain unverified because Docker is unavailable.
