# Checkpoint

Task: add DynamoDB billing_mode configuration and on-demand table creation behavior.
Status: complete.
Implemented: default pay_per_request and validation; explicit AWS billing mode and conditional throughput; status returns billing mode; startup suppresses auto scaling for on-demand tables and logs why; provisioned chart auto scaling; docs and focused tests.
Verification: GOPROXY=off GOSUMDB=off go test ./lib/backend/dynamo passed; focused tagged DynamoDB tests passed; git diff --check passed.
