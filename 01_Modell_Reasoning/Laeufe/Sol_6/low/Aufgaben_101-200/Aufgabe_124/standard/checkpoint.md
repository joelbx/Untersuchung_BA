# Checkpoint
Task: add DynamoDB backend billing_mode support with pay_per_request default.
Implemented: mode validation/default, create-table billing mode and throughput, status mode return, auto-scaling suppression for on-demand tables.
Verification: go test ./lib/backend/dynamo passed; git diff --check passed.
