Added per-ID `SetSeed` support to [hasher.go](/app/utils/hasher/hasher.go). Reseeding changes the hash, and restoring a previous seed restores the earlier result. A shared process seed also makes explicit seeds consistent across `Hasher` instances in the same process.

Added coverage in [hasher_test.go](/app/utils/hasher/hasher_test.go). The hasher, database, and persistence tests pass.