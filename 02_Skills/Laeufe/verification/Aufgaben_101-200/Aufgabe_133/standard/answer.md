Updated the OSS migration to downgrade the existing `admin` role in place, mark it with `OSSMigratedV6`, and skip migration when that label is present. Migrated users, trusted cluster mappings, and legacy-created users now use `admin`.

Verification passed: the focused migration test, the `lib/services`, `lib/auth`, and `tool/tctl/common` test suites, and `git diff --check`.