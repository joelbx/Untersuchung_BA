Task: Add log.grpc_level config with ERROR default, independent of existing log fields.
Status: Complete. Added LogConfig.GRPCLevel, default ERROR, and Load(path) handling for log.grpc_level. Updated sample default and advanced config fixture; added direct default/load assertion.
Verification: GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./config passed. git diff --check passed.
Delegation: None used.
