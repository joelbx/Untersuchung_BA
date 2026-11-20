# Checkpoint

Task: Add `timeOffset` support through streaming and transcoding.

Changes: Updated FFmpeg, streamer, cache keys, command templates, HTTP handlers, OpenSubsonic extension, call sites, mocks, and focused tests. Zero offset preserves the existing cache key and leaves legacy FFmpeg commands without `-ss`.

Verification: `go test ./core/ffmpeg ./core ./server/subsonic ./server/public ./tests` passed (exit 0). `git diff --check` passed (exit 0). The build emitted a pre-existing TagLib C++ deprecation warning.

Scope note: Time offsets affect FFmpeg transcoding. Raw streams still use direct file serving and HTTP byte-range seeking; no time-to-byte mapping was introduced for them.
