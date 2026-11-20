Implemented the OSS migration changes.

- Added `NewDowngradedOSSAdminRole`, which keeps the `admin` name, marks it with `OSSMigratedV6`, and grants the restricted OSS permissions.
- Updated migration to fetch and downgrade the existing `admin` role, skip with a debug message if it is already marked, and keep user and trusted-cluster mappings on `admin`.
- Updated legacy user creation to assign `admin`.
- Updated migration tests to seed the pre-migration admin role.

Verification: `go test ./lib/auth ./lib/services ./tool/tctl/common` passed, and `git diff --check` passed.