# Checkpoint

Task: migrate DynamoDB audit event metadata from JSON string `Fields` to native map `FieldsMap`, preserving compatibility and adding a resumable, locked migration.

Status: investigating repository code, tests, and history before edits.

## Investigation

Root cause: all three write paths set `event.Fields` to serialized JSON and `dynamodbattribute.MarshalMap` stores it as a DynamoDB string. Session and search reads deserialize only `Fields`. Existing RFD24 migration demonstrates a strongly consistent paged scan, bounded batches, retries of unprocessed writes, and `backend.RunWhileLocked`.

Hypothesis: storing a native map on writes, reconstructing JSON from it on reads (with legacy fallback), and idempotently migrating legacy records under a distributed lock will preserve behavior and expose fields to DynamoDB expressions. Numeric JSON tokens require explicit conversion to DynamoDB N and back to avoid precision loss.

## Implementation and verification

Added native `FieldsMap` serialization for all three event write paths, map-aware reads with legacy fallback, exact JSON number handling, and a bounded scan / batch-write migration with distributed locking, retry of unprocessed writes, progress logging, semantic validation, and a completion flag under `backend.FlagKey`. Changed sub-page checkpoints to use immutable event keys so conversion does not invalidate pagination.

The focused tests were first run before implementation and failed at compile time for missing `marshalEvent`, `unmarshalEvent`, and `convertLegacyItem`, as expected. After implementation, `go test ./lib/events/dynamoevents ./lib/backend -count=1` passed. `go test -v ./lib/events/dynamoevents -run 'TestFieldsMapRoundTrip|TestConvertLegacyItem|TestDynamoevents' -count=1` passed the two local tests; the existing AWS-dependent suite reported `0 passed, 5 skipped` because `AWSRunTests` is not enabled. No AWS integration validation was performed.
