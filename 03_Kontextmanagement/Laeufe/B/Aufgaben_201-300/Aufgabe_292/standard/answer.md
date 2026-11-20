Implemented polling lifecycle management across Git, local, Azure Blob, S3, and OCI snapshot stores. Each store now exposes `Close()`, which safely handles an inactive poller; the shared poller cancels and waits for active polling to stop.

Validation passed: `GOPROXY=off GOSUMDB=off go test ./internal/storage/fs/...`.