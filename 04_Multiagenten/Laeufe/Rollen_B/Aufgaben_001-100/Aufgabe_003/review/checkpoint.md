VERDICT: FIX
Reviewed applied diff and streaming call chain. CODE DEFECT: core/media_streamer.go:76-88 returns raw streams directly from os.Open without applying a positive timeOffset; /stream and /handleStream can select raw delivery, so playback begins at byte zero despite the supplied offset. Correction: implement time-based seeking for raw streams or route positive-offset requests through a suitable transcoding path, preserving offset=0 behavior.
TESTS: GOPROXY=off GOSUMDB=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic — exit 0; all four packages passed. The compiler emitted a TagLib deprecation warning, with no test failure.
TEST_ENVIRONMENT_PROBLEM: none.
