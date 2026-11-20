# Checkpoint

## Objective
Add configurable DynamoDB billing mode support, defaulting to on-demand, and ensure initialization and autoscaling follow the table's capacity mode.

## Completed
- Added `billing_mode` configuration validation for `pay_per_request` and `provisioned`; the default is `pay_per_request`.
- Table creation passes the corresponding AWS billing mode, omits provisioned throughput for on-demand, and uses configured capacity units for provisioned mode.
- Table status now includes the existing table's billing mode. Initialization suppresses autoscaling and logs when the table is or will be on-demand.
- Documented billing mode and its cost behavior. Updated the provisioned autoscaling test configuration and corrected stale test helper compatibility issues so the tagged test package compiles.

## Verification
- `go test ./lib/backend/dynamo` passed.
- `go test -tags dynamodb -run '^$' ./lib/backend/dynamo` passed (compile check only; tagged tests make live AWS calls).
- `git diff --check` passed.
