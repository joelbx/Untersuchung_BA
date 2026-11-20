# OCI configuration issue checkpoint

Objective: fix OCI storage configuration parsing/validation, bundle directory handling, and integration suite registration.
Status: complete.
Changes: OCI validation uses the OCI parser; config schema supports OCI fields and duration; default bundle path moved to config; NewStore takes dir; CLI and server pass directory; fs/oci suite and CI registration added.
Verification: go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./config ./internal/cmd ./cmd/flipt ./build/testing (passed); git diff --check (passed).
