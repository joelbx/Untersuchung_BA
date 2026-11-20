Added `storage.oci.manifest_version` with valid values `"1.0"` and `"1.1"`, defaulting to `"1.1"`. Configuration loading now rejects other values with the requested error. Bundle creation uses the configured version through `WithManifestVersion`.

Added configuration and bundle tests. The relevant Go tests passed.