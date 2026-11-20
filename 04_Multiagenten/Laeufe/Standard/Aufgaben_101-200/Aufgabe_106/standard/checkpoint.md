# Checkpoint

Issue: WordPress cache lookup and inactive package filtering.
Status: resolved.
Changes: cache maps passed directly with optional string values; nil entries are misses; scan reads per-server IgnoreInactive; package filtering uses Status.
Validation: GOPROXY=off GOSUMDB=off go test ./wordpress ./report ./models (passed).
