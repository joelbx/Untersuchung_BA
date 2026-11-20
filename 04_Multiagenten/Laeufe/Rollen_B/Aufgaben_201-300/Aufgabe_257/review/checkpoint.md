VERDICT: FIX

Reviewed the applied diff in tool/tsh/tsh.go, tool/tsh/db.go, lib/client/api.go, lib/service/service.go, and affected tests.

CODE_DEFECT: tool/tsh/tsh.go:1305-1326: in onSSH's ambiguous-node branch, `allNodes, err := tc.ListAllNodes(...)` shadows the SSH error. When lookup succeeds, `return err` returns nil after printing an SSH failure. Use a distinct lookup error variable and return the original SSH error.

TESTS: `go test ./tool/tsh ./lib/client ./lib/service` passed (tool/tsh 1.355s; lib/client 0.867s; lib/service 2.570s). `git diff --check` passed. No existing test found for this ambiguous-node error path.

TEST_ENVIRONMENT_PROBLEM: none.
