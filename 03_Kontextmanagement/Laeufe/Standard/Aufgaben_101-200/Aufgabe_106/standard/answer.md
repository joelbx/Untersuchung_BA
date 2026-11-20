Updated the WordPress cache lookup to use the map directly and treat a nil value as a cache miss. Package filtering now honors the per-server `IgnoreInactive` setting while preserving the existing report flag, excluding inactive plugins and themes while keeping active ones.

Added regression coverage. `GOPROXY=off go test ./wordpress ./report` and `git diff --check` pass.