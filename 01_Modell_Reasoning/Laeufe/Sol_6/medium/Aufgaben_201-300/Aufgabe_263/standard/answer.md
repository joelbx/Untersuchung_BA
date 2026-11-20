DynamoDB audit events now write metadata to the native `FieldsMap` attribute. Reads accept both `FieldsMap` and legacy `Fields` records during migration.

The background migration uses a distributed lock, bounded concurrent updates, conditional writes, and content validation. It logs progress and can resume after interruption. I added tests for map conversion and migration.

`go test ./lib/events/dynamoevents ./lib/backend -count=1` and `git diff --check` passed. The AWS integration suite was skipped by its existing environment gate.