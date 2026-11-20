Updated the DynamoDB event backend to write metadata as native `FieldsMap` values and read both `FieldsMap` and legacy JSON `Fields` records.

The background migration converts existing records in batches under a distributed lock. It validates each converted record, logs progress, retries unprocessed writes, and can resume after interruption. Added a conversion test covering nested fields, empty strings, and large integers.

`go test ./lib/events/dynamoevents ./lib/backend` passes. The AWS-dependent integration suite was skipped because `AWSRunTests` is not enabled.