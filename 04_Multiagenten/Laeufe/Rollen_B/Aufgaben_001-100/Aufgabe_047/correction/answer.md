Fixed the hasher’s cross-instance reproducibility issue. It now hashes the supplied seed and input deterministically, so restoring a seed restores the same hash. Added a test that checks matching results across fresh `Hasher` instances.

The reviewer’s offline hasher, race, DB, and persistence tests all pass. `git diff --check` passes. No test environment problems remain.