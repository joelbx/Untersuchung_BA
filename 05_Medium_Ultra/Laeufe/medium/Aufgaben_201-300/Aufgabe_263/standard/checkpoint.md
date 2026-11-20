# Checkpoint

Implemented native DynamoDB `FieldsMap` writes for all audit event paths, compatible reads for legacy `Fields`, and a locked, resumable batch migration with per-record validation, progress flags, and retry handling. Added local conversion tests. `go test ./lib/events/dynamoevents ./lib/backend` and `git diff --check` pass. AWS-dependent integration suite was skipped by its existing test gate.
