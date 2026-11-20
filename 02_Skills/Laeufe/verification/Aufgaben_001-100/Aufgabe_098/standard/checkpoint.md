# Checkpoint

Task: Add optional audit sink configuration to anonymous telemetry and update schema version to 1.3.

Implementation: `internal/telemetry/telemetry.go` reports `flipt.audit.sinks` for enabled log file and webhook audit sinks; omits audit when neither is enabled. Telemetry version is 1.3. Existing fields retain their previous construction.

Tests: Added cases for log only, webhook only, and both sinks. Existing basic case verifies audit omission. Updated version assertions. Red run: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/telemetry` failed as expected before implementation, showing version 1.2 and missing audit field. Green run: same command passed (`ok go.flipt.io/flipt/internal/telemetry 0.007s`). `git diff --check` passed.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`. Go test changed `go.work.sum`; restored its original worktree content from HEAD.
