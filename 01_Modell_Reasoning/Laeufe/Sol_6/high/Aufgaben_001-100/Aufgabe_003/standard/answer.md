Added `timeOffset` support through the stream and transcode call chain. FFmpeg templates use `-ss %t`; custom templates without `%t` receive `-ss` after the input path for nonzero offsets. Transcoding cache keys distinguish offsets while preserving the existing key for offset 0.

The public and Subsonic stream handlers default missing, invalid, or negative offsets to 0. The OpenSubsonic response advertises `transcodeOffset`. Updated mocks and added command, cache, and handler tests.

All affected Go package tests pass.