# Checkpoint

Task: add timeOffset support across streaming and FFmpeg transcoding.
Status: complete.
Changes: FFmpeg command interpolation/fallback, default templates, streamer signatures and offset-aware cache keys, public/Subsonic parameter parsing, OpenSubsonic extension advertisement, call sites and mocks.
Verification: gofmt and git diff --check passed. GOTOOLCHAIN=local GOPROXY=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic passed, including new offset command, cache, and handler tests.
