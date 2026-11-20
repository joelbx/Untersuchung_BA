Implemented `storage.oci.manifest_version` with a default of `"1.1"`. Configuration loading accepts `"1.0"` and `"1.1"` and rejects other values with the requested error. Both the server and bundle CLI pass the selected version to OCI bundle creation through the new `WithManifestVersion` option.

Added configuration and bundle manifest tests. The relevant Go tests and `git diff --check` pass.