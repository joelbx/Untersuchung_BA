# Debugging checkpoint

Issue: startup release/update separation and `-rc` release classification.

State: implementation complete and verified.

Root cause: `cmd/flipt/main.go:isRelease` checks only empty, `dev`, and `-snapshot`; `-rc` reaches the release branch. That branch performs GitHub lookup and semantic-version comparison in startup. `info.Flipt` already has the required status fields, but startup populates version from an uninitialized semver value for non-releases and latest version from an uninitialized value when no check succeeds.

Pattern: `info.Flipt` is passed to HTTP server and telemetry reporter. Centralizing release classification and update comparison in `internal/release` permits startup to consume one `Info` result. `release.Check` will own its warning on failure and return an error so startup can continue.

Hypothesis: extracting classification and check into `internal/release`, then consuming `Info` in startup, will correctly gate `-rc` builds and preserve status reporting.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`), so scoped `find`/`grep` will be used.

Reproduction: `go test ./internal/release` failed before implementation with `undefined: Is` in the new regression test.

Implementation: `internal/release/check.go` now owns release classification, GitHub release lookup, semantic-version comparison, and warning on check errors. Startup consumes `release.Info`, reports status by configured output mode, and disables telemetry for CI and non-release builds. `info.Flipt` already exposed the required fields; startup now populates its current version from the actual build version.

Verification: `go test ./internal/release ./cmd/flipt ./internal/info` passed; `go test ./internal/telemetry ./internal/cmd` passed; `git diff --check` passed. The release test uses a local HTTP server to verify update comparison and URL propagation without external access.
