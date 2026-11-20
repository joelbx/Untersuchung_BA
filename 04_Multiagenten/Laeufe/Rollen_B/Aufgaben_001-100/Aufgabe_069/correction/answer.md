Fixed matcher template parsing in [parse.go](/app/lib/utils/parse/parse.go). `Variable` now gives the required matcher-function error when a quoted regexp contains braces, and `Match` ignores `}}` inside quoted arguments when locating the closing delimiter. Added regression tests in [parse_test.go](/app/lib/utils/parse/parse_test.go).

`go test ./lib/utils/parse` and `git diff --check` pass.