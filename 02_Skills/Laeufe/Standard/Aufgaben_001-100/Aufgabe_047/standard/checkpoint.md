# Hasher deterministic seeding

Started work in `/app`. Repository status was clean. `rg` is unavailable, so local searches will use `grep`/`find`.

Implemented exported `Hasher`, package and instance `SetSeed`, seed restoration, automatic initialization, and synchronized seed map access. A process-wide `maphash.Seed` makes explicitly seeded hashes match across `Hasher` instances in the same process. Added regression tests for restoration, package-level assignment, cross-instance agreement, and automatic initialization.

Checks passed:
- `GOTOOLCHAIN=local GOPROXY=off go test ./utils/hasher ./db ./persistence`
- `GOTOOLCHAIN=local GOPROXY=off go test -race ./utils/hasher`
- `git diff --check`

The initial `rg` search could not run because `rg` is not installed; searches used `find` and `grep` instead. The process-wide `maphash.Seed` is randomized at process startup, so numeric hash values are not guaranteed to match across process restarts.
