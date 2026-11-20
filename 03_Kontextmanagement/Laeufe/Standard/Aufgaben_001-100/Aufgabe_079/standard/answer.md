The scanner now traverses directories with absolute OS paths, and audio file listing uses `os.ReadDir`. Directory ignore rules, recursive error logging, and folder detection remain in place. I added [IsDirReadable](/app/utils/paths.go) and updated the scanner tests.

Verification passed: `go test ./scanner ./utils` and `git diff --check`.