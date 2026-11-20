# Checkpoint

Task: validate required GitHub and OIDC authentication fields at startup, preserve GitHub organization scope validation, and run relevant existing tests.
Status: complete.
Changes: shared required-field validation in internal/config/authentication.go; provider-qualified GitHub scope error; existing scope fixture has valid credentials; startup integration tests cover GitHub/OIDC missing and whitespace fields, exact OIDC provider name, accepted read:org scope, and disabled methods.
Verification: go test ./internal/config ./internal/server/auth/method/github ./internal/server/auth/method/oidc -count=1 (passed); git diff --check (passed).
