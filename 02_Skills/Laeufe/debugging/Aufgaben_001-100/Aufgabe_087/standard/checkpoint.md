# Checkpoint

## Root cause and reproduction

- Configuration had no `Meta.TelemetryEnabled` or `Meta.StateDirectory`; server startup had no reporter. Version metadata was private to `cmd/flipt`.
- A focused pre-fix test compiling `config.Default().Meta.TelemetryEnabled` failed as expected: `config.Default().Meta.TelemetryEnabled undefined`.
- `rg` was unavailable (`/bin/bash: rg: command not found`); inspected the repository with `find` and `grep`.

## Patch

- Added opt-out telemetry config, environment loading, and an explicitly disabled advanced example.
- Added persistent per-host UUID state, four-hour scheduling, anonymous ping payload, error logging, and startup wiring. Added `internal/info.Flipt` HTTP handler for shared version metadata.
- Local tests cover config env/default, disabled mode, UUID persistence and recovery, invalid directory, event payload, failed/successful sends, timestamp persistence, and info response.

## Verification

- `GOPROXY=off go test ./... -count=1`: passed after final edits.
- `GOPROXY=off go test ./config ./telemetry ./internal/info ./cmd/flipt -count=1`: passed after all edits.
- `git diff --check`: passed.

## Remaining uncertainty

- The issue provides no telemetry collector URL. The reporter currently targets `https://telemetry.flipt.io/v1/track`; live delivery was not tested because external research/network checks are disallowed. Local HTTP tests verify request payload and success/failure handling.
