Implemented token audit support. The checker now recognizes `token:created` and `token:deleted`, including wildcard settings. gRPC startup passes the configured deletion status to the authentication server.

The relevant audit, authentication, command, and token creation middleware tests pass.