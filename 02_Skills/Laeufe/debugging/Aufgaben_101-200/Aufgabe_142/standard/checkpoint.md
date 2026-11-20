# Checkpoint

Investigating current parser and call sites before editing. `rg` is unavailable (`/bin/sh: rg: not found`); using local `find` and `grep`.

Root cause: `walk` returns a flat `walkResult` with one `transform`; an outer call replaces an inner transform, so nested functions cannot compose. It also flattens literals and selectors into parts, allowing malformed variable forms and preventing constant source evaluation. `Interpolate` checks only the root variable; nested variables cannot be validated by callers. The predicate parser in the local module cache supports function callbacks, identifier callbacks, and property callbacks, so it can construct a typed AST.

Regression before fix: `go test ./lib/utils/parse -run TestNestedExpressionRegression -count=1` failed because nested email.local was dropped; actual `alice@example.com-user`, expected `alice-user`.

Implementation: typed AST with predicate callbacks, recursive evaluation and variable validation; service and PAM callers validate every variable. Parser checks length and nesting before recursive parsing. Existing parser tests were updated to assert behavior rather than old struct layout.

Initial cross-package check `go test ./lib/services ./lib/srv -run 'TestApplyValueTraits|Test.*PAM.*Environment' -count=1` hit offline system-header failure: `/go/pkg/mod/github.com/flynn/hid@v0.0.0-20190502022136-f1b9b6cc019a/hid_linux.go:3:11: fatal error: linux/hidraw.h: No such file or directory`. Retrying with `CGO_ENABLED=0`. The check's final result is pending.

Final checks:
- `go test ./lib/utils/parse -count=1` passed.
- `git diff --check` passed.
- `CGO_ENABLED=0 go test ./lib/services ./lib/srv -run 'TestApplyValueTraits|Test.*PAM.*Environment' -count=1` could not complete: package compilation reported undefined BPF symbols (`lib/bpf/bpf_nop.go:29`), HID symbols (`github.com/flynn/u2f/u2fhid/hid.go:52`), PKCS#11 symbols (`github.com/ThalesIgnite/crypto11/crypto11.go:127`), and `getLoginShell` (`lib/shell/shell.go:33`). The command was interrupted after these compile failures. Service/PAM runtime behavior remains unverified by tests in this offline environment.
