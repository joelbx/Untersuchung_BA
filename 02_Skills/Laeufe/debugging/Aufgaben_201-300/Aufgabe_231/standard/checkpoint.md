# Checkpoint

Task: resolve Vuls2 schema version mismatch handling.
Status: investigating repository code and tests before changes.

Investigation: shouldDownload returns before GetMetadata when SkipUpdate is true and checks only timestamps otherwise. newDBConnection creates a closed DB handle and returns it without metadata validation. BoltDB GetMetadata requires Open; callers open the returned handle. Expected schema version is 0; test mismatch with version 1. Hypothesis: moving SkipUpdate after metadata validation and checking version before timestamps forces refresh or reports an error; opening, validating, then closing in newDBConnection catches incompatible fetched DBs without changing caller lifecycle.

Regression before fix: GOPROXY=off GOSUMDB=off go test ./detector/vuls2 -run Test_shouldDownload -count=1 failed as expected: recent mismatched schema returned false; SkipUpdate mismatched schema returned nil error. Applied schema checks in shouldDownload before freshness and SkipUpdate decisions; newDBConnection now opens, reads metadata, validates schema, and closes the temporary open.

Final verification: GOPROXY=off GOSUMDB=off go test ./detector/vuls2 -count=1 passed. git diff --check passed. Added a lifecycle test confirming newDBConnection returns a handle the detector can open after metadata validation. No offline tooling blocks encountered.
