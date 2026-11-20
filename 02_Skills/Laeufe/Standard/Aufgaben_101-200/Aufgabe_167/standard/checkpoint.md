# Checkpoint

Task: add OCI snapshot source and context-aware SnapshotSource.Get.
Status: implemented and verified.
Changes: new OCI source with digest-aware Get and polling Subscribe; local OCI stores reopened on every Fetch; layer annotations supplied to snapshot parsing; all SnapshotSource implementations and callers updated for context.
Verification: `GOPROXY=off go test ./internal/oci ./internal/storage/fs/...` passed. `git diff --check` passed.
Constraints observed: no downloads, git history/index changes, or harness changes.
