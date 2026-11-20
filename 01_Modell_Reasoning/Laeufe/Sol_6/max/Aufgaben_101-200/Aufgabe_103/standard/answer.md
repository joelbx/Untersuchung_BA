Updated [RPM parsing](/app/scanner/redhatbase.go) to preserve empty release fields, format epoch and release values consistently, and parse `-src.rpm` filenames while rejecting malformed ones. Added regression cases in [redhatbase_test.go](/app/scanner/redhatbase_test.go).

Verified: `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` passes.