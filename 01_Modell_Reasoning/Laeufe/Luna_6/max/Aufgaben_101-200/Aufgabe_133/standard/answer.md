Implemented the OSS migration fix.

- [init.go](/app/lib/auth/init.go:510) now downgrades the existing `admin` role, maps users and trusted clusters to `admin`, repairs prior `ossuser` assignments, and skips when the admin migration label is present. The label is written after resource updates succeed, allowing interrupted migrations to retry.
- [role.go](/app/lib/services/role.go:233) adds `NewDowngradedOSSAdminRole` with read only event and session rules and wildcard resource labels.
- [user_command.go](/app/tool/tctl/common/user_command.go:271) assigns legacy users to `admin`.
- Updated migration coverage and the `AdminRoleName` comment.

Verification passed: `go test ./lib/auth -run '^TestMigrateOSS$' -count=1`, `go test ./lib/services`, `go test ./tool/tctl/common`, and `git diff --check`.