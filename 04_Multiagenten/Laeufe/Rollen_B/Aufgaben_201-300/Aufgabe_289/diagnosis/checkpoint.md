Fault localization findings:
- internal/config/config.go has private decodeHooks and Load composes it with experimentalFieldSkipHookFunc; no exported DefaultConfig.
- internal/config/config_test.go contains a full defaultConfig helper currently available only to tests.
- internal/config/storage.go uses value Local/Git fields despite requested pointer shape; validation dereferences them. Existing storage test literals use value forms and would need updating if types change.
- Config.Version lacks a mapstructure tag. Most other schema fields have tags. Current CUE schema omits storage and some authentication session fields; exact added schema_test.go is unavailable in checkout.
- Package test baseline in progress.
- Baseline `go test ./internal/config` passes. The described schema_test.go is absent from this checkout, so its precise CUE decode/validation path cannot be verified locally.
- No project source or tests changed during this diagnosis.
