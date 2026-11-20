Implemented per-ID `SetSeed` on the exported `Hasher` and the package-level hasher. Hashing now initializes missing seeds automatically, supports reseeding and restoring a previous seed, and produces the same result for the same explicit seed across instances in one process.

Added tests for those behaviors. `go test ./utils/hasher ./db ./persistence` and `git diff --check` pass.

Because `maphash` uses a random seed at process startup, hash values are **not guaranteed to match across restarts**.