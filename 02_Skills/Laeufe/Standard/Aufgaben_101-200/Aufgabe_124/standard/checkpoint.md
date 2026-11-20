# DynamoDB billing mode issue

Implemented `billing_mode` for the DynamoDB backend, defaulting new tables to `pay_per_request`. Table creation passes the selected AWS billing mode and omits provisioned throughput for on-demand tables. Initialization suppresses auto scaling when the existing or new table is on-demand. Table status now returns billing mode. Updated configuration documentation and focused unit tests.

Checks:
- `go test ./lib/backend/dynamo` passed.
- `go test -tags dynamodb ./lib/backend/dynamo -run 'TestBillingModeDefaults|TestCreateTableBillingMode|TestGetTableStatusBillingMode|TestDisableAutoScaling'` passed after fixing existing tagged test compile errors.
- `git diff --check` passed.
- `go test ./lib/backend/...` failed during C compilation of `github.com/mattn/go-sqlite3`: `pread64` and `pwrite64` undeclared, `off64_t` unknown. Stopped the suite after this environment failure. Other backend packages were therefore not fully verified.

AWS integration tests requiring a live DynamoDB service were not run. No credentials or external services were accessed.
