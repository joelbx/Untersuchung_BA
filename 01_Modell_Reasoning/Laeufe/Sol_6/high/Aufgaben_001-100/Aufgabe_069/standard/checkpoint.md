Task: implement matcher expressions in lib/utils/parse.
Status: complete. Added Matcher and Match, regexp/glob/function parsing, prefix/suffix matching, negation, email.local matching, and Variable rejection of matcher functions.
Verification: go test -mod=vendor ./lib/utils/parse (passed); git diff --check (passed).
Constraints observed: local repository and tests only; git history, index baseline, and harness configuration untouched.
