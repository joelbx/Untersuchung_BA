Implemented native `FieldsMap` writes and backward compatible reads in the DynamoDB event store. Added a locked, resumable migration that validates legacy JSON before batch writing the map while preserving `Fields`, plus `backend.FlagKey` under `.flags`.

Validation passed: `go test ./lib/backend ./lib/events/dynamoevents` and `git diff --check`.