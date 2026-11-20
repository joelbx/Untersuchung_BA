Added the canonical EOL lookup, strict support end checks, and per-target scan warnings. The scan summary now prints each warning with `Warning: ` in evaluation order. Major-version parsing is shared across the affected components, including Amazon release handling.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./config ./util ./scan ./report ./oval ./gost && git diff --check`.