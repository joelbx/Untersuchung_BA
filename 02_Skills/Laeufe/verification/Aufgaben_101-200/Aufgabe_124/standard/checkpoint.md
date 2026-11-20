# Checkpoint

Task: add DynamoDB backend `billing_mode` support, defaulting new tables to `pay_per_request`.

Implemented:
- Validate `billing_mode` (`pay_per_request` or `provisioned`) and default to on-demand.
- Set AWS BillingMode and omit throughput for on-demand creation; retain configured throughput for provisioned creation.
- Read existing table billing mode; disable configured auto scaling and log when the table is or will be on-demand.
- Document the option and add local unit tests for defaults, creation requests, status, and scaling decisions.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/backend/dynamo` passed (`ok`, 0.021s) after the final edit. `git diff --check` passed. Initial test run failed due to a typo in the new test import; corrected. `rg` is unavailable (`/bin/sh: rg: not found`), so local `find` and `grep` were used.
