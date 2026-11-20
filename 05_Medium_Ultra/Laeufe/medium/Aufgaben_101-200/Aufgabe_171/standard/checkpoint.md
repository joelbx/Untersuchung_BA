Task complete: gRPC client accepted server version handling.
Implemented context setter/getter, v1.0.0 fallback, metadata parsing for prefixed and plain semantic versions, and server interceptor registration. Added focused tests.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/server/middleware/grpc ./internal/cmd passed; gofmt and git diff --check passed. Incidental go.work.sum change removed.
