Task: Implement matcher expression support in lib/utils/parse.
Status: Completed. Added Matcher and Match, regexp/prefix-suffix/negation matchers, function validation, Variable rejection, and matcher tests.
Verification: go test ./lib/utils/parse passed; go test ./lib/utils -check.f GlobToRegexp -count=1 passed; git diff --check passed.
Known unrelated failure: go test ./lib/utils fails CertsSuite.TestRejectsSelfSignedCertificate because its certificate fixture expired in 2021 (current date 2026).
