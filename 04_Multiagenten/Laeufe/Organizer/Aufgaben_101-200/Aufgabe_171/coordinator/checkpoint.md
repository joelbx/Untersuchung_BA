Task: implement gRPC middleware handling for x-flipt-accept-server-version.
Status: complete. Added context helpers and unary interceptor, wired it into the server, and added tests for missing, empty, invalid, prefixed, and unprefixed versions.
Decision: default accepted server version is 1.0.0; parse full semantic versions after optional lowercase v prefix.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/server/middleware/grpc ./internal/cmd passed; git diff --check passed. Restored generated go.work.sum changes.
Delegation: none.
