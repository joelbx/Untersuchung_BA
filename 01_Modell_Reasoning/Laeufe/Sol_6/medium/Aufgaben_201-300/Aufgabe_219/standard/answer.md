Added `token:created` and `token:deleted` to the audit checker, including wildcard matching. The gRPC setup now checks whether `token:deleted` is enabled and passes that boolean to the authentication server to control deletion audit logging. I also updated the audit documentation and added checker tests.

The relevant audit, authentication, command, and gRPC middleware test suites passed.