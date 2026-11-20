Implemented `storage.oci.manifest_version` with values `"1.0"` and `"1.1"`, a `"1.1"` default, and the required validation error. Bundle creation now uses the configured version through `WithManifestVersion` in both the bundle command and server store.

Relevant Go tests and `git diff --check` pass. Local build and fetch tests verify both manifest formats; a live ECR upload was not tested.