# Checkpoint

Task: Add configurable DynamoDB backend billing mode, defaulting to `pay_per_request`, with correct table creation and auto-scaling behavior.

Implemented in `lib/backend/dynamo`: `billing_mode` accepts `pay_per_request` (the default) and `provisioned`, rejects other values, and sends the matching AWS billing mode at creation. On-demand creation omits provisioned throughput. Initialization disables auto scaling and logs the reason for existing or new on-demand tables, using the reported mode for existing tables. Table status now returns the billing mode alongside the status.

Updated the DynamoDB storage documentation and added focused unit tests. The existing tagged integration test file had compile errors; fixed its UUID conversion and DynamoDB client helper types. Verification: `go test ./lib/backend/dynamo` and targeted `go test -tags dynamodb` unit tests both passed with module downloads disabled. AWS-dependent integration tests were not run.
