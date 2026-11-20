Task: Add DynamoDB backend billing_mode support with pay_per_request default.
Status: Complete. Config validates pay_per_request/provisioned and defaults to pay_per_request. Table creation sends the matching AWS billing mode and omits throughput for on-demand. Initialization suppresses auto scaling for existing or newly created on-demand tables and logs why. Table status returns status and billing mode. Documentation and tests updated.
Verification: go test ./lib/backend/dynamo (pass); git diff --check (pass). AWS-backed tests require external credentials and were not run.
