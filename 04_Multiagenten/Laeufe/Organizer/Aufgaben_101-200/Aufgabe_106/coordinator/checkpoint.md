# Checkpoint

Task: Fix WordPress cache lookup and inactive package filtering.
Implemented: direct map cache with nil-aware lookup; server WordPress ignore-inactive configuration; cache and package filtering tests.
Verification: GOPROXY=off GOSUMDB=off go test ./wordpress ./report passed (sqlite3 compiler warning only).
Delegation: none.
