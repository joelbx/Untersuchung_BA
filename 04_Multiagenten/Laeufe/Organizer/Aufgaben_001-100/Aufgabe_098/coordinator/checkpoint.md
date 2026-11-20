# Checkpoint

Task: add optional audit sink configuration to anonymous telemetry and update schema version to 1.3.
Status: implemented and verified.
Changes: telemetry flipt payload includes audit.sinks when log and/or webhook audit sinks are enabled; version is 1.3; table tests cover absent, log, webhook, and both.
Verification: go test ./internal/telemetry passed; git diff --check passed.
Delegation: none.
