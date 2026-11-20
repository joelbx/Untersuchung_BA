Implemented matcher support in [parse.go](/app/lib/utils/parse/parse.go): literals and globs, regexp match and not-match calls, email.local, static prefixes and suffixes, and validation for malformed or unsupported expressions. `Variable()` now rejects regexp matcher calls with the specified error.

The existing parse tests pass: `go test ./lib/utils/parse`.