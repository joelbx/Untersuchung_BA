# Checkpoint

Issue: nullable album/artist/share timestamps and album image_files cause scan errors after upgrade.
Implemented: generic gg.P and gg.V; pointer model fields for external_info_updated_at, expires_at, last_visited_at, and image_files; nil-safe callers; helper tests.
Validation: affected package tests pass; git diff --check passes. Full go test ./... has four unrelated TagLib test failures concerning fixture metadata and unreadable-file behavior.
