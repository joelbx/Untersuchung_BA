# Checkpoint

Implemented poller-owned cancellation and synchronous `Close()` waiting for active polling. Git, local, Azure Blob, S3 and OCI snapshot stores now retain their poller and expose `Close()`. The wrapping filesystem store forwards `Close()` when supported. Added poller lifecycle tests.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/storage/fs/...` passed after correcting duplicate struct fields introduced during editing. `GOTOOLCHAIN=local GOPROXY=off go test ./internal/storage/fs -run 'TestPoller' -count=1` passed. `git diff --check` passed. The first full test run failed to compile due to those duplicate fields; they were removed and the rerun passed. `rg` was unavailable, so local `find` and `grep` were used.
