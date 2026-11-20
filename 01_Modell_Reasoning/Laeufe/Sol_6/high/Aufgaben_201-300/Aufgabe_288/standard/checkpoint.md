Task: replace move-out heuristics with active ID membership and loading guard.
Status: complete. The hook checks the active ID against mailbox element IDs only after mailbox loading; both views receive IDs/loading; conversation view uses isAlwaysMessageLabels to choose message or conversation ID.
Verification: focused Jest suites passed (2 suites, 16 tests); ESLint on changed files passed; git diff --check passed.
Constraints observed: local code/tests only; git history/index and harness configuration unchanged.
