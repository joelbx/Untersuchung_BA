Implemented OS EOL lookup and scan warnings. The canonical lifecycle dates, family constants, evaluators, and warning messages are in [config/os.go](/app/config/os.go:49). Scans now attach warnings to target results, and summaries render them in order with the `Warning: ` prefix ([scan/serverapi.go](/app/scan/serverapi.go:604), [report/util.go](/app/report/util.go:55)).

Centralized epoch-aware major parsing in [util.Major](/app/util/util.go:43) and replaced duplicate parsers across `config`, `gost`, and `oval`.

Verification passed: `GOPROXY=off go test ./config ./util ./scan ./models ./report ./gost ./oval ./internal/version`. `git diff --check` passed.