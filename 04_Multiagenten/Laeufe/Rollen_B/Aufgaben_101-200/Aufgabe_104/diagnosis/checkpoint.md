Fault localization complete. No project source or tests edited.

Evidence:
- config/config.go:15-22 Config has no Metadata field; :86-121 Default initializes all current sections but no metadata.
- config/config.go:124-153 defines all recognized Viper keys; :155-245 Load starts with Default(), applies only explicit keys, then validates. Metadata/check_for_updates is never read from YAML/JSON or FLIPT_METADATA_CHECK_FOR_UPDATES.
- config/config.go:270-282 ServeHTTP marshals Config with JSON tags, so adding a field/tag also affects exposed config JSON.
- config/config_test.go:44-119 and config/testdata/config/{default,advanced,deprecated}.yml cover current defaults and YAML loading, but no metadata or JSON fixture.
- cmd/flipt/flipt.go:139-146 calls config.Load at initialization. No existing version-update-check code was found in cmd/config; issue's actual startup behavior may require separate implementation if intended beyond configuration capability.
- go test ./config passes.

Likely fix surface: config/config.go Config + metadataConfig with CheckForUpdates bool and JSON tag; Default() true; Viper key metadata.check_for_updates with IsSet/GetBool during Load to preserve explicit false; existing validate() should accept either bool. Add config tests for omitted section/field, true/false in YAML and JSON, and possibly env override; update example config if desired. Verify JSON key naming against project conventions (existing JSON uses camelCase while YAML uses snake_case).
