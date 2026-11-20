Added `LogConfig.GRPCLevel` with an `"ERROR"` default and support for loading `log.grpc_level`. The existing logging fields remain unchanged. Updated the config fixture and test to cover an explicit `"DEBUG"` value.

Verification: `GOPROXY=off go test ./config` passed.