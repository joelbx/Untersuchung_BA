Implemented configurable DynamoDB billing modes. `billing_mode` accepts `pay_per_request` and `provisioned`, and defaults to `pay_per_request`. Table creation sends the matching AWS billing mode, with provisioned throughput omitted for on-demand tables. Initialization also detects on-demand tables, disables autoscaling, and logs why. See [dynamodbbk.go](/app/lib/backend/dynamo/dynamodbbk.go:61).

Updated the backend documentation and made the provisioned autoscaling test explicitly select `provisioned` in [configure_test.go](/app/lib/backend/dynamo/configure_test.go:58).

Verification: `go test ./lib/backend/dynamo` passed, the DynamoDB tagged tests compiled with `-run '^$'`, and `git diff --check` passed. The tagged tests were not run against AWS.