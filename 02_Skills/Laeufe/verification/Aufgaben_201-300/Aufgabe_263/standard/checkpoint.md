# Checkpoint

Task: store DynamoDB audit event metadata in native `FieldsMap`, migrate legacy `Fields` rows, and preserve reads during migration.

Implemented:
- Event writes store nested JSON values as DynamoDB map, list, scalar, and null attributes. Large JSON numbers retain their decimal representation.
- Read paths accept both `FieldsMap` and legacy `Fields`.
- Background migration scans legacy rows, validates semantic content, writes in batches of at most 25, retries from the beginning while skipping converted rows, and logs progress/errors.
- Migration uses the existing distributed migration lock; date migration runs first to avoid concurrent whole-item writes.
- Added `backend.FlagKey` under `/.flags`.

Verification: `go test ./lib/events/dynamoevents ./lib/backend -count=1` passed after the final lock alias edit. AWS-dependent integration suite is skipped without the local AWS test environment.
