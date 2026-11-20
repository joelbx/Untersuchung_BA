Task: Add OCI SnapshotSource support and context-aware Get operations.
Status: Implemented and verified.
Changes: Added internal/storage/fs/oci source with digest caching and polling; OCI local layouts are reopened per fetch; OCI layers support namespace annotations, gzip, features media type, and creation timestamps. Updated SnapshotSource implementations and callers for context-aware Get. Added local OCI refresh/subscription test.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/oci ./internal/storage/fs/... passed; git diff --check passed.
