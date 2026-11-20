Implemented the OIDC fixes:

- Session domains are normalized to hostnames during authentication config validation, with URL parsing errors propagated.
- State cookies omit the `Domain` attribute when the configured domain is `localhost`.
- Callback URL construction removes one trailing slash from the host while preserving its scheme and port.

Verified with `go test ./internal/config ./internal/server/auth/method/oidc`; both packages passed.