# Checkpoint

Task: add OCI-backed fs snapshot source and context-aware SnapshotSource.Get.
Status: investigating repository and existing tests before edits.
Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Root cause evidence: ORAS OCI Store loads index/tag resolver in `oci.New`, so an existing `Store.store` holds stale tags after an external process changes index.json. `Store.Fetch` copies from that old instance. `SnapshotSource.Get` has no context. Existing decoder rejects features media type and ignores namespace annotation. Hypothesis: reopening the local OCI store per fetch and passing the chosen target to the decoder will expose external retags; a source can cache by digest.

Implementation: added `storage/fs/oci.Source` with 30s default polling, digest-based snapshot reuse, cancellation-aware subscription, and logger. `SnapshotSource.Get` now accepts context across implementations/callers. OCI `Store.Fetch` lazily opens local OCI stores on each call, and fetches manifest/layers from the selected target. Layers support namespace/features media types, namespace annotation, and gzip decoding. gRPC storage selection and OCI config validation/defaults now accept local OCI references.

Reproduction: `go test ./internal/oci -run TestStoreFetchSeesExternalRetag -count=1` failed before the fix because the second fetch incorrectly reported a digest match. `go test ./internal/oci -run TestStoreFetchGzipLayer -count=1` failed before gzip support with `unexpected layer encoding: "yaml+gzip"`. `go test ./internal/config -run TestOCIStorageValidationAcceptsLocalReference -count=1` failed before scheme handling with `invalid reference: invalid repository`.

Verification: `go test ./internal/config ./internal/cmd ./internal/storage/fs/... ./internal/oci` passed; `go test -race ./internal/storage/fs/oci ./internal/oci` passed; `git diff --check` passed. Earlier `go test ./internal/storage/... ./internal/oci` passed. Remote registry fetch is implemented through ORAS ReadOnlyTarget but no remote registry integration test was available locally.
