Task: Fix terminal restoration after canceled or completed tsh password login.
Status: Implemented restoration on password abandonment and Close, added NotifyExit for global stdin reader, called it from tsh main before exit handling, and added cancellation/deadline/Close tests.
Verification: go test ./lib/utils/prompt passed; git diff --check passed.
