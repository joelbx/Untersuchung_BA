Implemented the canonical EOL lookup, centralized OS family identifiers and major-version parsing, and added per-target EOL warnings to scan results. The scan summary now prints each warning with `Warning: ` in evaluation order.

The mapping, date boundaries, warning wording, version parsing, and summary rendering have focused tests. `go test -p 2 ./config ./util ./scan ./report ./gost ./oval` passed, as did `git diff --check`.

No delegation was used; I completed the changes directly.