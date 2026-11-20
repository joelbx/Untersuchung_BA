Task: Fix WordPress cache lookup and inactive package filtering.
State: Complete. Cache is passed directly as a map of nullable strings; searchCache returns empty/false for absent or nil values. WordPress scanning uses per-server IgnoreInactive. Tests: go test ./wordpress ./models ./report passed.
