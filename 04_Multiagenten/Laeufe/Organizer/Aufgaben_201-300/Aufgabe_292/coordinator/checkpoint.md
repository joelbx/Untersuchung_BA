Task: polling lifecycle management in storage backends.
Status: complete. Poller cancellation and join, backend and wrapper Close, request context propagation, server shutdown hook. Verified go test ./internal/storage/fs/... ./internal/cmd and git diff --check.
