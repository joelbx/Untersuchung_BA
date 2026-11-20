Task: Handle x-flipt-accept-server-version in gRPC middleware.
Completed: Added context setter/getter, metadata parsing with v-prefixed and unprefixed semantic versions, 1.0.0 fallback, production interceptor registration, and focused tests.
Verification: gofmt, git diff --check, and GOPROXY=off GOSUMDB=off go test ./internal/server/middleware/grpc ./internal/cmd passed. Restored incidental go.work.sum changes from the test run.
