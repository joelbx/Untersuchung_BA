Refactored directory scanning to use `fs.FS` throughout the walker, moved walker setup into `Scan`, and removed `utils.IsDirReadable`. Added a virtual filesystem test.

`go test -count=1 ./scanner ./utils` and `git diff --check` passed.