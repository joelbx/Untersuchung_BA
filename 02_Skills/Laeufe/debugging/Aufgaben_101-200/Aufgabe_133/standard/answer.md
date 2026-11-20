Updated the OSS migration to downgrade the existing `admin` role in place, mark it with `OSSMigratedV6`, and skip it on later runs. Migrated users, trusted cluster mappings, and legacy user creation now use `admin`, preserving access to leaf clusters during a partial upgrade.

The focused migration test and the full `lib/auth`, `lib/services`, and `tool/tctl/common` test packages passed.