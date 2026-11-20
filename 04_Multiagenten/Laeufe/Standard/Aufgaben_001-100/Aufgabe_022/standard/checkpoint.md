Completed RPM source filename parsing changes in `scanner/redhatbase.go` and regression tests in `scanner/redhatbase_test.go`.

Unparseable source filenames now append a warning while retaining binary packages. Epoch-prefixed source filenames now produce the expected source name and version. Verified with `go test ./scanner -count=1` and `git diff --check`.
