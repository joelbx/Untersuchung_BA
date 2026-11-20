# Checkpoint

Task: Fix OSS v6 migration to downgrade the existing `admin` role, preserve `admin` role mappings/assignments, and use `admin` in legacy user creation.

Implemented:
- Added `services.NewDowngradedOSSAdminRole`, based on the restricted OSS permissions, named `admin`, and labeled `OSSMigratedV6`.
- Migration now loads `admin`, exits with a debug log when already labeled, otherwise upserts the downgraded role and assigns existing users and trusted cluster mappings to `admin`.
- Legacy `tctl users add` with no roles now assigns `admin`.
- Updated migration test fixtures and expectations.

Verification:
- `go test -p 1 ./lib/auth -run '^TestMigrateOSS$' -count=1` passed.
- `go test -p 1 ./lib/services -run '^(TestRoleParse|TestValidateRole)$' -count=1` passed.
- `go test -p 1 ./tool/tctl/common -count=1` passed.
- Initial parallel test invocation hit the container process limit; rerunning serially succeeded.
