VERDICT: FIX

**Code defect:** The SQL Server agent forwards upstream login failures as error number `28353` in [stream.go](/app/lib/srv/db/sqlserver/protocol/stream.go:51). The new classifiers in [sqlserver.go](/app/lib/client/conntest/database/sqlserver.go:111) recognize only the original SQL Server numbers, so invalid users and database names reach the diagnostic flow as `UNKNOWN_ERROR`. Preserve the original error category across the agent response, or classify its forwarded form.

**Tests:** `go test ./lib/client/conntest/database ./lib/client/conntest` passed (1.164s and 0.032s). No test environment problem.