Task: Add audit support for token creation and deletion.
Status: Implemented token resource mapping, event-specific deletion enablement, and successful-deletion audit emission.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/server/audit ./internal/server/auth ./internal/server/middleware/grpc ./internal/cmd (passed).
