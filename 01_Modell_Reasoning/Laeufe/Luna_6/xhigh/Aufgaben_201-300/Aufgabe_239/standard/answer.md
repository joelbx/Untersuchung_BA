Implemented explicit user scoping for all `UserPropsRepository` operations and updated the SQL and mock repositories to use the supplied user ID.

LastFM session reads and writes now use the agent’s user ID. The auth router scopes status and unlink operations to the authenticated user; its callback uses expiring signed state issued to that user. The UI now requests that state before opening LastFM authorization.

Verification passed: `go test ./...`, ESLint on the changed UI files, and `git diff --check`.