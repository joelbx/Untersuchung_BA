Updated the OSS migration to downgrade the existing `admin` role in place. Migrated users, trusted cluster mappings, and legacy user creation now use `admin`; the migration also corrects entries previously labeled while pointing to `ossuser`.

Verification passed: the focused migration tests, the full tests for `lib/auth`, `lib/services`, and `tool/tctl/common`, and `git diff --check`.