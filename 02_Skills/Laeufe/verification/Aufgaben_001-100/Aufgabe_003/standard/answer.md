Added `timeOffset` support to the FFmpeg transcoding path. Stream handlers pass the offset through `NewStream` and `DoStream`; FFmpeg uses `%t` in updated templates or inserts `-ss` for older templates. Cache entries are distinct by offset, while zero retains the existing cache key. Call sites, mocks, and focused tests were updated.

Verification: `go test ./core/ffmpeg ./core ./server/subsonic ./server/public ./tests` and `git diff --check` passed.

**Scope:** Raw streams still use direct file serving and HTTP byte-range seeking; a time offset does not change their starting position.