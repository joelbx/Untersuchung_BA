Implemented deterministic per identifier seeding with exported `Hasher` and `SetSeed` APIs. Restoring a previous seed restores the same hash output; automatic seed initialization and `Reseed` remain supported.

Added regression coverage. `go test ./utils/hasher` and `git diff --check` pass.