Implemented `timeOffset` through FFmpeg transcoding and streaming. Offsets are included in the transcode cache key; default templates use `-ss %t`, and custom templates add `-ss` after the input path when needed. Public handlers default missing or invalid offsets to zero, and Subsonic advertises the `transcodeOffset` extension.

Updated call sites, mocks, and tests. Validation passed:

`GOPROXY=off GOSUMDB=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic`

`git diff --check` also passed. The build emitted a TagLib deprecation warning.