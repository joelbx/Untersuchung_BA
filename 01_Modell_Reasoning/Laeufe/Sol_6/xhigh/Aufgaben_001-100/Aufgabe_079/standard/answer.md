Updated the scanner to traverse absolute OS paths and read audio files with native filesystem calls. Added [IsDirReadable](/app/utils/paths.go), retained directory ignore and symlink handling, and fixed walker error delivery so a failed scan can report its error.

`go test ./scanner ./utils` and `git diff --check` passed. The Windows-specific tests were updated but could not be run on Linux.