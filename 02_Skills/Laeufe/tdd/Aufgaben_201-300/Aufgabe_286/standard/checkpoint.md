# Checkpoint

Task: Separate startup release/update handling, classify prereleases correctly, and gate telemetry. Following test driven development: add behavioral tests and observe failures before production edits.

Initial state: clean worktree. `rg` is unavailable (`/bin/bash: rg: command not found`); use `find` and `grep` for local inspection.

TDD progress: `TestIsExcludesPrereleaseBuilds` failed with undefined `Is`, then passed. `TestCheckWithClientReportsUpdateStatus` failed with undefined `checkWithClient`, then passed. All tests run with `GOPROXY=off GOSUMDB=off`.

Startup changes: main now uses release.Is and release.Check, reports release.Info through console/logger, preserves current version in info.Flipt, and disables telemetry for non-release builds. Targeted startup test failed before `reportUpdateStatus` existed and passed after implementation. Additional `v1.2.3-rc1` case failed then passed after classification change.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/release ./cmd/flipt` passed. `GOPROXY=off GOSUMDB=off go test ./...` failed only in `internal/server/cache/redis`: TestSet, TestGet, TestDelete cannot create Redis container because Docker daemon at unix:///var/run/docker.sock is unavailable. These tests remain unverified in this environment. All other packages listed by the command passed.
