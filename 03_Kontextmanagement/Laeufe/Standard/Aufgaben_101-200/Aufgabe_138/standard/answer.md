Added `storage.oci.manifest_version` with accepted values `"1.0"` and `"1.1"`, defaulting to `"1.1"`. Config loading returns the requested error for unsupported values. Bundle creation now uses the configured version through `WithManifestVersion`.

Tests passed for config loading, generated manifests, schemas, and the affected Go packages.