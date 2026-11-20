# Checkpoint

Task: Add timeOffset support throughout streaming and FFmpeg transcoding.
Status: Complete.
Changes: Updated FFmpeg command interpolation, default transcoding templates, streaming signatures and cache keys, public and Subsonic handlers, OpenSubsonic extension response, mocks and tests.
Verification: go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests; git diff --check.
