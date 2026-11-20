Reverted directory scanning to native OS filesystem operations with absolute paths. The scanner retains audio detection, directory ignore rules, and error logging. Added `utils.IsDirReadable` and a regression test for symlinks pointing outside the scan root.

`GOPROXY=off go test ./scanner ./utils` passed.