Task: Convert DynamoDB audit event storage from legacy Fields JSON strings to native FieldsMap maps.
Status: Implemented new map writes, dual-format reads, and a background migration with distributed backend lock, bounded concurrent conditional updates, progress/error logging, semantic round-trip checks, and a backend completion flag. Added unit tests and an AWS-gated migration integration test.
Verification: go test ./lib/events/dynamoevents ./lib/backend -count=1 passed; git diff --check passed. AWS-dependent suite was skipped by its existing environment gate.
Constraints: No external research/downloads; git history/index and harness configuration untouched.
