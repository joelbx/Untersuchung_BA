Task: Fix OIDC session domain normalization, localhost cookie handling, and callback URL slash handling.
Status: Complete. Focused regression tests added; relevant package tests passed.
Changes: AuthenticationConfig.validate normalizes Session.Domain via getHostname; OIDC state and token cookies omit Domain for localhost; callbackURL removes one trailing slash.
Verification: go test ./internal/config ./internal/server/auth/method/oidc (passed); git diff --check (passed).
Constraints: Local repository and existing tests only; git history, index baseline, and harness configuration untouched.
