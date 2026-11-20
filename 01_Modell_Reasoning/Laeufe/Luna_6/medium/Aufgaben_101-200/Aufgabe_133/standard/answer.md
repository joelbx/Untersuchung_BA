The OSS migration now downgrades the existing `admin` role, marks it with `OSSMigratedV6`, and keeps migrated users and trusted cluster mappings on `admin`. Legacy user creation also assigns `admin`. Added `services.NewDowngradedOSSAdminRole` with restricted event and session permissions.

Verification passed: `go test ./lib/auth ./lib/services ./tool/tctl/common` and `git diff --check`.