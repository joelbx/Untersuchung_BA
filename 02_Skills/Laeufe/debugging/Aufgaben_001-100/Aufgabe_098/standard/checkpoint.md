# Checkpoint

Task: include enabled audit sinks in anonymous telemetry and bump schema version to 1.3.

Root cause: `Reporter.ping` built `flipt` telemetry from storage, authentication, and experimental config but never read `cfg.Audit`. `config.AuditConfig.Enabled()` already reflects the two sink flags. Existing telemetry tests passed before changes. New log-only, webhook-only, and both-sinks cases failed as expected because `flipt.audit` was absent.

Fix: add optional `flipt.audit.sinks`, populated from enabled log and webhook flags, and update telemetry version to 1.3. Existing basic case confirms audit is omitted when no sink is enabled. Other telemetry field expectations remain intact.

Checks: `go test ./internal/telemetry -count=1` passed; `go test ./internal/config ./internal/telemetry -count=1` passed; `git diff --check` passed. `rg` was unavailable (`/bin/bash: rg: command not found`), so local searches used `find` and `grep`.
