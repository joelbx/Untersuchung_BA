# Checkpoint

Issue: Add timeOffset support to streaming and transcoding.
Status: implementation complete; focused tests pass.
Changes: FFmpeg command offset interpolation/fallback, default templates, stream/cache propagation, HTTP parsing, OpenSubsonic extension, mocks and tests.
Verification: go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests; git diff --check.
