# Checkpoint

Implemented storage.readOnly as optional backend metadata with validation and database support outside the filesystem storage experiment. Added the required invalid object storage fixture. UI exposes selectConfig, derives readonly from the flag with a storage-type fallback, and shows backend icons in the Read-Only badge. Authentication bootstrap avoids a database for all non-database storage when authentication is disabled.

Verification: GOPROXY=off go test ./internal/config ./internal/cmd passed after final changes; git diff --check passed. UI test tooling is not installed locally.
