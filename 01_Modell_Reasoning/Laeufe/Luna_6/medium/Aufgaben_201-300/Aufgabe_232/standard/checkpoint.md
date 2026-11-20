# Work checkpoint

Completed canonical EOL mapping and lookup in `config/os.go`, including strict-after support phase evaluators and current standard-support ended state. Added per-target EOL warnings with standardized wording and date formatting in `scan/base.go`, excluding pseudo and Raspbian targets. Added `util.Major` and routed OVAL/GOST parsing through it.

Validation passed: `go test ./scan ./config ./util ./models ./report`; `git diff --check`.
