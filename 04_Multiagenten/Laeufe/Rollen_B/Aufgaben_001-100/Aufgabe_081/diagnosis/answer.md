The failure has three direct causes:

- [AuthenticationConfig.validate](/app/internal/config/authentication.go:84) checks only whether `Session.Domain` is empty. It does not call `getHostname` or replace a scheme and port with the parsed host.
- [Middleware.Handler](/app/internal/server/auth/method/oidc/http.go:125) sets the state cookie’s `Domain` directly from config, including when it is `localhost`. Its provider-specific callback `Path` is already correct.
- [callbackURL](/app/internal/server/auth/method/oidc/server.go:160) appends the path without removing a trailing slash from the host.

The fix should cover scheme and port normalization with parse errors propagated, a state cookie with no `Domain` attribute for localhost, and callback URLs with one separator while preserving the scheme and port. [ForwardResponseOption](/app/internal/server/auth/method/oidc/http.go:59) also sets `Domain` on the token cookie; whether the localhost rule should apply there is unresolved by the stated `Handler` requirement.

The existing [OIDC integration test](/app/internal/server/auth/method/oidc/server_test.go:27) uses localhost without a trailing slash and does not assert cookie domain attributes or normalization. I did not run tests or edit source or tests: the assigned fault-localization role prohibits those edits. I recorded the findings in the required checkpoint.