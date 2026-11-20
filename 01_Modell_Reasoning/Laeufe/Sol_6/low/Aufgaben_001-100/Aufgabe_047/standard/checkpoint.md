Task: deterministic per-ID seeding in utils/hasher.
Completed: exported Hasher, added package and instance SetSeed, retained lazy initialization and Reseed, added mutex protection, and tested seed restoration.
Verification: go test ./utils/hasher passed; git diff --check passed.
