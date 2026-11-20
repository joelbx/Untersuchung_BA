# Checkpoint

Task: support Amazon Linux 2023 and later release recognition and EOL mapping.

Investigation started. Repository is clean at commit `984debe`. `rg` is unavailable, so local searches use `grep`. Relevant implementation and tests are in `config/os.go` and `config/os_test.go`.

Root cause: `getAmazonLinuxVersion` maps every one-field release to `1`, including `2023`; unknown multi-field releases pass through unvalidated. `GetEOL` has no entries after `2022`. Scanner `/etc/system-release` parsing checks `release 2` as a prefix, which also matches `release 2023`, truncates its label, and can index past the end on short input. EOL methods already support both dates; Amazon entries use a single standard support end, so extended support ends with it.

Hypothesis: recognizing the explicit Amazon release tokens, adding the odd-year EOL entries, and parsing scanner release tokens by their exact version will resolve the reported path. AL2023's five-year support end is March 15, 2028; for the requested future odd-year releases, use the corresponding March 15 five years after release. External research is blocked, so future dates cannot be independently confirmed online.

Regression result: `GOPROXY=off GOSUMDB=off go test ./config -run 'TestGetAmazonLinuxVersion|TestAmazonEOLDates' -count=1` failed before the fix: `2024` was mapped to `1` and empty input panicked in `config/os.go:335`. After the fix, the targeted test and full `./config` suite passed. `./scanner -run TestParseAmazonSystemRelease` passed after the parsing change.

Further data-flow finding: `oval/util.go` routes all Amazon releases other than 2 and 2022 to OVAL release 1, and `oval/oval.go` uses an unnormalized release for availability and freshness checks. This prevents ALAS2023 data lookup even when OS detection is corrected. A focused OVAL normalization regression test has been added and is being run before the patch.

OVAL regression result: `GOPROXY=off GOSUMDB=off go test ./oval -run TestOvalRelease -count=1` failed before its implementation with `undefined: ovalRelease`. OVAL fetch, freshness, and package lookup now share the normalization. ALAS2023 advisory links use the AL2023 path.

Additional reproduction: AL2023 dotted build release `2023.9.20251008 (Amazon Linux)` returned `unknown` in the focused config test before its normalization fix. Final check: `GOPROXY=off GOSUMDB=off go test ./config ./scanner ./oval -count=1 && git diff --check` passed with exit code 0. No remote scan was available, so live ALAS data retrieval was not verified. Future EOL dates remain based on the five-year March 15 pattern rather than online confirmation.
