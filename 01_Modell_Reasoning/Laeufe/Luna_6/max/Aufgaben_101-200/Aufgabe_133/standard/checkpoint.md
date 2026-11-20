# Checkpoint

## Objective
Fix the Teleport 6.0 OSS role migration so it downgrades the existing `admin` role in place, preserves admin role mapping for leaf clusters, skips already migrated roles, and assigns legacy users to `admin`.

## Progress
- Repository: `/app`.
- Initial `rg` searches could not run because `rg` is unavailable in this environment; switching to `find`/`grep`.
- Added `services.NewDowngradedOSSAdminRole`, preserving the `admin` name and restricting explicit rules to read-only events and sessions.
- Updated OSS migration to downgrade the existing admin role, skip when its migration label is present, and map users/trusted clusters to `admin`. The marker is written after the resource updates succeed so an interrupted migration can retry.
- Updated legacy `tctl users add` role assignment to `admin`.
- Updated the `AdminRoleName` comment to reflect OSS legacy user assignment.
- Updated the existing OSS migration coverage to verify upgraded role mappings and repair prior `ossuser` assignments.
- Verification passed: `go test ./lib/auth -run '^TestMigrateOSS$' -count=1`, `go test ./lib/services`, `go test ./tool/tctl/common`, and `git diff --check`.

## Next steps
1. Implementation and review are complete; report the changes and verification.
