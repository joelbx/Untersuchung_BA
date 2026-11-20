Implemented the version handling in [middleware.go](/app/internal/server/middleware/grpc/middleware.go) and registered the interceptor in the main gRPC chain in [grpc.go](/app/internal/cmd/grpc.go).

The interceptor stores a parsed client version in context, accepts versions with or without a lowercase `v`, and defaults to `0.0.0` when metadata is absent or invalid. The context getter also returns that default when no version is stored.

`gofmt` and `git diff --check` passed. The existing package tests could not compile because required modules are missing from the local cache and module lookup is disabled. I recorded the checkpoint at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).