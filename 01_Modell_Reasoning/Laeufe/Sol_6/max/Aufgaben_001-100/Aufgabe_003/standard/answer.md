Implemented `timeOffset` for transcoded streams. The Subsonic and shared-stream handlers now parse it, default missing, malformed, or negative values to 0, and pass it through the streamer and offset-specific cache entries to FFmpeg. Default templates use `-ss %t`; custom templates without `%t` receive `-ss` after the input path for positive offsets. I updated call sites and mocks and advertised `transcodeOffset` support.

Raw file responses still use HTTP byte-range seeking.

The relevant Go suites passed, and `git diff --check` is clean.