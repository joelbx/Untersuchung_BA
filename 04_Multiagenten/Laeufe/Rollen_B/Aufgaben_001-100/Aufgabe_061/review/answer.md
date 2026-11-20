VERDICT: FIX

**Code defect:** [parseOwnerPkgs](/app/scan/redhatbase.go:597) accepts an RPM owner when only its name matches the installed package. If `libgcc` release `39.el7` on `i686` owns a file while the package map holds release `44.el7` on `x86_64`, [pkgPs](/app/scan/base.go:919) marks the newer package as affected. Compare the owner’s version, release, and architecture with the stored package before associating the process, or retain distinct package identities.

**Tests:** `GOPROXY=off GOSUMDB=off go test ./scan` passed. `git diff --check` passed. An earlier `go test ./scan` was interrupted to rerun it with network access disabled.

**TEST_ENVIRONMENT_PROBLEM:** None.