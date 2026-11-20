Implemented the expression AST, nested evaluation, variable and namespace validation, matcher handling, and updates to trait and PAM interpolation.

`go test ./lib/utils/parse ./lib/services` and `git diff --check` passed. The `lib/srv` tests could not build because this environment lacks required C headers and SQLite symbols.