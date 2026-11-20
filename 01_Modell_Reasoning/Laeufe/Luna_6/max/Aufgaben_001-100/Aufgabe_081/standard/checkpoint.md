# Checkpoint

Issue: normalize `authentication.session.domain` to a host, omit the OIDC state cookie Domain for localhost, and avoid duplicate slashes in the OIDC callback URL.

Implementation:
- `AuthenticationConfig.validate()` now runs `Session.Domain` through `getHostname`, which adds `http://` when no `://` is present, parses with `net/url`, returns `Hostname()`, and propagates parse errors.
- OIDC authorize middleware leaves the state cookie Domain empty for `localhost`; its callback path remains provider specific.
- `callbackURL` removes one trailing slash before adding the callback path.

Validation: `gofmt` and `git diff --check` passed. `go test ./internal/config ./internal/server/auth/method/oidc` passed.
