# Checkpoint

Resolved the OSS migration by downgrading the existing `admin` role in place. `NewDowngradedOSSAdminRole` returns the restricted role with the `OSSMigratedV6` label. The migration uses the admin label to skip repeat runs, assigns users to `admin`, updates trusted cluster and CA mappings to `admin`, and converts previously labeled entries that still point to `ossuser`. Legacy `tctl users add` assigns `admin`, and OSS deletion protection targets `admin`.

Verification:
- `go test ./lib/auth ./lib/services ./tool/tctl/common -count=1` passed.
- `go test ./lib/auth -run TestMigrateOSS -count=1` passed after the final test addition.
- `git diff --check` passed.

Initial test failures were resolved: the migration fixture lacked the preexisting admin role, and one new assertion used nonexistent `types.RO` instead of `services.RO`.
