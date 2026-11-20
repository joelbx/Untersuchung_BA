# Checkpoint

Task: add DynamoDB billing_mode configuration and on-demand table handling.
Status: implemented and verified.
Verification: go test ./lib/backend/dynamo; go test -tags dynamodb ./lib/backend/dynamo -run billing unit tests; git diff --check.
