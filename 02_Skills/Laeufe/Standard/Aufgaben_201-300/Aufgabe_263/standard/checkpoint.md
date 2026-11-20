# Checkpoint

Implemented DynamoDB event `FieldsMap` writes, mixed-format reads, and an asynchronous, distributed-lock-protected migration. Migration scans consistently in 25-item pages, validates JSON semantic equivalence, writes batches with retry of unprocessed items, logs progress and conversion errors, and uses a backend `.flags` completion marker. On interruption or error, retry scans again and skips converted records.

Added unit tests for nested fields, large integer precision, and legacy reads. `go test ./lib/events/dynamoevents ./lib/backend` passed. AWS-dependent DynamoDB integration tests are skipped locally because `TELEPORT_AWS_RUN_TESTS` is not enabled; live migration behavior remains unverified here.

`rg` was unavailable (`/bin/bash: rg: command not found`); used grep/find for repository inspection.
