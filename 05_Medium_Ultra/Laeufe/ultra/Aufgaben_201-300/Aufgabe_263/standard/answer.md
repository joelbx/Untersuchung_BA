Implemented native DynamoDB `FieldsMap` storage for all audit event write paths. New readers accept both `FieldsMap` and legacy `Fields`, and the conversion preserves empty values, nested data, and large numbers. See [event_fields.go](/app/lib/events/dynamoevents/event_fields.go) and [dynamoevents.go](/app/lib/events/dynamoevents/dynamoevents.go).

The [migration](/app/lib/events/dynamoevents/fieldsmap_migration.go) uses a distributed lock, resumable page checkpoints, conditional batches of up to 25 updates, semantic validation, and record-level error logging. It also preserves older pagination cursors.

Delegated the format, migration, and backend helper work to native subagents, then reviewed and verified the combined patch. `go test ./lib/backend ./lib/events/dynamoevents -count=1` passed. The AWS-dependent integration suite was skipped by its existing test gate.

**Rollout limits:** older binaries cannot read map-only rows during a mixed-version deployment. The hourly sweep for late legacy writes scans the full table.