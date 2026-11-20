VERDICT: FIX

**Code defect:** [core/media_streamer.go](/app/core/media_streamer.go:76) opens raw files and returns them without applying `timeOffset`. A `/stream` request that selects raw delivery therefore starts at the beginning even with a positive offset. Apply a time based seek for raw streams or route those requests through transcoding.

**Tests:** `GOPROXY=off GOSUMDB=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic` passed in all four packages. `TEST_ENVIRONMENT_PROBLEM`: none.