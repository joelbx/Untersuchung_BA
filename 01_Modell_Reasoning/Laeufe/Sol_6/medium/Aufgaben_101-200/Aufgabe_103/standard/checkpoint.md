# Checkpoint

Task: Fix RPM installed-package, repoquery, source filename, and update candidate parsing.
Implemented and verified: preserve empty release fields; format source versions without trailing hyphen; accept -src.rpm; reject malformed filenames; handle (none) update epoch.
Tests: go test ./scanner -run Test_redhatBase_parseInstalledPackages\|TestSplitFileName\|TestParseYumCheckUpdate -count=1 passed; git diff --check passed.
