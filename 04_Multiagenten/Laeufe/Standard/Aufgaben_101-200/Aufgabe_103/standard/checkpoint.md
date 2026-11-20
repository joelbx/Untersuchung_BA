Task: Fix RPM installed-package and source-RPM parsing, including empty releases, and verify update candidate parsing.
Status: Complete. Focused scanner tests passed.
Changes: Preserve empty release columns in RPM and repoquery output; share epoch/version formatting; validate source RPM filenames including -src forms; treat (none) as absent epoch in update listings.
Verification: go test ./scanner -run 'Test(_redhatBase_parseInstalledPackages|InstalledPackagesEmptyRelease|SplitFileNameValidation|ParseYumCheckUpdate|ParseUpdatablePacksLinesNoneEpoch)' -count=1 (passed); git diff --check (passed).
Constraints: Local repository only; git history, index baseline, and harness configuration untouched.
