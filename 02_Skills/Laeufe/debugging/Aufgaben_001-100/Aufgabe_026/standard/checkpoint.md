# Checkpoint

Investigating CVE content source selection and report prioritization. `rg` is unavailable in this environment, so local searches use `grep`.

Root cause: `NewCveContentType(family)` returns a single type. `PrimarySrcURLs`, CPE/reference/CWE ordering, title/summary ordering, and both diff functions use that one type; Ubuntu API and Debian tracker therefore lose priority or are omitted. `Cvss3Scores` omits UbuntuAPI entirely. Severity conversion lacks NEGLIGIBLE. Existing `NewCveContentType` must remain compatible.

Added regression tests before implementation. `GOTOOLCHAIN=local GOPROXY=off go test ./models -run 'TestFamilyContentSources|TestUbuntuContentSourcesInReports|TestNegligibleSeverity' -count=1` failed as expected with `undefined: GetCveContentTypes`.

Implemented family source mapping, applied it to source URLs, report field ordering, and detector/reporter update comparison. CVSS v3 now reads numeric scores across family sources and uses rough severity scores where needed. NEGLIGIBLE maps to LOW.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./models ./detector ./reporter -count=1` passed for all three packages. `git diff --check` passed.

