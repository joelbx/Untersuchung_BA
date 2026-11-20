# Checkpoint

Issue: Add gRPC handling for the `x-flipt-accept-server-version` request metadata.

Completed:
- Added context setter/getter and a unary interceptor that parses strict semantic versions with an optional lowercase `v` prefix.
- Uses `0.0.0` as the fallback when metadata is absent or invalid, and logs invalid values when a logger is available.
- Wired the interceptor into the server's base unary interceptor chain.

Verification:
- `GOPROXY=off go test ./internal/server/middleware/grpc` passed.
- `GOPROXY=off go test ./internal/cmd` passed.
- `git diff --check` passed.
