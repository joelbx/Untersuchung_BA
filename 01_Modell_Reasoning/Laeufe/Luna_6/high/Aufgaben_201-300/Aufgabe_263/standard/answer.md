Implemented native DynamoDB `FieldsMap` storage and added `FlagKey` under the backend `.flags` prefix. Event readers support both the new map and legacy JSON strings.

Added a distributed-lock migration that scans and batches legacy events, validates converted values, logs progress, resumes after interruption, and records completion. It runs after the existing date migration to avoid conflicting item rewrites.

Verification passed: `go test ./lib/backend ./lib/events/dynamoevents` and `git diff --check`. AWS dependent integration tests require their existing environment setting.