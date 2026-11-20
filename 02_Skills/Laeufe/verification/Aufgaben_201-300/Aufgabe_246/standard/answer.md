Updated lockfile scanning and vulnerability reporting so findings retain their source path. Each lockfile is analyzed separately; library lookups use both path and name; duplicate CVEs retain findings from each file. Trivy imports now carry the path too.

Verification: the full offline test suite passed with `GOPROXY=off GOSUMDB=off go test -mod=mod -count=1 ./...`.