# OCI configuration issue checkpoint

Status: implementation and local verification complete.

Scope: validate OCI repository configuration, parse all OCI options, wire the bundle directory into the store, and register the OCI integration suite in build and CI matrices. Run relevant existing tests after edits.

Implemented: OCI scheme validation and missing-repository handling; schema, duration, bundle directory, and authentication wiring; explicit bundle root in NewStore; default bundle directory helper; gRPC OCI source; fs/oci integration case and CI entry.

Verified: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt ./build/testing` passed; `git diff --check` passed. A local CLI smoke check built and listed a bundle from the readonly integration fixtures using a configured bundle directory. The Dagger integration matrix was registered and compiled; its containerized run was not performed in this environment.
