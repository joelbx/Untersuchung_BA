Implemented the OIDC fixes:

- Session domains are normalized to hostnames during config validation, with URL parsing errors returned to the caller.
- State and token cookies omit the `Domain` attribute for `localhost`; the state cookie keeps its callback path.
- Callback URL construction removes one trailing slash from the host.

Verification passed: `go test ./internal/config` and `go test ./internal/server/auth/method/oidc`.