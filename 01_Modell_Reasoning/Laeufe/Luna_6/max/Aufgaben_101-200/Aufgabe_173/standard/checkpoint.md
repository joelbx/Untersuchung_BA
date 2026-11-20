# Checkpoint

## Objective
Resolve the HA database access issue: deduplicate database listings by service name and let the proxy retry shuffled same-name database servers over reverse tunnels.

## Completed
- Added `DeduplicateDatabaseServers`, stable name/host ID sorting, and host ID in database server log strings.
- Added the configurable proxy shuffle hook with a clock-seeded, concurrency-safe default.
- Authorization now retains every matching database server; proxy dialing retries connection problems and reports when no candidate is reachable.
- Added per-server offline simulation to `FakeRemoteSite` and deduplicated `tsh db ls` results.
- Added API tests and DB proxy tests for deterministic fallback and all-candidates-offline behavior.

## Verification
- Passed `GOMAXPROCS=2 go test -p 1 ./types` from `/app/api`.
- Passed `GOMAXPROCS=2 go test -p 1 ./lib/reversetunnel`.
- Passed `GOMAXPROCS=2 go test -p 1 ./lib/srv/db`.
- Passed `GOMAXPROCS=2 go test -p 1 ./tool/tsh`.
- Re-ran the two DB fallback tests and reverse tunnel package after the final fake-tunnel change; all passed.
- An initial parallel test invocation exceeded the container process/thread limit; sequential capped runs passed.

## Constraints
- Used repository code and tests only; no external research or delegation.
- Did not alter git history, index baseline, or harness configuration.
