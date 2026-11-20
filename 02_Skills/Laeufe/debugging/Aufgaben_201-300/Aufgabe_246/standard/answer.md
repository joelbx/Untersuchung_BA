Fixed lockfile provenance throughout scanning and reporting. Each lockfile is analyzed separately; vulnerability entries carry its path, and reports resolve a library by both path and name. Repeated CVEs retain entries from every affected lockfile. The Trivy JSON importer now supplies paths as well.

Updated the cached Fanal and Trivy dependencies to use the requested analysis and driver APIs. The new two-lockfile regression test reproduced the issue before the fix.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod -count=1 ./...` passed, as did `git diff --check`.