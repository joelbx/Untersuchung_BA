VERDICT: FIX

**Code defect:** [splitFileName](/app/scanner/redhatbase.go:720) handles a hyphenated release only for `-src.rpm`. It misparses `package-0-1-extra.src.rpm` as name `package-0`, version `1`, release `extra`; the expected fields are `package`, `0`, and `1-extra`. Its heuristic can also mistake a numeric component of the package name for the version. The source filename parsing needs a rule that handles both source suffixes and rejects ambiguous input instead of silently assigning incorrect fields.

**Tests:** Both relevant existing test commands passed:

- `GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_redhatBase_parseInstalledPackages$|Test_redhatBase_parseInstalledPackagesLine$|Test_redhatBase_parseInstalledPackagesLineFromRepoquery$|TestInstalledPackagesEmptyRelease$|TestParseInstalledPackagesEmptyReleaseAmazon2$|TestSplitFileNameSourceAndMalformed$|TestParseUpdatablePacksLinesNoneEpoch$|TestParseUpdatablePacksLines$' -count=1` — exit 0.
- `GOPROXY=off GOSUMDB=off go test ./scanner -run 'TestParseYumCheckUpdateLine$|TestParseYumCheckUpdateLines$|TestParseYumCheckUpdateLinesAmazon$' -count=1` — exit 0.

**TEST_ENVIRONMENT_PROBLEM:** None. The passing tests do not cover the misparsed filename above.