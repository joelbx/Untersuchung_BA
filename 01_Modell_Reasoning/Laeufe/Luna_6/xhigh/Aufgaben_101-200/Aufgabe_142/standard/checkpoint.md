# Checkpoint

Task: replace the brittle `lib/utils/parse` expression handling with a typed AST, consistent variable validation, string interpolation, and boolean matching; update the trait and PAM callers; run existing relevant tests.

Implemented:
- Added `lib/utils/parse/ast.go` with typed literal, variable, email-local, regexp-replace, and boolean matcher nodes, evaluation contexts, deterministic `String` methods, and kind checks.
- Replaced the old AST walk with `predicate.Parser` callbacks, strict namespace/two-part variable parsing, arity/type checks, shared regex compilation, expression depth/size guards, and typed matcher expressions.
- Added nested/constant string expression evaluation, interpolation validation callbacks, missing/empty value errors, and safe prefix/suffix application without mutating source trait slices.
- Updated role trait allowlisting and PAM namespace validation/logging.

Verification:
- `GOMAXPROCS=2 go test ./lib/utils/parse ./lib/services` passed.
- `go test ./lib/srv` could not build because the container lacks `linux/hidraw.h` and the system SQLite C declarations required by dependencies. `CGO_ENABLED=0 go test ./lib/srv` is also blocked by the dependency's missing non-cgo HID implementation.
