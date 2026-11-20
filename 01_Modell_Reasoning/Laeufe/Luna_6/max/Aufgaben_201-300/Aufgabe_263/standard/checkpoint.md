# Checkpoint

Implemented the DynamoDB event metadata migration.

- New event writes store metadata in the native `FieldsMap` DynamoDB map. Event readers accept both the legacy JSON `Fields` string and `FieldsMap`.
- Added `backend.FlagKey` under the `/.flags` namespace. The migration stores its scan cursor and completion marker there.
- Added a distributed lock around the migration. It scans in bounded pages, converts records in batches of at most 25 with up to 32 workers, persists progress after each completed page, and retries safely after interruption.
- Conversion validates metadata after a DynamoDB encode/decode round trip. Conversion and write failures are logged with record identifiers.
- Added unit coverage for map encoding, legacy conversion, checkpoint persistence, and `FlagKey`.

Verification: `go test -count=1 ./lib/backend ./lib/events/...` and `git diff --check` passed. The DynamoDB AWS-dependent suite is skipped unless its AWS test environment is enabled.
