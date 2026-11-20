# Checkpoint

Task: Fix RPM installed-package, repoquery, source RPM filename, and update-candidate parsing in `/app`.

Completed: `scanner/redhatbase.go` preserves empty release fields in the fixed RPM output formats, shares epoch/version/release formatting, validates RPM filenames, accepts `-src.rpm` names including empty release, and applies the shared epoch rule to update candidates. `scanner/redhatbase_test.go` covers empty releases through rpm and repoquery, the reported source filename forms, and malformed filenames. Existing CentOS and Amazon update tests remain in use.

Verification: `GOPROXY=off GOTOOLCHAIN=local go test ./scanner -run 'Test_redhatBase_parseInstalledPackages|TestSplitFileName|TestParseYumCheckUpdate' -count=1` passed. `git diff --check` passed.
