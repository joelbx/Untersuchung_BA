Restored native OS filesystem scanning with absolute paths, preserved audio detection and directory ignore rules, and added `utils.IsDirReadable`. I also fixed a walker error-channel deadlock exposed by the new missing-root test.

`GOPROXY=off GOSUMDB=off go test ./scanner ./utils` and `git diff --check` passed.