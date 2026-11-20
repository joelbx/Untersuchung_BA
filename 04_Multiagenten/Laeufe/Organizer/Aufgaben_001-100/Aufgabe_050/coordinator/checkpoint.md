# Checkpoint

Resolved nullable album image files and optional album, artist, and share timestamps with pointer model fields. Added generic `gg.P` and `gg.V`, updated writes and reads, and added helper plus repository regression tests.

Verification: `git diff --check` and `GOPROXY=off go test ./utils/gg ./model ./persistence ./core ./core/artwork ./scanner ./server/subsonic ./server/public` passed. No delegation used.
