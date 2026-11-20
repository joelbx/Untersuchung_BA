Added `SetSeed` for both the global hasher and individual `Hasher` instances. Explicit seeds now produce repeatable hashes across instances; reseeding changes the hash, and restoring a seed restores its result. Identifiers still receive a seed automatically on first use.

Verification passed: `go test -race ./utils/hasher`, `go test ./db ./persistence`, and `git diff --check`.