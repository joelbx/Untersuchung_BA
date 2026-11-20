Task: Make OCI bundle manifest version configurable as 1.0 or 1.1, default 1.1.
Status: Complete. Added configuration schema field, default and validation, store option and wiring, and focused tests for loading and generated manifests.
Verification: go test ./internal/config ./internal/oci ./internal/storage/fs/store; go test ./internal/storage/fs/oci; git diff --check. All passed.
Constraints: Local repository only; git history, index, and harness configuration untouched.
