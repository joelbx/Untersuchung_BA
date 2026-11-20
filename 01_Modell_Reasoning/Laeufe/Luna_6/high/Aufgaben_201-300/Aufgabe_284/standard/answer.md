Implemented the single `server.localSite` refactor and changed local-site initialization to reuse the server’s existing access point and clients. Service connections now reject empty or mismatching certificate cluster names with `BadParameter` errors.

Verified with `go test ./lib/reversetunnel` and `git diff --check`; both pass.