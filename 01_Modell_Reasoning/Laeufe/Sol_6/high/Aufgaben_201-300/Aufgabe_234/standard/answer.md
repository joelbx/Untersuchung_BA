The repository now keeps persistence work on the single `*sql.DB` supplied to `New()`. I removed the global fallback in `WithTx()`, configured the requested SQLite options, and changed startup setup to use its transaction store.

The issue’s final interface section asks for read/write separation, which conflicts with its title and single-connection requirements. I followed the single-connection behavior.

`go test ./db ./persistence ./server/... ./scanner` and `git diff --check` pass.