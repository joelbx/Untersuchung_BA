Task: Add optional audit sink configuration to anonymous telemetry and bump schema to 1.3.
Status: Implemented in internal/telemetry/telemetry.go. Added existing ping test cases for log, webhook, and both; existing no-sink cases verify omission. Updated version assertions. go test ./internal/telemetry passes; git diff --check passes.
