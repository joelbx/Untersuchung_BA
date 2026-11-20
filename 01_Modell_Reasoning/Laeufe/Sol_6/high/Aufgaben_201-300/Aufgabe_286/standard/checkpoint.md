# Checkpoint

- Task: separate startup release/update status from version logic; classify prereleases correctly; preserve logging and telemetry behavior.
- Initial state: working tree clean; no AGENTS.md found.
- Implemented: `internal/release` owns release classification, GitHub lookup, comparison, and warning on lookup failure. Startup consumes `release.Info`, reports status by log encoding, and disables telemetry for CI and non-release builds.
- Verified: `GOPROXY=off GOSUMDB=off go test ./internal/release ./internal/info ./internal/telemetry ./cmd/flipt` passed; `git diff --check` passed.
