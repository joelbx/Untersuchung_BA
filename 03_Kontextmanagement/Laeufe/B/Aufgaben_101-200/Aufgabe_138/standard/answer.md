Added `storage.oci.manifest_version` with `1.0` and `1.1` as valid values and `1.1` as the default. Configuration loading rejects other values with the requested error. Bundle creation now uses the configured version through `WithManifestVersion`.

Config, schema, and OCI bundle tests passed, including a local `1.0` build and fetch. A live ECR upload was not tested.