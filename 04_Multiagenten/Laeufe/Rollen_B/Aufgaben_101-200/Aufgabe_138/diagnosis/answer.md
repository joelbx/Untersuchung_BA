The failure originates in [Store.Build](/app/internal/oci/file.go:368), which hardcodes ORAS manifest v1.1. The configured version has no path to reach it:

- [OCI configuration](/app/internal/config/storage.go:294) has no `manifest_version` field, default, or validation. Both [CUE](/app/config/flipt.schema.cue:205) and [JSON](/app/config/flipt.schema.json:742) schemas also omit it.
- Both the [server store constructor](/app/internal/storage/fs/store/store.go:105) and [bundle CLI constructor](/app/cmd/flipt/bundle.go:146) would need to pass the selected version through a `WithManifestVersion` store option.
- [Copy](/app/internal/oci/file.go:426) transfers an existing manifest; selecting v1.0 for future builds would not convert bundles already built as v1.1.

The fix should cover loading `"1.0"`, defaulting to `"1.1"`, rejecting `"1.2"` with the exact requested error, and verifying the resulting manifest version. Existing starting points are [config tests](/app/internal/config/config_test.go:816) and [build tests](/app/internal/oci/file_test.go:201).

Per the fault localization scope, I made no project source or test changes. I recorded the diagnosis in [checkpoint.md](/app/.codex-role-output/checkpoint.md).