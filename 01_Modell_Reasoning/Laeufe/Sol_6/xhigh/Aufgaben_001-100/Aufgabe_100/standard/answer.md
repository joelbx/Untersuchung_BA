Added `LogConfig.GRPCLevel` with an `ERROR` default and made `Load(path)` read `log.grpc_level`. The existing logging settings remain unchanged. The tests now cover both the default and an explicit value.

Verification: `go test ./config` passed.