Updated the OSS migration to downgrade the existing `admin` role, mark it with `OSSMigratedV6`, and keep users and trusted cluster mappings assigned to `admin`. Legacy `tctl users add` now assigns `admin` as well.

Validation passed for the OSS migration test, role tests, `tctl` common tests, and `git diff --check`. The checkpoint is recorded in `.codex-role-output/checkpoint.md`.