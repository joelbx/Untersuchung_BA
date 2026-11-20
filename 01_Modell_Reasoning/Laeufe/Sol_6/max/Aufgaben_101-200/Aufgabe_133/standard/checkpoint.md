# OSS admin migration checkpoint

- Started investigation in `/app` on 2026-10-18.
- Goal: keep migrated OSS users on `admin`, downgrade that role in place, and preserve trusted cluster role mapping.
- Changed the OSS migration to fetch `admin`, check its migration label, migrate users and trusted-cluster mappings to `admin`, then replace that role with `NewDowngradedOSSAdminRole`.
- The migration repairs users and mappings that were already labeled by the earlier `ossuser` migration, preserving additional roles and mappings.
- Legacy `tctl users add` now assigns `admin`; OSS role deletion protection targets `admin`.
- Tests passed: `go test ./lib/auth -run '^TestMigrateOSS$' -count=1`, `go test ./lib/services -run '^TestRole' -count=1`, and `go test ./tool/tctl/common -count=1`.
- Final review: check formatting, diff, and repository status.
