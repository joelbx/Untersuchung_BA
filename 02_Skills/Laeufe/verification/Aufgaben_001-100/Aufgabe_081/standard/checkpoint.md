# Checkpoint

Task: normalize authentication session domains, correct OIDC state cookie domain handling, and avoid a doubled slash in callback URLs.

Status: implementation and focused tests added. `rg` is unavailable (`/bin/bash: rg: command not found`); used local fallback search.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/server/auth/method/oidc` passed (both packages).
- `git diff --check` passed.
