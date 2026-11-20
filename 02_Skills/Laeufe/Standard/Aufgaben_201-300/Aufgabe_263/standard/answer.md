Updated DynamoDB audit events to write metadata as a native `FieldsMap`. Readers accept both `FieldsMap` and legacy `Fields` records during migration.

Added a distributed-lock-protected migration that scans and writes in batches, validates each conversion, logs progress and errors, and can resume after interruption. Added unit tests for nested metadata, large integers, and legacy reads.

`go test ./lib/events/dynamoevents ./lib/backend` passed. The AWS-dependent integration tests were skipped locally, so the migration has not been verified against a live DynamoDB table.