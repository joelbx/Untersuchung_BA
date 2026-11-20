# Checkpoint

Implemented DynamoDB billing mode configuration in `lib/backend/dynamo`:
- `billing_mode` accepts `pay_per_request` and `provisioned`, defaulting to `pay_per_request`.
- Creation sends the selected AWS billing mode and only includes provisioned throughput for provisioned tables.
- Initialization suppresses configured autoscaling for on-demand tables and logs why.
- Table status lookup now returns the discovered billing mode.
- Updated the backend README with the capacity mode configuration.

Verification:
- `go test ./lib/backend/dynamo` passed.
- `go test -tags dynamodb -run '^$' ./lib/backend/dynamo` could not compile existing tagged tests: `configure_test.go` has incompatible `uuid.New()` concatenation and passes a `DynamoDBAPI` interface where `*dynamodb.DynamoDB` is required. No tagged tests were run.
- `git diff --check` passed.
