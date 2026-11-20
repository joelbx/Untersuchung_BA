Implemented the authentication database dependency checks.

- Added explicit `RequiresDatabase` values for all authentication methods: JWT is `false`; token, OIDC, GitHub, and Kubernetes are `true`.
- Added `AuthenticationConfig.RequiresDatabase()` and used it to select the non database startup path.
- Cleanup scheduling and `AuthenticationService.Run` now skip methods that do not require a database.

**Verification:** `go test ./internal/config` passed. `internal/cleanup` failed because its existing test expects JWT cleanup to delete records, which conflicts with the new requirement to skip JWT cleanup. The `internal/cmd` test run was interrupted during compilation. `git diff --check` passed.