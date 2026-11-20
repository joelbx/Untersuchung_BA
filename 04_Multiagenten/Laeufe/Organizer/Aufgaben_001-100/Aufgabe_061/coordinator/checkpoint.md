Task: Fix package lookup for process associations across RPM architectures/versions.
Status: Completed implementation and verification.
Changes: Added shared base.pkgPs; Debian and Red Hat postScan use it. RPM getOwnerPkgs resolves owner names, skips known file errors, rejects malformed lines; needsRestarting uses the same owner lookup. Added parser regression test.
Verification: GOPROXY=off GOSUMDB=off go test ./scan -count=1 passed; git diff --check passed.
Delegation: None.
