Implemented `timeOffset` support through FFmpeg transcoding and streaming. Default command templates include `-ss %t`; custom templates without `%t` add `-ss OFFSET` after the input path when the offset is positive. Stream cache keys include the offset, and public and Subsonic stream handlers parse `timeOffset`, defaulting invalid or missing values to `0`.

The OpenSubsonic response now advertises the `timeOffset` extension. Updated call sites and mocks to pass the new integer argument.

Verification: the relevant package tests passed, and `git diff --check` passed. `go test ./...` encountered three failures in `scanner/metadata/taglib` involving fixture enumeration, duplicate replaygain tags, and unreadable-file permissions; the changed packages passed.