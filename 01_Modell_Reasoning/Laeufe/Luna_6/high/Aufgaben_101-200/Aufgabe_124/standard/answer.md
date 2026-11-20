Implemented DynamoDB billing mode support. `billing_mode` accepts `pay_per_request` and `provisioned`, defaults to `pay_per_request`, and maps to the corresponding AWS billing mode. On-demand table creation omits provisioned throughput; provisioned creation uses the configured capacity units.

Initialization now reads the table’s billing mode and skips configured autoscaling for on-demand tables with a log message. Added focused tests and documented the setting.

**Validation:** `go test ./lib/backend/dynamo` and `git diff --check` passed.

Updated [dynamoddbk.go](/app/lib/backend/dynamo/dynamodbbk.go), [dynamodbbk_test.go](/app/lib/backend/dynamo/dynamodbbk_test.go), and the DynamoDB configuration docs. Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).