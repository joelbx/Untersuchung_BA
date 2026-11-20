Task: Validate required GitHub and OIDC authentication fields at startup, preserve GitHub read:org scope requirement, and emit provider-specific errors.
Status: Implemented in internal/config/authentication.go. Validation checks non-blank client_id, client_secret, and redirect_address for enabled GitHub and each enabled OIDC provider; GitHub scope error uses required provider/field format. Method validation runs before session-domain validation so incomplete provider configurations report their own fields.
Tests: GOPROXY=off GOSUMDB=off go test ./internal/config passed. git diff --check passed.
Delegation: none; solved directly.
