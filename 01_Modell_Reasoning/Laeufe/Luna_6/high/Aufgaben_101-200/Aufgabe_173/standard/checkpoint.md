# Checkpoint

## Task
Resolve HA database access by selecting among same-name database services, retrying tunnel connectivity failures, deduplicating `tsh db ls`, and adding deterministic test hooks/offline tunnel simulation.

## Initial state
- Repository: `/app`
- Working tree was clean.
- `rg` is unavailable in this environment; searches will use `find` and `grep`.

## Plan
1. Locate database server types, proxy selection/dialing, fake remote site, and CLI listing code/tests.
2. Implement deduplication, stable sorting/logging, candidate authorization context, configurable shuffle, retry/failover, and offline tunnel simulation.
3. Update or add relevant tests and run the existing focused tests.

## Progress
- Added `HostID` to database server strings and host ID as the same-name sort key.
- Added ordered name deduplication and applied it before `tsh db ls` rendering.
- Changed proxy authorization to retain all matching database servers; proxy dialing shuffles candidates and retries tunnel connection problems.
- Added a clock-seeded, concurrency-safe default shuffle hook and `FakeRemoteSite.OfflineTunnels` simulation.
- `go test ./types` from `/app/api` passed.
- `go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh` passed.
- `git diff --check` passed.
