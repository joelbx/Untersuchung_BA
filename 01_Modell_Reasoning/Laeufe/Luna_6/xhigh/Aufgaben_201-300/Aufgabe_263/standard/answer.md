Implemented native DynamoDB `FieldsMap` storage across all event write paths, with readers that accept both `FieldsMap` and legacy `Fields` data.

Added an automatically started migration that uses batch writes, validates converted metadata, records resumable checkpoints under `backend.FlagKey`, logs problematic records, and shares the existing distributed migration lock.

Added focused tests for map conversion, legacy reads, empty collections, and flag key composition.

Verification passed: `go test ./lib/events/dynamoevents ./lib/backend`; `git diff --check` is clean.