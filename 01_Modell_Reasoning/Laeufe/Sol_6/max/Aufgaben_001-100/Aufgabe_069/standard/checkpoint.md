# Matcher expression support

- Task: implement matcher parsing and validation in `lib/utils/parse`.
- Status: inspecting repository code and existing tests.
- Constraints: use local code and existing tests; leave git history, index, and harness configuration unchanged.
- Implemented Matcher and Match with literal/glob/raw-regexp handling, regexp functions, and fixed prefix/suffix matching.
- Variable rejects matcher functions, including nested calls.
- Added matcher behavior and validation tests.
- `GOPROXY=off GOFLAGS=-mod=vendor go test ./lib/utils/parse` passes.
- Status: final review and relevant package tests.
- Final verification: `GOPROXY=off GOFLAGS=-mod=vendor go test ./lib/utils/parse` passes.
- `GOPROXY=off GOFLAGS=-mod=vendor go test ./lib/utils -check.f GlobToRegexp` passes.
- Full `go test ./lib/utils` has one unrelated existing failure: `TestRejectsSelfSignedCertificate` uses a certificate expired in 2021 and now reports expiry (current date 2026) instead of unknown authority.
- `git diff --check` passes. Status: implementation complete.
