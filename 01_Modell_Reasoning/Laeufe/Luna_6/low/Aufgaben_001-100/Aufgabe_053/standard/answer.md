Updated `major` to return `""` for zero-length input and added an empty-input regression case. Existing non-empty parsing is unchanged.

`go test ./oval` passed. The compiler emitted a warning from `go-sqlite3` C code.