The scanner now traverses absolute paths using OS filesystem operations. Audio detection, directory ignore rules, and traversal logging remain in place. I added `utils.IsDirReadable` and updated the scanner tests for the new path based calls.

Verification passed: `GOPROXY=off go test ./scanner ./utils` and `git diff --check`.