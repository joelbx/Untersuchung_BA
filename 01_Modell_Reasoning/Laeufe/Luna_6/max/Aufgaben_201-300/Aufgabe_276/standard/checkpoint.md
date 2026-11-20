# Checkpoint

Task: Require complete GitHub and OIDC authentication fields at startup, and validate GitHub's `read:org` scope when organizations are restricted.

Progress:
- Located startup validation in `internal/config.Config.Load` and provider validation hooks in `internal/config/authentication.go`.
- Added required GitHub and OIDC provider field checks, provider-qualified errors, and provider validation before session checks.
- Updated the existing GitHub scope fixture and expected error format.
- `go test ./internal/config` passed.
