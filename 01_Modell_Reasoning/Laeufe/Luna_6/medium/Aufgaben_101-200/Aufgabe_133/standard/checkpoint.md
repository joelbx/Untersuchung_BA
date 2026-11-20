# Checkpoint

Implemented the OSS v6 migration using the existing `admin` role. Added `services.NewDowngradedOSSAdminRole`, which retains broad resource labels and read-only event/session rules, names the role `admin`, and labels it `migrate-v6.0`. Migration skips an already-labeled admin with a debug log, assigns migrated users to admin, and maps trusted clusters to admin. Legacy user creation now also assigns admin.

Updated migration tests to seed the existing admin role and assert the migrated role and mappings. Initial focused test run exposed that the auth test fixtures lacked an admin role; fixtures were corrected. Rerunning `go test ./lib/auth ./lib/services ./tool/tctl/common`.
