Implemented DynamoDB billing mode support in [dynamodbbk.go](/app/lib/backend/dynamo/dynamodbbk.go). `billing_mode` accepts `pay_per_request` or `provisioned` and defaults to `pay_per_request`. Table creation now sends the selected AWS billing mode and includes provisioned throughput only for provisioned tables. Initialization disables and logs autoscaling when the table is on-demand, whether it already exists or is about to be created. Table status now returns the billing mode alongside the status.

Added coverage for default and valid/invalid billing modes in [dynamodbbk_test.go](/app/lib/backend/dynamo/dynamodbbk_test.go).

Verification: `go test ./lib/backend/dynamo` passed; `git diff --check` passed.