# OSS admin migration checkpoint

Investigating the Teleport 6.0 OSS migration, downgraded role construction, and legacy user creation. Goal: retain the `admin` role name for migrated users and trusted cluster mappings while limiting permissions.

Implemented the downgraded admin role with `OSSMigratedV6` metadata, migrated users and trusted cluster mappings to `admin`, and changed legacy user creation. Focused role permission test passes. Auth migration tests are being rerun with an existing admin role in the test fixture, matching normal server initialization.

Verification complete: `go test ./lib/services -run '^TestNewDowngradedOSSAdminRole$' -count=1`, `go test ./lib/auth -run '^TestMigrateOSS$' -count=1`, and `go test ./tool/tctl/common -run '^Test.*User' -count=1` passed. `git diff --check` passed.
