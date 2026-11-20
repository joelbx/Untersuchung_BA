Task complete: database configuration accepts URL or protocol/host/port/user/password/name fields. URL takes precedence. Field mode validates and builds engine-specific URLs; Open and by-value NewMigrator use the same resolver. Parsing/open errors avoid credential text. TLS errors identify qualified settings. Sample config and tests updated.
Tests: go test ./config ./storage/db ./cmd/flipt; go test ./... (passed; sqlite3 upstream C warning).
Delegation: none.
