VERDICT: ACCEPT

The patch in [scan/base.go](/app/scan/base.go:744) returns a non-nil map with sorted, deduplicated port slices. Its sole consumer handles the new format. The cases in [scan/base_test.go](/app/scan/base_test.go:280) cover empty results, duplicates, and wildcard overlap. I found no defect requiring correction.

`go test ./scan` passed. `gofmt -l scan/base.go scan/base_test.go` produced no output, and `git diff --check` passed.