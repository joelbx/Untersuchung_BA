# Checkpoint

Implemented DynamoDB event metadata as native `FieldsMap` maps for all current event writers. Readers accept both `FieldsMap` and legacy `Fields`, preserving audit log access during conversion.

Added a `FlagKey` backend helper under the internal `.flags` namespace. Added a startup migration guarded by a distributed backend lock and completion flag. It scans legacy rows in bounded pages, converts and validates values through DynamoDB's attribute round trip, writes in batches, logs progress and record errors, and resumes by filtering already migrated rows. It runs after the existing date migration to avoid competing whole-item rewrites.

Verification: `go test ./lib/backend ./lib/events/dynamoevents` passed; `git diff --check` passed. AWS dependent DynamoDB integration tests are skipped unless enabled by their existing environment setting.
