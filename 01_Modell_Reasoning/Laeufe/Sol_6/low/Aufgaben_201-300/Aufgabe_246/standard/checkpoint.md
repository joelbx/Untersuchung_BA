Task: fix multi-lockfile vulnerability attribution.
Status: implemented and verified.
Changes: analyze each lockfile separately from in-memory content; retain file path in fixed-library findings; resolve library versions by path and name; merge duplicate CVE library findings; use locally cached analyzer/driver versions with error-returning APIs.
Verification: GOPROXY=off go test ./models ./scan ./report ./libmanager passed.
