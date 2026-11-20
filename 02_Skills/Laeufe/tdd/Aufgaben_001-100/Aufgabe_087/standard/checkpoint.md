# Telemetry implementation checkpoint

Implemented opt-out telemetry configuration, persisted anonymous UUID and report time, four-hour background reporting, startup integration, and `internal/info.Flipt` HTTP handling. The advanced example disables telemetry.

TDD: focused tests first failed for missing telemetry/config/info APIs. A test for failed state writes failed because the in-memory timestamp advanced; fixed by restoring it. A nil-UUID test failed because an all-zero UUID was retained; fixed by regenerating it.

Verification: `GOPROXY=off go test ./...` passed after the final edits. `git diff --check` passed. `rg` is unavailable (`/bin/bash: rg: command not found`); local `find`/`grep` were used.

Limitation: the default HTTPS destination (`https://telemetry.flipt.io/v1/track`) is an implementation assumption from local evidence; external research and live delivery checks were prohibited. The local HTTP test server verifies request shape and successful state updates, but does not verify that the production destination accepts events.
