# Checkpoint

Changed nullable album/artist metadata timestamps and share expiry/visit timestamps to pointers, with `gg.P` and `gg.V` at write/read sites. Added a migration to normalize legacy NULL `album.image_files` values reported in the issue. Added helper and nullable timestamp scan tests.

Verification: `GOPROXY=off go test ./utils/gg ./model ./scanner ./core ./server/subsonic ./server/public ./persistence ./db/...` exited 0. The TagLib C++ dependency emitted a deprecation warning; no test failures. `git diff --check` exited 0 before final review.
