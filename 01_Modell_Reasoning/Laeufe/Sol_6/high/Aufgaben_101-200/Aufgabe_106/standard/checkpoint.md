# Checkpoint

Task: Fix WordPress cache lookup and inactive package filtering in the checked-out repository.

Current state: Updated the WordPress cache to pass a map directly and handle nil values as misses; switched inactive filtering to the target server's setting. Added regression tests for nil cache entries and active/inactive plugins and themes. `GOPROXY=off GOSUMDB=off go test ./wordpress ./report ./models` passed, and `go test ./wordpress` passed again after strengthening the assertions. `git diff --check` passed.
