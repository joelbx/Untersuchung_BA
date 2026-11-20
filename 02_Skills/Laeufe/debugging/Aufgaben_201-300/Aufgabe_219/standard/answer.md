Added `token` to the audit event checker and its wildcard mapping. gRPC initialization now uses the configured event list to enable token deletion audit logging in the authentication server.

The new token event regression test failed before the fix and passes now. Tests for `internal/server/audit`, `internal/server/auth`, and `internal/cmd` pass.