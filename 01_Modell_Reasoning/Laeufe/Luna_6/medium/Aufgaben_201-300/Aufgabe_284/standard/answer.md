Implemented the single `localSite` refactor and reused the server’s existing local access point and clients. Service connections now validate the certificate cluster name against that site before registering.

`go test ./lib/reversetunnel` and `git diff --check` passed.