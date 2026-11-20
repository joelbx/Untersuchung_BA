# Checkpoint

Task: Add DynamoDB backend `billing_mode` support with `pay_per_request` default, provisioned option, and auto scaling behavior based on actual table mode.

Root cause: `createTable` always sent `ProvisionedThroughput` and omitted `BillingMode`. `getTableStatus` returned schema status only, so initialization could not distinguish an existing on-demand table before calling `SetAutoScaling`.

Implemented: configuration validation/default; explicit AWS billing mode and conditional throughput; status plus billing mode; auto scaling suppression and log for existing or newly created on-demand tables; documentation; unit tests and provisioned integration test configuration.

Verification:
- Before fix, `go test ./lib/backend/dynamo -run '^TestDefaultBillingModeCreateTable$' -count=1` failed as expected: billing mode was empty instead of PAY_PER_REQUEST.
- After fix, `go test ./lib/backend/dynamo -count=1` passed.
- `git diff --check` passed.
- `go test ./lib/backend/... -count=1` exited 1 because `lib/backend/lite` could not compile its existing `github.com/mattn/go-sqlite3` C dependency: `pread64` and `pwrite64` undeclared, and `off64_t` unknown. DynamoDB and other reported backend packages passed; the broader suite remains unverified because of this local C build issue.
- The tagged DynamoDB integration test requires external AWS/DynamoDB and was not run in this offline environment.

Tooling: `rg` is unavailable (`/bin/sh: rg: not found`); used local `grep`/`find`.
