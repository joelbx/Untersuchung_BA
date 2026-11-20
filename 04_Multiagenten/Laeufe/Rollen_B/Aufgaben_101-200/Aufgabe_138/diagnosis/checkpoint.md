Progress: Fault localization complete; no project source or tests changed.
- internal/oci/file.go Build hardcodes oras.PackManifestVersion1_1_RC4 in oras.PackManifest (line 368). StoreOptions has no manifest version or WithManifestVersion option; NewStore initializes only bundleDir.
- internal/config/storage.go OCI lacks manifest_version; StorageConfig.setDefaults sets only OCI poll interval and bundle directory; validate checks repository/reference only. Config.Load in internal/config/config.go runs defaults, unmarshal, then validators.
- Both config/flipt.schema.cue and config/flipt.schema.json define storage.oci without manifest_version.
- Store construction occurs in internal/storage/fs/store/store.go and cmd/flipt/bundle.go; both need configured version propagation. CLI getStore may see cfg.Storage.OCI == nil, so default must also be safe at OCI store level.
- internal/oci/file.go Copy uses oras.Copy of an existing manifest; configuring build version will not convert previously built v1.1 bundles during push.
- Existing tests: internal/config/config_test.go OCI fixture/table cases; internal/oci/file_test.go TestStore_Build and TestStore_Copy. Behavior coverage should include valid 1.0, invalid 1.2 exact error, omitted 1.1, and built manifest format.
