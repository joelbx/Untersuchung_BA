The scanner now traverses native OS paths, uses `os.ReadDir` for audio discovery, and calls the new `utils.IsDirReadable` helper. Audio detection, ignored directories, symlinks, and traversal logging remain covered. I also fixed an error-channel deadlock that prevented traversal errors from reaching the scanner.

`go test ./scanner ./utils -count=1 -timeout=30s` and `git diff --check` passed.