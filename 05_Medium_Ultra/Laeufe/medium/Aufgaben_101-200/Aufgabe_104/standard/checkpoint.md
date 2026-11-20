Task: Add metadata configuration with CheckForUpdates and backward-compatible default.
Status: Implemented metadata.check_for_updates in Config, Default, and Load. Added YAML and JSON coverage and documented the default in example config.
Verification: GOPROXY=off go test ./... passed; GOPROXY=off go test ./config passed after final test adjustment; git diff --check passed.
