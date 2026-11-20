Implemented per-ID seed control in [hasher.go](/app/utils/hasher/hasher.go). The exported `Hasher` now supports `SetSeed`, and the package provides the matching global function. Missing IDs are initialized automatically, reseeding assigns a fresh seed, and seed access is synchronized.

`go test ./utils/hasher` passed.