# Checkpoint

Task: manage polling lifecycle across Git, local, S3, Azure Blob, and OCI snapshot stores.

Implemented: Poller owns a cancellable context, update callback, and completion signal. Close cancels and joins polling, including an active update. Stores retain and close their pollers; stores without polling return nil. The declarative Store wrapper forwards Close. Git polling fetch uses FetchContext. Added poller lifecycle tests and local store cleanup.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/storage/fs/... && git diff --check` exited 0. Package results: fs, git, local, azblob, blob, s3, and oci passed; fs/store has no test files. External service dependent cases may skip when their test environment variables are unset.
