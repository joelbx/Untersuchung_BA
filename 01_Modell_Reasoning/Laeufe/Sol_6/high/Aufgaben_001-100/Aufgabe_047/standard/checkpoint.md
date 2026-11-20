Task: Implement deterministic per-ID seeding in utils/hasher/hasher.go.
Status: Complete. Exported Hasher; added package and method SetSeed; explicit seeds can be restored after Reseed; missing IDs initialize automatically. Seed map access is synchronized. Hash input includes length-delimited ID, seed, and string.
Validation: go test ./utils/hasher; go test ./db ./persistence; git diff --check (all passed).
Scope note: maphash's shared seed is process-local, so explicit seeds reproduce hashes within a process and across Hasher instances in that process.
