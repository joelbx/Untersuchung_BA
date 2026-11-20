# Checkpoint

Implemented native DynamoDB `FieldsMap` writes for current and session events, with readers accepting both `FieldsMap` and legacy JSON `Fields` values. Added `backend.FlagKey` under `.flags` using the backend's standard path separator.

Added a background migration under the existing distributed RFD 24 lock. It scans in bounded pages for records without `FieldsMap`, validates the decoded JSON map by round-tripping its semantic value, and batch writes each page while preserving the legacy `Fields` attribute. Restarting the scan is safe because completed records no longer match the filter. Errors are logged and retried until cancellation.

Validation: `go test ./lib/backend ./lib/events/dynamoevents` passed; `git diff --check` passed.
