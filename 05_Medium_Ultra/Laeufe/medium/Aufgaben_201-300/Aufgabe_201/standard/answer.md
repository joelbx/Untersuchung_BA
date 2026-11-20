Updated the repository so rule `segment` accepts either a string or a `keys`/`operator` object. Single key segments use `OR_SEGMENT_OPERATOR`; exports always use the object form. Import, filesystem snapshots, SQL rule and rollout persistence, and the requested fixtures are updated.

Relevant tests pass: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql`.