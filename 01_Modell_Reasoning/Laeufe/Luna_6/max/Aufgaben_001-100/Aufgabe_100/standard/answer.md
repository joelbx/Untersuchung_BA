Added `LogConfig.GRPCLevel`, defaulting to `ERROR`, and taught `Load()` to read `log.grpc_level`. The config example and existing loader fixture now cover the default and a custom `DEBUG` value; the other logging settings remain unchanged.

`go test ./config` and `git diff --check` passed.

- [config.go](/app/config/config.go:34)
- [config_test.go](/app/config/config_test.go:238)
- [default.yml](/app/config/default.yml:1)