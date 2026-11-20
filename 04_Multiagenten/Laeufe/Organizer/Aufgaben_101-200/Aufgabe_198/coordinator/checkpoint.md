# Checkpoint

Task completed: Red Hat family package CVE detection now uses OVAL, with family-specific advisory IDs and propagated package fix states.

Changes: goval-dictionary updated to cached v0.9.5; OVAL resolution states mapped to package status; Gost RedHat DetectCVEs removed and Red Hat family maps to Pseudo; detector skips Gost package detection for those families. Existing Gost unfixed-state tests replaced with a client selection regression test. No delegation used.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod ./...` passed; targeted OVAL/Gost/detector suites passed again after the final test edit; `git diff --check` passed.
