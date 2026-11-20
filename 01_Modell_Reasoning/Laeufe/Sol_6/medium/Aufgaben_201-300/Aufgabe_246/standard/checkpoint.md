Task: Resolve multi-lockfile vulnerability source ambiguity.
Status: Complete. Updated per-file lockfile analysis, path-aware library lookup and reporting, vulnerability source paths, duplicate-CVE merging, and error-returning driver initialization. Updated local module versions needed for AnalyzeFile and error-returning NewDriver.
Verification: GOPROXY=off go test ./... passed; relevant tests rerun after final test addition; git diff --check passed.
