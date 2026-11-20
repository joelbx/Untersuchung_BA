# Checkpoint

Issue: OSS v6 migration must keep the admin role name for trusted cluster mapping.

Changes:
- Downgrade the existing admin role in place, using the OSS migration label for idempotence.
- Assign migrated and legacy-created users to admin; map trusted clusters to admin.
- Protect the migrated admin system role from deletion in OSS.
- Update migration assertions for role permissions, users, and trusted cluster mappings.

Verification:
- `go test ./lib/auth -run '^TestMigrateOSS$' -count=1` — passed.
- `go test ./lib/services ./lib/auth ./tool/tctl/common -count=1` — passed (all three packages).
- `go test ./tool/tctl/common -count=1` — passed after final message text edit.
- `git diff --check` — passed.
