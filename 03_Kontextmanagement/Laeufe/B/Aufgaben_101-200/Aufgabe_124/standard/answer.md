Implemented DynamoDB `billing_mode` support. New tables default to `pay_per_request`; `provisioned` uses configured capacity units. Autoscaling is disabled with a log message for on-demand tables. The backend reference and focused tests are updated.

`go test ./lib/backend/dynamo -count=1` and `git diff --check` passed. AWS integration tests require a configured DynamoDB test environment.