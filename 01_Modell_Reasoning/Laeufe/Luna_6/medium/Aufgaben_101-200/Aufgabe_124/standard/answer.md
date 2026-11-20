Implemented DynamoDB billing mode support in [dynamodbbk.go](/app/lib/backend/dynamo/dynamodbbk.go).

`billing_mode` defaults to `pay_per_request` and accepts `pay_per_request` or `provisioned`. Table creation sets `BillingMode` accordingly and includes provisioned throughput only for provisioned mode. Initialization disables and logs autoscaling for on-demand tables, whether existing or newly created. Table status checks now also return the billing mode.

Validation passed: `go test ./lib/backend/dynamo` and `git diff --check`.