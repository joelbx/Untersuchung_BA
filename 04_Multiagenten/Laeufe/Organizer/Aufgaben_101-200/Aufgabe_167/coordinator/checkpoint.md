# Checkpoint

Task: Add OCI backed fs SnapshotSource and context aware Get calls.
Status: Complete. OCI source caches by digest, polls for changes, and uses local layout reopening on each fetch. Namespace annotation and gzip layers are handled. Relevant package tests pass.
Verification: go test ./internal/oci ./internal/storage/fs/...
Constraints: local code/tests only; git history, index, and harness preserved.
