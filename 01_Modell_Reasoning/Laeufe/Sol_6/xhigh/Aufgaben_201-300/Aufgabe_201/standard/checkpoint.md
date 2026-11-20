Task: Support string or keys/operator object in rule segment configuration.
Status: Complete. Added unified SegmentEmbed/IsSegment YAML representation and validation, canonical object export, importer/snapshot extraction, single-key OR fallback in import/export/snapshot/SQL rule and rollout paths, requested fixtures, and focused regression tests.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/ext ./internal/storage/fs ./internal/storage/sql -count=1 passed; git diff --check passed.
Constraints observed: Local code/tests only; no git history/index or harness changes.
