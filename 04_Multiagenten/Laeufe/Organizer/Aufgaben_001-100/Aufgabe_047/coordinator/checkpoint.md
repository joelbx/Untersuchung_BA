# Checkpoint

Task: deterministic per-ID seeding for utils/hasher.
Status: implemented and verified.
Changes: exported Hasher, package and method SetSeed, per-ID string seeds, automatic seed initialization, synchronized access, stable restore within a Hasher instance.
Tests: go test ./utils/hasher; go test -race ./utils/hasher; go test ./db ./persistence; git diff --check (all passed).
Delegation: none.
