# Checkpoint

Task: Normalize authentication session domain, fix OIDC cookie domains and callback URL.
Status: Completed.
Changes: AuthenticationConfig.validate normalizes Session.Domain via getHostname; OIDC state and token cookies omit Domain for localhost; callbackURL removes one trailing slash.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/server/auth/method/oidc (passed).
