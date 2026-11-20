# Checkpoint

Task: Add enabled audit sinks to anonymous telemetry and update schema version to 1.3.
Status: Complete.
Changes: Added optional flipt.audit.sinks payload based on audit log file and webhook Enabled flags; bumped telemetry version to 1.3; expanded telemetry tests for disabled, individual, and combined sinks.
Verification: go test ./internal/telemetry passed; git diff --check passed.
