Added `SetSeed` to the package and exported `Hasher` type. Each ID now has a stored seed; reseeding changes its hash, and restoring the previous seed restores the previous hash within the same `Hasher` instance. Seed access is synchronized for concurrent calls.

The hasher, race, database, and persistence tests passed. No delegation was used.