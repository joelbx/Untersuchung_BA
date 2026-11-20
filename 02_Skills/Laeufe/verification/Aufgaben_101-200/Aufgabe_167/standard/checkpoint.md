# Checkpoint

Task: Add OCI snapshot source and context-aware SnapshotSource.Get.
Status: implemented in checked-out files.

Changes:
- Added OCI Source with digest-cached Get, 30-second default polling, cancellation-aware Subscribe, and configurable interval.
- Reopen local OCI layout on every Fetch; fetch files from the active target; support gzip layers, namespace annotations, and both feature media types.
- Updated SnapshotSource.Get and all repository implementations and callers to take context.
- Added tests for external local-tag updates, unchanged digest reuse, subscription updates/cancellation, and gzip layer decoding.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/oci ./internal/storage/fs/... -count=1` exited 0; all six reported packages passed. `git diff --check` exited 0. `rg` was unavailable (`/bin/bash: rg: command not found`); used grep/find for searches.
