VERDICT: FIX

**Code defect:** In [onSSH](/app/tool/tsh/tsh.go:1305), the ambiguous-node branch shadows the SSH error with the node lookup error. If the lookup succeeds, it prints the SSH failure but returns `nil`, so `Run` reports success. Keep the errors separate and return the original SSH error.

**Tests:** `go test ./tool/tsh ./lib/client ./lib/service` passed for all three packages. `git diff --check` passed. The passing tests do not cover this error path.

**TEST_ENVIRONMENT_PROBLEM:** none.