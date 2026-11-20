# Checkpoint

Issue resolved in checked-out files: authentication session domains are parsed to hostnames; localhost cookies omit Domain; callback URLs trim one trailing host slash. Added focused config and OIDC tests.
Verification: `GOPROXY=off go test ./internal/config ./internal/server/auth/method/oidc` passed; `git diff --check` passed.
Delegation: none.
