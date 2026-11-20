# Checkpoint

Task: implement client accepted server version handling for gRPC at `/app`.

Completed:
- Added context setter/getter for `semver.Version`, with `0.0.0` as the safe default.
- Added a unary interceptor that reads `x-flipt-accept-server-version`, accepts strict semantic versions with or without a lowercase `v`, and uses the default when metadata is absent or parsing fails.
- Registered the interceptor in the main gRPC server chain.
- Kept generated dependency checksum changes from inspection out of the working tree.

Verification:
- `gofmt` and `git diff --check` passed.
- Attempted `GOWORK=off go test -mod=readonly ./internal/server/middleware/grpc ./internal/cmd`; both packages could not compile because required Go modules are absent from the local cache and module lookup is disabled. No dependency downloads were performed.
