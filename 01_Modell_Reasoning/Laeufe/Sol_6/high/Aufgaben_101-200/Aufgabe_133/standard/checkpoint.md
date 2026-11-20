# Checkpoint

Implemented OSS V6 migration using the existing `admin` role. `NewDowngradedOSSAdminRole` returns a restricted, labeled admin role; migration upserts it unless already labeled, assigns users and trusted cluster mappings to admin, and handles records previously migrated to `ossuser`. Legacy user creation also assigns admin. The OSS system-role deletion guard now protects admin.

Verification passed:
- `go test ./lib/auth -run '^TestMigrateOSS$' -count=1`
- `go test ./lib/services -run '^(TestRoleParse|TestCheckAccessToRemoteCluster)$' -count=1`
- `go test ./tool/tctl/common -run '^$'`
- `git diff --check`
