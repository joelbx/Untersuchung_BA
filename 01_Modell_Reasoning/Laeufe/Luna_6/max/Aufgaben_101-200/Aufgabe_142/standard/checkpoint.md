# Checkpoint

- Task: replace brittle expression parsing/evaluation in `lib/utils/parse` with a typed AST and update interpolation call sites.
- Constraints: use repository code and existing tests only; do not alter git history, index baseline, or harness configuration.
- Implemented: typed string, variable, email-local, regexp-replace, regexp-match, and regexp-not-match nodes; `predicate.Parser` callbacks build the AST, enforce argument types/arity, and validate two-part variables and namespaces.
- Implemented: nested and constant string expressions, shared regex compilation, bounded input/depth, static interpolation prefix/suffix, variable validation callbacks, and AST-backed `MatchExpression` matching.
- Implemented: role trait allowlisting and PAM external/literal namespace validation; PAM missing-value warnings wrap a redacted error without claim names.
- Verification passed: `go test -count=1 ./lib/utils/parse`; focused services tests (`TestApplyValueTraitsValidation`, `TestApplyTraits`, `TestTraitsToRoleMatchers`); `go test ./lib/pam`; `git diff --check`.
- Server package compile could not run: the default build lacks `linux/hidraw.h`; with CGO disabled, unrelated PKCS#11/HID dependencies fail to compile.
