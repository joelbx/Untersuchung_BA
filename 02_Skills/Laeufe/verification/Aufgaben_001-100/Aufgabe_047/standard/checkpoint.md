# Checkpoint

Implemented exported `Hasher` and package-level/method `SetSeed`. Explicit seed strings are hashed with FNV-1a and a length prefix for reproducibility across instances. Automatic initialization and `Reseed` generate per-ID seed strings from an instance maphash seed plus a counter. A mutex protects seeds and counter.

Verification:
- Red test: `GOTOOLCHAIN=local GOPROXY=off go test ./utils/hasher` failed to compile before implementation because SetSeed was absent.
- `GOTOOLCHAIN=local GOPROXY=off go test ./utils/hasher` passed after implementation.
- After final test edits, `GOTOOLCHAIN=local GOPROXY=off go test -race ./utils/hasher` passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./db ./persistence` passed.
- `git diff --check` passed.
