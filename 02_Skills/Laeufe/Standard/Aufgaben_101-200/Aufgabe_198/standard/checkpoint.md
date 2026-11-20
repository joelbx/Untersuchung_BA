# Checkpoint

Resolved Red Hat OVAL advisory and fix-state handling in the checked-out repository.

- Updated `github.com/vulsio/goval-dictionary` to locally cached `v0.9.5`, which includes `Advisory.AffectedResolution`; updated `go.sum` using offline Go tooling.
- Restricted distro advisory conversion to supported title prefixes and guarded nil advisories.
- Propagated OVAL fix states through HTTP/DB collection, `fixStat`, package statuses, and Red Hat result merging. `isOvalDefAffected` now returns affected, notFixedYet, fixState, and fixedIn.
- Removed Red Hat Gost `DetectCVEs`, routed Red Hat derived families to `Pseudo`, and skipped Gost package detection for those families.
- Added focused tests for advisory titles, package fix state, and resolution state behavior.

Checks: `GOPROXY=off GOSUMDB=off go test -mod=mod ./oval ./gost ./detector` passed. `git diff --check` passed. Initial test run failed on an unused import and an outdated FixedIn expectation; both were fixed before the passing run. `rg` is unavailable, so repository searches used grep/find.
