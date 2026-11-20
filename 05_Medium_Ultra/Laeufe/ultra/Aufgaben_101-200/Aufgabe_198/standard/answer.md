Resolved the Red Hat-family OVAL issue in the checked-out files. The analyser now accepts only distribution-specific advisory IDs, matches fix states to the installed package and module, and carries `FixState`, `NotFixedYet`, and `FixedIn` through the results. It uses the locally cached goval-dictionary v0.9.5.

Gost no longer detects package CVEs for these distributions; Red Hat API data only enriches CVEs already found. Three subagents handled the advisory, fix-state, and Gost changes; I integrated and reviewed the patch.

Offline tests passed: `go test -mod=readonly ./oval ./gost ./detector ./models`. `git diff --check` also passed.