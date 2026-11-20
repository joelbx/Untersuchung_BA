Implemented exact `${VARIABLE_NAME}` substitution as the first configuration decode hook. Matching values use the environment variable when present; other values stay unchanged. Added tests for multiple references, integer ports, log encoding, and existing `FLIPT_` overrides.

`go test ./internal/config -count=1` and `go test ./config -count=1` passed.