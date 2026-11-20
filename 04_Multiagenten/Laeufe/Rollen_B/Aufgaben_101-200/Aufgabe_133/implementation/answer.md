Updated the OSS migration to downgrade the existing `admin` role in place. Migrated users, trusted cluster mappings, and legacy user creation now use `admin`; a role marked `OSSMigratedV6` is skipped on later runs.

The focused migration test and relevant services and tctl package checks passed.