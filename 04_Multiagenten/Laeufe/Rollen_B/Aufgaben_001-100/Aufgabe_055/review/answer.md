VERDICT: ACCEPT

The applied patch meets the stated Trivy metadata and detector requirements. I found no correctness or regression defect. No project code was changed during this review.

`GOPROXY=off GOSUMDB=off go test ./contrib/trivy/parser/v2 ./detector` passed for both packages. `git diff --check` passed.

TEST_ENVIRONMENT_PROBLEM: none.