Implemented the expression AST and parser in [ast.go](/app/lib/utils/parse/ast.go:32) and [parse.go](/app/lib/utils/parse/parse.go:69). Interpolation now supports nested and constant string expressions, strict variable validation, and empty-result errors. Matchers use boolean AST nodes with shared regex compilation and prefix/suffix handling.

Updated role trait allowlisting in [role.go](/app/lib/services/role.go:491) and PAM namespace validation in [ctx.go](/app/lib/srv/ctx.go:979). Wrote the requested checkpoint at `.codex-role-output/checkpoint.md`.

`GOMAXPROCS=2 go test ./lib/utils/parse ./lib/services` passed. The server package could not build because this container lacks required native HID and SQLite declarations.