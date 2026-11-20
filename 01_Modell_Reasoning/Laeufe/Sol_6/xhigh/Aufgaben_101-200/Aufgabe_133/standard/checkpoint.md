# Checkpoint

Task: preserve OSS trusted-cluster access during Teleport 6 migration by downgrading the existing admin role and keeping users assigned to admin.

Completed: added NewDowngradedOSSAdminRole with read-only events and sessions, wildcard resource labels, admin name, and OSSMigratedV6 label. The migration reads admin, skips with a debug message if labeled, repairs old ossuser user and trusted-cluster mappings, then replaces admin after resource updates. Legacy tctl user creation and OSS role deletion protection use admin. The old NewOSSUserRole constructor remains available for compatibility but is no longer used by migration. Migration tests cover permissions, mappings, old migration repair, and idempotency.

Verification: go test -mod=vendor ./lib/auth ./lib/services ./tool/tctl/common -run '^(TestMigrateOSS|TestRoleParse|TestValidateRole)$' -count=1 passed. git diff --check passed.
