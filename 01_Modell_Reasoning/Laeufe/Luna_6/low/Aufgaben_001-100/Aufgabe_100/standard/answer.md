Added `LogConfig.GRPCLevel` with a default of `"ERROR"` and loading for the optional `log.grpc_level` key. Updated the advanced config fixture to verify a custom `"DEBUG"` value; existing logging fields retain their behavior.

`go test ./config` passed.