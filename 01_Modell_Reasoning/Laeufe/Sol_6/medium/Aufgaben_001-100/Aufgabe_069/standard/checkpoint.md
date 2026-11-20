Task: implement matcher expressions in lib/utils/parse.
Status: implemented Matcher, Match, regexpMatcher, prefixSuffixMatcher, notMatcher, and Variable rejection of matcher calls. Added focused tests.
Verification: GOPROXY=off go test ./lib/utils/parse passed; GOPROXY=off go test ./lib/utils -check.f TestGlobToRegexp passed. Full ./lib/utils fails in pre-existing expired certificate test (fixture expired 2021, current date 2026).
