Implemented per-ID deterministic seeding in [hasher.go](/app/utils/hasher/hasher.go). The package and `Hasher` now expose `SetSeed`; setting the same seed again restores the same hash. Missing IDs are initialized automatically, and `Reseed` assigns a fresh random seed. Seed access is mutex protected.

`go test ./utils/hasher` passes.