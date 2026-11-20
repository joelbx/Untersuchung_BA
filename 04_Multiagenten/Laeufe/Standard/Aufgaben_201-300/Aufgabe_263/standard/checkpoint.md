# Checkpoint

Implemented native DynamoDB FieldsMap storage for all event write paths, dual-format reads, and a background migration with backend distributed locking, batch writes, retry/backoff, per-record semantic validation, progress logs, and a completion flag. Added a conversion test covering nested metadata, empty strings, and large integers. Verified with `go test ./lib/events/dynamoevents ./lib/backend` and `git diff --check`. AWS-dependent integration suite is skipped without AWSRunTests.
