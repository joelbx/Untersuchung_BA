# Checkpoint

Task: update OS end-of-life data and Windows rollup KB mappings for the reported issue.

Completed:
- Corrected Fedora 37/38 dates and added Fedora 40; marked macOS 11 ended and added macOS 15.
- Added SUSE Enterprise Desktop/Server 13/14 dates and refreshed FreeBSD 13/14 lifecycle dates.
- Extended Windows 10 22H2, Windows 11 22H2/23H2, and Server 2022 rollup KB tables with named struct literals in revision order.
- Updated lifecycle tests and added coverage for unapplied/applied classification on lower and synthetic high kernel revisions.

Validation: `go test ./config ./scanner` passes; `git diff --check` passes.
