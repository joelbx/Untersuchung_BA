Implemented the OS EOL lookup and added lifecycle warnings to each scan result. The scan summary now prints each warning with the required `Warning: ` prefix and preserves its order. Major version parsing is shared across config, util, OVAL, and GOST.

Verification passed: `go test ./config ./util ./scan ./report ./oval ./gost` and `git diff --check`.