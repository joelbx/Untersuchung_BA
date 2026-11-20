Correction round: reviewing the existing patch and independent review. Reviewer found onSSH can return nil after an SSH failure when node lookup succeeds. Will preserve the original SSH error, then rerun go test ./tool/tsh ./lib/client ./lib/service and git diff --check.
Confirmed shadowing in onSSH ambiguous-host handling. Changed node lookup error to listErr so a successful lookup leaves the original SSH error intact for return. Running reviewer-flagged checks.
Reviewer-flagged checks passed: go test ./tool/tsh ./lib/client ./lib/service; git diff --check. No remaining failures.
