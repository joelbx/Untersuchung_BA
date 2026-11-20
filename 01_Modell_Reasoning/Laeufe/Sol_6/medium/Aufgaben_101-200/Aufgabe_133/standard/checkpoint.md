# Checkpoint

Completed OSS v6 migration fix: downgrade the existing admin role in place, mark it migrated, retain admin assignments and trusted-cluster mappings, and use admin for legacy user creation. The migrated admin role retains limited event/session read permissions. Updated migration tests for role replacement, mappings, users, and repeat-run behavior.

Verification: `go test ./lib/auth -run '^TestMigrateOSS$' -count=1` passed; `go test ./lib/services ./tool/tctl/common -run '^$'` passed; `git diff --check` passed.
