Fault localization complete (2026-10-22). No project source or tests changed.

- internal/config/storage.go: StorageConfig has Type/Local/Git/Object only; validate() checks backend-specific fields but never readOnly. A pointer/optional bool is needed to distinguish absent from explicit false, since both false and true on non-database storage should be rejected if defined. JSON/mapstructure tags must permit metadata and YAML/env propagation.
- internal/config/config.go: Load unmarshals then invokes validators; Storage is behind experimental filesystem_storage feature gate. Validation belongs in StorageConfig.validate().
- internal/config/config_test.go: table-driven YAML and env tests include storage cases around lines 613-700. Add invalid_readonly.yml case with exact error; existing s3_full.yml closely matches requested fixture.
- internal/server/metadata/server.go: GetConfiguration marshals whole Config, so adding a JSON-visible StorageConfig field propagates through existing endpoint.
- ui/src/types/Meta.ts: IStorage has only type; StorageType lacks OBJECT. Add optional readOnly and OBJECT.
- ui/src/app/meta/metaSlice.ts: fulfilled fetchConfigAsync sets readonly solely from type; there is no selectConfig. Add public selectConfig and use explicit readOnly when defined, otherwise type !== DATABASE.
- ui/src/components/Header.tsx: Read-Only badge already exists with a generic orange dot. Use configuration to choose database/local/git/object icon; badge visibility follows selectReadonly.
- internal/cmd/auth.go: authenticationGRPC early return bypasses getDB for disabled auth only for git/local. Include every non-database type, notably object.

Uncertainty: no direct tests found for these UI selectors/header or authenticationGRPC. Config test suite currently exercises YAML and env variants. No tests run; inspection only.
