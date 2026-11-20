Completed DynamoDB billing_mode support: pay_per_request default; provisioned throughput when selected; existing on-demand tables suppress auto scaling; status returns billing mode.
Updated documentation and DynamoDB tagged integration test compatibility.
Verified: go test ./lib/backend/dynamo; focused go test -tags dynamodb ./lib/backend/dynamo; git diff --check.
