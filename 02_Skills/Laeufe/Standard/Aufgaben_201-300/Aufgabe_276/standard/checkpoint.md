# Checkpoint

Task: validate required GitHub and OIDC authentication fields during configuration loading, preserving GitHub organization scope validation and provider-specific error messages.

Status: complete. `rg` is unavailable (`/bin/bash: rg: command not found`); used local grep/find instead.

Changes: added shared required OAuth credential validation for enabled GitHub and OIDC methods, with provider-specific errors. Updated GitHub organization scope error and its fixture. Added load-level tests for missing and whitespace-only required fields.

Checks: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/config` passed. `git diff --check` passed.
