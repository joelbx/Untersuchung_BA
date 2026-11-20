# Checkpoint

Implemented `billing_mode` for the DynamoDB backend. It defaults to `PAY_PER_REQUEST`, accepts only `PAY_PER_REQUEST` and `PROVISIONED` (AWS SDK enum values: `pay_per_request` and `provisioned`), sets throughput only for provisioned table creation, and disables/logs autoscaling for on-demand existing or newly created tables. `getTableStatus` now returns table status and billing mode.

Validation: `go test ./lib/backend/dynamo` passed; `git diff --check` passed.
