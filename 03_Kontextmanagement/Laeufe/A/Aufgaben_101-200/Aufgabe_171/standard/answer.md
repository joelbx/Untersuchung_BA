Implemented `x-flipt-accept-server-version` handling in the gRPC unary interceptor chain. Handlers can retrieve the parsed version with `FliptAcceptServerVersionFromContext`; missing or invalid headers fall back to `1.0.0`. Both `v1.0.0` and `1.0.0` are accepted.

The relevant middleware and command tests passed with `GOPROXY=off`.