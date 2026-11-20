# Checkpoint

Task: implement opt-out anonymous Flipt telemetry per repository issue.

Implemented:
- Default-enabled `Meta.TelemetryEnabled` and `Meta.StateDirectory`, including `FLIPT_META_TELEMETRY_ENABLED` and `FLIPT_META_STATE_DIRECTORY` loading.
- Persistent `telemetry.json` state with schema version, stable UUID repair, RFC3339 timestamps, safe directory creation, and disabling when the configured directory is a file.
- Anonymous `flipt.ping` reporting with the UUID and schema/Flipt versions, startup scheduling and four-hour cadence, cancellation, and logged non-fatal errors.
- Server startup integration, `internal/info.Flipt` HTTP handler, tests for telemetry/config/info behavior, and explicit telemetry opt-out in `config/testdata/advanced.yml`.

Verification: `go test ./...` passes; `git diff --check` passes. No git history, index baseline, or harness configuration was changed.
