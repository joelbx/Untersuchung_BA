# Checkpoint

Task: Resolve OSS user migration compatibility with leaf clusters by preserving the `admin` role name and assigning legacy users to `admin`.

Changes made:
- Added `services.NewDowngradedOSSAdminRole`, built from the restricted OSS permissions, named `admin`, and labeled with `OSSMigratedV6`.
- Updated `migrateOSS` to fetch the existing admin role, skip with a debug message when already marked, migrate users/trusted clusters/GitHub connectors to admin, then persist the downgraded role.
- Updated migration tests for the existing admin role, admin user assignment, trusted cluster mapping, and reduced permissions.
- Updated legacy `tctl users add` to assign `admin`.

Validation passed:
- `go test ./lib/auth -run '^TestMigrateOSS$' -count=1`
- `go test ./lib/services -run 'Test.*Role' -count=1`
- `go test ./tool/tctl/common -count=1`
- `git diff --check`

The initial broader package run exposed test fixtures without a preexisting admin role; fixtures were corrected because migration now explicitly requires retrieving the existing role.
