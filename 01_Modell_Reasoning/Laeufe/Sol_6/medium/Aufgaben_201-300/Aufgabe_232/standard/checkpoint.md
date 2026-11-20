Task complete: canonical OS EOL lookup, scan warnings, summary rendering, shared major parsing.
Implemented: config/os.go centralizes family constants and exact lifecycle table; scan/eol.go evaluates releases with a supplied time; base and HTTP scans append warnings; summaries render ordered Warning lines; util.Major and internal/version replace duplicated parsing in config, gost, and oval.
Verification: GOPROXY=off GOSUMDB=off go test ./config ./scan ./report ./util ./oval ./gost passed. git diff --check passed.
