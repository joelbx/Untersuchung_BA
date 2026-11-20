# Checkpoint

Task: Fix WordPress cache lookup and inactive package filtering in the checked-out repository.

Status: Complete. Cache uses a direct map with nil-capable values; searchCache returns ("", false) for missing or nil entries. WordPress scanning reads IgnoreInactive from the scan's server configuration and filters packages by Status. Added tests for nil and empty cache values and for active/inactive plugins and themes under both server settings.

Verification: GOPROXY=off GOSUMDB=off go test ./wordpress ./report ./models; git diff --check. Both passed.
