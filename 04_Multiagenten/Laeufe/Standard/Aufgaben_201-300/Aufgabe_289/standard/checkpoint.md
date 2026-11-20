Task: expose canonical defaults and decode hooks; align Storage pointer fields; verify configuration tests.
Status: complete. DefaultConfig is exported and returns the former test defaults. DecodeHooks is exported and used by Load. Storage Local/Git are pointers with nil validation. Existing tests updated for pointer expectations.
Verification: go test ./internal/config ./internal/cmd; go test ./internal/config; git diff --check all passed.
