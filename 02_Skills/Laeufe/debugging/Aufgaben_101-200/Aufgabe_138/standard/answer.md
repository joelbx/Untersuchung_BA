OCI bundle creation now accepts `storage.oci.manifest_version` as `"1.0"` or `"1.1"`. It defaults to `"1.1"`, rejects unsupported values with the specified error, and uses `WithManifestVersion` when building bundles. The config schema and regression tests were updated.

Relevant tests passed for configuration, OCI bundles, the OCI snapshot store, and the storage and CLI package builds.