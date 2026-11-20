Task: Add timeOffset support through streaming, transcoding, HTTP handlers, mocks, and tests.
Status: Complete.
Changes: Offset flows from public and Subsonic stream handlers through MediaStreamer, cache jobs, and FFmpeg; default templates use -ss %t; fallback commands add -ss after input only for nonzero offsets; OpenSubsonic advertises timeOffset version 1. Other callers pass 0.
Verification: go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests (passed); git diff --check (passed).
