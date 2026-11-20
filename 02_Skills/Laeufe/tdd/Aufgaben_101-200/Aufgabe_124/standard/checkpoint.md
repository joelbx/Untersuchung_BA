# Checkpoint

Task: add DynamoDB `billing_mode` with an on-demand default, table creation behavior, and auto-scaling handling.

Status: implementation, unit tests, integration fixture update, and docs complete.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./lib/backend/dynamo -count=1` passed.
- `git diff --check` passed.
- Before implementation, `GOPROXY=off GOSUMDB=off go test ./lib/backend/dynamo -run '^TestCreateTableUsesOnDemandByDefault$' -count=1` failed as expected: the CreateTable request had a nil BillingMode.
- `GOPROXY=off GOSUMDB=off timeout 120s go test ./...` did not complete (exit 143 after timeout). Compilation failed in unrelated dependencies because `linux/hidraw.h` and `gnu/libc-version.h` were missing; `github.com/mattn/go-sqlite3` also failed with `pread64`, `pwrite64`, and `off64_t` undeclared. The remaining repository-wide test result is unknown.

DynamoDB-tagged integration tests require an external AWS service and were not run. No dependencies were downloaded.
