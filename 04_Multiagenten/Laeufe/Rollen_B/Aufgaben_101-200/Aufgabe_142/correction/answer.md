Fixed the brace parsing defect in [parse.go](/app/lib/utils/parse/parse.go): ordinary single braces now work in literals and static text around templates, while malformed `{{` and `}}` delimiters still produce errors. Added regression cases in [parse_test.go](/app/lib/utils/parse/parse_test.go).

The reviewer’s exact `GOPROXY=off go test` commands for `./lib/utils/parse` and `./lib/services` pass. `git diff --check` passes.

**TEST_ENVIRONMENT_PROBLEM:** `./lib/srv` could not build because `linux/hidraw.h` and required sqlite3 symbols are unavailable. The CGO disabled retry also failed on missing platform symbols, so its tests did not run.