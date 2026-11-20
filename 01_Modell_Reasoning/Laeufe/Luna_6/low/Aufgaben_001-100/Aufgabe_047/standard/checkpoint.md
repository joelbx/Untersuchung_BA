# Checkpoint

Implemented deterministic per-ID seeds in `utils/hasher`.

- Added exported `Hasher` and package-level/method `SetSeed` APIs.
- Explicit string seeds now map deterministically to hash behavior, and assigning the same seed again restores the same output.
- Existing `Reseed` behavior and automatic per-ID seed initialization remain available.
- Added regression coverage for repeatability, reseeding, and seed restoration.

Validation: `go test ./utils/hasher` and `git diff --check` pass.
