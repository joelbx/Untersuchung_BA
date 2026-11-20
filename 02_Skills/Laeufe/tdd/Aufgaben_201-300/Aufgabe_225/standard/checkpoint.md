# Checkpoint

Task: add first class KEV data to vulnerabilities, including CISA and VulnCheck mappings.
Status: implemented and verified.

Changes:
- Added KEV model and source specific details on VulnInfo, with JSON output and legacy AlertDict.CISA retained.
- Added CVE summary and deterministic KEV ordering.
- Updated go-kev to the newer version already present in the local module cache, and mapped both response sources into KEVs, including XDB and reported exploitation details. Zero due dates become nil.
- Added model and detector tests before implementation; observed expected missing-symbol failures, then passing tests.

Checks:
- `GOPROXY=off GOSUMDB=off go test ./models ./detector -run 'TestFormatKEVCveSummaryCountsCVEs|TestSortForJSONOutputOrdersKEVs|TestKEVJSONHasDedicatedField|TestKEVsFromResponseMapsBothSources' -count=1`: passed.
- `GOPROXY=off GOSUMDB=off go test ./...`: passed.
- `git diff --check`: passed.
