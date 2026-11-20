# Checkpoint

Implemented nullable handling for optional album/artist metadata timestamps, share expiration and last-visited timestamps, and album image file paths. Added generic `gg.P`/`gg.V` helpers and unit coverage for zero and nil values. Updated field reads, writes, and scanner invalidation to preserve optional values.

Verification: `go test ./utils/gg ./model ./persistence ./core ./core/artwork ./server/subsonic ./server/public ./scanner` passed. `git diff --check` passed.
