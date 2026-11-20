# Fortinet advisory integration

Status: implemented Fortinet CPE detection, confidence ranking, advisory metadata conversion, enrichment, and report selection, including a title fallback. Updated the dictionary dependency and transitive versions. Kept the former exported enrichment entry point as a compatibility wrapper.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=readonly -modfile=/tmp/vuls-fortinet-test.mod ./detector ./models ./server ./reporter` passed. The temporary modfile mapped five unavailable transitive versions to cached equivalents for offline testing; the checked-out go.mod has no replacements.
