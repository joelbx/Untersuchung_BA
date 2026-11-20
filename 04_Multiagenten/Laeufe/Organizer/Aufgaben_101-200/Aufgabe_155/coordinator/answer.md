Image configurations now accept exactly one of a tag or digest, with the requested validation errors. Scanning uses `GetFullName()` to build `name:tag` or `name@digest`, scan results retain the digest, and report identifiers include the full image reference followed by `@serverName`. Per-image server names now use `index@originalServerName`.

`go test ./config ./scan ./report` passed. The broader `models` run remains blocked by existing vet warnings in `models/library.go`; with vet disabled, its existing `TestScan` fails because it finds no vulnerability.

No delegation was used.