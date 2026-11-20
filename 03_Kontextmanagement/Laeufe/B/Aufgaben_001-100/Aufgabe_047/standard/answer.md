Implemented deterministic per-ID seeding in [hasher.go](/app/utils/hasher/hasher.go). Setting a seed now reproduces the same hash, reseeding changes it, and restoring the seed restores the original hash. IDs without a seed initialize automatically.

Added coverage in [hasher_test.go](/app/utils/hasher/hasher_test.go). `go test -race ./utils/hasher` and `git diff --check` passed.