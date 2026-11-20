Updated the DynamoDB backend to accept `billing_mode`, defaulting to `pay_per_request`. New on-demand tables are created without provisioned throughput, and auto scaling is ignored for on-demand tables. Provisioned tables retain configured throughput and auto scaling support.

Added configuration tests. `go test ./lib/backend/dynamo` and `git diff --check` pass.