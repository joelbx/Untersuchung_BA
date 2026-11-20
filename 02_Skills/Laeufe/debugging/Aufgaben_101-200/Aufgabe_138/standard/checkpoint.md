# Checkpoint

Task: make OCI manifest version configurable with default 1.1 and validation.
Status: investigating repository flow before edits.
Note: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Root cause: `Store.Build` always passes `oras.PackManifestVersion1_1_RC4` to `PackManifest`; `StorageConfig.OCI` has no manifest version field and neither store constructor passes such an option. Existing OCI config defaults/validation only handle repository, directory, and interval. The CLI bundle constructor and storage constructor both create the OCI store.
Pattern: configuration uses Viper defaults in `StorageConfig.setDefaults`, validates in `StorageConfig.validate`, and forwards store behavior via functional options.
Hypothesis: adding a validated string setting, mapping 1.0 to ORAS's v1.0 enum at both constructors, and using a defaulted store option in `Build` resolves the incompatibility.
Pre-fix tests: `GOPROXY=off go test ./internal/config -run TestOCIManifestVersionConfig -count=1` failed to compile because `OCI.ManifestVersion` is undefined; `GOPROXY=off go test ./internal/oci -run TestStore_BuildManifestVersion -count=1` failed to compile because `WithManifestVersion` is undefined. Both failures match missing interfaces.

Implementation: added `storage.oci.manifest_version` (1.1 default; 1.0/1.1 validation) to config and both schemas; added `WithManifestVersion(oras.PackManifestVersion)` to OCI store and used the option in `Build`; forwarded 1.0 from both storage and CLI constructors.
Verification in progress: `GOPROXY=off go test ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt -count=1` has passed config and OCI, storage constructor compiled; CLI package remains compiling. `git diff --check` passed.

Final verification: `GOPROXY=off go test ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt -count=1` exited 0 (config and OCI tests passed; storage and CLI packages compiled, no tests). `GOPROXY=off go test ./internal/storage/fs/oci -count=1` exited 0. `git diff --check` exited 0. The bundle regression test inspects the generated manifest and distinguishes 1.0 from 1.1 by config media type and artifact type.
