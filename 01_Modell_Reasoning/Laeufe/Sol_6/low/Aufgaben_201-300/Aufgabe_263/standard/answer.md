Updated DynamoDB event writes to store metadata in the native `FieldsMap` attribute. Reads accept both `FieldsMap` and legacy `Fields` records while migration runs.

The background migration scans legacy records in batches, validates each conversion, logs progress, and runs under a distributed lock. It can resume after interruption. I also added `backend.FlagKey` for keys under `.flags`.

Verification passed: `go test ./lib/events/dynamoevents ./lib/backend`.