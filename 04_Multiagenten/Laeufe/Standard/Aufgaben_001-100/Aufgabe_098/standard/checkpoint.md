# Checkpoint

Task: include enabled audit sinks in anonymous telemetry and update schema version to 1.3.
Status: implemented and verified.
Changes: optional `flipt.audit.sinks` emits `log` and/or `webhook` from the audit sink enabled flags; omitted with no enabled sinks. Telemetry version is 1.3. Existing telemetry tests cover all sink combinations.
Verification: `GOPROXY=off GOSUMDB=off go test ./internal/telemetry` passed; `git diff --check` passed.
