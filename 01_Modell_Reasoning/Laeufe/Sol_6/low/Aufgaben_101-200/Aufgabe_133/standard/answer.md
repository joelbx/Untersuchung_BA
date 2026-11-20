Updated the OSS migration to replace the existing `admin` role with a restricted, `OSSMigratedV6`-labeled role. It now skips an already migrated admin role, assigns existing users to `admin`, and maps trusted clusters to `admin`. Legacy user creation also assigns `admin`.

The updated migration test passes. The services and tctl packages compile, and `git diff --check` passes.