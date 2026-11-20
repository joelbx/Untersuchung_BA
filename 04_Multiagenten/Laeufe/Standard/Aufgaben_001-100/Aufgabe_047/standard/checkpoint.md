# Checkpoint

Task: deterministic per-ID seeding for utils/hasher.
Status: complete.
Changes: exported Hasher and SetSeed APIs; deterministic seeded hashing; automatic per-ID initialization and reseeding; synchronized seed access; regression tests.
Verification: go test ./utils/hasher; go test ./db ./persistence; go test -race ./utils/hasher; git diff --check.
