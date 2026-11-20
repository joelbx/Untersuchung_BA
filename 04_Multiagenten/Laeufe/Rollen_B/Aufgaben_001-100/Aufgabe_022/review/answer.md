VERDICT: FIX

**Code defect:** [splitFileName](/app/scanner/redhatbase.go:692) removes a numeric epoch from the source filename but does not preserve it in the returned version. Both installed-package parsers then use the binary epoch field for `SrcPackage.Version`. For `bar 0 9 123a ia64 1:bar-9-123a.src.rpm`, the source version becomes `9-123a` instead of `1:9-123a`. Preserve the filename epoch for the source version without duplicating it when the epochs match. The existing epoch tests cover only matching values.

**Tests executed:**

- `GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_redhatBase_(sourceRPMFilename|parseInstalledPackagesContinuesAfterSourceFilenameWarning|parseInstalledPackagesLine|parseInstalledPackagesLineFromRepoquery)$' -count=1` — passed.
- `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` — passed.

TEST_ENVIRONMENT_PROBLEM: none. I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code was changed during this independent review.