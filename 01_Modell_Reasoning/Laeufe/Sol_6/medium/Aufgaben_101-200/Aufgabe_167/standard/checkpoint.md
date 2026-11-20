# Checkpoint

Task: add OCI snapshot source, context-aware SnapshotSource.Get, and update callers.
Status: implemented and verified.
Changes: OCI source with digest caching and configurable polling; local OCI store reopened lazily for each fetch; gzip layer support, namespace annotations, and optional manifest creation time; context-aware sources and callers. Added local refresh/subscription and gzip tests.
Verification: `go test ./internal/oci ./internal/storage/fs/...` passed; `git diff --check` passed.
Constraints: local code and existing tests only; git history, index baseline, and harness configuration untouched.
