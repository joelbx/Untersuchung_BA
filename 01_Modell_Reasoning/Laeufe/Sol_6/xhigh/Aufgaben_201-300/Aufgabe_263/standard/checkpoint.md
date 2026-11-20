Task completed: DynamoDB audit events now write native FieldsMap values. Reads accept both FieldsMap and legacy Fields. Conversion preserves nested maps/lists, nulls, strings, booleans, and JSON numeric precision, and validates the round trip.
Migration: background pass starts after RFD24 migration, uses a distributed backend lock, bounded consistent scans, 25-item batch writes, a persisted cursor under backend.FlagKey, progress/error logs, retry, and hourly passes for rows written by older nodes.
Pagination checkpoints use the stable DynamoDB primary key across conversion.
Verification: go test ./lib/events ./lib/events/dynamoevents ./lib/backend (pass). Added local fake-DynamoDB test for batch failure and cursor resume; conversion and compatibility tests pass. git diff --check passes.
Constraints observed: local repository/tests only; no git history/index/harness changes.
