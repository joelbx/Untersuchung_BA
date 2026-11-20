Implemented DynamoDB event writes using the native `FieldsMap` attribute, with readers that support both migrated and legacy records. Added a distributed-lock-protected migration that processes records in bounded batches, resumes safely after interruption, and logs progress and conversion errors. Added the requested `backend.FlagKey` helper.

Verification: `go test ./lib/backend ./lib/events/dynamoevents` passed.

The migration retries automatically after errors and logs records with invalid legacy JSON; those records need correction before migration can finish.