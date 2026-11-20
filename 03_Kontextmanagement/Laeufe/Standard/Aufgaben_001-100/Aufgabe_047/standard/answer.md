Added `Hasher.SetSeed` and the package-level `SetSeed` in [hasher.go](/app/utils/hasher/hasher.go). Each ID now keeps a string seed, so restoring a previous seed restores its hash results. Missing IDs still receive a seed automatically, and map access is synchronized.

Added coverage in [hasher_test.go](/app/utils/hasher/hasher_test.go). The package tests and race tests pass.