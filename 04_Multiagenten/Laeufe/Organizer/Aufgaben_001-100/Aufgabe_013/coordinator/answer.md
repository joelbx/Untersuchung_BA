Implemented `DocCLI.tty_ify()` to render `L()`, `R()`, and `HORIZONTALLINE` alongside the existing macros, including multiple macros on one line. It preserves unsupported text such as `IBM(International Business Machines)`.

The focused CLI tests passed: **30 passed**. The full CLI unit suite had failures outside the focused tests; an isolated Galaxy case passed. No delegation was used.