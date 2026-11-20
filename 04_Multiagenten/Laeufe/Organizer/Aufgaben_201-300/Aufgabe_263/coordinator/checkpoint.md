# Checkpoint

Implemented native DynamoDB `FieldsMap` writes for all three event producers, dual-format reads, and a locked, restart-safe, batched migration of legacy `Fields` records. The migration runs after the existing date migration to avoid concurrent full-item updates. Conversion checks semantic JSON equality before writing and logs progress and record errors. Added `backend.FlagKey` and focused format tests.

Verified: `go test ./lib/events/dynamoevents ./lib/backend -count=1` passed. AWS-dependent suite is skipped without its opt-in environment setting.
