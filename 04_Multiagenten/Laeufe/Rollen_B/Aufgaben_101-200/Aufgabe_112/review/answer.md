VERDICT: ACCEPT

The applied patch connects Fortinet CPE detection, advisory enrichment, confidence selection, and report content ordering. I found no correctness or regression defect in the reviewed changes.

`GOPROXY=off GOSUMDB=off go test ./detector ./models ./server` passed for `detector` and `models`; `server` compiled and has no test files. `git diff --check` passed. No `TEST_ENVIRONMENT_PROBLEM`.