# Checkpoint

Task: Add DynamoDB backend billing_mode support, defaulting to pay_per_request, and adjust table creation and autoscaling behavior.

Completed:
- Added billing_mode validation and default.
- CreateTable now sends the selected AWS billing mode, with nil throughput for on-demand and configured throughput for provisioned.
- Table status returns the existing billing mode. Startup ignores configured auto_scaling on on-demand tables and logs why.
- Updated backend documentation and tests, including tagged test compilation fixes.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./lib/backend/dynamo -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test -tags dynamodb ./lib/backend/dynamo -run 'Test(BillingModeDefaults|CreateTableBillingMode|GetTableStatusBillingMode|InitializeTableBillingMode)$' -count=1` passed.
- `git diff --check` passed.

AWS-dependent integration tests were not executed.
