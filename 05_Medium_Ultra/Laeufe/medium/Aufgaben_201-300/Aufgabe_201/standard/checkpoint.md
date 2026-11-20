Task: support string or keys/operator object for rule segment YAML.
Status: implemented unified rule segment YAML model and validation; import/export, filesystem snapshot, SQL rule and rollout fallback, fixtures and focused tests updated. Tests passing: go test ./internal/ext ./internal/storage/fs ./internal/storage/sql (GOPROXY=off GOSUMDB=off).
Constraints: local repository and existing tests only; keep git history/index/harness unchanged.
