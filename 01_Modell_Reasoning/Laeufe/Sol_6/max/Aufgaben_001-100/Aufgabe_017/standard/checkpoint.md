# SQL Server connection diagnostic

Status: complete. SQL Server pinger, protocol selection, timeout and cancellation handling, error categorization, and focused tests are implemented.

Validation: gofmt and `git diff --check` passed. `GOPROXY=off GOSUMDB=off go test ./lib/client/conntest/database ./lib/client/conntest` passed.
