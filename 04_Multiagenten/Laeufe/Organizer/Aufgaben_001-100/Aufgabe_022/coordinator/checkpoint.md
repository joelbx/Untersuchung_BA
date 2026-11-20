Task: fix RPM source filename warnings and epoch parsing.
Status: complete.
Changes: shared source RPM parser records warnings; splitFileName extracts epoch prefix; regression tests cover line and scan behavior.
Verification: GOPROXY=off go test ./scanner -run Test_redhatBase_parseInstalledPackages(ContinuesAfterBadSourceRPM|Line|LineFromRepoquery|$) -count=1 passed; git diff --check passed.
