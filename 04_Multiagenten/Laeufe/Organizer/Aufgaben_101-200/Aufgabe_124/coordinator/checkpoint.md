Task: DynamoDB backend billing_mode support.
Status: complete. Added validated pay_per_request default, explicit AWS BillingMode on creation, nil throughput for on-demand, actual table billing mode from status, and startup autoscaling guards with logs. Updated documentation and focused unit tests.
Verification: go test ./lib/backend/dynamo -count=1 passed; git diff --check passed. Existing AWS integration suite skips without TELEPORT_DYNAMODB_TEST.
Delegation: none.
