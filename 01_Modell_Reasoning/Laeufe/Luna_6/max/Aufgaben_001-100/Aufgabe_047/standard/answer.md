Implemented deterministic per-ID seeding in [hasher.go](/app/utils/hasher/hasher.go): added package-level and instance `SetSeed`, retained random `Reseed`, and added automatic seed initialization for IDs without a seed. Access to the seed map is synchronized.

`go test ./utils/hasher` and `git diff --check` passed.