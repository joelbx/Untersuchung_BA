# Checkpoint

Task: manage polling goroutine lifecycles across filesystem storage backends.
Status: complete. Poller owns its context, cancellation, and termination signal. Git, local, OCI, S3, and Azure Blob stores retain pollers and expose idempotent Close. The outer fs.Store forwards Close when supported. Added Poller lifecycle tests.
Verification: `go test ./internal/storage/fs/...` passed; `git diff --check` passed.
