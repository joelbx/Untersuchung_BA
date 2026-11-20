# Checkpoint

Task: Add timeOffset support through streaming and FFmpeg transcoding.
Status: Complete. HTTP handlers parse and forward offsets; media streaming and cache jobs propagate them; FFmpeg templates and command generation seek to the offset. All call sites and mocks use the new signatures. Focused tests cover command generation, cache identity, propagation, and HTTP defaults.
Verification: GOPROXY=off GOSUMDB=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests ./consts (passed); go test ./core/ffmpeg rerun after final guard change (passed); git diff --check (passed).
