# Checkpoint

Resolved nullable field scans by changing album `image_files`, album and artist `external_info_updated_at`, and share `expires_at`/`last_visited_at` to pointers. Added `gg.P` and `gg.V`, updated their reads and assignments, and added helper and share NULL timestamp tests.

Verification: `go test ./utils/gg ./model ./persistence ./core ./core/artwork ./scanner ./server/subsonic ./server/public` passed. `go test ./...` passed across affected packages, but failed in `scanner/metadata/taglib` on fixture enumeration, duplicate gain tags, and unreadable-file permission expectations. `git diff --check` passed.
