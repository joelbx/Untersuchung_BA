Implemented matcher support in [parse.go](/app/lib/utils/parse/parse.go), including literals, anchored wildcards, raw regexps, `regexp.match`, `regexp.not_match`, and static prefixes and suffixes. `Variable()` now rejects matcher functions. Added coverage in [parse_test.go](/app/lib/utils/parse/parse_test.go).

Verification passed: `GOPROXY=off go test ./lib/utils/parse` and `git diff --check`.