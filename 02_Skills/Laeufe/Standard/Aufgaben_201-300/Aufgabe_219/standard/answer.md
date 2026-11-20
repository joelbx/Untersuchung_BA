Added `token:created` and `token:deleted` to the audit checker, including wildcard matching. gRPC initialization now uses the configured audit events to decide whether token deletion logging is enabled and passes that boolean to the authentication server.

Added tests for event matching and enabled versus disabled deletion logging. The relevant Go test suites and `git diff --check` passed.