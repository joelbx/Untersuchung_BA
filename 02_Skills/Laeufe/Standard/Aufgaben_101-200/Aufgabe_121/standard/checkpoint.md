# Checkpoint

Investigating the authorization engine, protocol enum, and existing tests. `rg` is unavailable, so repository searches use `find` and `grep`.

Added global `flipt.is_auth_method` registration, enum-backed method mapping, and direct/registration tests. `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/engine/...` is running; it is compiling dependencies from the local module cache.

Completed implementation and verification. The final `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/engine/...` passed, as did `git diff --check`. Tests cover all seven labels, the Kubernetes alias, mismatches, unsupported values, missing authentication, and policy evaluation with role scoping.
