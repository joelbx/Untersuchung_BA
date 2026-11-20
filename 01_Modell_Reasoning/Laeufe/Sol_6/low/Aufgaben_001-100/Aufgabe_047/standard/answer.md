Added per-ID `SetSeed` support to the hasher. Setting the same seed restores the same hash for an identifier and input; reseeding changes it. IDs without a seed are initialized automatically.

The existing hasher tests, including new seed-restoration cases, pass with `go test ./utils/hasher`.