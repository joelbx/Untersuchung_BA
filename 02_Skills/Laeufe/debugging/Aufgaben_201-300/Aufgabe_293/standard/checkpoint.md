# OCI configuration investigation

Status: root cause confirmed. `rg` is unavailable in this environment; repository searches use `grep` and `find`.

The checkout was clean at `b22f5f0`. OCI validation sends a URL directly to `registry.ParseReference`, which does not accept the scheme. The OCI parser contains the scheme policy, but config cannot import it because OCI imports config. The JSON schema omits OCI from the type enum and omits two fields. `NewStore` computes its own default directory and the gRPC server has no OCI branch. Both integration matrices omit `fs/oci`.

Reproduction: `GOPROXY=off GOSUMDB=off go test ./internal/config -run 'TestLoad/OCI_invalid_repository_scheme' -count=1` exited 1. Expected the requested scheme error; actual result was `validating OCI configuration: invalid reference: invalid repository` for YAML and ENV.

Resolution: validate schemes before ORAS parsing, parse OCI duration and credentials, add schema fields, pass the bundle root to `NewStore`, expose `DefaultBundleDir`, wire OCI into gRPC storage, and register `fs/oci` in both integration matrices. A former invalid fixture was a valid bare local reference under OCI semantics; it now uses a malformed path.

Checks: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt ./build/testing -count=1` exited 0. `git diff --check` exited 0. A locally built CLI successfully ran `bundle build features:latest` on `build/testing/integration/readonly/testdata` using the configured bundle directory and emitted a digest. A local OCI server stayed running until a deliberate 5-second timeout (exit 124); this is a smoke check, not a full API assertion.

The Dagger integration command `mage dagger:run "test:integration fs/oci"` was not executed because it would require pulling container images, which the offline task forbids. Its runtime result remains unverified.
