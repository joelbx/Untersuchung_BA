# Checkpoint

## Issue
Refactor `reversetunnel.Server` to hold one `*localSite` and reuse the existing proxy access point/cache and clients. Update all single-site operations and validate with existing relevant tests.

## Progress
- Replaced `server.localSites` with a single `server.localSite` and changed local-site lookups, connection draining, tunnel-close handling, proxy fan-out, and site listing to use that instance.
- Changed `newlocalSite` to derive dependencies from `server` and reuse its auth client, access point, auth addresses, and peer client. It no longer creates a second caching access point.
- Added cluster-name validation for service connections, including empty and mismatching names.
- Updated `TestLocalSiteOverlap` for the new constructor.
- `go test ./lib/reversetunnel` passes; `git diff --check` passes.
