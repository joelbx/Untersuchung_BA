# Checkpoint

Implemented whole-string `${VARIABLE_NAME}` substitution as the first configuration decode hook. Added integration coverage for multiple variables, typed values, empty and missing variables, invalid references, and `FLIPT_` overrides.

Verified with `GOFLAGS=-mod=readonly GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./internal/config ./config -count=1` (both packages passed). Restored the incidental `go.work.sum` update produced during the first build.
