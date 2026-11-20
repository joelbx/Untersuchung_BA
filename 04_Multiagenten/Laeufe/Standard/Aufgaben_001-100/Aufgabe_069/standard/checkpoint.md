Task: Implement matcher expressions in lib/utils/parse.
Status: complete.
Changes: added Matcher and Match, regexp/prefix-suffix/negation matchers, validation of matcher syntax, and Variable rejection of matcher calls. Added focused tests.
Verification: go test ./lib/utils/parse; git diff --check.
