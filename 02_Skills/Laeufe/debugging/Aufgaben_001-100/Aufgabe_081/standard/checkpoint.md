# OIDC login issue checkpoint

Status: Fixed and verified locally.

Root cause: `AuthenticationConfig.validate` only rejects an empty session domain; `Middleware.Handler` copies the configured domain into the state cookie; `callbackURL` concatenates the host and path without trimming a trailing slash. Existing OIDC integration config uses `localhost`, while the callback address has no trailing slash.

Hypothesis: Normalizing the configured domain in validation, omitting `Domain` for localhost in the state cookie, and trimming one slash in `callbackURL` will correct the three reproduced outputs.

Reproduction: Added focused tests for session domain normalization and parse errors, state and token cookie domains, callback cookie path, and callback URL slash handling. Before changes, the tests failed on the reported domain and callback cases; the token cookie also failed with `Domain=localhost`.

Changes: `validate` calls `getHostname` for session compatible authentication and stores the parsed hostname. OIDC state and token cookies omit Domain for localhost. `callbackURL` trims one trailing slash before appending its path.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/server/auth/method/oidc -count=1` passed. `git diff --check` passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and repository files.
