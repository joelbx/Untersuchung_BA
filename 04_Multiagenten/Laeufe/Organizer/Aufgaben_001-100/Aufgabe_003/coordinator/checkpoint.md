Task: Add timeOffset support throughout FFmpeg transcoding and media streaming.
Status: Implemented and reviewed. No delegation used.
Changes: Added offset to Transcode/NewStream/DoStream and all call sites, FFmpeg %t interpolation/fallback -ss, default templates, offset cache key, public/Subsonic parsing, OpenSubsonic extension, and tests.
Validation: go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests passed. go test ./... failed only in scanner/metadata/taglib (three fixture/environment-related assertions); all other packages passed. git diff --check passed.
