Updated the OSS migration to downgrade the existing `admin` role in place and mark it with `OSSMigratedV6`. Migrated users, trusted cluster mappings, and users created through the legacy CLI path now use `admin`, including records that previously pointed to `ossuser`.

The focused auth and service tests passed, the CLI package compiled, and `git diff --check` passed.