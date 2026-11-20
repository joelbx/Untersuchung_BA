# Checkpoint

Task: add deterministic per-identifier seeding to `utils/hasher`.

Initial evidence: `hasher.go` stores `maphash.Seed` per ID, creates random seeds in `Reseed` and on first hash, and has no `SetSeed`. Investigation and baseline checks are in progress.

Baseline: `GOPROXY=off GOTOOLCHAIN=local go test ./utils/hasher` passed. `db/db.go` registers `HashFunc` as SQLite `SEEDEDRAND`; `persistence/sql_base_repository.go` calls `Reseed` when random sorting resets. Existing tests cover random reseeding and per-ID stability, but no explicit seed or restore. `maphash.Seed` is opaque and cannot be constructed from a string, so the current representation prevents caller supplied seeds. Hypothesis: retain one maphash seed for the hasher, store caller supplied seed strings per ID, and hash the stored seed with the input. A regression test will exercise set, reseed, and restore before editing the implementation.

Regression before fix: `GOPROXY=off GOTOOLCHAIN=local go test ./utils/hasher` failed because `SetSeed` was undefined on the instance and package, as expected. After the implementation, that command passed. `GOPROXY=off GOTOOLCHAIN=local go test -race ./utils/hasher` passed. `GOPROXY=off GOTOOLCHAIN=local go test ./persistence ./db` passed. `git diff --check` passed.

Implementation: exported `Hasher`, added package and instance `SetSeed`, stored seed strings per ID, kept one `maphash.Seed` per hasher, and generated random seed strings for reseeding and first use. Length-prefixed seed input avoids concatenation ambiguity. A mutex protects the seed map. Regression tests cover explicit seed stability, reseeding, restoration, and package-level access.
