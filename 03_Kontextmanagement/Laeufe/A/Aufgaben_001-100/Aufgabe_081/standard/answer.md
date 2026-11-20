Fixed the OIDC login issue in `/app`. Authentication validation now normalizes the session domain to a hostname, the state and token cookies omit `Domain` for localhost, and callback URL construction removes one trailing slash from the host. Added regression tests for these cases.

The existing tests for `internal/config` and `internal/server/auth/method/oidc` pass.