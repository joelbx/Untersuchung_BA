# Checkpoint

Task: Fix WordPress cache lookup and inactive package filtering in /app.
Status: Complete.
Changes: Cache is a direct map with nullable string entries; nil entries are cache misses. WordPress scan reads IgnoreInactive from the result's server configuration and filters packages by Status. Added cache and scan coverage.
Validation: GOPROXY=off GOSUMDB=off go test ./wordpress ./report ./models; git diff --check. Both passed.
Constraints observed: Used local code and tests only; did not change git history, index baseline, or harness configuration.
